---
citekey: Fudenberg2022b
title: Simplicity and Probability Weighting in Choice under Risk
authors: ["Fudenberg, Drew", "Puri, Indira"]
year: 2022
type: journalArticle
doi: 10.1257/pandp.20221091
zotero: "zotero://select/library/items/LN4MVJCE"
pdf: /Users/jesper/Zotero/storage/VDU9MYE3/Fudenberg2022a.pdf
tags: [literature]
keywords: [choice-under-risk, prospect-theory, probability-weighting, simplicity-preference, complexity-cost, prize-linked-savings, behavioral-economics]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We present a speculative application of model estimates from Fudenberg and Puri (2021) to prize-linked savings in South Africa. The models used include one combining simplicity theory (Puri 2018, 2022), a preference for lotteries with fewer possible outcomes, with cumulative prospect theory. The results and those of prior literature indicate that both simplicity and probability weighting have a role to play in understanding behavior in choice under risk. We discuss the properties of these models and their implications for behavior.

## Summary
This is a short AEA Papers & Proceedings companion piece that summarizes the larger working paper Fudenberg and Puri (2021) ("FP") and then applies its estimated parameters out-of-sample to a real-world field setting: take-up of a prize-linked savings (PLS) account ("Million a Month") offered by First National Bank in South Africa, 2005–2008. The core argument is that two ingredients are jointly needed to predict choice under risk: nonlinear probability weighting (the engine of prospect theory) and a "complexity cost" / simplicity preference that penalizes lotteries with larger support (more distinct outcomes). The hybrid CPT-simplicity model fits the lab data best and comes close to machine-learning performance, and in the field calibration it predicts PLS take-up (≈64%) much closer to the observed 63% than CPT alone (≈84%, too high because all CPT types overweight the small jackpot probability). Note: the field exercise is explicitly framed as speculative and statistically insignificant.

## Research question
Do both probability weighting and a preference for simplicity (fewer-outcome lotteries) have distinct, useful roles in explaining and predicting choice under risk — and can a model combining them, estimated on lab data, organize behavior in a field setting (PLS account take-up)?

## Method / identification
The paper relies on a family of structural decision-theoretic models estimated in FP and re-applies them. The central object is the **CPT-simplicity** representation: the value of a lottery $p$ with outcomes $x_i$ equals a rank-dependent (cumulative prospect theory) weighted sum of utilities, minus a complexity cost that depends only on the cardinality of the support:
$$u(p)=\sum_i u(x_i)\left[\pi\!\left(\sum_{k=1}^{i}p_k\right)-\pi\!\left(\sum_{k=1}^{i-1}p_k\right)\right]-C\big(|\operatorname{support}(p)|\big).$$
The **PT-simplicity** model is identical except probability weighting is applied without rank dependence (as in original PT). Functional forms follow the standard literature: a CRRA Bernoulli utility $u$, the Tversky–Kahneman one-parameter probability weighting function
$$\pi(p)=\frac{p^{\gamma}}{\left(p^{\gamma}+(1-p)^{\gamma}\right)^{1/\gamma}},$$
and a **sigmoid complexity cost** chosen to impose few constraints,
$$C(n)=\frac{\iota}{1+e^{\kappa(n-\rho)}}-\frac{\iota}{1+e^{\kappa(1-\rho)}},$$
where the second term normalizes $C(1)=0$ (a degenerate/sure outcome carries no complexity cost). Estimation allows for **heterogeneous agents** within a model class (following Bruhin, Epper, and Fehr-Duda 2010): FP classify subjects into latent groups (e.g., three CPT-simplicity groups), using validation sets to choose the number of groups. Only the gains domain is considered, with $0$ as the reference point. Performance is benchmarked against machine-learning algorithms via "ML completeness scores" (Fudenberg, Kleinberg, Liang, and Mullainathan 2022), taking expected value as the naive baseline and the best ML algorithm as the upper benchmark. CPT-simplicity nests both CPT and simplicity, so it is less restrictive in the Fudenberg–Gao–Liang (2021) sense (unquantified here).

The **field calibration** (Section III) is a Monte Carlo exercise: the South African PLS prize schedule is linearized down to the payoffs implied by a $5 principal investment (about the average payoff in FP); 1,000 simulation draws are taken, drawing each group's parameters independently from a normal distribution with the mean and SD reported in FP (with nonnegativity constraints, and no covariance because FP do not report it). For each draw and each group, the model determines whether the PLS account or a standard savings account is more attractive; the implied take-up share is compared to observed take-up.

## Data
Two distinct datasets. (1) **Lab data (FP, used for estimation):** a new experiment in which each participant provides certainty equivalents for lotteries with two, three, four, five, and six outcomes — the varying support is what lets a heterogeneous-agent model classify behavioral types. (2) **Field data (this paper's application):** take-up of the "Million a Month" PLS account run by First National Bank in South Africa (Jan 2005–Mar 2008, shut down after challenges from the South Africa Lottery Board). Observed take-up among bank employees is drawn from Cole, Iverson, and Tufano (2021); demographic correlates of take-up at the branch level are also compared. This paper itself runs no new experiment — it is a discussion-plus-application of pre-existing estimates.

## Key findings
- **Both ingredients matter (lab).** The hybrid **CPT-simplicity model performs best** and comes closest to ML performance, in absolute terms and on completeness scores. CPT alone and simplicity alone each beat PT; simplicity alone slightly underperforms CPT; PT beats only expected utility. So probability weighting and complexity aversion are complementary, not redundant.
- **Heterogeneity structure.** FP recover three groups: one distorts probabilities mildly and is mildly complexity-averse; a second heavily distorts probabilities and is more complexity-averse (these two are the large majority, and the strength of probability weighting and complexity aversion appear correlated across them); a third is not complexity-averse with intermediate probability weighting.
- **Field application (directional only).** CPT alone predicts PLS chosen ≈84% of the time — too high relative to actual ≈63% take-up — because every CPT type overweights the low jackpot probability and therefore likes PLS. **CPT-simplicity predicts ≈64%**, close to the data, because the complexity cost makes the guaranteed single-outcome savings account attractive: only the two groups whose probability distortion outweighs their complexity aversion take up PLS.
- **Demographics.** Cole, Iverson, and Tufano (2021) find income, age, education, and employment do not predict branch-level take-up, consistent with FP's finding that behavioral type is not well predicted by these demographics. (An effect of race exists in the field data that FP's data cannot speak to.)

## Contribution
The paper consolidates the case that the long-standing "certainty effect" evidence used to justify probability weighting is confounded with a preference for fewer outcomes — prominent certainty-effect experiments use only two-outcome lotteries, and the same patterns can be generated by simplicity preferences. It contributes (i) a clean joint model nesting CPT and simplicity, (ii) a concrete sigmoid functional form for complexity cost usable in future empirical work, and (iii) a first, deliberately speculative, demonstration that lab-estimated risk preferences with a simplicity term can rationalize a real financial-product take-up margin (PLS) where pure CPT over-predicts.

## Limitations & open questions
The authors are unusually explicit about caveats, which double as project hooks:
- **Statistical insignificance.** Simulation standard errors are high; the PLS results are not statistically significant and are discussed only directionally — "this exercise alone should not be taken as evidence of one model over another."
- **Calibration fragility.** Payoffs must be scaled down to match the experiment, and parameter estimates are sensitive to scaling; PLS payoffs are far larger than the experimental ones.
- **Population mismatch.** The experimental population may not correspond to the South African bank-employee population whose take-up is studied.
- **Literal model use.** Error terms come only from parameter uncertainty; the model is taken very literally.
- **Restrictive heterogeneity.** Groups are forced to share a model class (e.g., all three CPT-simplicity) rather than mixing PT and CPT groups, with no a priori justification.
- **Unquantified restrictiveness.** The claim that CPT-simplicity is less restrictive than its components (in the Fudenberg–Gao–Liang sense) is asserted but not measured.
- **Complexity is more than support size.** A uniform lottery over 20 outcomes may be more appealing than an irregular 19-outcome lottery with higher mean and lower variance — so support cardinality is only one notion of complexity. The authors flag exploring **richer complexity measures** and the **link between cognitive ability and complexity aversion** (building on Enke and Graeber 2019; Puri 2022) as open directions.

## Connections
The note sits squarely in the descriptive theory of choice under risk. It builds directly on **Fudenberg and Puri (2021)** (the parent estimation paper) and on **Puri (2018, 2022)** and **Goodman and Puri (2021)** for simplicity theory. Probability weighting is the **Kahneman–Tversky (1979)** PT / **Tversky–Kahneman (1992)** CPT tradition, with the weighting/utility forms standard since then. The heterogeneous-agent latent-type approach follows **Bruhin, Epper, and Fehr-Duda (2010)**. The "completeness"/ML-benchmarking and "restrictiveness" machinery come from **Fudenberg, Kleinberg, Liang, and Mullainathan (2022)** and **Fudenberg, Gao, and Liang (2021)**. The critique that certainty-effect evidence is confounded with outcome count engages **Bernheim and Sprenger (2020)** (rank-independent weighting, failing CPT), **Andreoni and Sprenger (2011)**, **Cohen and Jaffray (1988)**, **Moffatt, Sitzia, and Zizzo (2015)**, and **Sonsino, Benzion, and Mador (2002)**. The cognitive-limitation interpretation of probability insensitivity links to **Viscusi (1989)**, **Wakker (2010)**, and **Enke and Graeber (2019)**. The empirical PLS setting draws on **Kearney et al. (2010)**, **Cole, Iverson, and Tufano (2014, 2021)**, **Gertler et al. (2018)**, and **Bharadwaj and Suri (2020)**.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
