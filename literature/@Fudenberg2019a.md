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
keywords: [initial-play, level-k, cognitive-hierarchy, machine-learning, choice-prediction, matrix-games, model-interpretability]
topics: ["[[choice-prediction-risky-choice]]", "[[ml-evaluating-economic-theories]]"]
related: [Noti2016, Peysakhovich2017, Plonsky2019]
added: 2026-06-02
generated: 2026-06-02
---

> [!abstract] Abstract
> We use machine learning to uncover regularities in the initial play of matrix games. We first train a prediction algorithm on data from past experiments. Examining the games where our algorithm predicts correctly, but existing economic models don't, leads us to add a parameter to the best performing model that improves predictive accuracy. We then observe play in a collection of new "algorithmically generated" games, and learn that we can obtain even better predictions with a hybrid model that uses a decision tree to decide game-by-game which of two economic models to use for prediction.

## Summary

The paper asks how well we can predict the action a person takes the first time they encounter a simultaneous-move matrix game, and uses machine learning not as a black-box predictor but as a microscope for *theory discovery*. Existing behavioral models of initial play — level-$k$ reasoning, the Poisson Cognitive Hierarchy Model — depart from equilibrium analysis, which predicts first play poorly, but it is unclear how much predictable structure they leave on the table. Fudenberg & Liang treat off-the-shelf prediction algorithms as a benchmark for the best achievable accuracy on a given feature set, then inspect the games where the algorithm beats the leading economic model. Those discrepancies are diagnostic: they reveal a missing regularity (the salience of the payoff-maximizing outcome) that, once added as a parameter to the best model, closes much of the gap. The authors then validate the augmented model out of sample on a fresh corpus of *algorithmically generated* games designed to be hard for existing theories, and show that a hybrid decision-tree model — selecting game-by-game between two economic models — predicts best of all. The methodology is an explicit human–AI loop: the algorithm flags where theory fails, the analyst proposes new structure, and that structure is tested on data engineered to stress it.

## Research question

Can we predict how people will play the first time they encounter a given $3 \times 3$ matrix game, using only the payoff entries as features? And, more pointedly: where do the leading economic models of initial play fall short of the best achievable prediction, what regularity are they missing, and can identifying that regularity yield a better, still-interpretable model?

## Method / identification

The prediction target is the row player's chosen action $a \in \{a_1, a_2, a_3\}$; the features are the eighteen payoff entries of the $3 \times 3$ game, so a prediction rule is a map $f : \mathbb{R}^{18} \to \{a_1, a_2, a_3\}$. Performance is measured by out-of-sample misclassification rate, estimated by cross-validation, with a key wrinkle relative to within-sample fitting: games are split so that the same game does not appear in both training and test folds, which tests genuine *extrapolation across games* rather than memorization of game-specific play.

The workflow proceeds in three stages. First, a flexible prediction algorithm is trained on a meta data set of play pooled from prior experimental papers, establishing a benchmark for how predictable play is given the payoff features. Second, the authors compare this benchmark against leading economic models — the level-$k$ family and the Poisson Cognitive Hierarchy Model, in which a level-$k$ player best-responds to a Poisson$(\tau)$ belief over lower levels and the level-0 player randomizes uniformly. They then isolate the games where the algorithm predicts correctly but the economic model does not, and read those games to diagnose the missing feature: play gravitates toward the action profile with the highest joint payoff sum even when it lies outside the level-$k$ support — a welfare/efficiency salience the cognitive-hierarchy logic ignores. They formalize this by adding a parameter to the best-performing model that shifts predicted weight toward the payoff-maximizing action, improving accuracy while keeping the model interpretable. Third, to guard against overfitting the diagnosis to the existing corpus, they collect play on a new set of *algorithmically generated* games — including games deliberately constructed so that a target model performs poorly — and confirm the augmented model's gains hold out of sample. Finally, they show a *hybrid* model that uses a decision tree on the payoff features to decide, game by game, which of two economic models to apply, attaining the best predictions; the tree thereby learns the *region of applicability* of each behavioral model rather than committing to one globally.

## Data

This is an empirical / methodological paper, not pure theory, and it is unusually data-rich. The combined corpus comprises 23,137 observations of initial play across 486 $3 \times 3$ matrix games from three sources: (i) a meta data set of play in 86 games compiled from six prior experimental game-theory papers (the Wright & Leyton-Brown collection); (ii) 200 games with randomly generated payoffs, run on Amazon Mechanical Turk; and (iii) 200 games "algorithmically designed" so that a particular model (level 1) would predict poorly, also on MTurk. There was no learning within sessions: subjects were randomly matched, were not told their opponents' play, and learned their own payoffs only at the end. Subjects also wrote free-form explanations of their reasoning (reproduced in the online appendix), giving qualitative texture to the choice data.

## Key findings

- **The algorithm-versus-theory gap is informative.** Examining the games where the prediction algorithm is right but the economic model is wrong localizes a concrete, interpretable regularity rather than leaving an opaque accuracy gap — turning machine learning into an instrument for model building rather than a substitute for it.
- **Payoff-maximizing salience.** People disproportionately choose the action contributing to the highest joint-payoff profile, even when that action falls outside the support of level-$k$ actions. Adding a single parameter capturing this attraction to the best-performing economic model raises predictive accuracy while preserving interpretability.
- **Out-of-sample validation on adversarial games.** The augmented model's improvements persist on the freshly collected, algorithmically generated games engineered to be hard for existing theories — evidence the added feature reflects real behavior, not corpus-specific overfitting.
- **Hybrid model wins.** A decision tree that picks, game by game, which of two economic models to apply yields the best predictions of all, indicating that different behavioral models dominate in different regions of game space and that the choice among them is itself learnable from the payoff entries.

## Contribution

The contribution is both substantive and methodological. Substantively, it identifies a missing regularity in initial play — attraction to the payoff-maximizing outcome — and delivers an augmented, still-interpretable model that predicts better than standard level-$k$ / cognitive-hierarchy accounts. Methodologically, it demonstrates a reproducible human–AI theory-improvement loop: use a flexible algorithm as a ceiling on achievable accuracy, inspect where theory underperforms that ceiling to surface candidate features, formalize them parsimoniously, and stress-test on adversarially generated data. The hybrid decision-tree-over-models construction combines the interpretability of economic models with the flexibility of machine learning by learning each model's domain of validity. This program motivated the companion completeness measure — the published "Measuring the Completeness of Theories" (Fudenberg, Kleinberg, Liang & Mullainathan) lives separately under Fudenberg2022 — which reuses this paper's initial-play corpus as one of its applications.

## Limitations & open questions

- **Scope of games.** Results concern $3 \times 3$ simultaneous-move matrix games with the eighteen payoff entries as the only features; whether the payoff-maximization regularity and the hybrid approach generalize to larger games, asymmetric or non-matrix interactions, or richer feature sets (e.g. response times, free-text reasoning) is left open.
- **Representative-agent framing.** Play is pooled across subjects, so heterogeneity in strategic sophistication is folded into a single predictive distribution rather than modeled at the individual level.
- **Interpretability of the hybrid.** While each component model is interpretable, the decision tree that arbitrates between them adds a layer whose behavioral meaning is less transparent; the trade-off between predictive gain and explanatory clarity is acknowledged rather than resolved.
- **Generated-game distribution.** The algorithmically generated games are engineered relative to specific models, so the measured improvements are conditional on that design distribution and need not reflect any "natural" population of games encountered in the field.

## Connections

The paper extends the non-equilibrium initial-play tradition: the level-$k$ models of Stahl & Wilson (1994, 1995) and Nagel (1995), the Poisson Cognitive Hierarchy Model of Camerer, Ho & Chong (2004), and the structural survey of Crawford, Costa-Gomes & Iriberri (2013). Its level-0 meta-model benchmark and pooled game corpus build on Wright & Leyton-Brown (2014). Methodologically it belongs to the program using machine learning to evaluate and improve behavioral models of choice — [[@Peysakhovich2017|Peysakhovich & Naecker (2017)]], [[@Noti2016|Noti et al. (2016)]], [[@Plonsky2019|Plonsky et al. (2019)]], and Camerer, Nave & Smith (2018) on bargaining — and to Kleinberg et al. (2017) on contrasting human decisions with machine predictions. The diagnostic logic of comparing a model against an algorithmic best-achievable benchmark is formalized in the authors' own completeness work (Fudenberg, Kleinberg, Liang & Mullainathan), and the theme of cognitive-model priors for predicting human decisions appears in [[@Plonsky2019|Bourgin et al. (2019)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
