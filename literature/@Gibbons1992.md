---
citekey: Gibbons1992
title: "Optimal Incentive Contracts in the Presence of Career Concerns: Theory and Evidence"
authors: ["Gibbons, Robert", "Murphy, Kevin J."]
year: 1992
type: journalArticle
doi: 10.1086/261826
zotero: "zotero://select/library/items/IT4WRZ3L"
pdf: /Users/jesper/Zotero/storage/K9ISCHLC/Gibbons1992.pdf
tags: [literature]
keywords: [career-concerns, incentive-contracts, implicit-incentives, executive-compensation, principal-agent, dynamic-agency, bayesian-learning]
topics: []
related: [Holmstrom1982]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper studies optimal incentive contracts when workers have career concerns--concerns about the effects of current performance on future compensation. We show that the optimal compensation contract optimizes total incentives: the combination of the implicit incentives from career concerns and the explicit incentives from the compensation contract. Thus the explicit incentives from the optimal compensation contract should be strongest for workers close to retirement because career concerns are weakest for these workers. We find empirical support for this prediction in the relation between chief executive compensation and stock market performance.

## Summary
Gibbons and Murphy add explicit incentive contracts to the Fama-Holmstrom model of career concerns. Their central insight is that the optimal contract does not provide incentives in isolation: it optimizes *total* incentives, summing the implicit incentives that arise because the labor market updates its belief about a worker's ability from observed output, and the explicit incentives written into the pay-for-performance contract. Because career concerns are strongest early in a career and vanish near retirement, the optimal explicit pay-performance slope is *increasing* over the career and is largest just before retirement. They test this in a large longitudinal panel of CEOs and find pay is more sensitive to firm performance for executives close to retirement.

## Research question
How are optimal explicit incentive contracts shaped when implicit "career concern" incentives are already present? Specifically, when the market infers a worker's ability from current output and competes for future services, how should the slope of the pay-performance contract vary over a worker's career, and does observed CEO compensation behave this way?

## Method / identification
A dynamic principal-agent model with learning. A worker works $T$ periods. Period-$t$ output is $y_t=\eta+a_t+\varepsilon_t$, the sum of (unknown) ability $\eta$, non-negative unobserved effort $a_t$, and noise $\varepsilon_t$. Information about $\eta$ is symmetric but imperfect: $\eta\sim N(m_0,\sigma_\eta^2)$ and $\varepsilon_t\sim N(0,\sigma_\varepsilon^2)$ i.i.d. The risk-averse worker has exponential utility
$$U=-\exp\!\Big(-r\,\textstyle\sum_{t=1}^{T}\delta^{t-1}[w_t-g(a_t)]\Big),$$
with $g$ convex, $g'(0)=0$, $g'(\infty)=\infty$, $g'''>0$ (the last yields concavity / clean comparative statics). This form makes the worker indifferent among deterministic wage streams of equal present value, i.e. he behaves as if he "needs no" credit. Two contracting restrictions: (A1) one-period contracts are linear, $w_t(y_t)=c_t+b_t y_t$; (A2) long-term contracts are infeasible — shown in the appendix to be equivalent to requiring long-term contracts be renegotiation-proof (Pareto-efficient at each date). Competition among prospective employers imposes zero expected profit each period, fixing the intercept $c_t=(1-b_t)E\{y_t\mid y_1,\dots,y_{t-1}\}$. The market updates beliefs about $\eta$ via Bayesian (Normal-Normal) learning from the output history. The equilibrium is a pure-strategy rational-expectations equilibrium: the market's effort conjecture $\bar a_t$ must equal the worker's optimal effort $a_t^*$. The model is solved by backward induction from the two-period case to the $T$-period case.

**Empirical design.** Estimate the pay-performance relation between CEO cash compensation and shareholder wealth, and test whether it is steeper for CEOs nearer retirement, using interaction terms such as $\Delta\ln(w_{it})$ on $\Delta\ln(\text{Shareholder Value})_{it}$ interacted with a "Few Years Left" indicator (within 2, 3, or 4 years of departure). Logarithmic (elasticity) specifications control for firm-size heterogeneity; firm-specific intercepts and slopes control for unobserved firm heterogeneity.

## Data
A longitudinal panel built from the Forbes Executive Compensation Surveys (1971-1989, from corporate proxy statements): 2,972 executives in 1,493 large corporations over fiscal years 1970-1988, totaling 15,148 CEO-years. The main "completed spells" subsample of CEOs who left office during 1970-1988 has 1,631 CEOs (916 firms, 8,786 CEO-years). Descriptives validate the model's assumed career path: the average departing CEO had ~30 years in the firm and >10 years as CEO; 60% left between ages 60 and 66; only 2.2% (36 of 1,631) became CEO of another sample firm — consistent with retirement-terminated, largely non-mobile careers.

## Key findings
- **Total-incentives result.** First-period effort satisfies $g'(a_1)=b_1+\delta(1-b_2)\,\sigma_\eta^2/(\sigma_\eta^2+\sigma_\varepsilon^2)\equiv B_1$: total incentive is explicit slope plus a positive career-concern term that *increases* with uncertainty about ability $\sigma_\eta^2$ and *decreases* with production noise $\sigma_\varepsilon^2$.
- **Optimal slopes rise toward retirement.** In the two-period model $b_1^*<b_2^*$; in the $T$-period model the partial characterization is $b_t^*<b_T^*$ for all $t<T$ — contractual incentives are strongest for those about to retire. Three forces drive $b_1^*<b_2^*$ in (2.20): a *noise-reduction* effect (learning shrinks conditional output variance over time, $\Sigma_2^2<\Sigma_1^2$, tilting the insurance-incentive tradeoff toward incentives), the *career-concerns* effect (explicit pay is dialed down when implicit incentives are high), and a *human-capital-insurance* effect (risk-averse workers want insurance against bad ability draws, delivered as a flatter early slope).
- **Negative incentives possible.** It can be optimal for total first-period incentives to be negative ($B_1<0$) when human-capital insurance dominates; explicit slopes can even be negative ($b_1<0$) while total incentives stay positive.
- **Empirical support.** Each 10% change in shareholder wealth corresponds to ~1.5% cash-compensation change for CEOs within three years of retirement vs. only ~0.9% for those farther out — the predicted steepening near retirement. The result survives controls for firm size (median-firm sensitivity ~0.93 per \$1,000 of shareholder wealth), though the "Few Years Left" interaction becomes statistically insignificant once firm-specific elasticities are allowed (point estimate $\beta_i=.0297$, $t=1.4$), modestly weakening support for hypothesis H1.

## Contribution
The paper unifies two previously separate literatures: career-concerns models (Fama 1980; [[@Holmstrom1982|Holmstrom 1982]]) that have incentives, learning, and market forces but no contracts or risk aversion, and dynamic agency models (Holmstrom-Milgrom 1987 and others) that have contracts and risk aversion but no learning or market forces. By incorporating all five elements (incentives, learning, market forces, contracts, risk aversion), it shows career concerns matter *even with* contracts, and yields the sharp, testable, and empirically borne-out prediction that explicit pay-performance sensitivity rises over the career. It is a foundational reference for understanding implicit vs. explicit incentives and the design of executive compensation.

## Limitations & open questions
- The model is deliberately stylized via strong assumptions (linear short-term contracts (A1); no long-term contracts (A2); exponential utility with perfect capital access). The authors expect the qualitative results to be robust but note weaker assumptions would surface additional effects.
- Career concerns in *internal* labor markets (promotions, intra-firm competition) are conjectured to behave analogously but are *not* modeled — flagged as "the most natural application."
- The $T$-period career and job transitions are taken as *exogenous*. They call for integrating the model with a theory of learning and job assignment (symmetric learning as in MacDonald 1982 / Murphy 1986, or asymmetric learning as in Waldman 1984 / Ricart i Costa 1988) to *endogenize* transitions between jobs.
- They suspect optimal slopes increase monotonically in $t$ (no counterexample found) but only prove the weaker $b_t^*<b_T^*$.
- The CEO setting is an imperfect laboratory: career concerns require ability uncertainty, but most CEOs are long-tenured insiders whose ability may already be well known, and the assumed competitive market of prospective employers may not exist given organization-specific capital. A bilateral-monopoly / rent-sharing reformulation is sketched but not developed.
- New data on internal organization are identified as essential for future progress.

## Connections
Builds directly on Fama (1980), who argued the managerial labor market alone disciplines managers, and [[@Holmstrom1982|Holmstrom (1982)]], who showed labor-market discipline is an imperfect substitute (effort too high early, too low late) — this paper restores a role for contracts. It draws the linearity of optimal contracts from Holmstrom and Milgrom (1987), and relates to dynamic agency and consumption-smoothing models (Lambert 1983; Rogerson 1985; Murphy 1986; Fudenberg, Holmstrom, and Milgrom 1987). The pay-performance estimation connects to the executive-compensation literature (Coughlan and Schmidt 1985; Gibbons and Murphy 1990). The promotion-incentive intuition echoes Rosen (1986) on tournaments, and the career-concerns mechanism parallels the "ratchet effect" in regulation and employment (Laffont-Tirole 1988; Lazear 1986; Gibbons 1987).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
