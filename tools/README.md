# Frame Builder

This directory contains a simple offline tool for authoring `v0.1` Frames.

Open [frame-builder.html](frame-builder.html) in a browser.

The builder helps non-technical users produce:

- valid `type: frame` frontmatter
- the required `v0.1` metadata fields
- a Markdown body using common Frame sections
- a broader range of Frames than just style or brand examples

The generated output can be:

- copied into another tool
- saved as `frame.md`
- shared by email, chat, or git

This builder is intentionally simple and tracks the current [../spec/v0.1.md](../spec/v0.1.md) spec.

It now starts in a guided blank state and lets the user load an example on demand.
