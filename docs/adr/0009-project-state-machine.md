# ADR-0009: Project state machine — `status:` property + logged transitions

- Status: Accepted
- Date: 2026-05-29
- Covers decisions: state representation (#5) and transitions (#12)

## Context
Projects move through a lifecycle. State could be encoded as folders or as a property; transitions
could be free edits or audited. The user requires that a rejection reason always be recorded
somewhere.

## Decision
- State is a **`status:` frontmatter property** on notes in a single `projects/` folder. Values:
  `feasibility` → `planned` → `ongoing` → `finished`, with `on-hold` (from planned/ongoing) and
  `rejected` (terminal) as off-ramps. Entry is always `feasibility`.
- dataview/kanban render boards/queries directly from `status`.
- Transitions are made only by the **`project-status`** skill, which sets `status`, stamps `updated`,
  and appends a dated line to the note's **Decision log** (`<date> A → B: <reason>`). A reason is
  **mandatory** for `rejected` and `on-hold`.

## Consequences
- State changes never move files or break wikilinks/git history.
- Every transition is audited; rejection reasons can't be silently lost.
- A live project board comes "for free" from the existing dataview/kanban plugins.

## Alternatives considered
- **Subfolders per state** — visible in the file tree, but churns paths and breaks links.
- **Free-edit property** — simplest, but no audit trail; reasons get lost.
- **GitHub-issue-backed state** — reuses the tracker, but couples/duplicates state in two places.
