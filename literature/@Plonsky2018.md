---
citekey: Plonsky2018
title: When and how can social scientists add value to data scientists? A choice prediction competition for human decision making
authors: ["Plonsky, Ori", "Apel, Reut", "Erev, Ido", "Ert, Eyal", "Tennenholtz, Moshe"]
year: 2018
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/35NZAGW2"
pdf: /Users/jesper/Zotero/storage/3NB8KMGY/Plonsky2018.pdf
tags: [literature]
keywords: [choice-prediction-competition, decisions-from-experience, behavioral-vs-machine-learning, risk-and-ambiguity, beast-model, benchmark-dataset]
topics: []
related: [Erev2010, Erev2017, Kahneman1979, Plonsky2017, Rendle2010, Tversky1992]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
This white paper introduces CPC18 (Choice Prediction Competition 2018), an open competition designed to probe *when and how* behavioral decision theory adds predictive value beyond off-the-shelf machine learning for human choice among monetary gambles. Building on CPC15, where structured behavioral models beat theory-free ML, the paper sets up two prediction tracks (aggregate behavior on new problems; individual behavior on familiar problems), provides a 210-problem calibration dataset and strong hybrid baselines (BEAST.sd and Psychological Forest), and frames the contest as an empirical test of three competing explanations for why pure ML underperformed in CPC15. The note is composed from the white paper's prose sections (front matter through references plus Appendix A); the long Appendix C estimation tables (problem-by-problem choice rates) were sampled rather than fully ingested.

## Research question
When and how can social scientists (behavioral decision theorists) add value to data scientists in predicting human decision making? Concretely: why did theory-free machine learning underperform structured behavioral models in CPC15, and under what conditions (data sparsity / cold start, feature engineering, choice of ML tool) does each approach dominate for predicting choice among gambles over repeated trials?

## Method / identification
The design is a structured prediction competition over a well-defined 12-dimensional space of binary monetary choice problems. Each option is a discrete distribution with up to 10 outcomes, parameterized for each option by five dimensions ($L$, $H$, $pH$, $\text{LotNum}$, $\text{LotShape}$) plus two problem-level dimensions ($\text{Corr}$, $\text{Amb}$). Option A yields high outcome $H_A$ with probability $pH_A$ and $L_A$ with probability $1-pH_A$; lottery shapes can be symmetric (binomial discretization of a normal around the mean), right-skewed, or left-skewed (truncated geometric with parameter $\tfrac{1}{2}$). The experimental paradigm (inherited from CPC15): decision makers choose repeatedly for 25 trials, the first 5 without feedback, the remaining 20 with full feedback (both obtained and forgone payoffs revealed). Trials are pooled into five blocks of five.

Two tracks operationalize different generalization demands. **Track I (aggregate behavior, new problems):** predict the time-block progression of the mean choice rate of Option B for 60 novel problems unseen at development time; code submission required. **Track II (individual behavior, familiar problems):** predict the block-by-block choice rate of 30 target individuals on five target problems each, given those individuals' choices on 25 other problems plus other individuals' behavior on the target problems — a collaborative-filtering / recommender-style setup; only predictions (CSV) submitted. The scoring rule is mean squared error (MSE), a proper scoring rule, computed over 300 (Track I) or 750 (Track II) choice rates, and translated to Equivalent Number of Observations (ENO). Bootstrap confidence intervals over random problem and subject samples identify submissions statistically indistinguishable from the winner.

## Data
A large existing dataset from the CPC15 paradigm: 510,750 observations / 334,500 unique consequential decisions, publicly released on Zenodo. Estimation set comprises Problems 1–150 (CPC15) plus Problems 151–210 from a new Experiment 1 (240 participants, 139 female, mean age 24.5, run at the Technion and Hebrew University; payoffs 10–136 shekels, mean ~40, about 11 USD). Experiment 2 (to be run later) supplies the held-out Track I competition set, selected via stratified pseudo-random sampling to match the calibration distribution of problem types.

## Key findings
Being a competition white paper, the substantive "findings" are baseline results that set the bar. (i) **BEAST** (Best Estimate and Simulation Tools), the CPC15 baseline, evaluates each prospect as the sum of its best EV estimate, the mean of a small mentally drawn sample (via four simulation tools — unbiased, equal weighting, sign, contingent pessimism), and estimation noise; it achieves MSE 0.0129 on Experiment 1's 60 problems. (ii) **BEAST.sd** (subjective dominance) relaxes the "trivial problem" definition to perceived triviality (both EV and equal-weighting rules favor the same prospect with no immediate regret), raises noise in complex problems, and assumes faster learning under ambiguity — reaching MSE 0.0071. (iii) **Psychological Forest**, a random forest fed BEAST's prediction plus 13 hand-crafted theory-driven features, attains out-of-sample MSE 0.0080, reducible to 0.0077 by augmenting training data with BEAST-generated artificial examples to combat sparsity. (iv) For Track II, a naive baseline (predict the average decision maker) gives MSE 0.1038 (correlation 0.63); a Factorization Machine — surprisingly hard to beat the naive baseline by much — gives MSE 0.0976 (correlation 0.66).

## Contribution
Provides a shared, large, publicly available benchmark and an explicit experimental framework for adjudicating the behavioral-theory-vs-ML question in choice prediction. It contributes (a) an expanded 12-dimensional problem space generalizing CPC15 (up to 10 outcomes per option, both options possibly multi-outcome), (b) strong hybrid baselines demonstrating that injecting behavioral theory as engineered features (Psychological Forest) is a productive middle path, and (c) a method for handling sparse regions of the problem space by generating synthetic training labels from a trusted behavioral model (BEAST). It separates three interpretations of ML's CPC15 failure — the cold-start/data-sparsity problem, suboptimal feature choice, and suboptimal tool choice — into empirically testable hypotheses.

## Limitations & open questions
The paper explicitly leaves open: which of the three interpretations of CPC15's ML failure is correct (the competition is designed precisely to resolve this). Whether sophisticated theory-free tools (e.g., deep networks, as in strategic-game prediction) can win Track I without behavioral priors. Whether better feature engineering alone closes the gap. For Track II, the difficulty of beating the naive "average decision maker" baseline, and the open question of how best to link a decision maker's responses across heterogeneous problems (the maximization-rate transformation is offered as one option, with competitors invited to find better links). The factorization machine does not exploit known cross-block correlation within a problem — leaving room for temporally aware models. More broadly: whether behavioral theory's apparent edge persists in richer, less theoretically structured domains.

## Connections
Directly extends [[@Erev2017|Erev et al. (2017)]], "From Anomalies to Forecasts," which established the CPC15 paradigm and the BEAST model, and [[@Erev2010|Erev et al. (2010)]], the original choice-prediction competition on choices from experience and description. Psychological Forest derives from [[@Plonsky2017|Plonsky, Erev, Hazan & Tennenholtz]] (2017, AAAI), and the synthetic-data augmentation echoes that line. The deep-network-beats-behavioral-model result for strategic choice cited as the third interpretation is Hartford, Wright & Leyton-Brown (2016, NeurIPS). Foundational decision theory invoked includes von Neumann & Morgenstern (1944), Savage (1954), and Bernoulli (1738/1954) for rationality, and Allais (1953), Ellsberg (1961), and [[@Kahneman1979|Kahneman & Tversky (1979)]] / [[@Tversky1992|Tversky & Kahneman (1992)]] for the anomalies the models must capture. Methodological scaffolding draws on Selten (1998) for the quadratic/MSE proper scoring rule, Erev, Roth, Slonim & Barron (2007) for ENO, Breiman (2001) for random forests, [[@Rendle2010|Rendle (2010)]] for factorization machines, and Schein et al. (2002) for the cold-start problem. Task-complexity moderators reference Glöckner et al. (2016) and Weiss-Cohen et al. (2018).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
