# ADR-0008: Project ideas live in topic notes; promotion to projects is human-gated

- Status: Accepted
- Date: 2026-05-29

## Context
The payoff of the system is research-project idea creation. Ideas derive from the accumulated
*Limitations & open questions* of a topic's papers and cross-paper tensions. The user described
ideas as entering the project lifecycle at a feasibility-check state.

## Decision
Each topic note has a **Candidate ideas** section the `topic-cluster` agent populates (each idea: a
one-line pitch + which lit notes motivate it). Ideas become projects only via the human-gated
**`promote-idea`** skill, which creates `projects/<slug>.md` at `status: feasibility`, linked to the
topic and source papers. There is **no `idea` project status** — ideas are a pre-project concept.

## Consequences
- Ideas stay contextualized where they were born; nothing becomes a "project" without explicit go.
- Fits the collaborative model and the lifecycle entry point (ADR-0009).

## Alternatives considered
- **Dedicated `ideas/` notes** — own space to develop, but a fourth folder and more objects.
- **Direct to `projects/` at `status: idea`** — fewer layers, but fills `projects/` with raw,
  unfiltered ideas and adds a state.
