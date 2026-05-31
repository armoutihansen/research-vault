# ADR-0015: Open-access bibliographic lookup — a single open-only client for external literature

- Status: Accepted
- Date: 2026-05-31

## Context
The vault is closed: every layer (lit notes → topics → ideas → projects) works only on papers already
in Zotero. But three activities genuinely need *external, newer* literature:
1. **Idea harvesting + vetting** — find recent relevant work, and ground novelty/"closest prior work"
   checks in reality (the max-effort harvest's prior-work flags were LLM recall, i.e. hallucination-prone).
2. **`lit-sync` freshness** — e.g. a working paper in Zotero later becomes a published paper in a
   different version; detect it so the user can update Zotero.
3. **Feasibility check** (Layer 3, deferred) — deep-reads the relevant literature for a promoted idea.

It is explicitly **not** part of `topic-cluster`, which clusters the existing corpus and needs no
external access.

The hard constraint, from the user: be **absolutely certain that nothing is accessed, downloaded, or
stored that they are not allowed to.** Two reference implementations informed the design —
`flonat/claude-research` (a uv MCP biblio server over OpenAlex/Scopus/WoS) and
`Imbad0202/academic-research-skills` (prompt-based skills with tri-index existence verification). The
vault is a **public** GitHub repo, which means storage/redistribution — not just access — is in play.

## Decision

### Risk model: access-first, with a storage-ToS corollary
The binding risk is **access** — never retrieve/download material the user isn't entitled to. PDFs never
enter the repo (notes hold a `pdf:` *path* into Zotero storage, not the file), so full-text
redistribution is moot. Verbatim **abstracts** already live in committed notes (from Zotero) and stay —
abstract redistribution is de minimis / near-universally tolerated; scrubbing them is out of scope. The
one redistribution-adjacent rule that *does* bind: **source terms-of-service on stored metadata** —
which is why only open-data sources are allowed (below).

### The access line: the system never fetches web full-text
The automated system reads only **metadata + abstracts** from the web; **full-text enters only through
the user's Zotero/library** (`lit-sync`'s existing PDF path). When full-text is needed (a note refresh,
a feasibility read), the system **discovers and points** — it emits an **acquire-list** (each paper's
DOI + an open-access link when one exists) — and the **user acquires** it through a channel they're
entitled to use, routing it back via Zotero → `lit-sync`. One pattern across all consumers:
**discover/point (automated, open metadata) → acquire (the user's legitimate action) → read full-text
(local only).** The system never downloads a PDF, open-access or not — eliminating every per-paper "is
this really OA / the right URL / a rogue upload?" judgment call.

### Sources: open on both dimensions only
**OpenAlex** (CC0, keyless — primary: coverage, abstracts, citation graph, OA flags, version locations)
+ **Crossref** (open — DOI metadata and the `is-preprint-of`/`has-preprint` relations that power the
working-paper→published detection) + **RePEc/EconPapers** (econ-specialist; faster than OpenAlex for new
econ working papers; NEP feeds for recency). All three are free to query *and* licensed to store. RePEc
is accessed **only via its sanctioned interfaces** (OAI-PMH gateway, FTP/ReDIF archive, NEP feeds),
**never by HTML scraping**. **Scopus and Web of Science are excluded**: even with the user's
institutional access, their licenses prohibit caching/redistributing their abstracts — unsafe to store
in a public repo. ("Open access" here means *open data we may also store*, not merely *readable*.)

### Form: one deterministic `uv` client is the sole path; agents get no raw web-fetch for papers
A single deterministic client (`biblio`, stdlib + `uv run`, in the project's script idiom alongside
`bbt.py`/`corpus.py`) is the **only** way the system touches external literature. It does **discovery**
(search recent/relevant work) and **verification** (resolve a citation to a real OpenAlex/Crossref
record). The harvest/vetting/lit-sync agents are **not** handed raw `WebSearch`/`WebFetch` for papers.
(An MCP-server form — `flonat`'s route — was rejected as operational overhead a single-user vault
doesn't need; the same client can be wrapped as MCP later. A prompt+protocol form — `Imbad`'s route —
was rejected because it makes safety *behavioral*, not enforced.)

### Verification: external citations must be real before they're surfaced or stored
Any *externally-sourced* citation an agent emits — every acquire-list entry, every "prior work" claim in
a dossier — must pass existence-verification (`verify(doi | title+authors+year)` against
OpenAlex/Crossref) before it is asserted or stored; unverified ones are shown as **"⚠ unverified — may
not exist,"** never as fact. This grounds the novelty checks that were previously LLM recall, and keeps
the acquire-list from sending the user after phantom papers. (The vault's own citations are already
grounded in real PDFs, so this targets agent-generated/external claims.)

### Enforcement: hard-open by construction + a backstop hook
- **Layer 1 (client):** the `biblio` client only constructs requests against an **allowlist** of the
  three sources' API hosts, returns **metadata/abstracts only**, and **refuses any full-text/PDF URL**.
  The sanctioned path cannot breach the line.
- **Layer 2 (backstop):** a `PreToolUse` hook **blocks `WebFetch` of PDF / known-publisher-full-text
  URLs** (scoped, so ordinary non-paper fetches still work), so even a non-compliant agent physically
  cannot pull a paper off the web.

### Scope boundary
This ADR covers the **external-literature** capability (open discovery + verification + acquire-list)
and its consumers: **idea harvesting/vetting** and **`lit-sync` freshness**. It is **not** used by
`topic-cluster`. The vault-internal **citekey-migration** that the freshness case hands off to (rename
`@old.md`→`@new.md`, rewrite inbound `related:`/`topics:`/`area:`/citation links, update manifest +
`topic_state`, regenerate from the new PDF) has **no external-access dimension** and is a separate
`lit-sync` capability with its own future ADR — this ADR only names the hand-off.

## Consequences
- "Is this open access?" stops being a per-paper question: the system only ever pulls open, storable
  metadata/abstracts, and never full-text — open by construction, enforced by allowlist + hook.
- Novelty/prior-work claims become grounded (real existence checks) instead of hallucination-prone recall.
- Newer literature flows into idea work and freshness detection without widening the access surface.
- Full-text always routes through the user + Zotero, so acquisition stays legitimate and the library
  stays the single full-text home — at the cost of a manual "acquire these" step (the acquire-list).
- RePEc's OAI-PMH is cumbersome, so econ-recency coverage is a fast-follow behind OpenAlex+Crossref.

## Alternatives considered
- **Gated OA full-text fetch** (download only OpenAlex `is_oa` URLs) — convenient, but reintroduces the
  per-paper "really OA? right URL?" uncertainty the user wants gone; OA flags are occasionally wrong.
- **MCP biblio server** (`flonat`) — clean tool surface, but a separate server to run/maintain; a uv
  client enforces the same invariant with less overhead and fits the existing script idiom.
- **Prompt + protocol docs** (`Imbad`) — flexible, but safety becomes agent-compliance rather than
  enforced; incompatible with "absolutely certain."
- **Include Scopus/WoS** (`flonat` offers them) — better coverage, and the user is licensed to *access*
  them, but their ToS forbids storing/redistributing abstracts in a public repo. Excluded.
- **Scrubbing verbatim abstracts from committed notes** — maximal redistribution caution, but abstract
  redistribution is de minimis and the user judged it a non-concern; not worth a 469-note migration.
- **Scraping IDEAS/EconPapers HTML for RePEc** — easiest to code, but a ToS/etiquette breach; use the
  sanctioned OAI-PMH/FTP/NEP interfaces instead.
