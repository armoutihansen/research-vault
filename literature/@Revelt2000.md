---
citekey: Revelt2000
title: "Customer-specific taste parameters and mixed logit: Households' choice of electricity supplier"
authors: ["Revelt, David", "Train, Kenneth"]
year: 2000
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/2YZ5MFQL"
pdf: /Users/jesper/Zotero/storage/LRG64EXP/Revelt2000.pdf
tags: [literature]
keywords: [mixed-logit, random-coefficients, individual-taste-conditioning, discrete-choice, maximum-simulated-likelihood, electricity-supplier-choice, bayesian-conditioning]
topics: ["[[discrete-choice-econometrics]]"]
related: [McFadden2000, Revelt1998]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> In a discrete choice situation, information about the tastes of each sampled customer is inferred from estimates of the distribution of tastes in the population. First, maximum likelihood procedures are used to estimate the distribution of tastes in the population using the pooled data for all sampled customers. Then, the distribution of tastes of each sampled customer is derived conditional on the observed data for that customer and the estimated population distribution of tastes (accounting for uncertainty in the population estimates.) We apply the method to data on residential customers' choice among energy suppliers in conjoint-type experiments. The estimated distribution of tastes provides practical information that is useful for suppliers in designing their offers. The conditioning for individual customers is found to differentiate customers effectively for marketing purposes and to improve considerably the predictions in new situations.

## Summary
Revelt and Train show how a mixed (random-coefficients) logit, estimated by maximum simulated likelihood on pooled choice data, can be turned around to recover information about *each individual customer's* taste vector. After estimating the population distribution of tastes $g(\beta\mid\theta)$, they apply Bayes' rule to condition on a customer's own observed sequence of choices, producing a customer-specific posterior over tastes whose mean $E(\beta)$ summarizes that person's preferences. They call the procedure ML/COIT (maximum likelihood with conditioning of individual tastes). Applied to households' stated-preference choices among electricity suppliers, the conditional means differentiate customers sharply for targeted marketing and roughly cut prediction error on a held-out choice in half relative to using only the population distribution.

## Research question
Given only choice data and an estimated population taste distribution, how much can a researcher learn about the taste parameters of each *individual* sampled decision-maker, and does conditioning on a person's past choices improve out-of-sample prediction of that same person's future choices?

## Method / identification
A sampled customer faces $J$ alternatives in $T$ choice situations with utility $U_{tj}=\beta'X_{tj}+\varepsilon_{tj}$, where $\varepsilon_{tj}$ is iid extreme value and $\beta$ varies over customers with density $g(\beta\mid\theta)$. Conditional on $\beta$, the choice probability in situation $t$ is standard logit $L(i,t\mid\beta)=e^{\beta'X_{ti}}/\sum_j e^{\beta'X_{tj}}$, and the probability of the customer's whole sequence is the product of logits $P(y\mid\beta)=\prod_t L(y_t,t\mid\beta)$. The mixed logit probability integrates this over the population density, $P(y\mid\theta)=\int P(y\mid\beta)\,g(\beta\mid\theta)\,d\beta$, approximated by simulation over $R$ Halton draws as $\tilde P(y\mid\theta)=\frac{1}{R}\sum_r P(y\mid\beta^r)$. The population parameters $\theta$ are estimated by maximum simulated likelihood.

The novel step is **conditioning**. By Bayes' rule the posterior taste density given the customer's choices is
$$h(\beta\mid y,\theta)=\frac{P(y\mid\beta)\,g(\beta\mid\theta)}{P(y\mid\theta)}.$$
The conditional expectation of any function $k(\beta)$ is then estimated by importance-sampling–style reweighting of population draws:
$$\tilde E(k\mid y,\theta)=\frac{\sum_r k(\beta^r)\,P(y\mid\beta^r)}{\sum_r P(y\mid\beta^r)}.$$
With $k(\beta)=\beta$ this gives the customer's expected tastes; with $k(\beta)=L(i,T{+}1\mid\beta)$ it gives the predicted probability for a new ($T{+}1$) situation, which simplifies to $\tilde P(i,T{+}1\mid y,\theta)=\sum_r P(y^+\mid\beta^r)/\sum_r P(y\mid\beta^r)$, the simulated probability of the full sequence over that of the observed sequence. They further integrate over the sampling distribution $f(\theta\mid m,W)$ of the estimated population parameters to account for estimation uncertainty, $\tilde E(k\mid y,m,W)=\frac{1}{S}\sum_s \tilde E(k\mid y,\theta^s)$. The framework is classical (ML) and parallels Bayesian Gibbs-sampling approaches (Rossi–McCulloch–Allenby) and macro regime-switching inference, but is, to the authors' knowledge, the first classical-ML application of individual-level conditioning to discrete choice.

## Data
Two sources. (1) A **Monte Carlo** experiment: fifty data sets of 300 simulated customers with 1, 10, 20, or 50 choice situations, three alternatives, four variables (two fixed coefficients, two normal with mean and variance one), using 100/1,000/10,000 Halton draws, where true $\beta$ is known so $E(\beta)$ can be compared to truth. (2) **Stated-preference electricity-supplier data** collected by Research Triangle Institute (1997) for EPRI: 361 residential customers each faced 8–12 conjoint-type choice situations among four hypothetical suppliers differing in price type (fixed, time-of-day, seasonal), contract length, and supplier familiarity (local utility / known company / unknown). The last choice situation per customer was held out to test predictive accuracy.

## Key findings
- **Conditioning recovers substantial individual information.** In the Monte Carlo, even with one choice situation the standard deviation of $E(\beta)$ rises ~40% of the way toward the perfect-knowledge benchmark; with ten situations it reaches ~80%, with sharply decreasing returns thereafter (fifty situations leaves expected coefficients ~0.25 from true values on average). More than 100 draws is enough; draws should rise with $T$.
- **Empirical taste heterogeneity is large and economically meaningful.** The average customer would pay ~0.2–0.25 cents/kWh to shorten a contract by a year, yet a sizeable share prefers *longer* contracts (price insurance); the average customer pays ~2.5 cents/kWh more for the local utility than an unknown supplier and ~1.7–1.8 cents/kWh for any known supplier — implying entry by unknown suppliers is very hard (consistent with only ~1% California switching).
- **Expected tastes differentiate customers and enable clustering.** Variation in $E(\beta)$ captures >70% of estimated population variance per coefficient; cluster analysis on model-4 $E(\beta)$'s yields five interpretable marketing segments.
- **Conditioning improves prediction.** On the held-out last choice, the average probability of the actually-chosen alternative rises from 0.35 (population distribution only) to 0.50 (full conditional distribution with sampling variance). For 260 of 361 customers prediction improves (avg +0.25); for the rest it worsens (avg −0.11).
- **A specification diagnostic.** For a correctly specified, consistently estimated model, the sample average of conditional taste distributions equals the population distribution; discrepancies (as seen for the normal/uniform/triangular models 1–3 vs. the better-fitting lognormal model 4) reveal misspecification, insufficient draws, small samples, or convergence to a local maximum.

## Contribution
The paper operationalizes individual-level taste recovery within the classical mixed-logit / maximum-simulated-likelihood framework, providing closed importance-sampling estimators for both conditional expected tastes and conditional choice predictions, and showing how to propagate sampling uncertainty in $\theta$. It bridges classical estimation with the individual-level inference previously associated with hierarchical Bayes, supplies a model-checking diagnostic, and demonstrates concrete managerial value (customer differentiation, segmentation, improved forecasting) on real electricity-choice data.

## Limitations & open questions
The authors are explicit that conditioning does *not* always improve prediction, and they enumerate why — each a hook for further work: (1) the held-out situation may involve **new tradeoffs** outside the range of earlier ones, so past choices are uninformative or even detrimental; they suggest a better test would design choice tasks eliciting the relevant tradeoffs plus a *hold-out within that range*. (2) **Omitted attributes**: variables dropped for being population-insignificant may still matter to individuals, biasing their conditional densities — implying researchers should retain attributes important for *some* individuals even if insignificant overall. (3) Customers may answer **quixotically**, not applying earlier-revealed tastes to the last choice. (4) Pure **random factors**. A further unexplained anomaly: integrating over the sampling distribution of $\theta$ (Table 4) shifts misspecified models' coefficients toward the better-specified model's, a phenomenon that nearly vanishes when the point estimate of $\theta$ is used — "for reasons that we do not understand." Whether observed variances over- or under-state true individual uncertainty is also left open.

## Connections
A direct sequel to [[@Revelt1998|Revelt and Train]] (1998, *REStat*), which estimated the population taste distribution; the conditioning idea generalizes the random-coefficients tradition (Griffiths 1972; Judge et al. 1989) and macro regime-switching inference (Hamilton 1996; Hamilton–Susmel 1994) to discrete $y$. Its closest methodological cousins are the hierarchical-Bayes / Gibbs-sampling conjoint models of Rossi–McCulloch–Allenby (1996) and Allenby–Rossi (1999), and the diagnostic parallels Rossi–Allenby (1999). The simulation machinery rests on [[@McFadden2000|McFadden–Train (2000)]] (mixed logit approximates any RUM; MSL asymptotics), Halton-draw work (Bhat 1999; Train 1999), and MSL theory (Hajivassiliou–Ruud 1994; Lee 1992). The Metropolis–Hastings alternative for drawing from $h(\cdot)$ connects to Chib–Greenberg (1995) and Arora et al. (1998). The electricity application builds on Goett (1998) and Revelt (1999). This note sits squarely in the choice-modeling lineage central to the user's social-preference / discrete-choice work.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
