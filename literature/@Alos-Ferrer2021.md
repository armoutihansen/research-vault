---
citekey: Alos-Ferrer2021
title: "Time Will Tell: Recovering Preferences When Choices Are Noisy"
authors: ["Alós-Ferrer, Carlos", "Fehr, Ernst", "Netzer, Nick"]
year: 2021
type: journalArticle
doi: 10.1086/713732
zotero: "zotero://select/library/items/ZN38984B"
pdf: /Users/jesper/Zotero/storage/MWT2Y69L/Alos-Ferrer2021.pdf
tags: [literature]
keywords: [revealed-preference, stochastic-choice, response-times, random-utility-models, drift-diffusion-model, chronometric-function, nonparametric-identification]
topics: []
related: [Bernheim2009, Manzini2014]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> When choice is stochastic, revealed preference analysis often relies on random utility models. However, it is impossible to infer preferences without assumptions on the distribution of utility noise. We show that this difficulty can be overcome by using response time data. A simple condition on response time distributions ensures that choices reveal preferences without distributional assumptions. Standard models from economics and psychology generate data fulfilling this condition. Sharper results are obtained under symmetric or Fechnerian noise, where response times allow uncovering preferences or predicting choice probabilities out of sample. Application of our tools is simple and generates remarkable prediction accuracy.

## Summary
Random utility models (RUMs) cannot identify preferences from stochastic choice without untestable assumptions on the noise distribution: $p(x\mid\{x,y\})>1/2$ is consistent with $u(x)<u(y)$ under asymmetric noise. The paper's central move is to fold the *chronometric function* (harder choices, i.e. smaller utility differences, take longer) into the RUM and show that the observable distribution of response times (RTs) carries information about the unobservable distribution of utility noise. The headline result (Theorem 1) is a nonparametric, distribution-free sufficient condition — a generalized first-order stochastic dominance of RT distributions — under which choice plus RT data reveal preferences with *no* assumptions on noise. Stronger assumptions (symmetry, then Fechnerian) plus RTs buy progressively more: out-of-sample ordinal preference recovery (Theorem 2) and out-of-sample point predictions of choice probabilities (Theorem 3). RTs systematically substitute for "the next stronger distributional assumption." Applied to Clithero (2018) snack-choice data, the criterion has bite in 61% of stochastic problems and predicts second-phase choices at 80.7% accuracy — beating logit and matching a fully estimated drift-diffusion model (DDM) without any structural estimation.

## Research question
Can an analyst recover an agent's (or population's) deterministic preference ordering from *stochastic* choice data without imposing unverifiable assumptions on the distribution of utility noise, and can auxiliary response-time data close the well-known identification gap that makes "anything learnable / nothing learnable" within the RUM framework?

## Method / identification
The paper is pure decision theory plus an empirical illustration. The primitives are a **stochastic choice function with response times (SCF-RT)** $(p,f)$: $p(x,y)$ is the probability of choosing $x$ in binary problem $\{x,y\}$ (with $p(x,y)+p(y,x)=1$), and $f(x,y)$ is the density of RTs *conditional on* choosing $x$ over $y$, with CDF $F(x,y)$.

A **RUM** is a pair $(u,\tilde v)$ where $u:X\to\mathbb{R}$ and each pairwise utility difference $\tilde v(x,y)$ has density $g(x,y)$ satisfying: RUM.1 $\mathbb{E}[\tilde v(x,y)]=u(x)-u(y)$ (mean-zero noise); RUM.2 $\tilde v(x,y)=-\tilde v(y,x)$; RUM.3 connected support. Crucially, working directly with pairwise differences (rather than $\tilde u(x)=u(x)+\tilde e(x)$) makes the class *more general* than textbook RUMs and lets it absorb pair-specific complexity (e.g. dominance, He–Natenzon distances). A RUM **rationalizes** $p$ if $p(x,y)=\mathrm{Prob}[\tilde v(x,y)>0]=1-G(x,y)(0)$.

A **RUM-CF** adds a chronometric function $r:\mathbb{R}_{++}\to\mathbb{R}_+$, continuous and strictly decreasing where positive, with $\lim_{v\to0}r(v)=+\infty$ and $\lim_{v\to\infty}r(v)=0$. Observed RT when $x$ is chosen is $\tilde t(x,y)=r(\lvert\tilde v(x,y)\rvert)$ conditional on $\tilde v(x,y)>0$, giving the identifying link
$$F(x,y)(t)=\frac{1-G(x,y)(r^{-1}(t))}{1-G(x,y)(0)}.$$
This is more parsimonious than alternatives: a single source of randomness (utility) generates *both* stochastic choices and stochastic RTs, and indifference $v(x,y)=0$ yields finite RTs (since $\tilde v\neq0$ a.s.).

The key technical device is **$q$-first-order stochastic dominance**: $G$ $q$-FSD $H$ iff $G(t)\le q\cdot H(t)$ for all $t\ge0$ ($q\ge1$); strict version $q$-SFSD. For $q=1$ this is ordinary FSD; larger $q$ relaxes it. The model classes nest: all RUM-CFs $\supset$ symmetric $\supset$ Fechnerian (common symmetric shape shifted by $v(x,y)$; probit and logit are special cases). Section IV verifies the converse direction (models $\to$ data) for symmetric RUM-CFs, RUMs with a *noisy* chronometric function (RUM-NCF, multiplicative i.i.d. RT noise), and Ratcliff DDMs with constant or collapsing boundaries.

## Data
Empirical illustration uses **Clithero (2018)**: 31 subjects. Phase 1 — repeated binary choices (10 repetitions each) between 17 snack-food items and one fixed reference item, with RTs recorded; 77 problems were genuinely stochastic (770 choices). Phase 2 — each of the $17\cdot16/2=136$ non-reference pairs presented once. RT distributions are estimated nonparametrically via kernel density (Epanechnikov, on log-RT to respect $t\ge0$); choice probabilities by empirical frequencies. No structural estimation is required to apply the theorems.

## Key findings
- **Proposition 1 (impossibility).** Within the class of all RUMs, a rationalizable SCF reveals *no* preference between any distinct $x,y$. Choice data alone identify only $G(x,y)(0)$, not the sign of the mean $v(x,y)=u(x)-u(y)$. Example 1 makes this concrete: with independent mean-zero Gumbel errors of *different* variances ($\beta_x=1,\beta_y=2$), $u(x)=1>u(y)=3/4$ yet $p(x,y)\approx0.49<1/2$, so an analyst wrongly assuming symmetry infers the reverse preference.
- **Theorem 1 (distribution-free revelation).** Within *all* RUM-CFs, an SCF-RT reveals a (weak) preference for $x$ over $y$ if $F(y,x)$ $q$-FSD $F(x,y)$ with $q=p(x,y)/p(y,x)$, and a strict preference under $q$-SFSD. Intuition: a slow choice of $y$ relative to $x$ rules out the strongly-asymmetric noise that would otherwise rationalize $p(x,y)>1/2$ with $u(x)<u(y)$. As $p\to1/2$ the condition collapses to "$y$ chosen strictly slower than $x$ (FSD)"; as $p$ grows it only requires $y$ not be chosen *much* faster. Requires only monotonicity of $r$, not its shape.
- **Theorem 2 (symmetric, out-of-sample ordinal).** Define the percentile $\nu(x,y)$ by $F(x,y)(\nu(x,y))=0.5/p(x,y)$ (above the median, $\to$ median as $p\to1$). For an unobserved pair $(x,y)\notin D$, a strict preference for $x$ over $y$ is revealed if some third option $z$ satisfies $\nu(x,z)<\nu(y,z)$ or $\nu(z,x)>\nu(z,y)$. This formalizes the Krajbich–Oud–Fehr (2014) "fast vs. slow" triangulation for the stochastic case — and shows the correct statistic is the $0.5/p$ percentile, **not** mean, median, max, or min RT.
- **Theorem 3 (Fechnerian, out-of-sample cardinal).** Gives a closed-form prediction of the unobserved $p^*(x,y)$ from binary data on $(x,z)$ and $(y,z)$, e.g. for $p(y,z)>1/2$: $p^*(x,y)=p(x,z)F(x,z)(\nu(y,z))$. The factor $F(x,z)(\nu(y,z))$ is an observable, RT-based discount measuring where $u(y)$ sits in $[u(z),u(x)]$.
- **Propositions 4–6 (tightness / model tests).** The Theorem-1 condition is not merely sufficient but is *always satisfied* by data generated from any symmetric RUM-CF (Prop. 4), from symmetric RUM-NCFs with full-support utility noise (Prop. 5, since $q$-FSD is invariant to independent perturbations), and from DDMs with constant or collapsing boundaries (Prop. 6). Hence a frequent *violation* of the condition empirically falsifies symmetric RUM-CFs and DDMs alike. Propositions 2 and 3 (well-known) give the choice-only benchmarks under symmetry and the Fechnerian assumption; Prop. 7 / GRUM-CF handle rationalizability with two options and non-transitive relations.
- **Empirical bite & prediction.** The $q$-FSD condition holds in **61.0%** of stochastic problems (so preferences are recovered assumption-free in a majority); the **39%** of violations imply symmetric RUMs/DDMs are not the data-generating process there. Theorem 2's out-of-sample prediction is correct **80.7%** of the time — significantly better than logit (73.8%, $p<.0001$) and statistically indistinguishable from a fully fitted DDM (81.2%). Accuracy rises monotonically for faster decisions (up to 88.7% in the fastest quartile). Theorem 3 yields mean absolute error 0.237, beating logit (0.263) though edged by the estimated DDM (0.209).

Table 1 summarizes the central message: each row adds a stronger noise assumption, each column adds RTs, and **adding RTs is always a substitute for the next stronger distributional assumption** (None $\to$ within-sample preferences; Symmetric $\to$ out-of-sample preferences; Fechnerian $\to$ out-of-sample probabilities).

## Contribution
Resolves a foundational, "well-known but rarely stated" identification failure in stochastic revealed-preference theory: that nothing can be learned about preferences from choice frequencies without untestable noise assumptions. By rigorously and nonparametrically integrating response times into the RUM framework, the paper bridges the economics tradition (RUMs, probit/logit, McFadden) and the psychology/neuroscience tradition (chronometric function, DDMs, sequential sampling). It provides a falsifiable test of symmetric RUMs and DDMs, a population/welfare reinterpretation (RTs as a route to the cardinal/interpersonal comparisons utilitarianism needs), and a demonstration that simple kernel-based methods rival computation-intensive structural DDMs out of sample.

## Limitations & open questions
- **Scope of applicability.** The same chronometric function must apply across compared problems, so the tools fit everyday choices among options of *similar complexity* (snacks), not life-changing, multidimensional decisions (jobs, schools) where length reflects complexity rather than closeness; the authors would not mix simple payoffs with complex lotteries or known biases.
- **Real-world data (explicit future work).** Extend beyond the lab to field data (e.g. online marketplaces, where contemplation time is already recorded), where the challenge is distinguishing decision RT from reading/deliberation time (cf. Rubinstein 2007, 2013).
- **Full rationalizability characterization (explicit open problem).** The paper does *not* characterize which arbitrary SCF-RTs are rationalizable by RUM-CFs beyond the model classes of Section IV; with >2 options and RT distributions to match, this is substantially harder. Only necessary conditions are given (e.g. revealed preferences must be acyclic).
- **Other auxiliary data (explicit future work).** Whether physiological signals — pupil dilation, blood pressure, brain activation — can play the same identifying role as RTs and be added to the revealed-preference toolbox.
- **Incomplete revelation.** Theorem 1 may leave some preferences unrevealed (39% of cases here), and a violation contradicts specific subclasses but not the general approach.

## Connections
Builds directly on **Horan, Manzini & Mariotti (2019)** for when utility-difference distributions are (a)symmetric (source of the asymmetric-Gumbel counterexample) and generalizes the deterministic "fast/slow third-option" intuition of **Krajbich, Oud & Fehr (2014)** to the stochastic setting. The chronometric function's optimality foundation comes from **Fudenberg, Strack & Strzalecki (2018)** (optimal evidence accumulation; used in the Prop. 6 proof) and **Woodford (2014)**; the DDM lineage is **Ratcliff (1978)**, **Shadlen & Kiani (2013)**, and the axiomatization of **Baldassi et al. (2020)**. It complements structural RT-augmented estimation (**Clithero 2018**, whose data are used; **Konovalov & Krajbich 2019**; **Schotter & Trevino 2021**) by instead solving the *nonparametric* identification problem that fails even with rich choice data. Related stochastic-choice and behavioral-welfare work includes **Block & Marschak (1960)**, **Apesteguía & Ballester (2015, 2018)**, **[[@Manzini2014|Manzini & Mariotti (2014)]]**, **[[@Bernheim2009|Bernheim & Rangel (2009)]]**, and **Echenique & Saito (2017)** (chronometric axiomatization, but deterministic). The Fechnerian backbone traces to **Fechner (1860)**, **Thurstone (1927)**, **Debreu (1958)**, and **Luce (1959)**; the modern RUM tradition to **McFadden (1974, 2001)**.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
