# Protocol Sketch

This document describes a first draft shape for Frame artifacts and the packages that may carry them.

It is a working sketch, not yet a finalized specification.

## Protocol Goals

The first version should optimize for:

- human readability
- Cog usability
- explicit scope
- explicit inheritance
- explicit review state
- selective sharing
- diffability in version control

It should not yet optimize for:

- maximum compactness
- full graph semantics
- dynamic remote resolution
- advanced execution behavior

## Conceptual Layers

The protocol currently assumes five layers.

### 1. Frame

The Frame is the primary semantic artifact.

It answers:

- what context applies within a scope
- what is normative, preferred, or descriptive
- what humans and Cogs should understand there

### 2. Package

The package is the delivery unit.

It answers:

- what is being distributed
- who published it
- what version it is
- what Frames it contains
- what other packages it depends on

### 3. Document

The document is the concrete file representation of a Frame.

It answers:

- what scope it applies to
- what it inherits from
- what is visible or shareable
- what review state it has

### 4. Section

Sections group content into common categories such as:

- vision
- goals
- terminology
- rules
- norms
- skills
- tool specifications
- prompts
- architecture
- business process
- style
- review
- escalation

### 5. Policy

Policies express concrete expectations inside sections such as:

- required behavior
- preferred behavior
- forbidden behavior
- advisory background

## Frame As File Or Folder

A Frame may be represented as:

- a single structured file
- a folder of files with one main manifest

The protocol should allow both, though the examples below use a folder of files.

## Suggested Package Layout

```text
frame-package/
  nebi.toml
  frame/
    package.yaml
    company.yaml
    department.research.yaml
    project.alpha.yaml
  references/
    glossary.md
    rationale.md
```

Interpretation:

- `nebi.toml` carries packaging metadata if Nebi is used
- `frame/package.yaml` is the Frame package manifest
- each `frame/*.yaml` file defines one scoped Frame document
- `references/` holds supporting human-facing material

## Package Manifest Draft

```yaml
protocol_version: "0.1"
package_id: "acme.operating-frame"
package_version: "0.1.0"
package_name: "Acme Operating Frame"
publisher: "acme"
summary: "Shared cultural and operational context for Acme internal teams and approved partners."
default_format: "yaml"
root_scope: "company:acme"
frames:
  - "company.yaml"
  - "department.research.yaml"
  - "project.alpha.yaml"
dependencies:
  - package_id: "common.agent-coordination"
    version: "^0.1"
distribution:
  visibility: "internal"
  exportable_scopes:
    - "partner:acme-contoso"
review:
  status: "approved"
  approved_by:
    - "ops-lead"
    - "product-lead"
source_refs:
  - kind: "document"
    uri: "file://references/glossary.md"
    role: "terminology-source"
decision_refs:
  - kind: "decision"
    uri: "file://references/rationale.md"
    role: "package-rationale"
```

## Frame Document Draft

```yaml
document_id: "acme.company.core"
scope: "company:acme"
inherits_from: []
applies_to:
  entity_types:
    - "human"
    - "agent"
visibility: "internal"
status: "approved"
priority: 100
summary: "Core company-wide operating context."
owners:
  - "leadership"
reviewers:
  - "operations"
effective_date: "2026-05-18"
source_refs:
  - kind: "document"
    uri: "file://references/glossary.md"
    role: "terminology-source"
decision_refs:
  - kind: "decision"
    uri: "file://references/rationale.md"
    role: "scope-rationale"
sections:
  vision:
    intent:
      - "Help teams act with long-term clarity rather than short-term local optimization."
  terminology:
    preferred_terms:
      - term: "Frame"
        prefer_over:
          - "memory file"
  goals:
    objectives:
      - "Preserve coherent operating context across sessions and teams."
  rules:
    required:
      - "Escalate when a local optimization conflicts with stated priorities."
    forbidden:
      - "Treat unreviewed exported Frames as approved shared truth."
  style:
    communication:
      - "Be direct, calm, and precise."
  norms:
    expectations:
      - "Make important assumptions explicit when collaboration spans teams."
```

## Scope Model

The current draft assumes explicit scope identifiers:

```text
<scope-type>:<scope-id>
```

Examples:

- `company:acme`
- `department:acme/research`
- `team:acme/research/agents`
- `project:acme/research/atlas`
- `partner:acme-contoso`
- `vendor:acme-legal`

## Inheritance Rules

The initial inheritance model should remain simple:

1. Narrower scopes may inherit from broader scopes.
2. Inheritance must be explicit.
3. Narrower scopes may extend or refine broader guidance.
4. Required rules from broader scopes should not disappear silently.
5. Exceptions should be explicit and justified.

Suggested override modes:

- `extend`
- `replace`
- `exception`

## Visibility

Suggested visibility values:

- `private`
- `internal`
- `shared`
- `public`

These should control what can be exported or shared beyond the local working context.

## Review And Trust

Suggested status values:

- `draft`
- `review`
- `approved`
- `deprecated`
- `revoked`

Cogs should not treat these states as interchangeable.

## Provenance

Frames should support lightweight provenance through:

- `source_refs`
- `decision_refs`

Suggested reference fields:

- `kind`
- `uri`
- `role`
- optional `title`
- optional `notes`

The goal is traceability, not a full graph model.

## YAML As Current Default

YAML is the current default because it fits the protocol's current goals:

- easy human review
- straightforward nesting
- low punctuation overhead
- natural use in version-controlled text artifacts

This remains a default, not yet a permanent decision.

## Minimal V0

The minimal useful version likely needs only:

1. a package manifest
2. one scoped Frame document
3. explicit `scope`
4. explicit `inherits_from`
5. explicit `visibility`
6. explicit `status`
7. a small section taxonomy
8. optional provenance references

## Open Questions

1. Should one package usually contain one Frame tree or many independent scopes?
2. How strict should override validation be in v0?
3. Which sections are required versus merely allowed?
4. What should Desktop sharing require from Frame metadata?
5. How much schema enforcement should exist before more real examples are authored?
