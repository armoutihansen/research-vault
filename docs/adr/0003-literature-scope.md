# ADR-0003: Literature-note scope = PDF-bearing items + `to-note` tag

- Status: Accepted
- Date: 2026-05-29

## Context
The Zotero library has 12,224 items, but only ~481 have PDFs, and ~11,700 are a May-2026 bulk import
(abstracts only, not filed). Generating notes for all 12k is mostly low-value stubs of un-triaged
items. The curated, PDF-bearing ~481 are the genuine working bibliography and the only set we can
write *deep* notes for.

## Decision
Layer-1 scope = **items with a PDF attachment** (~481) **OR** items tagged **`to-note`** in Zotero.
Scope is encoded declaratively as a Zotero **saved search** named `Obsidian scope`. The bulk firehose
is excluded until triaged.

## Consequences
- Self-maintaining: attach a PDF (or add `to-note`) → item enters scope automatically.
- Enables deep, full-text notes (every in-scope item has text to read).
- Scope is steered from Zotero, where the user already curates.

## Alternatives considered
- **A designated collection/saved search of arbitrary items** — max control, but only 91 items are
  filed today (the saved-search-by-rule approach subsumes this).
- **All curated (~536) regardless of PDF** — slightly broader; abstract-only where no PDF.
- **All 12,224** — huge cost; mostly shallow stubs of un-triaged items.
