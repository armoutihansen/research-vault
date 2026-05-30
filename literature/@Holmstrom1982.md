---
citekey: Holmstrom1982
title: Moral Hazard in Teams
authors: ["Holmstrom, Bengt"]
year: 1982
type: journalArticle
doi: 10.2307/3003457
zotero: "zotero://select/library/items/8CBRFWCC"
pdf: /Users/jesper/Zotero/storage/U3KC6LDK/Holmstrom1982.pdf
tags: [literature]
keywords: [moral-hazard, team-production, free-rider-problem, principal-agent, relative-performance-evaluation, sufficient-statistic, contract-theory]
topics: []
related: [Lazear1981, Nalebuff1983]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This article studies moral hazard with many agents. The focus is on two features that are novel in a multiagent setting: free riding and competition. The free-rider problem implies a new role for the principal: administering incentive schemes that do not balance the budget. This new role is essential for controlling incentives and suggests that firms in which ownership and labor are partly separated will have an advantage over partnerships in which output is distributed among agents. A new characterization of informative (hence valuable) monitoring is derived and applied to analyze the value of relative performance evaluation. It is shown that competition among agents (due to relative evaluations) has merit solely as a device to extract information optimally. Competition per se is worthless. The role of aggregate measures in relative performance evaluation is also explored, and the implications for investment rules are discussed.

## Summary
Holmström's foundational paper on multi-agent moral hazard. It establishes two pillars of modern contract theory: (1) under budget balancing, joint production with unobservable effort cannot reach a Pareto-efficient Nash equilibrium (the free-rider/team problem), so the principal's essential function is to *break the budget constraint* via group penalties or bonuses, not to monitor; and (2) an agent's optimal sharing rule should depend on a signal vector only through a *sufficient statistic* for that agent's action — which both grounds and circumscribes relative performance evaluation. The upshot is that competition between agents has no intrinsic value: relative evaluation is worthwhile only when peers' outputs carry information about common (correlated) uncertainty.

## Research question
How should production be organized and incentives designed when many agents supply unobservable inputs to joint output? Specifically: can budget-balanced sharing rules restore efficiency under free riding; what is the principal's true role; and when is relative performance evaluation (comparing an agent to peers, e.g. tournaments or industry benchmarks) valuable?

## Method / identification
A formal principal–agent model with $n$ agents. Each agent $i$ takes an unobservable action $a_i\in A_i=[0,\infty)$ at strictly convex cost $v_i(a_i)$, with $v_i(0)=0$; preferences are additively separable and linear in money, $u_i(m_i,a_i)=m_i-v_i(a_i)$. Actions map to joint output $x(a)$ (increasing, concave, differentiable), allocated via sharing rules $s_i(x)\ge 0$.

Under **certainty**, budget balancing requires $\sum_i s_i(x)=x$ for all $x$, and Pareto optimality $a^\ast=\arg\max[x(a)-\sum_i v_i(a_i)]$. The first-order conditions for a Nash equilibrium, $s_i' x_i' - v_i'=0$, are inconsistent with the optimality conditions $x_i' - v_i'=0$ once $\sum_i s_i'=1$ is imposed — the source of the impossibility.

Under **uncertainty**, output $x(a,\theta)$ is random with conditional distribution $F(x,a)$ and density $f(x,a)$. Three regularity assumptions drive the results: (1) $F$ convex in $a$ (a form of stochastically diminishing returns ensuring global optimality of actions); (2) $F_i(x,a)/F(x,a)\to-\infty$ as $x$ falls to its lower bound (a monotone-likelihood-ratio-type tail condition for penalties); (3) $F_i(x,a)/(1-F(x,a))\to-\infty$ as $x$ rises (the analogous condition for bonuses).

The monitoring analysis introduces a signal vector $y$ with distribution $G(y,a)$, density $g(y,a)$. A function $T_i(y)$ is **sufficient** for $y$ with respect to $a_i$ if $g(y,a)=h_i(y,a_{-i})\,p_i(T_i(y),a)$ — the Fisher–Neyman factorization, but with $a_i$ a strategically chosen parameter rather than a state of nature. A global version uses likelihood-ratio equality across the level sets of $T$.

## Data
None — this is a pure economic-theory paper. Identification is analytical (theorems and proofs), not empirical.

## Key findings
- **Theorem 1 (impossibility):** No budget-balancing sharing rules $\{s_i(x)\}$ yield the efficient $a^\ast$ as a Nash equilibrium when externalities are present. Free riding is inescapable under budget balance.
- **Theorem 2:** Relaxing balance to $\sum_i s_i(x)\le x$ admits efficient equilibria; a step scheme paying $s_i(x)=b_i$ if $x\ge x(a^\ast)$ and $0$ otherwise (a group bonus/penalty) implements first best under certainty, independent of team size.
- **Theorem 3 (highlighted by the reader):** Under Assumptions 1–2, the first best can be approximated arbitrarily closely with group penalties even under uncertainty; the wasted expected residual $\to 0$ as the penalty threshold falls. Endowment constraints generally limit team size unless the output distribution is "tight."
- **Theorem 4:** Under Assumptions 1 and 3, a principal with unbounded wealth can enforce first best at negligible cost via bonuses, even with limited agent endowments.
- **Theorems 5 & 6 (sufficient-statistic characterization):** $s_i$ can be based on $T_i(y)$ without welfare loss *iff* $T_i$ is sufficient; if $T$ is globally insufficient, using all of $y$ yields a strict Pareto improvement — achieved purely through *better risk sharing* while holding actions fixed. This generalizes the informativeness principle of Holmström (1979) and Shavell (1979) and relates to (but is not a corollary of) Blackwell's theorem.
- **Theorem 7:** With $x(a,\theta)=\sum_i x_i(a_i,\theta_i)$ and $x_i$ monotone in $\theta_i$, the optimal $s_i$ depends on $x_i$ alone *iff* outputs are independent. Hence relative performance evaluation is valuable only under common uncertainty; competition per se is worthless and rank-order tournaments are generally informationally wasteful (rank is not sufficient for cardinal output).
- **Theorem 8:** Under normal, independent common factor $\eta$ and idiosyncratic risks, a precision-weighted peer average $\bar{x}$ is a sufficient aggregate — rationalizing benchmarking executives against industry averages.
- **Theorem 9:** As $n\to\infty$, common uncertainty can be inferred away from peer signals, so the team solution converges to the no-common-uncertainty single-agent solution; only idiosyncratic risk remains priced, with implications for investment/diversification rules that depart from standard asset pricing.

## Contribution
Defines the multi-agent moral hazard problem and supplies its two organizing principles: budget-breaking as the principal's essential role (reframing Alchian–Demsetz: the principal is needed as residual claimant/enforcer, not as monitor), and the sufficient-statistic / informativeness condition as the universal criterion for valuable monitoring and relative performance evaluation. It unifies and subsumes contemporaneous tournament results (Lazear–Rosen, Green–Stokey, Nalebuff–Stiglitz) as derivatives of sufficiency, and connects agency theory to financial/asset-pricing normative implications.

## Limitations & open questions
- Assumption 1 ($F$ convex in $a$) is not satisfied by natural specifications such as $x(a,\theta)=(\sum_i a_i)\theta$ with normal $\theta$; it is a technical convenience.
- Theorem 4 relies heavily on risk neutrality and an unboundedly wealthy principal; Holmström conjectures (unverified) that asymptotic risk neutrality suffices.
- Self-imposed group penalties are time-inconsistent (an imperfect equilibrium in Selten's sense) — efficiency requires an outside residual claimant who will not renegotiate and who supplies no productive input.
- Whether the *necessary* part of Blackwell's theorem (incomparability of non-nested information systems) holds in the agency framework is left open.
- **Collusion among agents** under relative performance evaluation may restrict admissible reward structures — explicitly flagged as worth studying.
- **Endogenous monitoring hierarchies:** monitoring technology is taken as exogenous; what determines the choice of monitors, and how output should be shared to incentivize monitors themselves, is posed as a key open problem for the theory of nonmarket organization.

## Connections
Reframes Alchian & Demsetz (1972) on the firm as a monitoring solution. Extends the single-agent informativeness results of Holmström (1979) and Shavell (1979), and the penalty argument of Mirrlees (1974, 1976); related characterizations appear in Grossman & Hart (1983) and Gjesdal (1982). The relative-performance analysis subsumes the tournament models of [[@Lazear1981|Lazear & Rosen (1981)]], Green & Stokey (1983), and [[@Nalebuff1983|Nalebuff & Stiglitz (1983)]]. The sufficient-statistic condition parallels Blackwell's comparison of experiments and the Fisher–Neyman factorization in statistical decision theory. The budget-breaking theme connects to Groves (1973) mechanisms for public goods and to Green (1976) on property rights. It is foundational for later multitasking and team-incentive work, e.g. Holmström & Milgrom (1991).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
