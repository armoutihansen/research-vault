# ADR-0010: Vault = thinking & state; execution hands off to per-project repos

- Status: Accepted
- Date: 2026-05-29

## Context
"Human–AI collaborative research" includes executing projects, not only identifying them. The user
already works in dedicated repos per project (`pred_comp_soc_pref`, `predictive-completeness`,
`efficiency-wages`). The research-vault was set up with a GitHub issue tracker.

## Decision
The vault owns **identification → state → thinking** (literature, topics, ideas, project notes,
decisions). When a project reaches `planned`/`ongoing`, execution hands off to a **dedicated
execution repo** (code/data/paper), recorded in the project note's `repo:` property; task-level
tracking lives there. The **research-vault's own GitHub issues are reserved for building/evolving the
vault system itself** — the use case for the configured `to-prd`/`to-issues`/`triage` skills.

## Consequences
- Clean split: vault = thinking & state, project repo = doing.
- Matches the user's existing repo-per-project workflow.
- The vault stays focused; it doesn't accumulate research-task issues.

## Alternatives considered
- **Vault issues drive execution** (`to-prd`→`to-issues` on the vault) — tightest integration, but
  mixes research tasks with vault-dev issues and fits code/data work poorly.
- **Hybrid, case-by-case** — flexible, but the boundary must be decided each time.
