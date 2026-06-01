---
citekey: Fudenberg2019a
title: Measuring the Completeness of Theories
authors: ["Fudenberg, Drew", "Kleinberg, Jon", "Liang, Annie", "Mullainathan, Sendhil"]
year: 2019
type: preprint
doi: ""
zotero: "zotero://select/library/items/SYVB2K9I"
pdf: /Users/jesper/Zotero/storage/EMPT38B3/Fudenberg2019a.pdf
tags: [literature]
keywords: [model-completeness, predictive-accuracy, machine-learning, cumulative-prospect-theory, initial-play, cognitive-hierarchy, behavioral-models]
topics: []
related: [Gneiting2007, Noti2016, Peysakhovich2017, Plonsky2019]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> We use machine learning to provide a tractable measure of the amount of predictable variation in the data that a theory captures, which we call its "completeness." We apply this measure to three problems: assigning certain equivalents to lotteries, initial play in games, and human generation of random sequences. We discover considerable variation in the completeness of existing models, which sheds light on whether to focus on developing better models with the same features or instead to look for new features that will improve predictions. We also illustrate how and why completeness varies with the experiments considered, which highlights the role played in choosing which experiments to run.

## Summary

The paper proposes a single scalar diagnostic — *completeness* — for evaluating how good an economic theory is at prediction, given a fixed feature set. The central observation is that raw predictive accuracy is uninterpretable in isolation, because prediction error confounds two distinct things: (i) the *opportunity for a better model* built on the same features, and (ii) *irreducible noise* stemming from the limits of the feature set itself. An accuracy of 55% may be remarkable for predicting stock movements but worthless for predicting planetary motion; the difference lies in the best achievable performance each problem permits. Completeness measures how close a theory comes to that achievable bound. The authors estimate the bound non-parametrically with a Table Lookup algorithm and apply the measure to three canonical experimental-economics domains, finding striking heterogeneity: Cumulative Prospect Theory is 95% complete for certainty equivalents, the Poisson Cognitive Hierarchy Model is roughly 67–68% complete for initial play, while the best model of human randomness generation is only ~24% complete.

## Research question

Holding fixed the measured features, how much of the *predictable* variation in a domain does a given theory capture, and how much room remains for a better model built on the same features versus the need for new features? Equivalently: how close is a theory's predictive performance to the best achievable performance for that feature set and data?

## Method / identification

A prediction problem has features $X = X_1 \times \cdots \times X_N$ and outcome space $\mathcal{Y}$; a point prediction rule is a map $f : X \to \mathcal{Y}$, and an economic model is a parametric family $F = (f_\theta)_{\theta \in \Theta}$. Predicting a distribution over $\mathcal{Y}$ is cast as predicting a point in $\mathcal{Y}' = \Delta(\mathcal{Y})$. Given a loss $L$, three reference errors are defined:

- $e^{\text{naive}}$: error of an uninformative benchmark (e.g. unconditional mean / mode / Expected Value).
- $e^{\text{model}}$: out-of-sample error of the theory under study.
- $e^{*}$: the irreducible error — the loss of the ideal rule $f^{*}_P(x) = \mathbb{E}_P[y \mid x]$.

Completeness is the fraction of the feasible improvement that the model achieves:
$$\kappa = \frac{e^{\text{naive}} - e^{\text{model}}}{e^{\text{naive}} - e^{*}}.$$
So the naive benchmark is 0% complete and the ideal rule is 100% complete.

The key operational move is estimating $e^{*}$ via **Table Lookup**: build a table whose rows are the unique feature vectors $x$ and whose prediction is the training-data mean (for regression / MSE) or modal outcome (for classification / misclassification rate) for that $x$. With enough observations per row, Table Lookup converges to $f^{*}_P$ and its out-of-sample error approximates $e^{*}$. All errors are estimated by $K$-fold cross-validation. Appendix A justifies this: under MSE the expected error decomposes into irreducible noise + bias + sampling error; Table Lookup is unbiased, so the cross-validated variance estimates the sampling error and the cross-validated standard errors bound how well Table Lookup approximates the irreducible noise. The authors confirm robustness by comparing Table Lookup against bagged decision trees (Table Lookup weakly wins) and by subsampling (70% of data yields nearly identical accuracy), evidencing that the data are large enough relative to the number of unique feature vectors.

## Data

Three experimental data sets, each with discrete or finitely-many unique feature vectors (a precondition for Table Lookup): (1) **risk preferences** — certainty equivalents for 50 unique two-outcome lotteries from Bruhin, Fehr-Duda & Epper (2010); (2) **initial play in games** — two data sets (A and B) of first-encounter play in simultaneous-move games (the Fudenberg & Liang 2018 corpus); (3) **human random-sequence generation** — a new Mechanical Turk data set of incentivized length-8 strings meant to mimic a Bernoulli(0.5) process. This is an applied-methodology paper, so it is data-rich rather than a pure theory paper.

## Key findings

- **Risk (CPT).** Expected Utility is only 11% complete while Cumulative Prospect Theory reaches 95% (errors: naive 103.81, EU 99.67, CPT 67.38, Table Lookup 65.58). CPT thus captures nearly all predictable variation available from $(z_1, z_2, p)$; further gains require *new features* (e.g. subject type, response times), not better functional forms.
- **Initial play (PCHM).** The Poisson Cognitive Hierarchy Model is 68% complete on Data Set A and 67% on Data Set B — nearly identical *despite* different absolute improvements — illustrating that raw accuracy misleads without a benchmark. On a curated subset of games where the level-1 action dominates against uniform play, PCHM reaches 97% complete.
- **Randomness.** The best model (a Rabin-style account) is only ~24% complete (and 9–19% under a misclassification-rate variant), signalling large unmodelled structure in how humans fake randomness.
- **Feature-set comparison (§3.2).** Compressed Table Lookups isolate the predictive value of feature subsets: "number of Heads" alone achieves 59% of full completeness, the last three flips 36% — demonstrating that early flips carry residual predictive content and that completeness is feature-set- and data-set-relative.

## Contribution

The paper's main contribution is methodological: a portable, model-agnostic yardstick that decomposes predictive error into "room for a better model on these features" versus "irreducible noise," using off-the-shelf machine learning (Table Lookup / non-parametric conditional expectation) to estimate the achievable frontier. It operationalizes the long-standing distinction between a theory being *predictive* and being *complete*, and it reframes experimental design as a lever on completeness — the choice of lotteries or games changes the irreducible error and hence what completeness even means.

## Limitations & open questions

- **Feasibility ceiling.** Table Lookup only approximates $e^{*}$ when data are large relative to the number of unique feature vectors; it requires discrete features or finitely many instances and breaks down with rich continuous covariates.
- **Relativity.** Completeness is conditional on a chosen feature set *and* data set; the 95% figure for CPT need not generalize beyond two-outcome lotteries. Building richer, transferable feature sets is left open.
- **Predictiveness is only one criterion.** Interpretability and generality may justify preferring a less-complete model; the paper does not formalize that trade-off.
- **Cross-domain transfer.** The whole apparatus is within-domain; the authors explicitly flag *transferability* — whether economically structured models that lose in-domain transfer better out-of-domain — as future work, and an "overall completeness" notion as undeveloped.

## Connections

The estimand $f^{*}_P(x) = \mathbb{E}_P[y \mid x]$ and the bias–variance decomposition follow Hastie, Tibshirani & Friedman (2009) and Domingos (2000). The risk application uses Bruhin, Fehr-Duda & Epper (2010) and engages Expected Utility versus Cumulative Prospect Theory, with Rabin (2000) on calibration critiques. The initial-play application builds directly on Fudenberg & Liang (2018) on predicting and understanding initial play, the Poisson Cognitive Hierarchy Model of Camerer, Ho & Chong (2004), and the structural level-$k$ tradition of Nagel (1995) and Crawford, Costa-Gomes & Iriberri (2013). The randomness application draws on the gambler's-fallacy and misperception-of-randomness literature — Tversky & Kahneman (1971), Bar-Hillel & Wagenaar (1991), Barberis, Shleifer & Vishny (1998), Chen, Shue & Moskowitz (2016) — and Rabin-style models of inference from short sequences. Methodologically it sits beside the "machine learning to evaluate behavioral models" program of [[@Peysakhovich2017|Peysakhovich & Naecker (2017)]], [[@Plonsky2019|Plonsky et al. (2019)]], [[@Noti2016|Noti et al. (2016)]], and Kleinberg et al. (2017) on human decisions and machine predictions. The probabilistic-prediction framing connects to proper scoring rules as in [[@Gneiting2007|Gneiting & Raftery (2007)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
