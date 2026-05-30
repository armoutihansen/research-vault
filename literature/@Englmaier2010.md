---
citekey: Englmaier2010
title: Optimal incentive contracts under inequity aversion
authors: ["Englmaier, Florian", "Wambach, Achim"]
year: 2010
type: journalArticle
doi: 10.1016/j.geb.2009.12.007
zotero: "zotero://select/library/items/22YJ8RLX"
pdf: /Users/jesper/Zotero/storage/MMIE5F68/Englmaier2010.pdf
tags: [literature]
keywords: [inequity-aversion, moral-hazard, optimal-contracts, linear-sharing-rules, sufficient-statistics, team-incentives, social-preferences, contract-theory]
topics: []
related: [Bolton2000, Dufwenberg2004, Falk2006, Falk2008, Fehr1999, Itoh2004, Milgrom1981, Rabin1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We analyze the classic moral hazard problem with the additional assumption that agents are inequity averse. The presence of inequity aversion alters the structure of optimal contracts. When the concern for equity becomes more important, there is convergence towards linear sharing rules. The sufficient statistics result is violated. Depending on the environment, contracts may be either overdetermined, i.e. include non-informative performance measures, or incomplete, i.e. neglect informative performance measures. Finally, our model delivers a simple rationale for team based incentives, implying wage compression.

## Summary
Englmaier and Wambach embed Fehr–Schmidt / Bolton–Ockenfels inequity aversion into the canonical Holmström (1979) principal–agent (moral hazard) model. A risk-neutral principal contracts with an inequity-averse agent who dislikes deviations between his own payoff and the principal's. The optimal contract must now trade off three forces rather than two: insurance, incentives, and fairness. Inequity aversion pushes contracts toward linear (and, in the limit, equal-split) sharing rules, breaks Holmström's sufficient-statistics result (so contracts can be overdetermined or incomplete), and rationalizes team-based incentives with wage compression even when tasks are technologically independent.

## Research question
How does the structure of optimal incentive contracts change when the agent in a standard moral-hazard problem has social preferences, specifically inequity aversion over his own versus the principal's payoff? Which classical contract-theoretic predictions (linearity, the sufficient-statistics result, relative performance evaluation) survive, and which empirical regularities does the augmented model explain?

## Method / identification
Pure contract-theoretic analysis. A risk-neutral principal hires an agent whose effort $e$ determines the density $f(x\mid e)$ of profit $x$ on $[\underline{x},\bar{x}]$. The principal maximizes $EU_P=\int f(x\mid e)\,(x-w(x))\,dx$. The agent's additively separable utility is
$$EU_A = \int f(x\mid e)\Big[u\big(w(x)\big) - \alpha\,G\big(x - 2w(x)\big)\Big]dx - c(e),$$
where $u$ is increasing (risk attitude over wealth), $c(e)$ is effort cost with $c'(e)>0$, and $G(\cdot)$ is a convex disutility-from-inequity function with $G(0)=0$, $G'(0)=0$, $G''>0$, weighted by $\alpha>0$. Setting $\alpha=0$ recovers Holmström (1979). The argument $x-2w(x)$ is the gap between the principal's net payoff $x-w(x)$ and the agent's wage $w(x)$. Convexity of $G$ makes the agent averse to lotteries over levels of inequity (the key "insurance against variations in inequity" channel). MLRP ([[@Milgrom1981|Milgrom 1981]]) is assumed; following Innes (1990) the agent can secretly boost or destroy profit, bounding the slope $0\le w'(x)\le 1$. The non-contractible-effort case is solved via the first-order approach (Rogerson 1985; Jewitt 1988), replacing the (IC) with its FOC $0=\int f_e(x\mid e)[u(w(x))-\alpha G(x-2w(x))]dx - c'(e)$. Extensions: an additive purely random profit component $\Pi=x+y$ (overdetermination), an extra informative signal $m$ (incompleteness), and a two-agent team model where agent 1 has separate inequity weights $\alpha_{P1}$ (toward principal, via $G$) and $\alpha_{A1}$ (toward the co-worker, via convex $H$).

## Data
None — this is a theory paper. Section 4 marshals existing empirical/field studies (baseball free agents, police arbitration, theft after wage cuts, sharecropping contracts, profit-sharing plans, team-incentive field experiments) as stylized facts the model rationalizes, but the paper estimates nothing.

## Key findings
- **Proposition 1:** With contractible effort and a risk-neutral agent, the unique optimal contract is linear with slope $\tfrac{1}{2}$ (equal sharing of marginal surplus), since inequity is the only welfare-loss source and is minimized by a constant inequity level. **Corollary 1:** the principal's profit decreases in $\alpha$.
- **Proposition 2:** Contractible effort, risk-averse agent — optimal contract strictly increasing with slope between $0$ and $\tfrac{1}{2}$ (flat-wage insurance motive pulls against the equal-split fairness motive).
- **Proposition 3:** Non-contractible effort, risk-neutral agent — slope strictly between $\tfrac{1}{2}$ and $1$; the franchise ("sell the firm") solution is no longer optimal because residual claimancy generates volatile inequity. Incentives are distorted downward.
- **Proposition 4:** With a risk-neutral agent the optimal contract specifies a more equitable distribution as realized profit rises — fairness becomes an extra incentive instrument (reward good performance by paying more equitably).
- **Propositions 5–7:** Risk-averse, non-contractible case — the contract is strictly increasing (Prop 5); for high enough $\alpha$, MLRP is not needed for monotonicity (Prop 6); as $\alpha\to\infty$ the contract converges to the equal split $w(x)=\tfrac{1}{2}x$ (Prop 7).
- **Proposition 8 / Corollary 2:** The sufficient-statistics result fails. Contracts may be **overdetermined** — conditioning on the uninformative component $y$ because the agent intrinsically cares about total profit distribution — or **incomplete** — as $\alpha\to\infty$ even a superior signal $m$ (one that SOSD-dominates $x$) is asymptotically disregarded in favor of $w(x)=\tfrac12 x$. An amended sufficient-statistics result: condition on variables informative about effort *and* those helping insure against variations in inequity.
- **Proposition 9 / Corollary 3:** Team incentives are rational even for technologically independent tasks; the optimal scheme rewards joint output ($\partial w_i/\partial x_j>0$), not relative performance, and as $\alpha_A\to\infty$ pay rests solely on overall profit — implying wage compression.

## Contribution
Brings social preferences into mainstream contract theory by perturbing the most-cited moral-hazard benchmark (Holmström 1979) with a tractable, convex, continuously differentiable inequity-aversion term, while keeping continuous effort and continuous outcomes. It generates a unified rationale for several real-world phenomena that standard theory struggles with: the prevalence of linear and equal-split sharing (sharecropping), profit sharing extended to workers with negligible influence (overdetermination), incomplete contracts, broad-based team incentives, and wage compression. It also reframes fairness as an additional incentive instrument rather than merely a friction.

## Limitations & open questions
The authors' own highlighted closing passage stresses that the analysis is "only a first step." Explicit open problems: (i) what determines the **reference group** for social comparison, and how to control whom agents compare to so that ill-led comparisons do not produce detrimental outcomes; (ii) implications for the **boundaries of the firm** — e.g., it may be impractical to set up a new in-house division requiring very highly paid hires (who would enter the reference group), favoring a spin-off instead. Modeling choices that bound the results: the convexity (vs. piecewise-linear Fehr–Schmidt) of $G$; inequity defined over realized rather than expected outcomes (the latter would violate the vNM independence axiom, per Kircher et al. 2009); equal split as the fairness reference point; an exogenous outside option that confines the reference group to the firm; a selfish (non-inequity-averse) principal; and reliance on the first-order approach.

## Connections
Builds directly on Holmström (1979) and Holmström (1982) and the sufficient-statistics / relative-performance-evaluation tradition ([[@Milgrom1981|Milgrom 1981]]; Mirrlees 1999). The inequity-aversion primitives are [[@Fehr1999|Fehr & Schmidt (1999)]] and [[@Bolton2000|Bolton & Ockenfels (2000)]]; the broader survey context is Fehr & Schmidt (2003) and Englmaier (2005). Closest prior contract-theory work with social preferences is [[@Itoh2004|Itoh (2004)]] and Dur & Glazer (2008), which restrict to discrete outcomes and binary effort. Related alternative approaches: Hart & Moore (2008) on contracts as reference points (tested by [[@Falk2008|Fehr et al. 2008]]); Englmaier & Leider (2008) on reciprocity (à la [[@Rabin1993|Rabin 1993]]; [[@Dufwenberg2004|Dufwenberg & Kirchsteiger 2004]]; [[@Falk2006|Falk & Fischbacher 2006]]); and Charness & Dufwenberg (2006) on guilt aversion. Linearity results connect to Holmström & Milgrom (1987), Innes (1990), and Bhattacharyya & Lafontaine (1995). Empirical touchstones include Lord & Hohenfeld (1979), Mas (2006), Greenberg (1993), Bewley (1999, 2002), Thaler (1989), Bertrand & Mullainathan (2001), Bandiera et al. (2005), Agell (2004), and Knez & Simester (2001), with the motivating quote from Milgrom & Roberts (1992).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
