---
citekey: Manzini2018
title: Dual random utility maximisation
authors: ["Manzini, Paola", "Mariotti, Marco"]
year: 2018
type: journalArticle
doi: 10.1016/j.jet.2018.05.015
zotero: "zotero://select/library/items/R66PAGQK"
pdf: /Users/jesper/Zotero/storage/4KD4G9HE/Manzini2018.pdf
tags: [literature]
keywords: [stochastic-choice, random-utility, axiomatization, attraction-effect, revealed-preference, menu-dependence, dual-self]
topics: []
related: [Cherepanov2013, Eliaz2006, Eliaz2011, Huber1982, Manzini2014, deClippel2012]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Many prominent regularities of stochastic choice, such as the attraction, similarity and compromise effects, are incompatible with Random Utility Maximisation (RUM) as they violate Monotonicity. We argue that these regularities can be conveniently represented by a variation of RUM in which utility depends on only two states and state probabilities are allowed to depend on the menu. We call this model Dual Random Utility Maximisation (dRUM). dRUM is a parsimonious model that admits violations of Monotonicity. We characterise dRUM in terms of three transparent expansion/contraction conditions. We also characterise the important special case in which state probabilities are constant across menus.

## Summary
The paper proposes **dual random utility maximisation (dRUM)**: a random utility model with exactly *two* preference rankings whose mixing weight is allowed to depend on the menu. Restricting to two states keeps the model parsimonious, while menu-dependent weights let it accommodate the attraction, similarity and compromise effects that defeat ordinary RUM (because those effects violate Monotonicity). The main results are clean revealed-preference characterisations stated as expansion/contraction axioms: three axioms pin down dRUM, and three (overlapping) axioms pin down the menu-independent special case (idRUM). A central conceptual point is that with menu-dependent weights, choice data are only **modal** — they reveal whether an alternative is chosen with certainty, with positive probability, or never — so the axioms are "modal" versions of standard RUM properties.

## Research question
Can the standard regularities of stochastic choice that violate Monotonicity (attraction, similarity, compromise, frog-legs, dual-self, household, normative-vs-selfish) be captured by a tractable, axiomatically transparent variant of RUM? Concretely: what observable restrictions on a stochastic choice rule $p(a,A)$ characterise (a) a two-ranking RUM with menu-dependent state probabilities (dRUM), and (b) its menu-independent special case (idRUM)? This fills a gap, since RUM itself lacks a behaviourally interpretable (rather than representation-mirroring) axiomatisation.

## Method / identification
Pure axiomatic revealed-preference theory; no data. The primitive is a **stochastic choice rule** $p:X\times\mathcal D\to[0,1]$ on a finite set $X$ of $n\ge 2$ alternatives, with $\sum_{a\in A}p(a,A)=1$ and $p(a,A)=0$ for $a\notin A$; $p(a,A)$ is read either as an individual's choice probability or a population frequency. A **RUM** is $p(a,A)=\mu(R(a,A))$ where $\mu$ is a distribution over strict rankings and $R(a,A)$ is the set of rankings putting $a$ top in $A$.

A **dRUM** is a triple $(r_1,r_2,\tilde\alpha)$ with two rankings and a menu-dependent weight $\tilde\alpha:2^X\setminus\emptyset\to(0,1)$ giving
$$p(a,A)=\tilde\alpha(A)\,\mathbf 1_{R(a,A)}(r_1)+(1-\tilde\alpha(A))\,\mathbf 1_{R(a,A)}(r_2).$$
An **idRUM** fixes $\tilde\alpha(A)=\alpha$ for all menus, so it is a triple $(r_1,r_2,\alpha)$. Notation $a\succ_i b$ abbreviates $r_i^{-1}(a)<r_i^{-1}(b)$.

For idRUM the axioms use the relation "$b$ impacts $a$ in $A$" ($p(a,A)>p(a,A\cup\{b\})$, from [[@Manzini2014|Manzini & Mariotti 2014)]]: **Monotonicity** ($a\in A\subset B\Rightarrow p(a,A)\ge p(a,B)$); **Contraction Consistency** (impact is inherited by sub-menus); **Impact Consistency** (if $b$ impacts nothing in $A$ then $p(b,A\cup\{b\})=0$); **Negative Expansion** (if $a\in A$ and $p(a,A)<p(a,B)<1$ then $p(a,A\cup B)=0$). The first three hold in *any* RUM; Negative Expansion is the strong menu-independence restriction.

For general dRUM the data are modal: "$b$ **modally impacts** $a$ in $A$" means adding $b$ turns $a$ from possible to impossible ($p(a,A)>0$, $p(a,A\cup\{b\})=0$) or from certain to merely possible ($p(a,A)=1$, $p(a,A\cup\{b\})\in(0,1)$). The modal axioms are **Modal Monotonicity** (removing alternatives preserves "possibly chosen" and "certainly chosen"), **Modal Contraction Consistency**, **Modal Impact Consistency**, and **Modal Negative Expansion**.

The sufficiency proof for dRUM is via a clever reduction: associate to each $p$ a derived rule $\hat p$ with $\hat p(a,A)\in\{0,\tfrac12,1\}$ recording only the modal status of $p$; then $p$ is a dRUM iff $\hat p$ is an idRUM with $\alpha=\tfrac12$, so Theorem 2 follows from Theorem 1. Binariness (at most two alternatives get positive probability in any menu) is *derived*, not assumed: Lemmas 1–2 get it from Monotonicity + Negative Expansion, Lemma 3 from Modal Monotonicity + Modal Impact Consistency.

## Data
None — this is a theory paper. It discusses experimental and field phenomena (attraction/similarity/compromise effects, dictator-game giving, bimodal ratings/financial-market demand, minimum-effort games) as motivation and as targets the model can rationalise, but estimates nothing.

## Key findings
- **Lemma 1 / Lemma 2.** Under Monotonicity and Negative Expansion, every menu has at most two alternatives with positive probability, and there is a single $\alpha\in(0,1)$ with $p(a,A)\in\{0,\alpha,1-\alpha,1\}$ for all menus — the binary structure is *implied*, not postulated.
- **Theorem 1 (idRUM).** A stochastic choice rule is an idRUM iff it satisfies **Monotonicity, Negative Expansion and Contraction Consistency**. (Impact Consistency is redundant here, being implied by Monotonicity.)
- **Theorem 2 (dRUM).** A stochastic choice rule is a dRUM iff it satisfies **Modal Monotonicity, Modal Contraction Consistency and Modal Impact Consistency**. Modal Negative Expansion is implied by the others. Notably the modal axiomatisation is obtained simply by taking modal versions of three properties that hold in any RUM.
- **Anomalies as dRUM.** Attraction, compromise, and "phantom-decoy" effects are all captured by two rankings $t\succ_1 o\succ_1 d$, $o\succ_2 t\succ_2 d$ where introducing decoy $d$ raises the weight on $\succ_1$ — independent of the precise decoy type or causal psychology. dRUM also accommodates violations of Weak Stochastic Transitivity.
- **Identification (Section 5).** When $\alpha\ne\tfrac12$, the two rankings of an idRUM are uniquely recovered (up to relabelling) from binary choices. When $\alpha=\tfrac12$ — and equivalently for *any* dRUM — uniqueness is lost: two ranking-pairs generate the same $p$ iff they are **equivalent** (Definition 1: for every menu $A$ and alternative $a$, the *set* of positions $a$ occupies under the two restricted rankings coincides). The paper argues this informational loss is mild: equivalence is highly restrictive across all sub-menus, and when the two rankings are anonymous, only their Borda-type aggregate matters.
- **Independence of axioms.** Appendices A–B give explicit tables (Tables 2–7) showing each axiom in Theorems 1 and 2 is independent — e.g. a rule satisfying Monotonicity and Contraction Consistency but failing Negative Expansion, and a rule satisfying both parts of Modal Monotonicity and Modal Impact Consistency but failing Modal Contraction Consistency.

## Contribution
Provides what RUM had lacked: a **transparent, behavioural** axiomatisation of an empirically useful random-utility model, using only expansion/contraction conditions structurally familiar from deterministic revealed-preference theory (rather than the opaque Block–Marschak–Falmagne inequalities). dRUM is a unifying representation for several two-state stories — dual-self/temptation models ([[@Eliaz2006|Eliaz & Spiegler 2006]]; Chatterjee & Krishna 2009), random-dictatorship household models, normative-vs-selfish conflict, and binary population heterogeneity (fast/slow, strategic/non-strategic types). It thereby supplies a direct choice-from-menus characterisation of models previously stated via preferences over menus or contract design.

## Limitations & open questions
The authors flag explicitly:
- **Generalising the state count.** Can one obtain appealing behavioural characterisations of random utility maximisation with at most $k$ states, $2<k\le n!$? (dRUM is the $k=2$ point; full RUM is $k=n!$.)
- **Econometrics of bimodality.** Since dRUM is a theoretical idealisation of empirically common *bimodal* choice distributions, what econometric specification best treats such data when generated by the model? They sketch grafting a unimodal noise term on each state's deterministic utility, yielding a two-component mixture $u_i+\varepsilon$ whose mixture is bimodal under suitable conditions.
Implicit limitations: as an individual-choice model idRUM is restrictive (it must satisfy Monotonicity); identification of *which* ranking is the "normative"/"temptation" one requires extra-choice information; and the two-alternatives-per-menu support is an idealisation that real data will only approximate.

## Connections
The two-ordering machinery is the stochastic counterpart of the deterministic **"top-and-the-top" (TAT)** model of [[@Eliaz2011|Eliaz, Richter & Rubinstein (2011)]] [[@Eliaz2011]]; indeed the $\alpha=\tfrac12$ case carries the same information about the rankings as a TAT. The "impact" relation underpinning Contraction Consistency is taken from the authors' own earlier work [[@Manzini2014]]. The paper situates itself against the classical RUM characterisations (Block & Marschak 1960; Falmagne 1978; Barberá & Pattanaik 1986) and against structured special cases — Luce/logit (Luce & Duncan 1959), Gul & Pesendorfer (2006) on lotteries, Apesteguia, Ballester & Lu (2017) single-crossing random utility, and Lu & Saito (2016) intertemporal RUM. Behavioural anchors include [[@Huber1982|Huber, Payne & Puto (1982)]] on asymmetric dominance, Mochon & Frederick (2012) on order effects in the compromise effect, the dual-self/temptation literature (Eliaz & Spiegler 2006; Chatterjee & Krishna 2009; de [[@deClippel2012|Clippel & Eliaz 2012)]], warm-glow normativity ([[@Cherepanov2013|Cherepanov, Feinberg & Ozdenoren 2013)]], and Bayesian testing of stochastic choice (McCausland & Marley 2014). For empirical bimodality it cites dictator-game, ratings, financial-market, and minimum-effort-game evidence.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
