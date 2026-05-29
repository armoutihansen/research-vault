# ADR-0005: Managed AI region + protected human region in every generated note

- Status: Accepted
- Date: 2026-05-29

## Context
Notes are regenerated when their source changes (a new PDF, updated metadata, re-clustering). The
user adds their own annotations and must not lose them on regeneration.

## Decision
Every generated note (literature, topic) splits at a fence marker
(`%% ─── below is yours; regeneration never touches it ─── %%`). Everything **above** is agent-owned
and freely regenerable; everything **below** (`## My notes`) is the user's and **never** overwritten.

## Consequences
- One file per object; matches how users annotate in Obsidian.
- Regeneration is safe and idempotent on the AI region.
- Skills must parse the fence and rewrite only the AI region.
- For Layer 2, incremental clustering (ADR-0007) ensures the human region isn't stranded by topic
  merges/splits.

## Alternatives considered
- **Two files** (AI + human) — cleanest separation, but two files per object, more navigation.
- **Full regenerate, annotations in Zotero** — simplest, but clobbers in-vault notes.
