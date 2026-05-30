# Frame Spec v0.1.1

## Purpose

This is the smallest adopt-now definition of a Frame.

The goal of `v0.1.1` is immediate use, not completeness.

If someone can write a Frame today, send it to another person by email, chat, or git, and that person can read and use it, then `v0.1.1` is doing its job.

## Definition

A Frame is a scoped, text-based artifact that carries cultural and operational context for work.

In `v0.1.1`, a Frame should be:

- a Markdown file
- human-readable
- usable by a Cog or other AI assistant
- easy to share manually

## File Format

The preferred `v0.1.1` format is:

- Markdown body
- YAML frontmatter at the top

This intentionally follows the general shape that Skills already use, without requiring the full Skills standard to define what a Frame is.

In `v0.1.1`, the canonical form is a single Markdown file.

Future versions may also support a directory form with a canonical entry file such as `frame.md` plus optional supporting assets.

That future directory shape is intentionally left open for later, since it is more closely tied to implementation and distribution concerns than to the minimum adopt-now definition.

## Required Fields

Every `v0.1.1` Frame should have:

- `type`
- `version`
- `name`
- `description`
- `visibility`

### `type`

This must be:

```yaml
type: frame
```

or, to specify which version of the Frame Spec the Frame conforms to:

```yaml
type: frame [0.1.1]
```

This is the minimal explicit hook that tells an AI system or surrounding implementation that the file is intended to be handled as a Frame rather than as generic Markdown. The bracketed spec version is optional but recommended.

### `version`

The current version of this Frame.

```yaml
version: 0.1.0
```

This tracks the Frame's own revision history, not the spec version. Authors should update this when the content of the Frame changes.

### `name`

Short human-readable name for the Frame.

### `description`

One or two sentences describing what the Frame is for and when it should be used.

### `visibility`

Suggested values:

- `private`
- `internal`
- `shared`
- `public`

## Recommended Fields

These are not required in `v0.1.1`, but they are encouraged:

- `scope`
- `author`

### `scope`

A short description of where this Frame applies.

Examples:

- `company`
- `department`
- `project`
- `partner`
- `personal`

`v0.1.1` does not require a formal scope grammar.

### `author`

The person, team, or organization that wrote the Frame.

## Body Content

After the frontmatter, the rest of the file is normal Markdown.

The body should contain the context the Frame is meant to carry.

Typical content may include:

- terminology
- goals
- rules
- style guidance
- norms
- relevant skills
- business process notes

`v0.1.1` does not require a fixed section taxonomy.

## Minimal Example

```md
---
type: frame [0.1.1]
version: 0.1.0
name: OpenTeams Brand Voice
description: Shared guidance for how OpenTeams communicates in external-facing writing.
visibility: internal
scope: company
author: marketing
---

# OpenTeams Brand Voice

## Goals

- Be clear, direct, and credible.
- Avoid hype when describing technical capabilities.

## Terminology

- Prefer "Frame" over "alignment file".

## Style

- Use calm, explanatory language.
- Make important assumptions explicit.
```

## What v0.1.1 Does Not Try To Define

`v0.1.1` intentionally does not standardize:

- package manifests
- inheritance semantics
- layering behavior
- canonical identity
- provenance
- review workflows
- publication registries
- runtime management

Those may become part of later versions, but they should not block immediate use.

## Sharing

A `v0.1.1` Frame may be shared in any ordinary way, including:

- email
- chat
- git
- shared folders

No special infrastructure is required.

## Expected Agent Handling

At a minimum, an implementation should be able to:

1. Detect `type: frame` in the frontmatter.
2. Read the remaining frontmatter as lightweight metadata.
3. Read the Markdown body as contextual guidance for work.
4. Apply that guidance when the Frame is made active by a user or system.

`v0.1.1` does not require more advanced behavior such as inheritance resolution, formal layering, provenance validation, or canonical-source lookup.

## Relationship To Future Work

This document is the current adopt-now spec.

Future ideas such as richer identity, packaging, layering semantics, Desktop behavior, and whitepaper alignment are tracked separately in the discussion docs.
