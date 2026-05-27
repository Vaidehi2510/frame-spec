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

- Read [spec/v0.1.md](spec/v0.1.md) for the current minimum adopt-now spec.
- Review [examples/v0.1-minimal/README.md](examples/v0.1-minimal/README.md) for a concrete minimal example.

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
  future-directions.md
  spec-and-implementation.md
  spec-sketch.md
  nebi-integration.md
  desktop-sharing.md
  v1-gap-analysis.md
  canonical-identity-proposal.md
spec/
  README.md
  v0.1.md
examples/
  v0.1-minimal/
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
- a small `v0.1` spec that can be adopted immediately
- a design note describing the problem and direction
- future-oriented spec discussion documents
- a Nebi integration illustration
- concrete example Frame packages

What is intentionally not required for `v0.1`:

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
