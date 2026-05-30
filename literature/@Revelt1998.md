---
citekey: Revelt1998
title: "Mixed Logit with Repeated Choices: Households' Choices of Appliance Efficiency Level"
authors: ["Revelt, David", "Train, Kenneth"]
year: 1998
type: journalArticle
doi: 10.1162/003465398557735
zotero: "zotero://select/library/items/WXZ4BJXI"
pdf: /Users/jesper/Zotero/storage/5ZJA37SS/Revelt1998.pdf
tags: [literature]
keywords: [mixed-logit, random-parameters, discrete-choice, maximum-simulated-likelihood, taste-heterogeneity, stated-preference]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Mixed logit models, also called random-parameters or error-components logit, are a generalization of standard logit that do not exhibit the restrictive "independence from irrelevant alternatives" property and explicitly account for correlations in unobserved utility over repeated choices by each customer. Mixed logits are estimated for households' choices of appliances under utility-sponsored programs that offer rebates or loans on high-efficiency appliances.

## Summary
This is one of the foundational applied papers establishing mixed logit (random-parameters logit) as a practical workhorse for discrete-choice estimation. Revelt and Train estimate the model on stated-preference panel data in which Southern California Edison customers make repeated choices among refrigerators of differing efficiency, price, and incentive (rebate or loan). The key methodological move is to exploit the *repeated-choices* structure: each respondent's taste parameters are held fixed across their own choice situations, so a single random draw of the coefficient vector enters the *product* of the within-person logits. This induces correlation across alternatives and over time, breaks IIA, and lets the population distribution of tastes be identified even from binary experiments. The model is estimated by maximum simulated likelihood (MSL). Substantively, the paper recovers large, significant taste heterogeneity and uses the calibrated model to forecast take-up of low-interest loan programs as an alternative to rebates.

## Research question
Two intertwined questions. Methodologically: how can one estimate flexible, non-IIA random-utility models with correlated unobserved utility when each respondent supplies *multiple* choices? Substantively: what is the demand response of residential customers to appliance-efficiency incentives, and specifically would low-interest loans (which can be profitable for the utility) promote efficiency comparably to rebates as the electricity industry deregulates?

## Method / identification
A person $n$ faces alternatives $j \in J$ in each of $T$ choice situations. Utility is
$$U_{njt} = \beta_n' x_{njt} + \varepsilon_{njt},$$
where $\varepsilon_{njt}$ is iid extreme value and the taste vector $\beta_n$ is random across people with density $f(\beta_n \mid \theta^*)$. Conditional on $\beta_n$, the choice probability is standard logit
$$L_{nit}(\beta_n) = \frac{e^{\beta_n' x_{nit}}}{\sum_j e^{\beta_n' x_{njt}}}.$$
Because tastes are assumed constant over a person's choice situations, the probability of person $n$'s observed *sequence* is the product of within-person logits, $S_n(\beta_n) = \prod_t L_{i(n,t)t}(\beta_n)$, and the unconditional sequence probability is
$$P_n(\theta^*) = \int S_n(\beta_n)\, f(\beta_n \mid \theta^*)\, d\beta_n.$$
This integral has no closed form, so it is approximated by simulation: draw $\beta_n^r$ from $f(\cdot\mid\theta)$, average $S_n$ over $R$ draws to get an unbiased simulated probability $SP_n = (1/R)\sum_r S_n(\beta_n^r)$, and maximize the simulated log-likelihood $SLL(\theta) = \sum_n \ln SP_n(\theta)$. The authors use $R = 500$ draws and bhhh/approximate-Hessian iteration; the simulated score has a tractable closed form. Citing Lee (1992) and Hajivassiliou & Ruud (1994), MSL is consistent and asymptotically normal, and asymptotically equivalent to ML when $R$ rises faster than $\sqrt{N}$. They discuss but reject MSM (infeasible here, requiring simulation of hundreds of thousands of sequence probabilities) and MSS (no easy unbiased score simulator).

Specifications escalate: (1) independent normal coefficients $\beta_n = b + W \mu_n$ with $W$ diagonal and price fixed (so willingness-to-pay ratios are well defined); (2) demographics (income, education) interacted with price; (3) full covariance $\beta_n \sim N(b,\Omega)$ via Choleski factor $\beta_n = b + L\mu_n$, $LL' = \Omega$; (4) log-normal distributions $\beta_{nk} = \exp(b_k + s_k\mu_{nk})$ for savings, amount-borrowed, and (negated) interest-rate coefficients to impose sign restrictions. Identification (footnote 6) comes from heteroskedasticity in utility differences induced by the variance of $\beta_n$ over experiments — so $\theta$ is identified even in binary experiments, unlike fixed-coefficient models.

## Data
Stated-preference survey of 401 Southern California Edison residential customers, yielding 6,081 choice experiments (each customer: up to twelve binary plus up to four trinary refrigerator choices). Attributes: price net of rebate, annual operating-cost savings, amount borrowed, interest rate, plus efficiency/rebate/finance dummies. Experiments were designed orthogonally with no dominated alternatives. These SP data are supplemented by limited revealed-preference data (actual purchases in the last three years) for 163 customers, used for calibration.

## Key findings
Mixed-logit mean coefficients are roughly three times the standard-logit coefficients, because variance previously absorbed into the extreme-value term is reallocated to the explicit random-parameter component, changing the scale normalization. Estimated standard deviations are highly significant, confirming substantial taste heterogeneity, and the likelihood-ratio index rises sharply (0.275 to 0.461) over standard logit. Willingness to pay for $1 of annual savings is normally distributed with mean ~$2.46 (s.d. ~$1.81), implying high implicit discount rates (~39 to 46 percent) consistent with prior energy literature. Under normality ~9 percent of customers have negative savings coefficients (possibly mistrust of conservation claims; addressed via the log-normal model). The efficiency-dummy mean is large (high-efficiency preference for ~88 percent), but is largely a stated-preference artifact and drops sharply after calibration. The rebate-dummy mean is near zero while its s.d. is large and significant: customers are split between reading a rebate as a positive credibility signal versus a negative quality signal — heterogeneity that standard logit masks. The covariance model finds, e.g., savings negatively correlated with the efficiency and rebate dummies, and rebate and finance dummies positively correlated. Calibration to revealed-preference data lowers the efficiency and rebate constants. Simulations (Table 7) forecast loan take-up across interest rates: at low rates, loans capture a meaningful share of high-efficiency purchases, supporting loans as a viable DSM instrument.

## Contribution
A canonical demonstration that mixed logit with the panel/repeated-choices likelihood is estimable by MSL on real data, delivering flexible non-IIA substitution and full taste-heterogeneity distributions. It operationalizes the McFadden–Train approximation result (any random-utility model is approximable by mixed logit) and provides a template — fixed price coefficient for WTP, escalating normal/correlated/log-normal specifications, SP-to-RP calibration — that became standard practice in environmental and transport demand estimation.

## Limitations & open questions
The authors flag several explicit issues. Models with *all* coefficients random did not converge (Ruud 1996): when random parameters dominate, the extreme-value scaling becomes unstable, motivating the fixed price coefficient. Distributional assumptions are consequential — normality forces a share of negative savings coefficients whether or not real; log-normality fixes signs but converges very slowly (~100 iterations) and yields a lower log-likelihood. Demographic interactions explain only part of the heterogeneity, reflecting limited sociodemographic data. The taste vector is assumed constant within person across choices (could be relaxed to vary over $t$). Reliance on stated-preference data requires calibration against thin revealed-preference data (only 163 customers, no loan option ever actually offered), so loan forecasts rest on out-of-sample extrapolation. Finite-$R$ MSL bias and the choice of $R$ remain practical concerns.

## Connections
Builds directly on McFadden's logit and the McFadden & Train (1997) approximation theorem, and on the simulation-estimation literature — Lee (1992), Hajivassiliou & Ruud (1994), McFadden (1989) on MSM, Hajivassiliou & McFadden on MSS. It sits alongside contemporaneous mixed-logit applications without repeated choices: Ben-Akiva et al. (1993), Ben-Akiva & Bolduc (1996), Bhat (1996), and Brownstone & Train (1996), the last comparing probit and mixed logit on car choice. The "probit with a logit kernel" framing is from Ben-Akiva & Bolduc (1996). The empirical setting and calibration procedure follow Atherton & Train (1995), whose nested-logit model is a special case of this mixed logit. Foundational texts include Ben-Akiva & Lerman (1985) and Train's later textbook treatment. The rebate-as-signal interpretation draws on Train (1988) and the consumer-skepticism literature (Constantzo et al. 1986; Bruner & Vivian 1979; Craig & McCann 1978).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
