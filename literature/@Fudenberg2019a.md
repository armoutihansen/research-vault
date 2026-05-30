---
citekey: Fudenberg2019a
title: Predicting and Understanding Initial Play
authors: ["Fudenberg, Drew", "Liang, Annie"]
year: 2019
type: journalArticle
doi: 10.1257/aer.20180654
zotero: "zotero://select/library/items/ZBSF9MFQ"
pdf: /Users/jesper/Zotero/storage/PI6QUWFY/Fudenberg2019.pdf
tags: [literature]
keywords: [initial-play, level-k, cognitive-hierarchy, machine-learning, model-completeness, matrix-games, behavioral-game-theory]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We use machine learning to uncover regularities in the initial play of matrix games. We first train a prediction algorithm on data from past experiments. Examining the games where our algorithm predicts correctly, but existing economic models don't, leads us to add a parameter to the best performing model that improves predictive accuracy. We then observe play in a collection of new "algorithmically generated" games, and learn that we can obtain even better predictions with a hybrid model that uses a decision tree to decide game-by-game which of two economic models to use for prediction.

## Summary
Fudenberg and Liang use machine learning not to replace behavioral game-theory models but to discover where they fail and to guide their improvement. Treating initial play in $3\times3$ matrix games as a supervised prediction problem (payoff matrix $\to$ row action), they train a black-box predictor, isolate the games where it beats the best structural model, read off the behavioral regularity the model is missing, and fold that regularity back into the model as a new parameter. They then collect play on "algorithmically generated" games designed to be hard for existing models, and show a decision-tree hybrid that selects, game by game, between two economic models predicts best of all. The method treats ML as a diagnostic and a performance ceiling rather than an end in itself.

## Research question
How well can we predict how people play a matrix game the *first* time they see it, which existing behavioral model predicts best, and—crucially—can a model-agnostic machine-learning benchmark reveal the *systematic* regularities those models miss so that the models can be improved rather than merely outperformed?

## Method / identification
The prediction problem: the outcome is the row player's chosen action; the features are the 18 entries of a $3\times3$ payoff matrix. A prediction rule is any map $f:\mathbb{R}^{18}\to\{a_1,a_2,a_3\}$, and performance is the out-of-sample misclassification rate $\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}(f(g_i)\neq a_i)$, evaluated by tenfold cross-validation. The naive baseline is uniform guessing (expected error $2/3$).

Structural benchmarks come from the level-$k$ / cognitive-hierarchy family: the level-0 player randomizes uniformly, level-1 best-responds to level-0, and the Poisson Cognitive Hierarchy Model (PCHM, Camerer–Ho–Chong) places a Poisson($\tau$) distribution over levels, with level-$k$ players ($k\ge2$) best-responding to the normalized truncated belief $p_k(h)=\pi_\tau(h)/\sum_{l=0}^{k-1}\pi_\tau(l)$ for $h\in\mathbb{N}_{<k}$; $\tau$ is estimated on training data. The point prediction is the modal action of the induced distribution.

The identification of *what models miss* is the core methodological move. They train a flexible ML predictor, then partition the test games into those the ML rule classifies correctly versus those it does not, and inspect the games where ML succeeds but the structural model fails. Diagnosing this gap motivates adding a parameter to the best-performing model. Finally, they design "algorithmically generated" games—payoffs constructed so a target model (e.g. level-1) predicts poorly—collect fresh play on them, and fit a hybrid: a decision tree that, conditional on the game's payoffs, routes each game to whichever of two economic models to trust. A companion paper (Fudenberg, Kleinberg, Liang, Mullainathan, "Measuring the Completeness of Economic Models," whose draft is the attached PDF and which reuses this exact data set) formalizes the ceiling via a Table Lookup benchmark: rows are games, predictions are training-set modal actions; with enough observations per game this approximates the best achievable error, and *completeness* $=$ (model improvement over naive) $/$ (Table Lookup improvement over naive).

## Data
23,137 observations of initial play across 486 distinct $3\times3$ matrix games, pooled across subjects and games. The corpus aggregates three sources: a meta-dataset of 86 games compiled from six prior experimental papers (Wright and Leyton-Brown, 2014); 200 randomly-generated-payoff games run on Amazon Mechanical Turk; and 200 "algorithmically designed" games built to make a target model predict poorly. There was no learning—subjects were randomly rematched, never told partners' play, and saw their own payoffs only at the end—so the data are genuinely *initial* play. (Coverage note: the directly attached PDF is the closely related completeness manuscript plus the online appendix; figures here for the data and PCHM analysis are drawn from that manuscript's Domain #2, which is built on this paper's dataset and the metadata abstract.)

## Key findings
PCHM is clearly predictive—on subsets of the data it improves the misclassification rate from the naive $0.66$ to roughly $0.44$–$0.49$, and to $0.28$ on games where the level-1 action's expected payoff against uniform play dominates the next best action. But it is far from the achievable ceiling: relative to Table Lookup, PCHM attains about 67–68% completeness on the harder game sets and up to 97% on the "obvious level-1" games, showing that predictive accuracy is meaningless without a benchmark for irreducible noise. Examining the games where ML beats PCHM exposes a missing behavioral regularity that, encoded as one extra parameter, raises the best model's accuracy. On the algorithmically generated games, a decision-tree hybrid that selects between two economic models game-by-game predicts better than either model alone.

## Contribution
The paper pioneers a "complementary" use of machine learning in economics: ML as an upper bound on predictability and as a microscope for *where and how* structural models are incomplete, rather than as a competitor that merely wins on accuracy. It delivers an improved, still-interpretable model of initial play, introduces algorithmically generated games as a tool to stress-test theories, and supplies the empirical backbone for the completeness measure developed in the companion paper—reframing model evaluation around the gap between a model and the best feasible predictor on a fixed feature set.

## Limitations & open questions
The authors are explicit that (i) a model's measured completeness is tied to a *specific* dataset and feature set—here, $3\times3$ games and the 18 raw payoffs—and need not generalize; expanding either feature set or game class can change the verdict. (ii) High completeness may reflect either a good match to behavior *or* a functional form flexible enough to mimic Table Lookup, and disentangling these is left to future work. (iii) Predictiveness is only one criterion; interpretability and generality may justify preferring a less-complete model. (iv) All evaluation is within-domain (train and test on the same kind of games); how to measure *transferability* of models across domains—where economic models may beat ML—is posed as an open problem. (v) Substantially better prediction would require new features (e.g. response times, subject types) beyond the payoff matrix.

## Connections
The structural benchmarks are the level-$k$ models of Stahl and Wilson (1994, 1995) and Nagel (1995) and the Poisson Cognitive Hierarchy Model of Camerer, Ho and Chong (2004), with the broader landscape surveyed by Crawford, Costa-Gomes and Iriberri (2013). The aggregated game data builds on Wright and Leyton-Brown (2014). The methodological program—ML as a yardstick for the predictable variation a theory captures—is formalized in the companion Fudenberg, Kleinberg, Liang and Mullainathan "completeness" paper, which also applies the Table Lookup benchmark to risk preferences (Cumulative Prospect Theory, with data from Bruhin, Fehr-Duda and Epper, 2010) and to human generation of random sequences (Rabin, 2002; Rabin and Vayanos, 2010). The use of ML to interrogate human decisions echoes Kleinberg et al. (2017) on predicting judicial decisions, and the general agenda of prediction-focused economics relates to Mullainathan and Spiess on machine learning as an applied econometric tool.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
