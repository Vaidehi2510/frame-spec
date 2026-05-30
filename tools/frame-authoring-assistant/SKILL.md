---
name: frame-authoring-assistant
description: Use this skill when helping someone create a Frame through conversation. It interviews the user, turns tacit organizational knowledge into a concise Frame draft, and outputs valid Frame Spec v0.1.1 Markdown with `type: frame`, `name`, `description`, and `visibility`.
---

# Frame Authoring Assistant

Use this skill to help a person create a useful `v0.1.1` Frame when they are more comfortable talking than filling out the structure directly.

For the exact `v0.1.1` field expectations and examples, read `../../spec/v0.1.1.md`.

## Goal

Turn conversation, notes, or pasted source material into a draft `frame.md` that:

- follows Frame Spec `v0.1.1`
- reflects how the person or team actually wants work to happen
- stays concise enough to be practical
- preserves useful wording from the user where possible

## Core Prompting Stance

Treat the process as guided interviewing, not metadata collection.

The most useful framing question is:

> What are the things that you would teach a new employee about how you want them to work?

Use that question to surface:

- goals and priorities
- terminology
- rules and constraints
- norms and expectations
- common mistakes to avoid
- useful process guidance

## Workflow

1. Establish what the Frame is for.
Ask what team, project, role, or situation the Frame should help with.

2. Elicit the working context.
Ask short questions about how good work is done, what matters most, and what people often get wrong.

3. Pull out reusable guidance.
Prefer durable context over one-off task instructions.

4. Suggest the minimum metadata.
Propose `name`, `description`, `visibility`, and optional `scope` and `author` based on the conversation.

5. Draft the Frame.
Return valid `v0.1.1` Markdown with YAML frontmatter and a clear Markdown body.

6. Close with a lightweight review pass.
Call out any assumptions or unresolved choices briefly.

## Interview Guidance

Keep the interview lightweight. Do not ask a long questionnaire up front.

Start with one or two questions, then adapt based on the answer. Good follow-ups include:

- What kind of work should this Frame help with?
- Who is this mainly for?
- What should a new person understand right away?
- What does good work look like here?
- What mistakes or misunderstandings happen often?
- Are there terms, rules, or constraints people need to follow?
- Is this private, internal, shared with partners, or public?

If the user pastes source material instead of answering questions, extract the guidance directly and only ask for missing essentials.

## Drafting Rules

- Always output `type: frame` in the frontmatter.
- Always include `name`, `description`, and `visibility`.
- Include `scope` and `author` when the conversation supports them.
- Keep the body in normal Markdown.
- Use section headings only when they help clarity.
- Do not invent rigid taxonomy if the content does not need it.
- Prefer concise bullets over long prose blocks.
- Preserve the user's own terminology when it is clear and useful.

## Output Shape

Default to this structure when drafting:

```md
---
type: frame
name: ...
description: ...
visibility: ...
scope: ...
author: ...
---

# ...

## Goals

- ...

## Terminology

- ...

## Ways Of Working

- ...

## Constraints

- ...
```

Adjust the sections to fit the material. Omit empty sections rather than forcing them.

## Quality Bar

A good draft should:

- feel like something a real team would reuse
- be specific enough to shape work
- avoid unnecessary implementation detail
- avoid sounding generic or consultant-like
- be short enough that a person or AI would actually use it

## When To Be More Directive

Be more directive when the user is unsure how to express their context.

In that case:

- propose a draft structure
- suggest concise wording
- offer one or two visibility or scope options
- make assumptions explicit instead of hiding them

## Final Response Pattern

When the draft is ready, provide:

1. the draft Frame Markdown
2. a short list of assumptions or open questions, if any

Do not bury the actual Frame below long explanation.
