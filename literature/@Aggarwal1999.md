---
citekey: Aggarwal1999
title: "The Other Side of the Trade‐Off: The Impact of Risk on Executive Compensation"
authors: ["Aggarwal, Rajesh K.", "Samwick, Andrew A."]
year: 1999
type: journalArticle
doi: 10.1086/250051
zotero: "zotero://select/library/items/CGCCX5DL"
pdf: /Users/jesper/Zotero/storage/U8V8VB5W/Aggarwal1999.pdf
tags: [literature]
keywords: [executive-compensation, principal-agent, pay-performance-sensitivity, moral-hazard, relative-performance-evaluation, quantile-regression]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Aggarwal & Samwick provide direct empirical support for the principal-agent model of executive compensation by testing its central *comparative-static* prediction rather than the level of the pay-performance sensitivity. Using ExecuComp data on the top five executives at 1,500 large U.S. firms (1993-96) merged with CRSP return volatilities, they show that the pay-performance sensitivity (PPS) is strongly *decreasing* in the variance of a firm's stock returns: executives at the least volatile firms have a PPS an order of magnitude larger than those at the most volatile firms. They also show that regressions omitting firm-return variance bias the PPS toward zero, reconciling the small estimates of Jensen & Murphy (1990b) with the model. A companion test of relative performance evaluation (RPE) finds little support.

## Research question
Does the standard principal-agent model actually describe executive pay? Specifically, is an executive's pay-performance sensitivity decreasing in the riskiness (variance) of the firm's performance, as the model's risk-sharing/incentive trade-off predicts? And is there evidence of relative performance evaluation, whereby pay loads negatively on rival-firm performance?

## Method / identification
The theoretical backbone is the Holmström-Milgrom (1987) linear-contract model. Firm performance is $\pi = x + \epsilon$ with $\epsilon \sim N[0,\sigma_\epsilon^2]$ and action $x$; the linear contract is $w = \alpha_0 + \alpha_1\pi$, and the optimal pay-performance sensitivity for a risk-averse manager is
$$\alpha_1^* = \frac{1}{1 + r\,k\,\sigma_\epsilon^2},$$
where $r$ is absolute risk aversion and $k$ is the curvature of the disutility of effort. The key feature is that $\alpha_1^*$ is decreasing in $\sigma_\epsilon^2$ — the comparative static the paper tests.

The estimating equation lets the PPS vary across the cross-section of firm volatilities:
$$w_{ijt} = \gamma_0 + \gamma_1 \pi_{jt} + \gamma_2 F(\sigma_{jt}^2)\pi_{jt} + \gamma_3 F(\sigma_{jt}^2) + \lambda_i + \mu_t + \epsilon_{it},$$
where $F(\cdot)$ is the empirical CDF of the firm-return variance. This device makes the implied PPS at any percentile read directly off the coefficients: $\alpha_1 = \gamma_1 + F(\sigma_{jt}^2)\,\gamma_2$, so the median-variance firm has $\gamma_1 + 0.5\gamma_2$ and the minimum/maximum variance firms have $\gamma_1$ and $\gamma_1 + \gamma_2$. The model predicts $\gamma_1 > 0$ and $\gamma_2 < 0$; the sign of $\gamma_3$ is not a test. Entering the CDF separately purges any cross-sectional relation between variance and pay *levels* from the estimate of $\gamma_2$.

Estimation uses median (quantile) regression — robust to the heavy right skew and outliers in compensation — with bootstrapped standard errors (Gould 1992, 20 replications), as well as OLS with executive fixed effects $\lambda_i$ and year effects $\mu_t$. The fixed effects absorb the firm-size/pay relationship and identify the PPS purely from within-executive variation. Performance $\pi$ is specified both as *dollar* returns to shareholders (so variance scales with firm size, consistent with Jensen-Murphy) and as *percentage* returns. Compensation is measured five ways: flow compensation, change in flow, percentage change in flow, change in firm-specific wealth (including existing stock/option holdings), and that change excluding existing options.

For RPE, the paper shows within the Holmström-Milgrom framework that, with stock returns as the performance measure, a firm's stock beta measured relative to its *industry* return is a sufficient index for the degree of RPE: the ratio of the industry PPS to the own-firm PPS should be increasing in this beta. The idiosyncratic-return variance is $\sigma_\epsilon^2(1-\rho^2)$ and the industry beta is $\rho\sigma_\epsilon/\sigma_\theta$.

## Data
S&P ExecuComp (top five executives, ranked by salary+bonus, at S&P 500 / Midcap 400 / SmallCap 600 firms), 1993-96, virtually complete due to post-1992 SEC disclosure rules. Compensation and current option grants (Black-Scholes valued) come from ExecuComp; monthly stock-return variances and industry covariances are computed from CRSP over the 60 months preceding each sample year. About 200 firms are dropped for insufficient (four-year) return history. The sample is three times as many firms and five times as many executives per firm as Jensen-Murphy (1990a) or Hall-Liebman (1998). CEO flow compensation averages $2.3M (median $1.4M); ~98% of CEOs own stock, with median ownership ~0.3% of the firm.

## Key findings
- **PPS decreases in variance (the model's core prediction holds).** With dollar returns and change in firm-specific wealth, the CEO PPS falls from $27.60 per $1,000 at the minimum variance to $1.45 at the maximum; the median-variance PPS is $14.52 per $1,000. The interaction coefficient $\gamma_2$ is negative and significant in essentially every specification, and the min-vs-max PPS differs by an order of magnitude.
- **The result holds for non-CEO executives too**, with PPS about one-fifth the CEO magnitude at the median but the same qualitative pattern — extending the model beyond CEOs.
- **Omitting variance biases PPS toward zero.** Imposing $\gamma_2 = \gamma_3 = 0$ collapses the CEO PPS estimate from $14.52 to $3.47 per $1,000 — recovering the Jensen-Murphy (1990b) figure of $3.25 — because the omitted interaction $\gamma_2 F(\sigma^2)\pi$ is strongly negatively correlated with included performance.
- **Flow compensation also conforms**: PPS is positive at the median variance and often insignificant at the maximum; the variance effect is not merely mechanical from stock/option holdings. Flow accounts for only ~5-6% of total incentives.
- **Little support for RPE.** The industry PPS is rarely negative and significant, and the ratio of industry to own-firm PPS is not increasing in the firm's industry beta — contradicting the RPE prediction across return specifications, estimators, and pay measures.

## Contribution
The paper rescues the principal-agent model from the "PPS is too small" critique (Jensen-Murphy; Haubrich 1994) by shifting the test from the *level* of the PPS — which depends on unobserved $r,k$ and is therefore uninformative — to its *comparative static* with respect to risk, which is unambiguous. The CDF-interaction specification is a clean device for recovering heterogeneous PPS across the volatility distribution and for demonstrating the omitted-variable bias quantitatively. It thereby supplies some of the strongest direct evidence that principal-agent considerations are embedded in real compensation contracts, while documenting that RPE is not.

## Limitations & open questions
- ExecuComp reports existing options only when in the money, biasing the wealth-based PPS; the authors bound this by also estimating excluding existing options, but the bias is not fully resolved.
- The linear Holmström-Milgrom contract is an approximation; real contracts (convex option payoffs) are nonlinear, and the structural parameters $r,k$ remain unidentified.
- Why is RPE absent despite its informativeness benefit? The authors point to strategic interaction among rival managers (developed in Aggarwal & Samwick, in press) as an explanation, but the present paper only documents the absence rather than testing its cause here.
- The short 1993-96 panel and large-firm focus limit external validity; whether the variance-PPS relation holds for smaller/private firms or over longer horizons is open.

## Connections
Builds directly on the Holmström-Milgrom (1987) linear-contract / aggregation framework and Holmström's (1979, 1982) moral-hazard and sufficient-statistic results. It confronts the influential Jensen & Murphy (1990b) finding of a small ($3.25 per $1,000) PPS and Hall & Liebman (1998) on growing PPS, arguing both miss the relevant comparative static; Haubrich (1994) had shown low PPS can be consistent with the model. The empirical strategy follows and improves on Garen (1994), Lambert & Larcker (1987), and Janakiraman, Lambert & Larcker (1992), all of which found only weak or mixed evidence on variance and on RPE. The RPE tests engage Antle & Smith (1986), Gibbons & Murphy (1990), Barro & Barro (1990), and Joh (1996). The strategic-interaction explanation for absent RPE is developed in the companion Aggarwal & Samwick (in press, J. Finance). Methodologically it draws on Koenker & Bassett (1982) and Buchinsky (1998) for quantile regression and Gould (1992) for bootstrapped standard errors, and frames the agency problem via Berle & Means (1932) and Shleifer & Vishny (1997).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
