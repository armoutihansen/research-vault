---
citekey: Fudenberg2022
title: Measuring the Completeness of Economic Models
authors: ["Fudenberg, Drew", "Kleinberg, Jon", "Liang, Annie", "Mullainathan, Sendhil"]
year: 2022
type: journalArticle
doi: 10.1086/718371
zotero: "zotero://select/library/items/8YVN2SVA"
pdf: /Users/jesper/Zotero/storage/Q8UYSXVW/Fudenberg2022.pdf
tags: [literature]
keywords: [model-completeness, irreducible-error, predictive-accuracy, machine-learning-economics, experimental-economics, behavioral-models]
topics: []
related: [Bruhin2010, Charness2002, Fudenberg2019a, Fudenberg2020, Peysakhovich2017, Tversky1992]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Economic models are evaluated by testing the correctness of their predictions. We suggest an additional measure, "completeness": the fraction of the predictable variation in the data that the model captures. We calculate the completeness of prominent models in three problems from experimental economics: assigning certainty equivalents to lotteries, predicting initial play in games, and predicting human generation of random sequences. The completeness measure reveals new insights about these models, including how much room there is for improving their predictions.

## Summary
The paper proposes **completeness** as a second axis (alongside correctness) for evaluating economic models: not "is the model right?" but "how much of the *predictable* signal in the data, given the measured features, does the model capture?" A model's prediction error decomposes into (i) **irreducible error** — the floor set by intrinsic noise in the outcome given the features — and (ii) regularities the model misses. Completeness normalizes the model's improvement over a baseline by the *achievable* improvement (baseline error minus irreducible error). The key methodological insight is that in many experimental data sets there are enough observations per feature value that the irreducible error can be estimated nonparametrically with a simple **lookup table**. The authors estimate completeness for three canonical behavioral models and show that raw error and raw error-reduction are both badly misleading guides to how much room remains for better theory.

## Research question
When an economic model predicts a given outcome with some error, how do we know whether that error is large because the *model* is bad (missing regularities that other models on the same features could capture) versus because the *outcome is intrinsically noisy* given the available features? Equivalently: how close is a model to the best achievable prediction, and hence how much headroom exists for improving theory without collecting new kinds of data?

## Method / identification
The setup is a **prediction problem**: an outcome $Y$, features $X$, an unknown joint distribution $P$ over $X\times Y$, and a loss function $\ell(y',y)$ (e.g. squared error $\ell(y',y)=(y'-y)^2$ or misclassification $\ell(y',y)=\mathbf{1}(y'\ne y)$). The expected error (risk) of a prediction rule $f$ is $E_P(f)=\mathbb{E}_P[\ell(f(x),y)]$.

An economic model is a parametric family $F_\Theta$ of prediction rules; its best member has error $E_P(f_\Theta^\*)$ where $f_\Theta^\*\in\arg\min_{f\in F_\Theta}E_P(f)$. Two reference points bracket it:
- The **ideal rule** $f^\*(x)\in\arg\min_{y'\in Y}\mathbb{E}_P[\ell(y',y)\mid x]$, whose error is the **irreducible error** $E_P(f^\*)$ — a lower bound on any rule built from $X$.
- A problem-appropriate **baseline** $f_{base}\in\Delta(F_\Theta)$ (e.g. predict a lottery's expected value; guess uniformly at random in games), interpreted as the "worst-case" accuracy.

**Completeness** is then defined as
$$\frac{E_P(f_{base})-E_P(f_\Theta^\*)}{E_P(f_{base})-E_P(f^\*)}.$$
A model with completeness $0$ does no better than baseline; completeness $1$ removes all but irreducible error. Crucially a model can be near-complete even with low $R^2$ and large absolute error.

**Estimation.** Working over an arbitrary set $F$ of maps (with the special cases $F=\{f_{base}\}$, $F=F_\Theta$, and $F=X^Y$, the unrestricted set of all maps, recovering the three errors), each error is estimated by **10-fold cross-validated out-of-sample error**: split data into $K=10$ folds; on each training set pick $f_i\in\arg\min_{f\in F}e(f,Z^{train}_i)$; evaluate $\mathrm{CV}_i=e(f_i,Z^{test}_i)$; average. The empirical completeness $(\hat{E}_{base}-\hat{E}_\Theta)/(\hat{E}_{base}-\hat{E}_{best})$ is a **consistent estimator** of the theoretical ratio. Irreducible error $\hat{E}_{best}$ is estimated by a **lookup table** — for each unique $x$, predict the training-data mean (or modal) outcome — which approximates $f^\*$ when there are many observations per $x$. Two validation checks: a bagged-decision-tree alternative (lookup table has lower error in all applications), and a 70%-subsample convergence check. Standard errors come from a subject-clustered block bootstrap (1,000 draws).

## Data
Three experimental data sets, all with many observations per feature value:
- **Lotteries (risk):** [[@Bruhin2010|Bruhin, Fehr-Duda & Epper (2010)]] — 8,906 certainty equivalents from 179 subjects over 50 two-outcome lotteries (Zurich 2003); plus Beijing 2005 (4,225 obs, 151 subjects) and Zurich 2006 (4,669 obs, 118 subjects). ~179 obs per unique lottery.
- **Initial play in games:** [[@Fudenberg2019a|Fudenberg & Liang (2019)]] — 23,137 observations of row-player play in 486 $3\times3$ matrix games (pooled from a Wright–Leyton-Brown meta-set plus MTurk games, some algorithmically designed against level-1); no learning. ~50 obs per game. Analyzed via three subsamples (game sets A/B/C).
- **Random sequences:** authors' own MTurk data — 21,975 length-8 strings from 167 subjects asked to mimic a Bernoulli(0.5) process (incentivized so payment required strings not detectable as human-generated). ~164 obs per length-7 prefix.

## Key findings
- **Cumulative prospect theory (CPT)** for certainty equivalents: absolute MSE is large (67.78 vs baseline 104.63), but irreducible error is 65.58, so CPT is **94% complete** — almost no headroom for new models on $(\bar z,\underline z,p)$. Across the three lottery data sets raw CPT error ranges 4.94–67.78 yet completeness is stable, **lower-bounded at 92%** (Zurich 2003 94%, Beijing 2005 99%, Zurich 2006 92%). This illustrates that *absolute error is misleading*.
- **Poisson cognitive hierarchy model (PCHM)** for initial play: completeness **varies sharply by game class** — ~68% on game set A (no dominated actions) and game set B (cooperative profile dominates), but **97%** on game set C (level-1 action clearly highest expected payoff against uniform play). So substantial predictable structure beyond PCHM exists in some game families but not others.
- **[[@Charness2002|Rabin (2002)]] / Rabin & Vayanos (2010)** for human-generated randomness: best absolute error-reduction over baseline is only 0.0006, which against perfect prediction would suggest ~0.2% completeness; but irreducible error is 0.2441, so the models reach **up to 10% completeness** ([[@Charness2002|Rabin 2002]] 7%, Rabin–Vayanos 10%). Negative autocorrelation is real but much predictable structure remains. This illustrates that *absolute gain over baseline is also misleading*.
- **Extensions.** (i) Heterogeneity: CPT estimated separately for Bruhin et al.'s three subject groups is **89% complete** — comparable to the representative-agent version (heterogeneity weakly lowers both completeness and irreducible error, with ambiguous net effect). (ii) Feature-set comparison: for randomness, using only the *number of heads* in the first seven flips reaches 65% of the achievable reduction, and only the *most recent three flips* reaches 40%, with flips 1–3 carrying predictive content beyond flips 4–7.

## Contribution
Introduces a portable, loss-function-agnostic completeness measure and — more importantly — shows that **irreducible error can be directly and cheaply estimated** (via lookup tables) across a range of experimental settings, rather than only lower-bounded by black-box ML as in prior work ([[@Peysakhovich2017|Peysakhovich & Naecker 2017]]; Bodoh-Creed et al. 2019). It supplies a vocabulary for the trade-off between simple/interpretable and predictive models analogous to "optimal solution vs approximation algorithm," and demonstrates that several leading behavioral models are far more (or differently) complete than their raw errors suggest.

## Limitations & open questions
The paper is explicit about several open hooks:
- **Better subject grouping.** A highlighted passage: "The development of better grouping techniques is an interesting avenue for future work." Because the same grouping algorithm is used everywhere, the irreducible-error gap does *not* reveal how much better grouping could improve predictions.
- **What drives game-class differences.** "We leave to future work the question of what additional properties of the game are important determinants of the completeness of the PCHM" (the 68% vs 97% gap across game sets A/B/C).
- **Feature dependence / expanding $X$.** Completeness is defined for a fixed feature set; expanding $X$ weakly raises the optimum, so a complete model can become incomplete. Which neuroeconomic/demographic features (response time, age, education) would help is left open.
- **Counterfactuals.** Completeness speaks to within-sample prediction; genuine policy counterfactuals (e.g. a sales tax when data only contain firm price changes) still rest on untested robustness assumptions.
- **Portability / "overall completeness."** Models outperformed in-domain by ML may transfer better out-of-domain; within-domain completeness may be an insufficient measure of overall completeness — a notion left to future work.
- **Alternative ways to estimate irreducible noise** (analogy to the "missing heritability" problem in biology) when lookup tables are infeasible.

## Connections
The completeness ratio specializes, under MSE with an unconditional-mean baseline, to a ratio of the model's $R^2$ to the nonparametric $R^2$ (App. B). It is a companion to **[[@Fudenberg2020|Fudenberg, Gao & Liang (2020)]]** on model *restrictiveness* (completeness on synthetic data) and to **[[@Fudenberg2019a|Fudenberg & Liang (2019)]]** on predicting modal play; together these form a program for ML-assisted theory evaluation. It contrasts with earlier predictive-success measures — Selten (1991), Erev et al. (2007), Apesteguia & Ballester (2021) — by benchmarking against the *best achievable* prediction. Related ML-comparison work includes [[@Peysakhovich2017|Peysakhovich & Naecker (2017)]], Bodoh-Creed, Boehnke & Hickman (2019), Noti et al. (2016), Plonsky et al. (2017, 2019), Bourgin et al. (2019, on intrinsic noise), and the bias–variance/irreducible-error literature (Hastie, Tibshirani & Friedman 2009). The substantive models tested are [[@Tversky1992|Tversky & Kahneman (1992)]] CPT, the Camerer–Ho–Chong (2004) PCHM with its level-$k$ antecedents (Stahl & Wilson 1994; Nagel 1995), and [[@Charness2002|Rabin (2002)]] / Rabin & Vayanos (2010) on misperceived randomness.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
