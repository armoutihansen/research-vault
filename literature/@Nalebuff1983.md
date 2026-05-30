---
citekey: Nalebuff1983
title: "Prizes and incentives: towards a general theory of compensation and competition"
authors: ["Nalebuff, Barry J.", "Stiglitz, Joseph E."]
year: 1983
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/MFX4F75Z"
pdf: /Users/jesper/Zotero/storage/834FPWC8/Nalebuff and Stiglitz - 1983 - Prizes and incentives towards a general theory of.pdf
tags: [literature]
keywords: [tournaments, relative-performance-pay, principal-agent, moral-hazard, contest-design, incentive-theory, sufficient-statistic]
topics: []
related: [Lazear1981]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This article analyzes the role of competitive compensation schemes (in which pay depends on relative performance) in economies with imperfect information. These compensation schemes have desirable risk, incentive, and flexibility properties; they provide for an automatic adjustment of rewards and incentives in response to common changes in the environment. When environmental uncertainty is large, such schemes are shown to be preferable to individualistic reward structures; in the limit, as the number of contestants becomes large, expected utility may approach the first-best (perfect information) level. We study the design of contests, including the optimal use of prizes versus punishments and absolute versus relative performance standards. The analysis can also be viewed as a contribution to the multiagent, single-principal problem. (Zotero abstract field empty; transcribed verbatim from the journal's printed abstract.)

## Summary
A foundational theory paper on the use of relative-performance ("competitive") compensation — rank-order tournaments and contests — as an incentive device when a principal cannot observe agent effort and output is contaminated by a *common* environmental shock plus *idiosyncratic* noise. The central insight is that contests provide automatic *flexibility*: because a common shock raises (or lowers) everyone's output together, relative rankings filter it out, so the same reward structure remains incentive-compatible across environments without renegotiation. The authors derive a "cornerstone equation" for contest equilibria, characterize optimal prizes versus penalties, and show that with many contestants well-designed schemes can approach the first-best, while pinning down when contests beat individualistic piece rates.

## Research question
When is it optimal to base an agent's compensation on *relative* performance (ordinal rank) rather than on *individualistic* output (piece rates, quotas)? More specifically: how should contests be designed (prizes vs. penalties, absolute vs. relative standards, single vs. multiple prizes, winning "by a gap"), and under what conditions do they dominate individualistic schemes in a competitive, zero-profit, imperfect-information economy?

## Method / identification
A formal principal–agent (single principal, $n$ identical risk-averse agents) model under moral hazard. Agent $i$'s output is a random function of effort, $Q_i = G(\mu_i, \theta, \varepsilon_i)$, with $\theta$ a *common* environmental shock and $\varepsilon_i$ idiosyncratic noise; most analysis uses the linear form $Q_i = \mu_i\theta + \varepsilon_i$ with $E[\theta]=1$. The contract is signed before $\theta,\varepsilon$ realize; the agent privately observes $\theta$ then chooses unobservable effort $\mu$. Preferences are additively separable, $W = E[U(Y) - V(\mu(\theta))]$, with $U'>0, U''<0, V'>0$. The principal is constrained to zero expected profit (competitive market), so total prizes equal total expected output. For a two-person rank-order tournament, define a safe income $\bar Y = E[Q_i]$ and a spread $x$, giving expected utility $W = PU(\bar Y + x) + (1-P)U(\bar Y - x) - E[V(\mu)]$, where $P(\mu_1,\mu_2,\theta)$ is the win probability. Differentiating the win probability at the symmetric equilibrium $\mu_1=\mu_2$ yields the marginal incentive $\theta\bar g$, where $\bar g = E[g(\varepsilon)]$ is the expected noise density. The analysis is comparative-statics / optimal-design throughout (first-order and second-order conditions, mean-preserving spreads), with worked examples for normal and other error distributions. No estimation; this is pure theory.

## Data
None — this is a theoretical contribution. Identification comes from the structure of the model, not from data; illustrative parametric examples (quadratic disutility, normal noise, specific bounded densities) substitute for empirics.

## Key findings
- **Cornerstone equation of contests** (eq. 17): in the symmetric equilibrium, $\theta\,\Delta U\,\bar g = V'(\mu(\theta))$, where $\Delta U = U(\bar Y+x) - U(\bar Y-x)$. Effort tracks $\theta$ while expected income does not — this is the *flexibility* property.
- **Theorem 1 (sufficient statistic / independence):** when outputs are independent ($\sigma_\theta^2 = 0$, i.e. no common shock), observing rivals conveys nothing about an agent's effort and the optimal scheme is *individualistic*. With a common shock, a sufficient statistic $T(Q)$ (e.g. average output $\bar Q$ with many agents) optimally enters compensation, $Y_i = Y_i(Q_i, T(Q))$.
- **Theorem 2:** a larger prize motivates greater effort and raises mean income ($d\bar Y/dx > 0$).
- **Theorem 3:** the second-best contest *undersupplies* effort relative to what would raise welfare at the chosen prize — yet (point 4 of the summary) contests can induce *more* effort than the first-best under decreasing absolute risk aversion, because risk-bearing pushes agents to work harder.
- **Theorem 4 (nonconvexity):** as noise variance $\to 0$, the marginal return to effort $\bar g \to \infty$, prizes shrink, and *no symmetric pure-strategy equilibrium* exists — "a mile is as good as a miss," so a shirker is sure to lose but saves all effort cost.
- **Theorem 5:** with quadratic disutility, welfare is increasing in $\mathrm{Var}(\theta)$; mean-preserving spreads in $\theta$ raise contest welfare and depend on $\theta$ only through its first two moments ($dW/dE[\theta^4]=0$).
- **Theorem 6 (winning by a gap):** ranking agent $i$ above $j$ only if output exceeds by a gap $\gamma$ strictly improves welfare when the noise density at the margin exceeds its mean ($g(\underline\varepsilon) > \bar g$); gaps lower the probability a prize is paid while preserving marginal incentives, and aid contest sustainability.
- **Prizes vs. penalties with large $n$:** with one prize to the top, the nonconvexity persists and shirking is attractive; a *penalty to the lowest-ranked* agent restores a pure-strategy Nash equilibrium and lets welfare approach the first-best as $n \to \infty$, because shirking shifts marginal errors toward the high-density region, raising the chance of being penalized.
- **Contests vs. piece rates:** with risk-neutral agents both achieve first-best ($a=1$ piece rate; $x^* = 1/(2\bar g)$ contest). With quadratic risk aversion, a contest beats a linear piece rate iff $\sigma_\varepsilon^2 + b^2\mathrm{Var}(\theta^2) > 1/(4\bar g^2)$ — contests win when common environmental variance is large.
- **Multiple-prize tournaments:** cannot in general replicate nonlinear individualistic schemes (the marginal incentives differ), and in the worked examples optimal contests use at most three distinct prizes even when $n$ are available.

## Contribution
Provides a *general* theory unifying and extending the then-nascent tournament literature ([[@Lazear1981|Lazear–Rosen 1981]], Stiglitz 1975, Green–Stokey 1981, Holmström 1982). It is among the first to articulate the flexibility/insurance rationale for relative-performance pay — relative evaluation filters out common shocks, automatically adjusting incentives without costly recontracting — and to systematically analyze contest *design*: prizes vs. penalties, the gap refinement, large-$n$ asymptotics toward first-best, and conditions under which contests dominate piece rates and quotas. It also frames the exercise as a contribution to the multiagent single-principal problem and connects relative-performance evaluation to the sufficient-statistic logic of optimal contracting.

## Limitations & open questions
- Most results assume **identical agents** and abstract from screening/sorting by ability; the authors note handicapping is needed when abilities differ and that "a sure loser destroys everyone's incentives."
- Output is mostly **linear in effort**; Section 14 shows tournaments may or may not replicate first-best marginal incentives once output is nonlinear (they give an example of each).
- The **nonconvexity / nonexistence of pure-strategy equilibria** at low noise is only partly resolved (penalties, gaps, asymmetric equilibria); a full characterization of mixed-strategy equilibria is left open.
- Contests give **no incentive to cooperate** and may reward mutually destructive sabotage — a serious concern under technological returns to cooperation (e.g. patent races, information sharing).
- The authors flag a puzzle: competitive compensation "seems less widespread than their evident advantages would suggest," conjecturing unmodeled **worker-satisfaction / social-incentive** factors (disapproval, fairness, group homogeneity) — explicitly an open empirical/behavioral hook.
- Whether contests dominate even *nonlinear* piece rates as $\mathrm{Var}(\theta)$ grows is sketched but not fully generalized.

## Connections
Builds directly on [[@Lazear1981|Lazear & Rosen (1981)]] on rank-order tournaments as optimum labor contracts and on Stiglitz (1975) on hierarchy, incentives, and risk; contrasts the additively-separable utility specification here with the Lazear–Rosen $W = E[U(Y - V(\mu))]$ form. Closely related to Green & Stokey (1981) on tournaments versus contests and to Holmström (1982) on moral hazard in teams and the sufficient-statistic / informativeness principle; the independence result echoes Holmström's informativeness logic and Grossman & Hart (1983) on the principal–agent problem. The flexibility argument parallels Stiglitz (1974) on sharecropping as risk-sharing under moral hazard. Connects to Mirrlees (1974, 1975) on near-first-best implementation via large penalties (which the authors qualify, correcting an over-extension to "high but unlikely bonuses"). The cooperation/sabotage and social-incentive discussion draws on Akerlof (1976) on the rat race and Akerlof & Soskice (1976) on sanctions. The multi-project efficiency-loss point references Nalebuff & Varian (1981); risk-ordering uses Rothschild & Stiglitz (1970) on increasing risk.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
