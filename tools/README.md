# Tools

This directory contains lightweight tools and aids for authoring `v0.1` Frames.

## Frame Builder

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

## AI-Guided Authoring

This directory also includes lightweight AI authoring aids:

- [frame-authoring-assistant-prompt.md](frame-authoring-assistant-prompt.md): a copy-paste prompt for any chat-based AI assistant
- [frame-authoring-assistant/SKILL.md](frame-authoring-assistant/SKILL.md): a reusable skill for AI-assisted Frame interviews and drafting

These are meant for people who would rather talk through a Frame than build it from scratch in the form.
