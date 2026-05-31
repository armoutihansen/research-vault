---
citekey: Peterson2021
title: Using large-scale experiments and machine learning to discover theories of human decision-making
authors: ["Peterson, Joshua C.", "Bourgin, David D.", "Agrawal, Mayank", "Reichman, Daniel", "Griffiths, Thomas L."]
year: 2021
type: journalArticle
doi: 10.1126/science.abe2629
zotero: "zotero://select/library/items/VWKH3A3E"
pdf: /Users/jesper/Zotero/storage/HZ4R3WKL/Peterson2021.pdf
tags: [literature]
keywords: [risky-choice, prospect-theory, machine-learning, decision-theory, neural-networks, theory-discovery, expected-utility]
topics: ["[[choice-prediction-risky-choice]]"]
related: [Erev2017, Fudenberg2019a, Kleinberg2018, Plonsky2019]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Predicting and understanding how people make decisions has been a long-standing goal in many fields, with quantitative models of human decision-making informing research in both the social sciences and engineering. We show how progress toward this goal can be accelerated by using large datasets to power machine-learning algorithms that are constrained to produce interpretable psychological theories. Conducting the largest experiment on risky choice to date and analyzing the results using gradient-based optimization of differentiable decision theories implemented through artificial neural networks, we were able to recapitulate historical discoveries, establish that there is room to improve on existing theories, and discover a new, more accurate model of human decision-making in a form that preserves the insights from centuries of research.

## Summary

Peterson et al. collect the largest dataset of risky-choice decisions to date (9831 choice problems, plus a 1000-problem replication) and use it to power a machine-learning search over theories of decision-making. The key methodological move is the *differentiable decision theory*: classic models (EV, EU, prospect theory) are re-implemented as neural-network architectures whose psychologically meaningful constraints define a nested hierarchy of function classes, then fit by gradient descent. This lets the authors recapitulate historically discovered functional forms (concave utility, probability overweighting), establish an empirical lower bound on prediction error via an unconstrained network, show that there is real room to improve on existing theories, and distill a new interpretable model — Mixture of Theories (MOT) — that nearly matches the unconstrained bound while preserving the insights of EU and PT.

## Research question

Can machine learning, constrained by psychological theory and powered by a sufficiently large behavioral dataset, automate the search for predictive *and interpretable* theories of human risky choice — outperforming both off-the-shelf ML (interpretability problem) and centuries of human-derived theory (predictive ceiling)?

## Method / identification

The authors formalize a theory of risky choice as a function mapping a pair of gambles $(A,B)$ to the probability $P(A)$ that a decision-maker chooses $A$. The space of theories is the set of all functions from $\mathbb{R}^{2d}$ (a vector of $d$ payoffs and $d$ probabilities per gamble) to a choice probability. They define a *hierarchy of function classes* via successively relaxed constraints, each enforced by modifying neural-network architecture:

- **EV (expected value):** $V(A)=\sum_i x_i p_i$ — no free parameters, the simplest theory.
- **Neural EU:** subjective payoffs via a learned utility $u(\cdot)$, with $V(A)=\sum_i u(x_i)p_i$ and choice $P(A)\propto\exp\{h\sum_i u(x_i)p_i\}$, where $h$ is a softmax determinism parameter (a McFadden-style logit). $u$ is learned by a neural net rather than assumed parametric; EU contains EV when $u(x)=x$.
- **Neural PT:** also subjective probabilities via a learned weighting $p(\cdot)$, $V(A)=\sum_i u(x_i)p(p_i)$. **Neural CPT** applies separate weighting functions to ordered gains/losses cumulatively and cannot violate stochastic dominance (so it does not contain neural PT).
- **Value-based:** a net $f(\cdot,\cdot)$ with $P(A)\propto\exp\{f(x_A,p_A)\}$ that values each gamble independently but drops linearity; this class admits violations of the independence axiom.
- **Context-dependent:** the most general class, $P(A)=g(x_A,p_A,x_B,p_B)$, an unconstrained differentiable net that lets one gamble's contents affect the other's valuation; admits violations of both independence and transitivity. Used to estimate the near-optimal prediction bound.

To localize *which* context matters, a second pass defines **contextual multiplicative** models $V(A)=\sum_{i\in A} u(x_i,c_1)\,p(p_i,c_2)$, where conditioning vectors $c_1,c_2$ can carry intra-gamble vs. inter-gamble outcome/probability information. The final **Mixture of Theories (MOT)** is a mixture-of-experts: two learned utility functions and two learned probability-weighting functions, with two gating networks (taking both gambles as input) outputting convex mixture weights; dominated gambles are routed to a separate learned fixed choice probability. All models are evaluated by cross-validated generalization (MSE on ~1000 held-out problems, averaged over 50 runs; cross-entropy in supplement), so complexity is implicitly penalized.

## Data

A new large-scale incentivized experiment: 9831 risky choice problems (pairs of gambles presented in the classic format), with participants paid on one randomly selected gamble. This is >30 times the largest prior dataset (which had <300 problems). A second independent dataset of 1000 problems replicates the core findings, including at the individual-participant level. Data are public at github.com/jcpeterson/choices13k.

## Key findings

- **Recapitulation of human theory:** learned $u(\cdot)$ shows decreasing marginal utility and gain/loss asymmetry; learned $p(\cdot)$ shows overweighting of low-to-medium probabilities — but each *outperforms* every parametric form proposed by theorists, and can be learned from a quarter (EU) to a fifth (PT) of the data.
- **Data scale flips model rankings:** CPT beats PT at small (historical) sample sizes, but the ordering reverses with more data — small datasets misled prior evaluations.
- **Context matters most:** moving from value-based to context-dependent functions yields the single largest accuracy gain (decision-preference accuracy rising to 84.81%), evidence that valuation of one gamble depends on the competing gamble. Ablation locates this in *inter-gamble outcome context*; probability interactions add little, and the fully contextual model overfits.
- **MOT:** matches the unconstrained context-dependent bound (84.15% accuracy) with fewer data, recovering interpretable EU/PT-like components (one utility function with loss aversion, one weighting function overweighting low probabilities). Best predictors of which utility component fires are max outcome, min outcome, and outcome variability.
- **Individual level:** MOT fine-tuned per participant achieves MSE 0.058 vs. 0.063 for best parametric PT.
- **Benchmarking:** 21 well-known risky-choice theories, including the BEAST process model, fail to beat PT on this dataset; BEAST leads only in the small-data regime.

## Contribution

A general recipe — *differentiable theories embedding psychological constraints, searched by gradient descent over large behavioral data* — that unifies theory-driven and data-driven modeling. It supplies a principled empirical lower bound on achievable prediction (the unconstrained net), a systematic hierarchy for attributing predictive gains to specific theoretical commitments, and a concrete new descriptive theory (MOT) that is both more accurate and more sample-efficient than human-derived models while remaining interpretable and continuous with EU/PT.

## Limitations & open questions

- MOT is *descriptive* only; the authors flag translating it into **normative and process models** as open work.
- The unconstrained context-dependent net offers little psychological insight and overfits noise in small datasets — interpretability and expressiveness trade off.
- Probability overweighting recovered here is smaller than in classic PT applications, attributed to the broader range of choice problems sampled; the dependence of findings on the *problem distribution* is acknowledged but not resolved.
- Scope is restricted to two-option risky choice with described gambles; generalization to decisions from experience, multi-option, or other domains is conjectured ("can be applied in other settings") but untested.
- The claim that psychological theories have been "constrained by limited data," implying theories must grow more complex in the big-data regime, is a hypothesis the paper raises rather than settles.

## Connections

The paper sits at the intersection of decision theory and machine-learning-driven theory discovery. It builds directly on expected-utility theory (von Neumann & Morgenstern, 1944; Bernoulli, 1954/1738) and prospect theory and its cumulative variant (Kahneman & Tversky, 1979; Tversky & Kahneman, 1992; Fennema & Wakker, 1997; Wakker, 2010), and uses a McFadden (1973) logit choice rule. Its central empirical foil is the BEAST process model and the large prior datasets of Erev, Ert, Plonsky and co-authors ([[@Erev2017|Erev et al., 2017]]; [[@Plonsky2019|Plonsky et al., 2019]]; Plonsky, Erev, Hazan & Tennenholtz, 2017), whose "psychological forest" represents the competing ML approach. The "measuring the completeness of theories" agenda of [[@Fudenberg2019a|Fudenberg, Kleinberg, Liang & Mullainathan (2019)]] is a close methodological cousin, as is work predicting behavior with ML in economics (Peysakhovich & Naecker, 2017; [[@Kleinberg2018|Kleinberg et al., 2018]]; Camerer, 2018) and game-theoretic settings (Hartford, Wright & Leyton-Brown, 2016). Anomalies motivating non-EU models trace to Allais (1953) and Ellsberg (1961). The mixture-of-experts architecture follows Jacobs, Jordan, Nowlan & Hinton (1991), dual-process accounts follow Mukherjee (2010), and the broader program of using large datasets to study cognition is articulated by Griffiths (2015). The companion Perspective is Bhatia & He.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
