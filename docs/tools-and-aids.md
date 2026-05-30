# Tools And Aids

This repo can include lightweight aids that help people understand, create, and verify Frames.

These aids support the spec. They are not meant to become the full system that manages, activates, or operationalizes Frames in production.

## Fits In This Repo

Examples of tools and aids that fit here:

- simple offline builders that generate valid `frame.md` files
- prompt templates that help people draft Frames
- small skills that interview, rewrite, or validate Frames
- validation and lint-style tools for `v0.1.1` and later spec versions
- sample inputs and outputs for authoring workflows
- tiny conversion helpers that turn guided input into spec-compliant Frames

These belong here because their primary purpose is to help someone produce or verify a Frame artifact.

## Better In Another Repo

Examples of things that should probably live elsewhere:

- multi-user web apps
- storage, auth, sync, or collaboration systems
- runtime or harness systems that decide when Frames are applied
- deployment and distribution infrastructure
- ingest pipelines and operational services
- product surfaces that manage live Frame use at scale

These are implementation systems, not spec-adjacent aids.

## Working Rule

If the tool's main job is to help someone author, review, or validate a Frame, it fits here.

If the tool's main job is to manage, activate, distribute, or execute Frames in a live system, it probably belongs in a separate repo.
