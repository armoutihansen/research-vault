---
citekey: Mullainathan2023
title: From Predictive Algorithms to Automatic Generation of Anomalies
authors: ["Mullainathan, Sendhil", "Rambachan, Ashesh"]
year: 2023
type: preprint
doi: 10.2139/ssrn.4443738
zotero: "zotero://select/library/items/HGB799BN"
pdf: /Users/jesper/Zotero/storage/ADF7H2TJ/Mullainathan2023.pdf
tags: [literature]
keywords: [anomaly-generation, machine-learning-for-theory, expected-utility-theory, adversarial-learning, prospect-theory, econometric-theory]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We ask how machine learning can change a crucial step of the scientific process in economics: the advancement of theories through the discovery of "anomalies." Canonical examples of anomalies include the Allais Paradox and the Kahneman-Tversky choice experiments, which are concrete examples of menus of lotteries that highlighted flaws in expected utility theory and spurred the development of new theories for decision-making under uncertainty. We develop an econometric framework for anomaly generation and develop two algorithmic procedures to generate anomalies (if they exist) when provided a formal theory and data that the theory seeks to explain. Our algorithmic procedures are general since anomalies play an important role across a wide variety of fields in economics. As an illustration, we apply our procedures to generate anomalies for expected utility theory using simulated lottery choice data by an individual who behaves according to cumulative prospect theory. We produce novel anomalies for the independence axiom based on the probability weighting function that to our knowledge have not been noticed before. While this illustration is specific, it is our view that automatic anomaly generation can accelerate the development of new theories.

## Summary
The paper builds an econometric theory of "anomaly generation" — the construction of minimal datasets (like the Allais Paradox) that are logically incompatible with an existing scientific theory and thereby reveal how it fails. It abstracts any economic theory (expected utility, Nash equilibrium, CAPM) as a black-box correspondence satisfying four axioms, proves such theories are equivalent to an *allowable function class* and always admit anomalies, and then turns supervised ML loose to find them via two procedures: an adversarial max-min game and a gradient-based "dataset morphing" routine. Applied to simulated cumulative-prospect-theory choices, the algorithms re-derive known anomalies and discover a genuinely new one (the "dominated consequence effect"). Coverage here is full: I read the front matter, introduction, the model and axiomatization (Sec. 2), both algorithmic sections (Secs. 3-4), and the simulations and conclusion (Secs. 5-6); the appendix proofs and GDA convergence appendix were sampled rather than read line-by-line.

## Research question
Can machine learning automate the discovery of *anomalies* — concrete minimal examples on which a formal theory's predictions diverge from reality — and thereby accelerate the theory-development cycle in economics? Operationally: given (i) a formal theory and (ii) data from the domain it seeks to explain, can one algorithmically generate anomalies if they exist, and characterize when they must exist?

## Method / identification
The core move is to model a theory domain-agnostically. With feature $x\in\mathcal{X}$ and modeled outcome $y^{*}\in\mathcal{Y}^{*}$, a **theory** is a pair $(T(\cdot),\mathcal{M})$ where $T(\cdot):\mathcal{D}\to\mathcal{C}$ maps any hypothetical dataset $D$ to a correspondence $T(\cdot;D):\mathcal{X}\rightrightarrows\mathcal{Y}^{*}$ summarizing every implication the theory can draw, and $\mathcal{M}$ are scope-limiting "modeled contexts." $D$ is *incompatible* if $T(x;D)=\emptyset$ for all $x$; an **anomaly** is a minimal incompatible dataset, i.e. $D$ is incompatible but $D\setminus\{(x,y^{*})\}$ is compatible for every $(x,y^{*})\in D$.

Four axioms discipline $T(\cdot)$: (1) **Compatibility** (every $D$ is compatible or incompatible, not both); (2) **Consistency** (if compatible with $D$ then $T(x;D)=y^{*}$ on $D$); (3) **Refinement** ($D\subseteq D'\Rightarrow T(x;D')\subseteq T(x;D)$); (4) **Non-trivial implications** (some $D$, $x\notin D$ give $T(x;D)\subset\mathcal{Y}^{*}$). The bridge to data: the empirical modeled outcome is an identified functional $f^{*}_{m}(x):=E_{m}[g(Y_{i})\mid X_{i}=x]$.

**Procedure 1 — adversarial learning.** Anomalies are characterized as datasets inducing strictly positive loss for every allowable function. The search solves the max-min program
$$\max_{x_{1:n}}\ \min_{f(\cdot)\in\mathcal{F}^{T}}\ n^{-1}\sum_{i=1}^{n}\ell\!\left(f(x_{i}),f^{*}_{m}(x_{i})\right),$$
read as a zero-sum game between a falsifier (proposing data) and the theory (fitting an allowable function by empirical risk minimization). Iterating over $n=1,2,\dots$ and stopping at the first $n^{*}$ with positive value yields an anomaly. Because the outer maximization is generically non-concave, it is solved with gradient descent ascent (GDA) borrowed from non-convex/concave min-max optimization, after parametrizing $\mathcal{F}^{T}=\{f_{\theta}:\theta\in\Theta\}$ (sieves or neural nets).

**Procedure 2 — dataset morphing.** Strengthening Axiom 4 to **Axiom 5 (sharp implications)** guarantees a non-trivial lower-dimensional representation: a pair $x_{1},x_{2}$ that are *representationally equivalent*, i.e. $f(x_{1})=f(x_{2})$ for all $f\in\mathcal{F}^{T}$. Anomalies then split into *representational* (equivalent features that behave differently in nature) versus *specification* anomalies; classic anomalies are representational. Morphing locally hunts for representational anomalies by stepping along directions in the null space $N^{T}(x)=\{v:\nabla f(x)'v=0\ \forall f\in\mathcal{F}^{T}\}$ that leave all allowable functions fixed but move the truth, updating $x_{t+1}=x_{t}-\eta\,\mathrm{Proj}\!\left(\nabla f^{*}_{m}(x_{t})\mid N^{T}(x_{t})\right)$. The projection is approximated by sampling $B$ parameter vectors $\theta$ and orthogonalizing against $\nabla f_{\theta}(x)$.

## Data
None for the core results — these are theoretical (axioms, representation theorem, convergence bounds). The empirical illustration uses **simulated** lottery-choice data: a CRRA agent ($\rho=0.5$) with a Lattimore-Baker-Witte probability weighting function $\pi_{j}(p;\delta,\gamma)=\delta p_{j}^{\gamma}/(\delta p_{j}^{\gamma}+\sum_{k\neq j}p_{k}^{\gamma})$ at $\delta=\gamma=0.1$, evaluating menus by subjective expected utility with an i.i.d. logistic choice shock. The authors flag ongoing collection of real lottery-choice data as future work.

## Key findings
- **Proposition 2.1 (representation + existence).** $T(\cdot)$ satisfies Axioms 1-4 iff there is an allowable function class $\mathcal{F}^{T}\subset\mathcal{F}$ with $T(x;D)=\{f(x):f\in\mathcal{F}^{T},\ f\text{ consistent with }D\}$; and anomalies exist for *any* theory satisfying Axioms 1-4. So every such theory is "restrictive."
- **Proposition 3.1.** $D$ is incompatible iff $\min_{f\in\mathcal{F}^{T}}|D|^{-1}\sum\ell(f(x),y^{*})>0$; the smallest incompatible dataset is an anomaly.
- **Proposition 3.2 (statistical guarantee).** With a differentiable, $\alpha$-strongly-convex loss with gradients bounded by $K$, the plug-in vs. population optimal values satisfy $|\widehat{E}_{n}-E^{*}_{n}|\le(\delta+\nu)+3\left(K+\tfrac{\alpha}{2}\right)\lVert\widehat{f}^{*}_{m}-f^{*}_{m}\rVert_{\infty}$ — uniform ($\sup$-norm) consistency of the estimated outcome function drives validity.
- **Proposition 4.1 / Corollary 4.1 / Observation 4.1.** Axiom 5 forces representational equivalence; anomalies partition into representational and specification types.
- **Proposition 4.2 / 4.3.** The plug-in morphing step stays a valid descent direction when the gradient estimation error is small; "average" representational anomalies across contexts coincide with single-context ones absent compositional shifts.
- **Empirical headline.** The procedures recover (a) first-order stochastic dominance violations driven by subcertainty, and (b) a *novel* independence-axiom violation dubbed the **"dominated consequence effect"** — menu B mixes lottery A0 with a certain payoff equal to its *maximal* payoff and A1 with one equal to its *minimal* payoff, producing $A_{0}\succ A_{1}$ alongside $\alpha_{1}A_{1}+(1-\alpha_{1})\delta_{z_1}\succ\alpha_{0}A_{0}+(1-\alpha_{0})\delta_{z_0}$, contradicting independence. It uses only two payoffs (like the common-ratio effect) yet mixes with certain prospects (like the common-consequence effect), and is, to the authors' knowledge, new.

## Contribution
A unifying, domain-agnostic econometric language for "what is an anomaly" that covers theories as disparate as expected utility, Nash equilibrium, and CAPM; an existence theorem tying anomalies to allowable function classes; and two implementable, statistically analyzed ML procedures (adversarial GDA and gradient morphing) that convert a predictive algorithm into an anomaly generator. The work reframes ML's role in economics from measuring theory "completeness/restrictiveness" or "opening the black box" toward *generative* theory criticism, and demonstrates a real discovery even in simulated data.

## Limitations & open questions
- The validity bound (Prop. 3.2) requires **uniform ($\sup$-norm) convergence** of $\widehat{f}^{*}_{m}$, which the authors themselves call "strong" — a demanding nonparametric estimation requirement, especially in high dimensions.
- The outer maximization is **non-concave**; GDA finds only local solutions, so anomaly search is not guaranteed globally optimal or exhaustive.
- Morphing relies on **Assumption 4.1 (local/differentiable representational equivalence)**; theories with non-local or non-smooth representations are not covered.
- Modeled contexts $\mathcal{M}$ are taken as a **primitive** — the theory's scope is assumed, not learned.
- The empirical demonstration is **entirely simulated**; whether the dominated-consequence effect appears in real human choices is explicitly left to ongoing data collection.
- Practical implementation (basis choice, $B$ samples, probability clipping at $\varepsilon=10^{-6}$ near the diverging weighting-function gradient) introduces tuning sensitivity flagged in Appendix D.

## Connections
The framework directly engages the ML-meets-theory literature: it weakens and generalizes the "restrictiveness" notion of Fudenberg, Gao and Liang (2020), complements "completeness" measurement (Fudenberg et al., 2022), and reinterprets Fudenberg and Liang (2019)'s game-prediction approach as a special-case heuristic of the adversarial characterization. The morphing procedure is the choice-theoretic analogue of Ludwig and Mullainathan (2023)'s image-morphing for hypothesis generation from mug-shots, and sits beside Andrews et al. (2022) on conformal transfer-performance of theories. Substantively it is rooted in the decision-under-uncertainty tradition — von Neumann-Morgenstern expected utility, the Allais (1953) paradox, Kahneman-Tversky (1979) and cumulative prospect theory (Tversky and Kahneman, 1992), with probability weighting parametrized after Lattimore, Baker and Witte (1992). The optimization machinery imports adversarial/data-poisoning ideas (Madry et al., 2017) and non-convex/concave min-max results (Jin, Netrapalli and Jordan, 2019; Razaviyayn et al., 2020).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
