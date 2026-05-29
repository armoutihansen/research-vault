# ADR-0006: Continuous sync via Zotero saved search + live BBT + content-hash manifest

- Status: Accepted
- Date: 2026-05-29

## Context
The system must detect new/changed in-scope items "when prompted." The human-friendly **citekey**
(the note filename and join key) lives in BetterBibTeX, not `zotero.sqlite`. The auto-exported
`library.bib` is stale (509 vs 12k). BBT exposes a live JSON-RPC API (verified): `item.search`
returns CSL-JSON with `citekey`/`abstract`/metadata; `item.attachments(citekey)` returns PDF paths.

## Decision
- Scope is the Zotero **saved search** `Obsidian scope` (ADR-0003).
- `lit-sync` pulls that set **live via BBT JSON-RPC**, resolves PDF paths via `item.attachments`.
- Change detection diffs against `.research/manifest.json`: a **content hash per citekey** over
  metadata + PDF path/mtime. New citekey → create note; changed hash → regenerate AI region only;
  unchanged → skip.

## Consequences
- Always current; no stale-file dependency.
- Requires Zotero running at sync time (acceptable — sync is manual/interactive).
- Manifest is machine state in `.research/` (hidden from Obsidian, tracked in git).

## Alternatives considered
- **sqlite + BBT citekey resolution** — exact `version`/`dateModified` change signal, works without a
  saved search, but schema-brittle and DB-lock-prone.
- **Reconfigured CSL-JSON auto-export file** — fully offline, but auto-export is demonstrably stale.
