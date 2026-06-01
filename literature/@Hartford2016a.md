---
citekey: Hartford2016a
title: Deep learning for predicting human strategic behavior
authors: ["Hartford, Jason S.", "Wright, James R.", "Leyton-Brown, Kevin"]
year: 2016
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/M6FEUXM5"
pdf: /Users/jesper/Zotero/storage/EYX874PN/Hartford et al. - 2016 - Deep learning for predicting human strategic behavior.pdf
tags: [literature]
keywords: [deep-learning, behavioral-game-theory, normal-form-games, predicting-human-behavior, level-k-reasoning, quantal-response, bounded-rationality]
topics: []
related: []
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> Predicting the behavior of human participants in strategic settings is an important problem in many domains. Most existing work either assumes that participants are perfectly rational, or attempts to directly model each participant's cognitive processes based on insights from cognitive psychology and experimental economics. In this work, we present an alternative, a deep learning approach that automatically performs cognitive modeling without relying on such expert knowledge. We introduce a novel architecture that allows a single network to generalize across different input and output dimensions by using matrix units rather than scalar units, and show that its performance significantly outperforms that of the previous state of the art, which relies on expert-constructed features.

## Summary
The paper applies deep learning to the prediction of boundedly rational human behavior in one-shot, simultaneous-move normal-form games. The supervised task is to map a payoff matrix to the empirical distribution over the row player's chosen actions. Whereas behavioral game theory builds low-parameter models grounded in hand-crafted cognitive features, the authors design a neural architecture that learns this mapping end-to-end while remaining structurally faithful to the field's two core ingredients — quantal (noisy) response and limited iterative reasoning. The key technical innovation is the use of *matrix units* (and accompanying *pooling units*) that make the network invariant to the dimensions of the input game, so a single trained network can predict play in games of arbitrary size. On a pooled dataset of nine human-subject experiments the model sets a new state of the art, with the gain from learning larger than the gain previously obtained by adding expert features to the leading benchmark.

## Research question
Can a deep network learn to predict the distribution of human action choices in normal-form games more accurately than the leading behavioral-game-theory model, *without* relying on expert-engineered features — while remaining rich enough to subsume the cognitive mechanisms (quantal response, level-$k$/cognitive hierarchy reasoning) that domain experts found essential?

## Method / identification
This is a supervised deep-learning method paper. The unit of prediction is a normal-form game; the target is the observed frequency vector of row-player actions, a point on the simplex $\Delta^m$. Models are fit by maximizing training likelihood $P(D\mid\theta)$ and evaluated by held-out negative log-likelihood (NLL).

The architecture has three stacked components:

1. **Feature (hidden) layers with matrix units.** Each hidden unit maps a tensor of $k$ input matrices in $\mathbb{R}^{k\times m\times n}$ to an output matrix in $\mathbb{R}^{m\times n}$ via *scalar* weights shared across all cells. This weight-tying is the source of input-size invariance: the parameter count depends on the number of units, not on $m,n$, so the trained net generalizes to game shapes unseen in training. These units are mathematically MLP-convolution (network-in-network, $1\times1$ patch) layers, but the design is derived from a game-theoretic argument rather than borrowed from vision.

2. **Pooling units.** Because each matrix cell is processed independently, the net cannot represent the game-theoretic notion of "related elements" (the row/column of payoffs an opponent could realize). Pooling units restore this by outputting row- and column-preserving maxima, $H\to\{H_c,H_r\}$, broadcast back to full matrix shape and fed to later layers, so a downstream cell can condition on its own value *and* its row/column maxima.

3. **Softmax output and action-response layers.** Each final hidden matrix is row-summed and passed through a softmax to a distribution $f_i\in\Delta^m$; the feature output is a simplex-weighted mixture $ar_0=\sum_i w_i f_i$. To represent *iterative reasoning*, action-response layers let the row player best-respond to beliefs about the column player and vice versa. With internal utility $\sum_i w_{l,i}H_{L,i}$ and beliefs $ar_j^{(c)}$ about the opponent, the $l$-th response layer is
$$ar_l^{(r)}=\mathrm{softmax}\!\left(\lambda_l\sum_{j=0}^{l-1}v_{l,j}\Big(\big(\sum_{i=1}^{k}w_{l,i}^{(r)}H_{L,i}^{(r)}\big)\cdot ar_j^{(c)}\Big)\right),\quad ar_l^{(r)}\in\Delta^m.$$
The sharpness $\lambda_l$ plays the role of the quantal-response precision; the simplex weights $v_{l,j}$ over lower levels mirror the level distribution in a cognitive hierarchy. The final output is a simplex mixture over response layers, $y=\sum_j w_j\,ar_j^{(r)}$.

Training uses Adam (lr $0.0002$), dropout ($p=0.2$), $L_1$ regularization ($0.01$), and projected-gradient SGD to enforce the simplex constraints, up to 25,000 epochs.

## Data
A pooled corpus from **nine** human-subject experimental studies run by behavioral economists, in which paid subjects chose actions in normal-form games against an unseen, simultaneously-moving opponent. The same dataset underlies the Wright & Leyton-Brown benchmark, enabling a like-for-like comparison. Evaluation is by 10 rounds of 10-fold cross-validation with 95% confidence intervals on test NLL.

## Key findings
- **New state of the art.** Every instantiation with three or more layers (using a single action-response layer, i.e. no explicit iteration) significantly beat both the prior best, quantal cognitive hierarchy (QCH) with hand-crafted features, *and* the best feature-free model (QCH with uniform level-0). The improvement from learning exceeded the improvement previously gained by adding expert features to QCH.
- **Depth and width.** A 2-layer net (single 50-unit hidden layer) underfit; adding a second hidden layer already beat the prior art. Performance rose with width up to ~50 units/layer with diminishing returns; 4-layer feature nets improved training loss but overfit on test, so the chosen configuration is two 50-unit hidden layers with pooling.
- **Pooling is essential.** Removing pooling units caused severe underfitting and poor test performance; even disabling dropout could not recover the pooled networks' fit. Information sharing across rows/columns is doing real representational work.
- **Iterative reasoning was not needed.** Varying action-response layers from 1 to 4, the *best* model used only a single response layer — i.e. explicit level-$k$ iteration did not help once the flexible feature layers were present. This suggests the network maps payoffs to action distributions in a way "substantially different from previous successful models."
- **Representational generality (claimed, proved in supplement).** The architecture can express quantal cognitive hierarchy and quantal level-$k$, their best-response limits as sharpness $\to\infty$, and all of Wright & Leyton-Brown's behavioral features. It is *not* universal: notably it cannot represent identification of dominated strategies.

## Contribution
First successful application of deep learning to predicting human play in general-sum normal-form games. The conceptual contribution is matrix/pooling units that yield input-size invariance and let one network generalize across game dimensions, paired with a demonstration that the learned model subsumes, and empirically dominates, the hand-engineered behavioral-game-theory state of the art — removing the need for expert feature construction.

## Limitations & open questions
- **Scope:** restricted to two-player, unrepeated, simultaneous-move, complete-information games. Extensions to $>2$ players, repeated interaction, and imperfect-information games are open and named by the authors.
- **Representational gaps:** the architecture cannot express dominated-strategy identification, a plausibly useful behavioral feature; closing this gap is flagged for future work.
- **Interpretability:** the best model bypasses iterative reasoning, so what cognitive structure the net actually learns is unexplained — an open interpretability question.
- **Data regime:** results rest on one pooled corpus; out-of-distribution generalization to genuinely new game families (beyond size invariance) is untested.

## Connections
Directly extends the behavioral-game-theory prediction literature, especially Wright & Leyton-Brown's quantal cognitive hierarchy with hand-crafted features (the benchmark dethroned here), building on quantal response (McKelvey & Palfrey, 1995), level-$k$ reasoning (Costa-Gomes, Crawford & Broseta), and cognitive hierarchy (Camerer, Ho & Chong, 2004). On the deep-learning side it parallels the human-move policy network in Silver et al. (2016) for Go and Clark & Storkey, while its hidden units derive from Lin et al.'s Network-in-Network and its size invariance echoes the fully-convolutional networks of Long, Shelhamer & Darrell. The likelihood-based distribution-prediction framing connects to proper-scoring-rule evaluation of probabilistic forecasts (Gneiting & Raftery, 2007) and to later work benchmarking behavioral models against flexible machine-learning predictors (Fudenberg, Camerer, et al.).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
