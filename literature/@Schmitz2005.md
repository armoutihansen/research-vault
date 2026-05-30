---
citekey: Schmitz2005
title: Allocating control in agency problems with limited liability and sequential hidden actions
authors: ["Schmitz, Patrick W."]
year: 2005
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/X3CAFB68"
pdf: /Users/jesper/Zotero/storage/M9AZCBFI/Schmitz - 2005 - Allocating control in agency problems with limited.pdf
tags: [literature]
keywords: [moral-hazard, limited-liability, control-allocation, sequential-agency, integration-vs-separation, complete-contracting, renegotiation]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Schmitz studies when a principal should put a single agent in control of both stages of a sequential project (integration) versus assigning each stage to a different agent (separation). Working in a pure moral-hazard, complete-contracting framework with risk-neutral but cash-constrained agents, he shows that both organizational modes can be rationalized purely by incentive considerations, without invoking hold-up, limited commitment, or ad hoc restrictions on contracts. The key new force is that a first-stage success makes second-stage effort more effective, which lowers the rent needed in the second stage; under integration this tempts the agent to sabotage the first stage to inflate his later rent, making separation attractive when stakes are high, while a "rent-saving" effect favors integration when stakes are low.

## Research question
Should control over two sequential tasks of a project be allocated to the same agent (integration) or split across two agents (separation), when effort is a hidden action but control is contractible, agents have limited liability, and a first-stage success raises the productivity of second-stage effort?

## Method / identification
The paper builds a two-stage principal-agent game with one principal $P$ and up to two identical, risk-neutral, wealth-less agents, solved by backward induction under complete contracting (mechanism design), so no ad hoc contract restrictions are imposed. In stage 1 (date 1), agent $A$ chooses hidden effort $e_1\in\{0,1\}$ at cost $c_1 e_1$; the verifiable outcome $x_1=1$ occurs with probability $pe_1$, so a failure is certain if the agent shirks. In stage 2 (date 2), the agent in charge (the same $A$ under integration, or a separate $B$ under separation) chooses hidden effort $e_2\in\{0,1\}$ at cost $c_2 e_2$. The innovation $x_2=1$ occurs with probability $q$ if he shirks and $r$ if he works, where the productivity of effort depends on the first-stage outcome: $r=r_1$ after a success and $r=r_0$ after a failure, with $q<r_0<r_1<1$. The principal's value of the innovation is $V$, realized only on $x_2=1$.

Contracts specify limited-liability wages $w^i_{x_1 x_2}\ge 0$ conditioned on verifiable outcomes; the target effort profile is $e=(e_1,e_2(0),e_2(1))$. The driving observation is that the limited-liability rent needed to induce second-stage effort is $qc_2/(r-q)$, which is larger after a failure (since $r_0<r_1$). Incentive-compatibility for the second stage requires $(r_\ell-q)(w_{\ell 1}-w_{\ell 0})\ge c_2$ for $\ell\in\{0,1\}$. Under integration, the first-stage IC constraint folds in expected continuation rents, creating the temptation to shirk in stage 1 to secure the higher post-failure rent. Assumption 1 restricts attention to the case where the principal always wants high first-stage effort. Extensions analyze collusion via a Tirole-style "leaky bucket" side contract (fraction $\lambda\in(0,1)$ of bribes transmitted), conditional control (assigning the second stage to $A$ or $B$ depending on $x_1$), asymmetric second-stage costs $c_2^A<c_2^B$, and renegotiation (principal cannot commit not to re-offer contracts at date 2).

## Data
None - this is a theoretical contract-theory paper. Motivating institutional examples (Bell Labs, the German Research Center for AI, San Diego congestion pricing, NASA contracting) are cited illustratively, not as data.

## Key findings
Lemma 1 and Lemma 2 derive the optimal limited-liability contracts and profits under separation and integration for the two relevant effort targets $e=(1,0,1)$ and $e=(1,1,1)$. When the principal induces second-stage effort only selectively (after success), integration is optimal because the single agent works in stage 1 simply to preserve his second-stage rent (rent-saving). When she induces second-stage effort unconditionally, $e=(1,1,1)$, separation is strictly cheaper because under integration she must inflate the success-success wage to deter first-stage sabotage. Proposition 1 makes this precise: separation is preferred iff $V$ exceeds the cutoff $\frac{1}{(1-p)(r_0-q)}c_1+\frac{r_0}{(r_0-q)^2}c_2$, and integration otherwise; since effort is hidden, these are strict preferences (first-best is indifferent). Remark 1 shows the result survives collusion, with a larger cutoff. Proposition 2 (conditional control) shows that if control can be switched on $x_1$, the principal sets $j_0=B, j_1=A$ — switching to $B$ after a failure — preferring integration only for small $V<r_0c_2/(r_0-q)^2$. Proposition 3 extends to asymmetric costs $c_2^A<c_2^B$, raising the cutoff but preserving the qualitative result. Proposition 4 shows that under no-commitment to renegotiation the main results hold (with cutoff $r_0c_2/(r_0-q)^2$), and Corollary 1 gives the striking result that the principal may deliberately choose an inferior project ($V_2<V_1$) as a commitment device. Proposition 5 combines renegotiation with asymmetric costs.

## Contribution
The paper provides a unified complete-contracting moral-hazard explanation of both integration and separation of control in sequential agency problems. The novel mechanism — that separation can be optimal because of a "technological diseconomy," where a first-stage success lowers the second-stage rent and thereby tempts an integrated agent to sabotage early stages — is new relative to the task-assignment and job-design literature, which had emphasized only rent-saving economies of scope. It contrasts sharply with incomplete-contracting/hold-up explanations of organizational boundaries by deriving divided control without restricting contracts or assuming non-commitment, and connects wealth/limited-liability rents to renegotiation-proofness.

## Limitations & open questions
The author explicitly notes that binary effort and a binary verifiable signal are simplifying assumptions, suggesting (via Demougin and Fluet) that a binary statistic suffices and that richer effort spaces could be explored. He flags that the analysis does not pin down whether agents are employees within a firm or managers across firms — the logic is silent on firm boundaries — and that connecting the right to control an action to ownership of an asset, which would let the model speak to property-rights/incomplete-contracting questions, "so far has not been addressed in the literature... and awaits further research." The treatment of collusion relies on a specific leaky-bucket enforcement technology, and the alternative formulation where a first-stage success lowers $c_2$ rather than raising $r$ is only asserted to give qualitatively similar results.

## Connections
The paper situates itself against the incomplete-contracting / hold-up tradition of Grossman & Hart (1986) and Hart & Moore (1999), and explicitly against Hart, Shleifer & Vishny on public-private partnerships (bundling building and running a prison). It builds on Tirole (1999) on R&D and complete-contracting tools, and on Tirole (1992) for the leaky-bucket collusion model. The task-assignment and job-design literature it extends includes Holmström & Milgrom (1991), Itoh (1992), Hemmer (1995), Dana (1993), Gilbert & Riordan (1995), and Severinov (1999), with related economies-of-scope results in Baron & Besanko (1992), Che & Yoo (2001), and Laffont & Martimort (2002). It relates to Lewis & Sappington and Aghion & Tirole (1997) on information acquisition, Aghion, Dewatripont & Rey (2001) on contractible control actions, and the ratchet-effect literature (Laffont & Tirole 1993; Meyer 1995). The author's companion work — Schmitz (2002a, 2002b, 2005) and Rosenkranz & Schmitz (2003) — develops related two-stage R&D and renegotiation models, and Nöldeke & Schmidt (1998) is cited for control switching in incomplete-contracting settings.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
