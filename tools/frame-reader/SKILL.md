---
name: frame-reader
description: Use this skill when an AI assistant should read one or more Frames, determine which are active for the current task, and apply them consistently while surfacing conflicts or missing context.
---

# Frame Reader

Use this skill when a person provides one or more Frames and wants them used as part of a task.

This skill is standalone.

It is meant to guide how an assistant should interpret and apply Frames in ordinary AI work, even when no surrounding Frame-management system exists.

## What A Frame Is

For the purposes of this skill, a Frame is a scoped text artifact that carries context for work.

A Frame may include things such as:

- goals
- terminology
- rules
- norms
- style guidance
- process expectations
- customer or partner context

The important point is that a Frame carries reusable context that should shape repeated work.

## What This Skill Should Do

When Frames are present, this skill should help the assistant:

- recognize which provided materials are Frames
- understand what each Frame governs
- determine which Frames are active for the current task
- resolve broad-to-narrow layering when possible
- respect explicit parent-child relationships when they are provided
- apply the most relevant guidance
- surface ambiguity, conflict, or missing context instead of silently guessing

## Core Assumptions

Use these assumptions unless the user gives more specific instructions.

### 1. Not all provided files are necessarily Frames

A file is likely a Frame if it presents itself as reusable contextual guidance rather than one-off task content.

### 2. Not all provided Frames are necessarily active

Only some Frames may matter for the current task.

Choose the smallest relevant working set rather than treating every available Frame as equally active.

### 3. Broader Frames provide defaults

Company- or organization-level context often provides defaults.

### 4. Narrower Frames refine the work

Department, project, customer, partner, proposal, or task-family Frames often narrow or refine broader guidance.

### 5. Explicit inheritance is stronger than inferred hierarchy

If a Frame explicitly says it extends or inherits another Frame, respect that relationship.

Do not assume that a structural hierarchy automatically means inheritance unless the Frame or user makes that clear.

### 6. Conflicts should be surfaced

If two relevant Frames appear to disagree, do not silently choose unless the precedence is clear.

### 7. Missing context should be surfaced

If the task appears to depend on a Frame that is not available, say so.

## Workflow

### 1. Identify candidate Frames

Determine which provided materials appear to be Frames.

For each likely Frame, identify as much as is available:

- name
- purpose
- scope
- visibility
- version
- parent or inherited relationships
- the main kinds of guidance it carries

If metadata is absent, infer carefully from the content.

### 2. Determine task relevance

Decide which Frames appear relevant to the current task.

Use:

- the user’s stated task
- the apparent scope of each Frame
- any explicit user guidance about priority or specificity

### 3. Resolve parent-child and broad-to-narrow relationships

If explicit inheritance or parent-child relationships are present:

- treat parent guidance as baseline context
- treat child guidance as refinement or override context
- if multiple parents are present, prefer the later or more specific one when the relationship is clearly ordered

If inheritance is not explicit, use broad-to-narrow reasoning cautiously as a heuristic, not as a hard rule.

### 4. Build the working Frame set

Determine:

- which Frames were provided
- which Frames are active for this task
- which Frames are inactive or irrelevant for this task
- which Frame is broadest
- which Frame is most specific
- the likely precedence order

### 5. Summarize activation when helpful

Before substantial work, briefly summarize the working Frame set when it will help the user understand how the task is being grounded.

Keep this concise unless the user wants a deeper explanation.

### 6. Form a working synthesis

For the active working set, synthesize:

- baseline context from broader Frames
- refinements from narrower Frames
- task-specific constraints that emerge from the set
- unresolved ambiguity that may affect the task

### 7. Perform the task using the resolved working set

Use the synthesized context to shape the response, draft, analysis, or other output.

### 8. Surface issues

If there are problems that materially affect the result, say so clearly.

## Multi-Frame Issue Types

When useful, recognize issues like these:

- direct conflict: two active Frames say incompatible things
- precedence conflict: two Frames may both apply, but the ordering is unclear
- overlap without conflict: two Frames cover similar ground but can coexist
- missing parent: a Frame depends on another Frame that is not available
- stale duplicate: two Frames seem to cover the same role but differ in version or likely freshness
- missing bridge context: the task likely depends on a Frame that was not provided

Use the lightest useful label.

Do not over-formalize ordinary work.

## Consumption Rules

- Do not assume every provided file is a Frame.
- Do not assume every provided Frame is active for the task.
- Do not silently ignore explicit parent-child relationships.
- Do not silently invent missing context.
- Do not silently ignore a conflict between relevant Frames.
- Do not treat broad organizational context as automatically overriding more specific customer, project, or proposal context.
- Do not assume structural hierarchy alone defines semantic precedence.

## When To Ask For Clarification

Ask a short clarification question only when the ambiguity materially affects the outcome.

Examples:

- two equally specific Frames appear to conflict
- a missing parent or missing related Frame likely matters
- the user provided many Frames but did not indicate which ones are in play
- the task appears to require customer-, proposal-, or project-specific context that is absent

If the ambiguity is minor, make a reasonable assumption and state it briefly.

## Output Behavior

Depending on the task, the assistant may:

- draft content shaped by the Frames
- summarize the resolved working Frame set
- compare Frames
- identify conflicts or gaps
- explain likely precedence
- explain which Frame likely governs which aspect of the work

Adapt the output to the task rather than always producing the same template.

## Good Outcomes

A good use of this skill should:

- make Frame usage clearer to the user
- reduce context drift
- preserve important scoped guidance
- make multi-Frame activation easier to understand
- avoid overstating what the Frames say
- make conflicts and missing context visible rather than hidden
