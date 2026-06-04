#!/usr/bin/env python3
"""Validate Frame Markdown files against the v0.2 minimum spec.

The v0.2 Frame spec requires these frontmatter fields:

    type, version, name, description, visibility

This tool uses only the Python standard library. It performs lightweight
frontmatter checks rather than full YAML validation, which is enough to catch
required-field drift in examples without adding install steps.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REQUIRED_FIELDS = ("type", "version", "name", "description", "visibility")
DEFAULT_TARGET = "examples"


def is_markdown(path: Path) -> bool:
    return path.suffix.lower() in {".md", ".markdown"}


def is_hidden_or_metadata(path: Path) -> bool:
    return any(part.startswith(".") for part in path.parts) or path.name.startswith("._")


def split_frontmatter(text: str) -> tuple[list[str] | None, str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, None

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return lines[1:index], None

    return None, "frontmatter opening '---' has no closing '---'"


def normalize_scalar(value: str | None) -> str | None:
    if value is None:
        return None

    normalized = value.strip()
    if len(normalized) >= 2 and normalized[0] == normalized[-1] and normalized[0] in {"'", '"'}:
        normalized = normalized[1:-1].strip()
    return normalized


def parse_frontmatter(lines: list[str]) -> tuple[dict[str, object], list[str]]:
    data: dict[str, object] = {}
    problems: list[str] = []
    last_key: str | None = None

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            continue

        if line.lstrip().startswith("- "):
            if last_key is None:
                problems.append(f"list item has no parent key: {stripped}")
                continue

            existing = data.get(last_key)
            item = normalize_scalar(line.lstrip()[2:].strip())
            if isinstance(existing, list):
                existing.append(item or "")
            else:
                data[last_key] = [item or ""]
            continue

        if ":" in line and not line.startswith((" ", "\t")):
            key, _, raw_value = line.partition(":")
            key = key.strip()
            value = raw_value.strip()
            last_key = key

            if not key:
                problems.append(f"frontmatter key is empty: {stripped}")
                continue

            for quote in ("'", '"'):
                if value.startswith(quote) and not value.endswith(quote):
                    problems.append(f"value for '{key}' looks like an unterminated string: {value}")

            data[key] = normalize_scalar(value) if value else None
            continue

        problems.append(f"could not parse frontmatter line: {stripped}")

    return data, problems


def validate_frame(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        return [f"could not read file: {error}"]

    frontmatter, error = split_frontmatter(text)
    if error:
        return [error]
    if frontmatter is None:
        return []

    data, problems = parse_frontmatter(frontmatter)

    for field in REQUIRED_FIELDS:
        value = data.get(field)
        if field not in data:
            problems.append(f"missing required field: {field}")
        elif value is None or str(value).strip() == "":
            problems.append(f"required field is empty: {field}")

    type_value = data.get("type")
    if type_value is not None and not str(type_value).strip().startswith("frame"):
        problems.append(f"type should declare a Frame, got: {type_value!r}")

    return problems


def collect_files(targets: list[str]) -> list[Path]:
    files: set[Path] = set()

    for target in targets:
        path = Path(target)
        if path.is_dir():
            files.update(
                candidate
                for candidate in path.rglob("*")
                if candidate.is_file() and is_markdown(candidate) and not is_hidden_or_metadata(candidate)
            )
        elif path.is_file():
            if is_markdown(path) and not is_hidden_or_metadata(path):
                files.add(path)
        else:
            sys.stderr.write(f"warning: path not found, skipping: {target}\n")

    return sorted(files)


def has_frontmatter(path: Path) -> bool:
    try:
        with path.open(encoding="utf-8", errors="replace") as handle:
            return handle.readline().strip() == "---"
    except OSError:
        return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate Frame Markdown files against the v0.2 minimum spec."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=[DEFAULT_TARGET],
        help=f"Files or directories to check (default: {DEFAULT_TARGET}).",
    )
    args = parser.parse_args(argv)

    files = collect_files(args.paths)
    if not files:
        print("No Markdown files found to check.")
        return 0

    checked = 0
    failed = 0
    skipped = 0

    print(f"Checking {len(files)} Markdown file(s)...\n")

    for path in files:
        if not has_frontmatter(path):
            skipped += 1
            continue

        checked += 1
        problems = validate_frame(path)
        if problems:
            failed += 1
            print(f"FAIL  {path}")
            for problem in problems:
                print(f"      - {problem}")
        else:
            print(f"OK    {path}")

    print()
    print(
        f"Frames checked: {checked}   passed: {checked - failed}   "
        f"failed: {failed}   non-Frame files skipped: {skipped}"
    )

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
