---
citekey: Brunnermeier2005
title: Optimal Expectations
authors: ["Brunnermeier, Markus K.", "Parker, Jonathan A."]
year: 2005
type: journalArticle
doi: 10.1257/0002828054825493
zotero: "zotero://select/library/items/YJCGHWT5"
pdf: /Users/jesper/Zotero/storage/HRLJJQ2W/Brunnermeier2005a.pdf
tags: [literature]
keywords: [optimal-expectations, anticipatory-utility, overconfidence, subjective-beliefs, skewness-preference, heterogeneous-priors, life-cycle-consumption, behavioral-finance]
topics: []
related: [Akerlof1982, Caplin2001]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper introduces a tractable, structural model of subjective beliefs. Forward-looking agents care about expected future utility flows, and hence have higher current felicity if they believe that better outcomes are more likely. On the other hand, biased expectations lead to poorer decisions and worse realized outcomes on average. Optimal expectations balance these forces by maximizing average felicity. A small bias in beliefs typically leads to first-order gains due to increased anticipatory utility and only to second-order costs due to distorted behavior. We show that in a portfolio choice problem, agents overestimate the return on their investment and exhibit a preference for skewness. In general equilibrium, agents' prior beliefs are endogenously heterogeneous. Finally, in a consumption-saving problem with stochastic income, agents are both overconfident and overoptimistic.

## Summary
Brunnermeier and Parker propose **optimal expectations (OE)**: a structural, disciplined theory of subjective beliefs in which an agent's prior is *chosen* (subconsciously, once and for all) to maximize well-being — the objective time-average of expected felicity. Because forward-looking agents derive *anticipatory utility* from believing good outcomes are likely, optimism raises current felicity (first-order gain) while distorting actions only at second-order cost. The framework endogenizes optimism, overconfidence, preference for skewness, heterogeneous priors, and undersaving from a single optimization principle, and rationalizes several finance and consumption puzzles.

## Research question
Can a single, disciplined optimization principle for *prior beliefs* — rather than the rational-expectations / common-priors assumptions — generate the systematic belief biases documented in psychology (overoptimism, overconfidence) and simultaneously explain observed economic anomalies (skewness preference, underdiversification, the equity premium, declining life-cycle consumption)? What beliefs maximize an agent's well-being when expectations about the future themselves enter present felicity?

## Method / identification
A two-stage structural model. **Stage 1 (optimization given beliefs):** in a canonical finite-state dynamic problem, the agent holds subjective conditional probabilities $\hat{\pi}(s_t\mid \bar{s}_{t-1})$ and chooses controls $c_t$ to maximize *felicity* — the subjectively-expected present discounted value of flow utilities, $\hat{E}[U(c_1,\dots,c_T)\mid \bar{s}_t]$ — which decomposes into memory, current-flow, and *anticipatory* utility. Subjective probabilities must satisfy Assumption 1: sum to one, be non-negative, respect the law of iterated expectations, and assign zero probability only to objectively impossible states ($\hat{\pi}=0$ if $\pi=0$, so agents understand the model but misperceive odds).

**Stage 2 (optimal beliefs):** optimal expectations are the $\{\hat{\pi}^{OE}\}$ that maximize **well-being**, the *objective* expected time-average of felicity:
$$W := E\!\left[\frac{1}{T}\sum_{t=1}^{T}\hat{E}[U(c_1^*,\dots,c_T^*)\mid \bar{s}_t]\right]$$
subject to Assumption 1. Beliefs are fixed once-and-for-all, so the law of iterated expectations holds for $\hat{\pi}$ and standard dynamic programming applies; equivalently the agent is endowed with an optimal prior and is fully Bayesian thereafter. A **competitive optimal expectations equilibrium** adds market clearing and that each agent's beliefs are optimal taking aggregate dynamics as given. The framework is then applied to three canonical settings: (i) a two-period, two-asset portfolio problem; (ii) a continuum-agent exchange economy with no aggregate risk; (iii) a multi-period consumption-saving problem with i.i.d. stochastic income and quadratic (certainty-equivalent) utility.

## Data
None — this is a pure theory paper. The authors discipline and validate the model qualitatively against existing empirical regularities and surveys: overconfidence evidence (Lichtenstein-Fischhoff-Phillips; Alpert-Raiffa), pari-mutuel horse-betting odds (Golec & Tamarkin 1998), home-bias and pension underdiversification (Lewis 1999; Poterba 2003), trading-volume patterns (Chen, Hong & Stein 2001), and desired vs. actual life-cycle consumption profiles (Barsky-Juster-Kimball-Shapiro 1997; Gourinchas & Parker 2002; Attanasio 1999).

## Key findings
- **Proposition 1 (excess risk-taking due to optimism):** optimal beliefs are biased upward for states where the chosen portfolio pays off positively; the OE agent invests *more aggressively* than the rational agent ($\alpha^{OE}>\alpha^{RE}$) or takes the opposite position.
- **Proposition 2 (preference for skewness):** for unbounded utility, even when $E[Z]<0$, there is a range of probabilities for which the agent is optimistic and *holds* the positively-skewed asset — buying lottery-like, negative-expected-return bets. OE agents hold underdiversified portfolios.
- **Proposition 3 (heterogeneous beliefs and gambling):** an OE equilibrium exists; with $S>2$ states and no aggregate risk, priors are *endogenously heterogeneous* — some agents optimistic and long, others pessimistic and short — so agents gamble against one another despite full insurance being feasible. A worked example yields a **1.4% higher equity premium** than rational expectations for negatively-skewed returns (and lower premium for positively-skewed assets), plus nonzero trading volume.
- **Proposition 4 (overconsumption due to optimism):** with quadratic utility, certainty equivalence makes optimal beliefs minimize subjective uncertainty — agents perceive future income as *certain* (extreme overconfidence) and *overestimate* its mean. They over-consume early, revise human wealth down on average, and exhibit declining, concave life-cycle consumption.
- **Proposition 5 (time consistency of beliefs):** in this consumption-saving problem optimal expectations are time-consistent across the agent's selves. Beliefs become more rational as the horizon $T\to\infty$ (stakes grow), with $c^{OE}\to c^{RE}$.

## Contribution
Provides the **discipline** that subjective-belief and heterogeneous-priors models traditionally lacked: rather than positing arbitrary priors (Savage) or imposing rational expectations / the Harsanyi common-prior doctrine, beliefs are pinned down by an explicit objective — maximizing well-being. It reframes optimal expectations as *a theory of prior beliefs for Bayesian-rational agents*, unifying overoptimism, overconfidence, skewness preference, endogenous heterogeneity, and undersaving, and connecting them to anticipatory-utility roots in classical utilitarianism (Bentham, Hume, Böhm-Bawerk; Jevonian view of utility).

## Limitations & open questions
- **Frictionless beliefs:** subjective probabilities are chosen with no anchoring to reality. The authors flag that one could add constraints penalizing large distortions, restrict beliefs to be "smooth" / coarser-partition / parsimonious-model-consistent, or impose robust-control-style non-detectability — at a cost in tractability. (Explicitly left for future work.)
- **Extreme overconfidence** under quadratic utility (future income perceived as *certain*) is an artifact of certainty equivalence; less extreme overconfidence would not change choices, only lower early felicity. General-curvature cases (decreasing absolute risk aversion) may yield positive bias in *both* mean and variance — left open.
- **Fixed vs. period-by-period beliefs:** the paper assumes conditional probabilities are fixed forever; resetting beliefs each period generally breaks Bayesian updating (selves disagree) — only shown time-consistent in the quadratic case.
- **Welfare/objective-function choice:** results may depend on the time-average specification of $W$ (an earlier version used a weighted average); the general normative status of OE is unsettled.
- **Endowment-driven equilibrium selection** drives the gambling/trading-volume results; heterogeneous-endowment economies are only speculated about.
- **Evolutionary survival** of OE agents against rational agents is argued informally, not proven.

## Connections
Builds on belief-dependent / anticipatory-utility models — Geanakoplos, Pearce & Stacchetti (1989), [[@Caplin2001|Caplin & Leahy]] (2001, 2000, 2004), and Yariv (2001, 2002) — and on the psychology of overconfidence (Alpert & Raiffa 1982; Weinstein 1980; Buehler, Griffin & Ross 1994). It is a structural alternative to exogenous-belief macro (Nerlove 1958) and to the Muth–Lucas rational-expectations / Aumann common-prior tradition, with Savage (1954) and Myerson (1986) providing the subjective-probability foundations. Related belief-distortion models include [[@Akerlof1982|Akerlof & Dickens (1982)]], Landier (2000), Brunnermeier & Parker (2002), Bénabou & Tirole (2002, 2004), Carrillo & Mariotti (2000), Harbaugh (2002), and memory-based accounts (Mullainathan 2002; Piccione & Rubinstein 1997; Bernheim & Thomadsen 2003; Rabin & Schrag 1999). Empirical touchpoints include Golec & Tamarkin (1998) on skewness and returns, Chen, Hong & Stein (2001) on trading, Lewis (1999) and Poterba (2003) on home bias, and Barsky, Juster, Kimball & Shapiro (1997) and Gourinchas & Parker (2002) on life-cycle consumption. The noise-trader risk-taking advantage echoes DeLong, Shleifer, Summers & Waldmann (1990).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
