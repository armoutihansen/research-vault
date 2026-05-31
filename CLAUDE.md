# research-vault

A human–AI collaborative research system: a standalone, git-versioned Obsidian vault that turns a
Zotero library into literature notes → emergent topic notes → research projects with a tracked
lifecycle.

- **Vocabulary:** [`CONTEXT.md`](CONTEXT.md) — canonical domain terms; use them, don't drift.
- **Design:** [`docs/architecture.md`](docs/architecture.md) — full design, data flow, build order.
- **Decisions:** [`docs/adr/`](docs/adr/) — one ADR per architectural choice.

## Python

Run **all** Python via **`uv run python …`**, never bare `python3`. The interpreter and the one
third-party dep (`networkx`, for topic-cluster's Louvain prior) are pinned in `pyproject.toml` /
`uv.lock`; `uv run` provisions the `.venv` (gitignored) on first use. Skill scripts are otherwise
standard-library; bare `python3` mostly works but is off-environment and skips networkx.

## Agent skills

### Issue tracker

Issues and PRDs are tracked as GitHub issues in `armoutihansen/research-vault` via the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

Canonical triage labels — `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `CONTEXT.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.
