---
citekey: Fudenberg2019b
title: Predicting and Understanding Initial Play
authors: ["Fudenberg, Drew", "Liang, Annie"]
year: 2019
type: journalArticle
doi: 10.1257/aer.20180654
zotero: "zotero://select/library/items/ZBSF9MFQ"
pdf: /Users/jesper/Zotero/storage/EEMEXMP5/26848479.pdf
tags: [literature]
keywords: [initial-play, level-k, cognitive-hierarchy, machine-learning, choice-prediction, completeness, matrix-games, risk-aversion]
topics: ["[[choice-prediction-risky-choice]]", "[[ml-evaluating-economic-theories]]"]
related: []
added: 2026-06-02
generated: 2026-06-02
---

> [!abstract] Abstract
> We use machine learning to uncover regularities in the initial play of matrix games. We first train a prediction algorithm on data from past experiments. Examining the games where our algorithm predicts correctly, but existing economic models don't, leads us to add a parameter to the best performing model that improves predictive accuracy. We then observe play in a collection of new "algorithmically generated" games, and learn that we can obtain even better predictions with a hybrid model that uses a decision tree to decide game-by-game which of two economic models to use for prediction.

## Summary
Fudenberg and Liang use machine learning not merely to predict initial play in $3 \times 3$ matrix games, but as an instrument for theory-building: ML serves as an oracle for the predictable variation in the data, and the residual gap between simple economic models and that oracle is treated as a signal pointing toward missing structure. The pipeline is a loop. First, train a bagged decision tree on lab data and inspect the games where the tree beats level-1; this reveals a "risk-aversion"-like regularity motivating a one-parameter extension, level-1($\alpha$). Second, generate new games — first at random, then via "algorithmic experimental design" filtered for games where level-1($\alpha$) is predicted to fail. Third, learn that Pareto-dominant Nash equilibrium (PDNE) predicts well exactly where level-1($\alpha$) fails. Fourth, combine the two via a hybrid "mixture-of-experts" model that uses a regression tree on game features to decide, game-by-game, which component to trust. The recurring methodological claim — central to the ML-for-theory program — is that completeness (the fraction of attainable improvement over random guessing a model captures) diagnoses how much interpretable structure remains to be modeled.

## Research question
How well can simple, interpretable, portable economic models predict the modal action chosen the first time subjects play a new matrix game, and can machine learning be used to (i) measure the ceiling on predictable variation and (ii) guide the discovery of better, still-interpretable models?

## Method / identification
The prediction target is a classification problem: a rule is a map $f : G \to A_1$ from games $G = \mathbb{R}^{18}$ (a $3 \times 3$ symmetric game's payoffs) to the modal row-player action. Performance is reported as accuracy (fraction of games whose modal action is predicted correctly) and completeness — the share of the gap between random guessing (accuracy $1/3$) and the "ideal" rule (which knows each game's observed mode, accuracy $1$) that a model recovers. All numbers are tenfold cross-validated out-of-sample, with standard errors taken as the across-fold standard deviation divided by $\sqrt{10}$.

Two ML algorithms are used: an interpretable single decision tree (greedy, single-feature splits) and a more accurate but opaque bagged (bootstrap-aggregated) ensemble; two-layer neural nets do not improve on the bagged trees here. Trees operate on hand-built features encoding strategic properties of each action — part of a pure-strategy Nash equilibrium, a Pareto-dominant Nash equilibrium, a payoff-sum-maximizing (efficient/altruistic) profile, level-$k$ for $k \in \{1,\dots,7\}$, max-max (optimistic), or maximin (pessimistic) — plus a "score" counting satisfied properties.

The theoretical innovation is level-1($\alpha$): players best-respond to a uniform (level-0) opponent distribution, but dollar payoffs $u$ are transformed by $f(u) = u^{\alpha}$, nesting standard level-1 at $\alpha = 1$. The estimated $\alpha^{*} = 0.625$ on lab data is read as small-stakes risk aversion, though the authors flag the Rabin (2000) critique that such risk aversion is hard to square with expected-utility theory. The benchmark structural models are uniform Nash, level-$k$, and the Poisson cognitive hierarchy model (PCHM) of Camerer, Ho, and Chong, whose level-$k$ types best-respond to $g_k(h) = \pi_\tau(h)/\sum_{l=0}^{k-1}\pi_\tau(l)$ for Poisson rate $\tau$; the best-fit $\tau$ collapses PCHM to level-1 on this data.

The "algorithmic experimental design" step is the methodological centerpiece: a regression-tree ensemble predicts the frequency of level-1($\alpha^{*}$) play from game features, random games are filtered to retain only those predicted below $0.5$ frequency, and play is collected on the survivors — analogized to adversarial ML, repurposed for data collection. The hybrid model fits, per component, a regression tree mapping game features to the probability that model predicts correctly (estimated on the binary correct/incorrect outcome vector over training games), then selects the model with higher predicted accuracy out-of-sample — a mixture-of-experts / model-tree construction.

## Data
Lab data: all $86$ symmetric $3 \times 3$ matrix games (6,887 observations, 40–147 per game) from six experimental papers (Stahl–Wilson and successors, Rogers–Palfrey–Camerer), all using anonymous random matching without feedback. Two newly collected MTurk datasets: 200 random-payoff games (payoffs uniform on $\{10,\dots,90\}^{18}$, ~41 subjects/game) and 200 algorithmically designed games (payoffs drawn from the empirical lab distribution, 40 subjects/game). No subject-level identifiers, precluding individual heterogeneity analysis.

## Key findings
On lab games, PDNE and uniform Nash barely beat random (completeness 7%, 13%); level-1/PCHM reaches 58% completeness (accuracy 0.72), bagged trees 66%, and level-1($\alpha$) 69% (accuracy 0.79) — i.e., the interpretable risk-aversion extension matches the opaque ensemble. On random games level-1($\alpha$) is even stronger (accuracy 0.92, completeness 88%), because those games are strategically simpler (more often dominance-solvable). The algorithmic design works: on designed games level-1($\alpha$) collapses to 7% completeness (accuracy 0.38), while a two-split tree — "predict the PDNE if one exists, else $a_3$" — motivates the PDNE rule (accuracy 0.65, completeness 48% on designed games). A cross-tabulation (Table 6) shows level-1($\alpha$) and PDNE succeed on largely disjoint games, so the hybrid wins: on all games it reaches accuracy 0.79 / completeness 69%, versus 0.68 / 52% for level-1($\alpha$) and 0.56 / 34% for PDNE; on lab games 0.82 / 73%. A control experiment running lab games on MTurk (level-1 accuracy 0.68, near the 0.72 lab figure) shows the random-game gains are driven by game structure, not subject pool.

## Contribution
A template for ML-guided economic theory: use a flexible predictor to bound predictable variation, mine its successes-over-theory for interpretable regularities, and use ML to design experiments that stress-test the resulting model. The concrete deliverables are the portable level-1($\alpha$) extension, the PDNE predictor, and a mixture-of-experts hybrid that straddles the behavioral-versus-algorithmic divide. The completeness metric reframes model evaluation around the attainable ceiling rather than raw accuracy.

## Limitations & open questions
Restricted to $3 \times 3$ symmetric matrix games and modal-action (not full-distribution) prediction; small, low-parameter models are advantaged when the test set is small or homogeneous. The risk-aversion reading of $\alpha$ is one interpretation among several and conflicts with Rabin-style arguments. The performance ranking of models depends heavily on which dataset is used, cautioning against generalizing from purpose-designed experiments. No subject identifiers, so heterogeneity and learning/feedback dynamics are out of scope. Several feature thresholds (25%, 75%, 0.5 frequency) are chosen somewhat arbitrarily, with only partial robustness checks.

## Connections
The completeness measure and the "how much is predictable" framing come from Peysakhovich and Naecker and from Fudenberg, Kleinberg, Liang, and Mullainathan, situating this in the choice-prediction / ML-for-theory program. It extends the cognitive-hierarchy lineage — Stahl and Wilson, Nagel, Camerer, Ho, and Chong's PCHM — and allies with Wright and Leyton-Brown, who likewise marry ML with behavioral game-theory models; survey context is Crawford, Costa-Gomes, and Iriberri. The feature taxonomy (optimistic, pessimistic, altruistic actions) borrows from Costa-Gomes, Crawford, and Broseta. The hybrid draws on mixtures of experts (Masoudnia and Ebrahimpour), model trees (Quinlan et al.; Landwehr, Hall, and Frank), forecast combination (Timmermann), and bagging (Breiman); the algorithmic design step is framed against adversarial ML (Huang et al.) and GANs (Goodfellow et al.). The risk-aversion discussion engages Rabin and Fudenberg and Levine on small-stakes risk aversion, and Khaw, Li, and Woodford on cognitive imprecision. Related prediction-in-games work includes Hartford, Wright, and Leyton-Brown, Sgroi and Zizzo, and Ert, Erev, and Roth on social-preference model combination.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
