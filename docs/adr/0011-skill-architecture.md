# ADR-0011: Skills as entry points + deterministic helper scripts + Workflow fan-out

- Status: Accepted
- Date: 2026-05-29

## Context
The system needs reliable mechanical I/O (BBT calls, manifest diffing, PDF extraction) and
judgment-heavy steps (summarizing, clustering, synthesizing ideas), some over many items at once
(backfilling ~481 papers, assigning N notes).

## Decision
Each capability is a **Claude Code skill** in `.claude/skills/` (the user-facing entry point:
`/lit-sync`, `/topic-cluster`, `/promote-idea`, `/project-status`). The mechanical, must-be-reliable
parts live in **deterministic helper scripts** (Python/shell) the skills call — no LLM, testable.
Bulk LLM work **fans out via the Workflow tool**, one agent per paper/note. This matches the existing
Matt Pocock skill pattern in the repo.

## Consequences
- Brittle I/O is deterministic and unit-testable; the LLM is used only where judgment is needed.
- Parallel scale for backfills via fan-out.
- Discoverable slash-command entry points.

## Alternatives considered
- **Pure prompt-driven skills** (instructions only) — simpler to author, but non-deterministic I/O
  and slower at scale.
- **Subagents, no skills** — no slash-command entry points, less discoverable.
