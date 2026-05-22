# Frame Protocol

Frames are scoped, text-based artifacts that carry the cultural and operational context within which work happens.

They are intended to be:

- readable by humans
- applied by Cogs
- shareable across organizational boundaries when appropriate
- inheritable across scopes such as company, department, team, project, partner, or vendor
- first-class artifacts that can be authored, discovered, sold, and shared independently

This repository seed is a standalone starting point for the Frame protocol as its own project.

## Start Here

- Read [docs/overview.md](docs/overview.md) for the concept and current working definition.
- Read [docs/design-note.md](docs/design-note.md) for the problem framing and open questions.
- Read [docs/protocol-sketch.md](docs/protocol-sketch.md) for the draft protocol shape.
- Read [docs/nebi-integration.md](docs/nebi-integration.md) for one possible Nebi-based packaging and delivery model.
- Read [docs/v1-gap-analysis.md](docs/v1-gap-analysis.md) for a concrete gap list between the current draft and the Intelligence Hub whitepaper assumptions.
- Review [examples/self-frame/README.md](examples/self-frame/README.md) for a concrete self-referential example.

## Repository Layout

```text
docs/
  overview.md
  design-note.md
  protocol-sketch.md
  nebi-integration.md
  desktop-sharing.md
  v1-gap-analysis.md
spec/
  README.md
examples/
  self-frame/
  nebi-frame-package/
references/
  travis-definition.md
```

## Current Status

This is still an early draft.

What exists now:

- a working concept and definition for Frames
- a design note describing the problem and direction
- a protocol sketch for Frame package and document structure
- a Nebi integration illustration
- concrete example Frame packages

What does not exist yet:

- a finalized schema
- a finalized Nebi contract
- a built-in Desktop sharing implementation
- settled governance for publication and discovery

## Working Position On Nebi

Nebi is treated here as a potential mechanism, not as the semantic definition of a Frame.

The intended boundary is:

- Frames are the semantic artifacts
- Nebi may package, version, and distribute Frames
- Desktop may become a discovery, import, export, and sharing surface for Frames
