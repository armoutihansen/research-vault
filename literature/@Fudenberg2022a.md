---
citekey: Fudenberg2022a
title: Simplicity and Probability Weighting in Choice under Risk
authors: ["Fudenberg, Drew", "Puri, Indira"]
year: 2022
type: conferencePaper
doi: ""
zotero: "zotero://select/library/items/2KAJQ7JR"
pdf: /Users/jesper/Zotero/storage/4798XQQC/Fudenberg2022b.pdf
tags: [literature]
keywords: [prospect-theory, probability-weighting, simplicity-preference, choice-under-risk, prize-linked-savings, heterogeneous-agents]
topics: []
related: [Bruhin2010, Fudenberg2021, Fudenberg2021a, Fudenberg2022, Kahneman1979, Tversky1992]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> (no abstract in Zotero) This AEA Papers & Proceedings piece discusses [[@Fudenberg2021a|Fudenberg and Puri (2021)]], which empirically implements hybrid models combining prospect theory (PT) and cumulative prospect theory (CPT) with a "complexity cost" capturing a preference for lotteries with fewer outcomes. The hybrid CPT-simplicity model predicts well, indicating that both probability weighting and complexity costs matter for choice under risk. The authors then present a novel speculative application of the estimated model to field data: take-up of a prize-linked savings (PLS) account offered in South Africa during 2005–2008.

## Summary
This short proceedings paper does two things. First, it recaps [[@Fudenberg2021a|Fudenberg and Puri (2021]], "FP"), whose central empirical finding is that a hybrid model joining CPT-style probability weighting with a simplicity-based complexity cost (a penalty on the number of distinct outcomes a lottery has) out-of-sample predicts certainty equivalents better than PT, CPT, or simplicity alone, and comes close to matching machine-learning performance. Second, it carries out a speculative out-of-sample exercise: it feeds FP's calibrated parameters into field data on the take-up of a South African prize-linked savings (PLS) product. The CPT-simplicity model predicts roughly 64% take-up against an actual 63%, whereas plain CPT predicts 84% (too high), because adding a complexity penalty makes the multi-outcome PLS lottery less attractive relative to a sure-return savings account. The authors stress the field exercise is illustrative, not confirmatory.

## Research question
Do both nonlinear probability weighting and a preference for "simple" (fewer-outcome) lotteries independently improve the prediction of choice under risk, and can a model embedding both be transported from the lab to explain real financial behavior (take-up of prize-linked savings)?

## Method / identification
The core object is a hybrid CPT-simplicity representation. The value of a lottery $p$ with outcomes $x_i$ is the standard rank-dependent CPT functional minus a complexity cost that depends only on the size of the support:
$$u(p) = \sum_i u(x_i)\left[\pi\!\left(\sum_{k=1}^{i} p_k\right) - \pi\!\left(\sum_{k=1}^{i-1} p_k\right)\right] - C(\,|\operatorname{support}(p)|\,).$$
The PT-simplicity model is the same but drops the rank dependence of the weighting. For empirical implementation they adopt the canonical Tversky-Kahneman functional forms: a one-parameter probability weighting function
$$\pi(p) = \frac{p^{\gamma}}{\left(p^{\gamma} + (1-p)^{\gamma}\right)^{1/\gamma}},$$
CRRA Bernoulli utility for $u$, and a sigmoid complexity cost
$$C(n) = \frac{\iota}{1 + e^{\kappa(n-\rho)}} - \frac{\iota}{1 + e^{\kappa(1-\rho)}},$$
where the second term normalizes $C(1)=0$ so that degenerate (single-outcome) lotteries carry no penalty. Analysis is restricted to the gains domain with $0$ as the reference point. Estimation allows heterogeneous preferences following [[@Bruhin2010|Bruhin, Epper, and Fehr-Duda (2010)]]: agents are sorted into a small number of behavioral groups (e.g., three CPT-simplicity groups), each with its own weighting and cost parameters; for tractability all groups are constrained to share the same model class. For the field application, the PLS prize structure is linearized/scaled down to a $5 principal investment (about the average payoff in FP). They run 1,000 simulation draws; in each draw, each group's parameters are sampled independently from normal distributions with the means and standard deviations reported by FP (subject to nonnegativity constraints), then they compute whether a standard bank account or the PLS account is more attractive to each group. Models are also benchmarked against the best of several ML algorithms using "ML completeness scores" (expected value as the naive baseline, ML as the best-performing model), adapting [[@Fudenberg2022|Fudenberg, Kleinberg, Liang, and Mullainathan (2022)]].

## Data
Two sources. (1) FP's lab dataset: each participant supplies certainty equivalents for lotteries with two, three, four, five, and six outcomes — the variation in support size is what identifies behavioral type. (2) Field data on the "Million a Month" PLS accounts run by First National Bank in South Africa, January 2005–March 2008 (shut down after Lottery Board legal challenges). The calibration targets the take-up percentage among bank employees studied by Cole, Iverson, and Tufano (2021), and compares predicted demographic gradients to observed ones.

## Key findings
1. In FP's out-of-sample horse race, the heterogeneous CPT-simplicity hybrid performs best and nearly matches ML performance; CPT alone is second; simplicity alone beats PT but trails CPT; PT beats only expected utility. Hence both probability weighting and complexity aversion carry independent predictive weight.
2. Estimated heterogeneity yields three groups: one distorts probabilities mildly and is mildly complexity-averse; a second heavily distorts probabilities and is more complexity-averse (these two form a large majority, so weighting strength and complexity aversion appear correlated); a third is not complexity-averse with intermediate probability weighting.
3. In the PLS field exercise, CPT-simplicity predicts ~64% take-up versus actual ~63%, while CPT alone predicts ~84%. CPT overshoots because every group overweights the small PLS prize probabilities and so should like PLS; the complexity penalty in CPT-simplicity makes only the two groups whose probability distortion outweighs their complexity dislike take up the product, pulling the prediction down toward the data.
4. Consistent with FP, behavioral type is not well predicted by income, age, education, or employment — matching Cole, Iverson, and Tufano's finding that these branch-level aggregates do not predict PLS take-up.

## Contribution
Provides a compact statement of the CPT-simplicity functional form (including a reusable sigmoid complexity-cost specification the authors suggest for future empirical work) and supplies the first, if speculative, demonstration that a lab-calibrated simplicity-augmented CPT model can rationalize a real-world financial choice (PLS take-up) better than CPT alone. It thereby reframes the "certainty effect" literature: phenomena usually attributed to probability weighting may partly reflect a preference for lotteries with fewer outcomes, since canonical certainty-effect experiments compare only two-outcome lotteries to sure things.

## Limitations & open questions
The authors are explicit that the field exercise "should not be taken as evidence of one model over another" and carries strong caveats: (i) payoffs must be scaled down to match the experiment, and parameter estimates are sensitive to this scaling; (ii) the experimental population may not match the PLS take-up population; (iii) the calibration takes the model literally, with error coming only from parameter uncertainty; simulation standard errors are high and results are not statistically significant, so only the directional point estimates are discussed. Other open problems they name: complexity may operate through channels beyond support size (e.g., a uniform 20-outcome lottery may beat an irregular 19-outcome lottery with higher mean and lower variance); whether CPT-simplicity is formally less restrictive than CPT or simplicity in the Fudenberg-Gao-Liang sense is conjectured but not quantified; the cost function could be re-estimated on other data with optimization improvements (validation sets to choose the number of groups); the restriction forcing all heterogeneous groups into one model class has no a priori justification; and the link between cognitive ability and complexity aversion (suggested by Puri 2022) deserves further study.

## Connections
The paper sits at the intersection of prospect theory and a newer "simplicity" research program. The probability-weighting backbone is [[@Kahneman1979|Kahneman and Tversky (1979)]] [[@Tversky1992|PT and Tversky and Kahneman (1992)]] CPT; the complexity-cost idea derives from Puri (2018) "Preference for Simplicity," with related evidence in [[@Fudenberg2021a|Goodman and Puri (2021]], traders overpay for simple binary options) and Puri (2022, simplicity-and-risk predictions plus a cognitive-ability link). Heterogeneous-agent estimation follows Bruhin, Epper, and Fehr-Duda (2010). The model-evaluation methodology — completeness relative to ML and restrictiveness of functional forms — comes from Fudenberg, Kleinberg, Liang, and Mullainathan (2022) and [[@Fudenberg2021|Fudenberg, Gao, and Liang (2021)]]. The critique that the certainty effect may reflect support size rather than weighting connects to Bernheim and Sprenger (2020), Andreoni and Sprenger (2011), Moffatt, Sitzia, and Zizzo (2015), and Sonsino, Benzion, and Mador (2002). Enke and Graeber (2019) on cognitive uncertainty offers an alternative cognitive-limitation account. The PLS application builds on Kearney et al. (2010), Cole, Iverson, and Tufano (2014, 2021), Gertler et al. (2018), and Bharadwaj and Suri (2020).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
