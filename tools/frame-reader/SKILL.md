---
name: frame-reader
description: Use this skill when an AI assistant should read one or more Frames, determine which are active for the current task, and apply them consistently while surfacing conflicts or missing context.
---

# Frame Reader

Use this skill when a person provides one or more Frame files and wants the assistant to use them while completing a task.

This skill is intentionally lightweight.

It does not define a full runtime or management system for Frames.

Its purpose is to help an assistant consume Frames more consistently in ordinary chat-based tools.

For the current minimum Frame format, read `../../spec/v0.1.md`.

For practical human guidance on when and how to use Frames, read `../../docs/how-to-use-frames.md`.

## Goal

Help the assistant:

- recognize Frame files
- understand what each Frame governs
- determine which Frames are active for the task
- apply the most relevant guidance
- surface ambiguity instead of silently guessing

## Core Prompting Stance

Treat Frames as scoped contextual guidance, not as generic attachments.

A Frame should shape the work when it is relevant, but it should not be treated as if all attached context is equally important.

Prefer explicitness over silent interpretation.

## Workflow

1. Identify the Frames.
Determine which provided files appear to be Frames by looking for `type: frame` and Frame-like metadata.

2. Read scope and purpose.
For each Frame, identify:
- name
- description
- visibility
- scope if present
- the main kinds of guidance it carries

3. Determine relevance.
Infer which Frames are relevant to the task based on:
- the user's stated task
- the scopes involved
- any user guidance about priority or specificity

4. Form a working interpretation.
Briefly determine:
- which Frame is broadest
- which Frame is most specific
- whether one Frame appears to refine another

5. Apply the guidance.
Use the relevant Frames to shape the response, draft, analysis, or other task output.

6. Surface issues.
If the Frames conflict, are stale, or are insufficient for the task, say so clearly.

## Consumption Rules

- Do not assume every attached file is a Frame.
- Do not assume every provided Frame is active for the current task.
- Do not silently ignore a conflict between relevant Frames.
- Do not silently invent missing context when the Frame does not provide it.
- Do not treat a broad company-level Frame as if it automatically overrides a more specific customer, project, or proposal Frame.

## Working Heuristics

When multiple relevant Frames are present, use these heuristics unless the user says otherwise:

- broader Frames provide defaults
- narrower Frames refine the task
- customer, partner, project, or proposal context is usually more specific than department context
- department context is usually more specific than company-wide context

These are practical heuristics, not formal spec semantics.

## Recommended Response Pattern

When helpful, begin with a short summary such as:

- which Frames were identified
- which ones appear active
- which one is most specific
- any conflicts or missing context

Keep this brief unless the user explicitly wants a deeper analysis.

## When To Ask For Clarification

Ask a short clarification question only when the ambiguity materially affects the outcome.

Examples:

- two equally specific Frames appear to conflict
- the user attached many Frames but did not indicate which are active
- a critical Frame for the task seems missing

If the ambiguity is minor, make a reasonable assumption and state it briefly.

## Output Behavior

Depending on the task, the assistant may:

- draft content shaped by the Frames
- summarize Frame guidance
- compare Frames
- identify conflicts or gaps
- explain which Frame likely applies to which work

The assistant should adapt the output to the task instead of always producing the same template.

## Good Outcomes

A good use of this skill should:

- make Frame usage feel clearer to the user
- reduce context drift
- preserve important scoped guidance
- avoid overclaiming what the Frames say
- make conflicts visible rather than hidden

## Example Starter Prompt

Use this skill together with a task prompt like:

```text
Please read the attached Frame files first.

For this task:
- identify which Frames are relevant
- apply the most specific relevant guidance
- tell me if the Frames conflict
- tell me if important context is missing

Task: Draft a follow-up note for this customer using the attached company, department, and customer Frames.
```
