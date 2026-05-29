# ADR-0006: Continuous sync via Zotero saved search + live BBT + content-hash manifest

- Status: Accepted
- Date: 2026-05-29

## Context
The system must detect new/changed in-scope items "when prompted." The human-friendly **citekey**
(the note filename and join key) lives in BetterBibTeX, not `zotero.sqlite`. The auto-exported
`library.bib` is stale (509 vs 12k). BBT exposes a live JSON-RPC API (verified): `item.search`
returns CSL-JSON with `citekey`/`abstract`/metadata; `item.attachments(citekey)` returns PDF paths.

## Decision
- Scope is the predicate **(has PDF) ∪ (tag `to-note`)** (ADR-0003). Optionally surface it as a Zotero
  saved search `Obsidian scope` for a human-curatable view — but that is **not load-bearing**: BBT has
  no saved-search-by-name enumeration (verified — no `system.listMethods`, and `item.search` is
  term-based).
- `lit-sync` **enumerates** the in-scope list by replicating the predicate against `zotero.sqlite`
  (read-only copy), or the on-demand-refreshed `library.bib` (which already ≈ the curated PDF set,
  with citekeys + file paths).
- `lit-sync` then **enriches each item live via BBT JSON-RPC**: `item.search`/export for
  citekey + abstract + metadata; `item.attachments(citekey)` for the current PDF path **and the user's
  highlight annotations** (usable to seed/weight the note).
- Change detection diffs against `.research/manifest.json`: a **content hash per citekey** over
  metadata + PDF path/mtime. New → create; changed → regenerate AI region only; unchanged → skip.

## Validation (2026-05-29)
- `item.attachments("Bruhin2019")` → returns PDF path **and** annotation highlights. ✓
- `item.search("…")` → CSL-JSON with `citekey` / `abstract` / metadata. ✓
- `system.listMethods` unsupported; no saved-search enumeration → sqlite/bib for the list, BBT for
  enrichment.

## Consequences
- Enrichment is always current; the list comes from a local read.
- Enumeration needs no Zotero uptime; enrichment does need Zotero running (fine for manual sync).
- The user's existing highlights become available to the note writer — a bonus signal.
- Manifest is machine state in `.research/` (hidden from Obsidian, tracked in git).

## Alternatives considered
- **Live saved-search pull via BBT** (the original Q7 framing) — not possible: BBT can't enumerate a
  saved search by name. Reduced to the optional human-facing view above.
- **Reconfigured CSL-JSON auto-export file** — fully offline, but the existing auto-export is stale.
