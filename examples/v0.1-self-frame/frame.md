---
type: frame
name: Frame Spec v0.1 Working Frame
description: Minimal self-referential Frame describing how the current adopt-now Frame spec should be understood and used.
visibility: internal
scope: project
author: frame-spec-authors
---

# Frame Spec v0.1 Working Frame

## Purpose

- Define the smallest practical shape of a Frame so people can start using Frames immediately.
- Keep the spec simple enough to share by email, chat, git, or a shared folder.
- Make Frames understandable to both humans and AI assistants without requiring extra infrastructure.

## What Counts As A Frame

- A `v0.1` Frame is a Markdown file with YAML frontmatter.
- It must include `type: frame`, `name`, `description`, and `visibility`.
- It may also include fields like `scope` and `author`.
- The rest of the file should contain useful cultural or operational context in normal Markdown.

## Ways Of Working

- Prefer immediate usability over completeness.
- Keep the authored artifact simple and portable.
- Reuse familiar patterns such as Markdown plus frontmatter.
- Learn from real use before standardizing richer semantics.

## Constraints

- Do not require package manifests, registries, or special runtime infrastructure for `v0.1`.
- Do not treat implementation details as part of the minimum spec.
- Do not assume inheritance, layering, provenance, or governance semantics are settled in `v0.1`.

## Terminology

- Prefer `Frame spec` over `Frame protocol`.
- Prefer `spec` for the current minimum definition.
- Treat Frames as contextual artifacts, not as full applications or management systems.

## Review Notes

- If a proposed addition makes Frames harder to author or share immediately, it probably belongs in future work instead of `v0.1`.
- If a tool helps people create or validate Frame artifacts, it can fit alongside the spec.
- If a feature manages, activates, or operationalizes Frames in a live system, it likely belongs outside the minimum spec.
