# Frame Spec

Frames are scoped, text-based artifacts that carry the cultural and operational context within which work happens.

They are intended to be:

- readable by humans
- applied by Cogs
- shareable across organizational boundaries when appropriate
- inheritable across scopes such as company, department, team, project, partner, or vendor
- first-class artifacts that can be authored, discovered, sold, and shared independently

This repository seed is a standalone starting point for the Frame spec as its own project.

## Adopt Now

- Read [spec/frame-spec.md](spec/frame-spec.md) for the current minimum adopt-now spec.
- Review [examples/minimal/README.md](examples/minimal/README.md) for a concrete minimal example.
- Review [examples/minimal-self-frame/README.md](examples/minimal-self-frame/README.md) for a self-referential example that uses the minimal spec to describe the spec itself.
- Open [tools/frame-builder.html](tools/frame-builder.html) for a simple offline builder that generates valid Frame Markdown.
- Use [tools/frame-authoring-assistant-prompt.md](tools/frame-authoring-assistant-prompt.md) when someone would rather create a Frame through an AI-guided conversation.
- Use [share/frame-builder-kit/README.md](share/frame-builder-kit/README.md) for the Slack/email-friendly distribution copy of the builder.

## Tools And Aids

This repo can include lightweight, spec-adjacent aids such as:

- offline builders
- prompt templates
- small authoring or validation skills
- lint and validation tools
- sample authoring workflows

These aids help people create or verify Frames. They do not define the full runtime or management system for Frames.

For the current boundary, read [docs/tools-and-aids.md](docs/tools-and-aids.md).

## Background

- Read [docs/overview.md](docs/overview.md) for the concept and current working definition.
- Read [docs/design-note.md](docs/design-note.md) for the problem framing and open questions.

## Discussion And Future Work

- Read [docs/future-directions.md](docs/future-directions.md) for the map of future and discussion documents.
- Read [docs/spec-and-implementation.md](docs/spec-and-implementation.md) for the boundary between the Frame spec and the systems that realize Frames.
- Read [references/Intelligence Hub Whitepaper - v4.md](references/Intelligence%20Hub%20Whitepaper%20-%20v4.md) for the repository copy of the whitepaper that informed the later spec alignment notes.
- Review [examples/self-frame/README.md](examples/self-frame/README.md) and [examples/nebi-frame-package/README.md](examples/nebi-frame-package/README.md) for richer future-oriented examples.

## Repository Layout

```text
docs/
  overview.md
  design-note.md
  tools-and-aids.md
  future-directions.md
  spec-and-implementation.md
  spec-sketch.md
  nebi-integration.md
  desktop-sharing.md
  v1-gap-analysis.md
  canonical-identity-proposal.md
tools/
  README.md
  frame-builder.html
  frame-authoring-assistant-prompt.md
  frame-authoring-assistant/
share/
  frame-builder-kit/
spec/
  README.md
  frame-spec.md
examples/
  minimal/
  minimal-self-frame/
  OT-FIR-program.md
  self-frame/
  nebi-frame-package/
references/
  Intelligence Hub Whitepaper - v4.md
  travis-definition.md
```

## Current Status

This is still an early draft.

What exists now:

- a working concept and definition for Frames
- a small spec that can be adopted immediately (currently `v0.2`)
- a design note describing the problem and direction
- future-oriented spec discussion documents
- a Nebi integration illustration
- concrete example Frame packages

What is intentionally not required for the current spec:

- a finalized schema
- a finalized Nebi contract
- a built-in Desktop sharing implementation
- settled governance for publication and discovery
- a standardized management or layering system

## Working Position On Nebi

Nebi is treated here as a potential mechanism, not as the semantic definition of a Frame.

The intended boundary is:

- Frames are the semantic artifacts
- Nebi may package, version, and distribute Frames
- Desktop may become a discovery, import, export, and sharing surface for Frames
