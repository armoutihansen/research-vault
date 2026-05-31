---
citekey: Hartford2016
title: Deep Learning for Predicting Human Strategic Behavior
authors: ["Hartford, Jason S", "Wright, James R", "Leyton-Brown, Kevin"]
year: 2016
type: conferencePaper
doi: ""
zotero: "zotero://select/library/items/CHFSCGG9"
pdf: /Users/jesper/Zotero/storage/U7SFU9QW/Hartford2016.pdf
tags: [literature]
keywords: [behavioral-game-theory, deep-learning, human-behavior-prediction, normal-form-games, level-k-reasoning, quantal-response]
topics: ["[[ml-evaluating-economic-theories]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Predicting the behavior of human participants in strategic settings is an important problem in many domains. Most existing work either assumes that participants are perfectly rational, or attempts to directly model each participant's cognitive processes based on insights from cognitive psychology and experimental economics. In this work, we present an alternative, a deep learning approach that automatically performs cognitive modeling without relying on such expert knowledge. We introduce a novel architecture that allows a single network to generalize across different input and output dimensions by using matrix units rather than scalar units, and show that its performance significantly outperforms that of the previous state of the art, which relies on expert-constructed features.

## Summary
The paper proposes a deep learning architecture for predicting the distribution of human play in unrepeated, simultaneous-move, two-player normal-form games. Rather than hand-crafting cognitive features as in behavioral game theory, the network learns its own representation of boundedly-rational behavior end-to-end. The central innovation is an architecture built from *matrix units* (rather than scalar units) plus row/column *pooling units* and *action-response layers*, which together enforce invariance to game size and to permutations of actions, while remaining rich enough to nest existing iterative-reasoning + quantal-response models. On a pooled dataset of nine human-subject experiments the feature-free model significantly beats the previous state of the art (quantal cognitive hierarchy with expert features).

## Research question
Can a deep network learn to predict human behavior in normal-form games *without* expert-constructed cognitive features, while generalizing across games of arbitrary size $m\times n$, and outperform the hand-engineered state of the art?

## Method / identification
The model maps two normalized payoff matrices $U^{(r)},U^{(c)}\in\mathbb{R}^{m\times n}$ (row and column player utilities) to a predicted distribution $y\in\Delta^m$ over the row player's $m$ actions. It is invariant to (i) the size of the input matrices and (ii) permutations of rows/columns, and is differentiable end-to-end. It has two parts:

**Feature layers (invariance-preserving hidden matrix units).** Encoding the assumption that a player reasons about each action identically, parameters are tied so that a single scalar weight multiplies each whole utility matrix. A hidden matrix unit is
$$H_{l,i}=\phi\!\left(\sum_{j} w_{l,i,j}\,H_{l-1,j}+b_{l,i}\right),\qquad H_{l,i}\in\mathbb{R}^{m\times n},$$
with scalar weights $w_{l,i,j}$, scalar bias $b_{l,i}$, and element-wise nonlinearity $\phi$. Each unit holds a *matrix* (not a scalar), so the architecture mirrors Network-in-Network mlpconv layers with $1\times1$ patches — but was derived independently from game-theoretic invariances.

**Pooling units.** Plain tied units force independence between matrix cells. Pooling units restore information sharing by emitting row- and column-preserving aggregates (the authors use $\max$, which is needed to represent known behavioral functions), so each later hidden cell depends both on the corresponding cell below and on its row/column maxima.

**Softmax (feature) units.** A row-preserving sum collapses each final hidden matrix to a vector, softmaxed into a distribution $f_i\in\Delta^m$. The feature output is a simplex-weighted mixture $ar_0=\sum_i w_i f_i$ with $w_i\ge0,\ \sum_i w_i=1$.

**Action-response layers (iterative reasoning).** To represent level-$k$ style reasoning, the same feature layers applied to the transposed matrices give column-player beliefs $ar_0^{(c)}\in\Delta^n$. The $l$-th action-response layer computes expected utility of an internal utility representation $\sum_i w_{l,i}H_{L,i}$ against beliefs about the opponent:
$$ar_l^{(r)}=\operatorname{softmax}\!\left(\lambda_l\sum_{j=0}^{l-1} v_{l,j}^{(r)}\left(\sum_{i=1}^{k} w_{l,i}^{(r)} H_{L,i}^{(r)}\cdot ar_j^{(c)}\right)\right),\quad ar_l^{(r)}\in\Delta^m,$$
with sharpness $\lambda_l$ and simplex-constrained $w,v$. The final prediction is a simplex mixture over response levels: $y=\sum_{j=1}^{K} w_j\, ar_j^{(r)}$, $w\in\Delta^K$.

Training maximizes the likelihood $P(D\mid\theta)$ of observed action frequencies; evaluation is by held-out negative log-likelihood. Optimization uses Adam ($\eta=0.0002$), Dropout ($p=0.2$), L1 regularization ($0.01$), and projected-gradient SGD to enforce the simplex constraints, up to 25,000 epochs with early stopping on training fit.

## Data
A pooled corpus from nine human-subject experimental studies by behavioral economists, in which paid subjects chose actions in normal-form games against an unseen, simultaneously-moving opponent. The target is the *distribution* over the row player's action (not just the modal action). Evaluation uses 10 rounds of 10-fold cross-validation with 95% confidence intervals.

## Key findings
- Any instantiation of the architecture with 3+ layers significantly beats both the previous SOTA (QCH with hand-crafted features) and the best feature-free baseline (QCH with uniform level-0); the gain exceeds the gain QCH got from adding expert features.
- The final architecture uses two hidden layers of 50 matrix units plus pooling, and only a *single* action-response layer (no explicit iterative reasoning). Deeper feature stacks and additional action-response layers overfit (training NLL falls, test NLL rises).
- Pooling units are essential: networks without them underfit and generalize poorly, even after disabling dropout.
- Representational generality: the architecture can express quantal cognitive hierarchy and quantal level-$k$ (and, as $\lambda\to\infty$, their best-response equivalents cognitive hierarchy and level-$k$), and can encode all behavioral features of Wright & Leyton-Brown (2014).
- That the best model needed no action-response layers suggests it learns a payoff-to-distribution mapping qualitatively different from prior iterative-reasoning models.

## Contribution
Brings representation learning to behavioral game theory: a size- and permutation-invariant deep architecture (matrix units + pooling + action-response layers) that nests the leading hand-engineered models yet is learned automatically, and sets a new state of the art for predicting human play in normal-form games without expert features.

## Limitations & open questions
- The architecture is **not universal**: it cannot express some likely-useful features such as identification of dominated strategies — flagged for future work.
- Action-response (iterative-reasoning) layers overfit; better regularization of their parameters is left open.
- Action-ordering **salience effects** are ignored by the permutation-invariance assumption; the authors plan to explore them.
- Scope is two-player, unrepeated, complete-information games. Extensions named: more than two players, repeated interaction, and games of imperfect information.

## Connections
The work builds directly on the behavioral game theory tradition: quantal response equilibrium (McKelvey & Palfrey, 1995), level-$k$ reasoning (Stahl & Wilson, 1994; Costa-Gomes, Crawford & Broseta, 2001), the cognitive hierarchy model (Camerer, Ho & Chong, 2004), and especially Wright & Leyton-Brown (2010, 2012, 2014), whose quantal cognitive hierarchy with level-0 meta-model features is the state-of-the-art baseline. The deep-learning lineage includes representation learning (Bengio, Courville & Vincent, 2013), Network-in-Network (Lin, Chen & Yan, 2014) — to which the matrix units are mathematically close — fully convolutional networks (Long, Shelhamer & Darrell, 2015) for size invariance, and the human-move prediction policy networks of Clark & Storkey (2015) and Silver et al. (2016) for Go. Optimization draws on Adam (Kingma & Ba, 2015) and projected-gradient methods (Goldstein, 1964). Motivating applications cite security games (Tambe, 2011; Yang et al., 2013), position/ad auctions (Edelman, Ostrovsky & Schwarz, 2007; Varian, 2007), and spectrum auctions (Milgrom & Segal, 2014).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
