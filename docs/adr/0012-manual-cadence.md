# ADR-0012: All skills run manually / when prompted

- Status: Accepted
- Date: 2026-05-29

## Context
The user framed literature-note refresh as happening "when prompted." Scheduled runs would need
Zotero running at a fixed time and would write to the knowledge base unattended.

## Decision
Every skill is **invoked explicitly** by the user (`/lit-sync`, `/topic-cluster`, …). Nothing runs on
a schedule for now. Scheduling (via the `schedule`/`loop` skills) can be added later once the output
is trusted.

## Consequences
- Full human control over a knowledge base where note quality matters.
- No dependence on background processes or Zotero being up at a set time.
- Re-evaluate once `lit-sync` output is trusted (revisit candidate; not binding).

## Alternatives considered
- **Manual + scheduled `lit-sync`** — convenient, but unattended writes + Zotero-uptime dependency.
- **Aggressive automation** (scheduled sync + auto-clustering) — hands-off, but autonomous edits to
  the knowledge base without a human in the loop.
