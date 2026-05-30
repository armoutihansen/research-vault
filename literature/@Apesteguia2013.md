---
citekey: Apesteguia2013
title: Choice by sequential procedures
authors: ["Apesteguia, Jose", "Ballester, Miguel A."]
year: 2013
type: journalArticle
doi: 10.1016/j.geb.2012.09.006
zotero: "zotero://select/library/items/P6HCU6PR"
pdf: /Users/jesper/Zotero/storage/XDL272I8/Apesteguia2013.pdf
tags: [literature]
keywords: [bounded-rationality, choice-theory, revealed-preference, sequential-rationalizability, status-quo-bias, game-tree-rationalizability, decision-theory]
topics: []
related: [Kalai2002, Manzini2007, Salant2008, Xu2007]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We propose a rule of decision-making, the sequential procedure guided by routes, and show that three influential boundedly rational choice models can be equivalently understood as special cases of this rule. In addition, the sequential procedure guided by routes is instrumental in showing that the three models are intimately related. We show that choice with a status quo bias is a refinement of rationalizability by game trees, which, in turn, is also a refinement of sequential rationalizability. Thus, we provide a sharp taxonomy of these choice models, and show that they all can be understood as choice by sequential procedures.

## Summary
The paper introduces a single procedural heuristic, the *sequential procedure guided by routes*, in which a decision-maker (DM) facing a menu repeatedly looks at the first available pair according to a fixed order over pairs (a "route"), discards the disliked alternative, and continues until one alternative survives. By varying only the *class of routes* the DM is allowed to contemplate, the authors show that classical rational choice, endogenous status-quo biased choice (after Masatlioglu and Ok), rationalizability by game trees (Xu and Zhou), and sequential rationalizability (Manzini and Mariotti) are each exactly characterized. This common language yields a clean nesting result: $C^{RAT}\subset C^{SQB}\subset C^{RGT}\subset C^{SR}$, a previously non-obvious taxonomy among otherwise heterogeneously-formulated models.

## Research question
Can a variety of prominent boundedly-rational choice models be expressed as instances of one unifying procedural rule, and if so, what does that common representation reveal about how the models relate to one another (which is a refinement of which)?

## Method / identification
The setting is abstract revealed-preference theory. Let $X$ be a finite set of alternatives, $\mathcal{X}$ its non-empty subsets, and $\mathcal{B}$ its binary subsets. A choice function is $c:\mathcal{X}\to X$ with $c(A)\in A$. A **route** is a linear order $<$ over $\mathcal{B}$ (the order in which the DM contemplates pairs). For a menu $A$, $A^{<}$ denotes the first binary subset of $A$ under $<$, and $nc(B)$ the element not chosen from binary menu $B$. The core behavioral primitive is **$<$-consistency**: $c$ is $<$-consistent if for every $A$ with at least two alternatives, $c(A)=c(A\setminus nc(A^{<}))$ — i.e. removing the disliked element of the first contemplated pair never changes the choice.

The identification strategy is to characterize each model by *which routes* the DM may follow, formalized through a **similarity structure** $S$ (a cover of $X$ by non-empty subsets). A route *respects* $S$ if, for disjoint $A,B\in S$, all within-class pairs precede the crossed pairs. Each model corresponds to a structural restriction on $S$ plus a consistency axiom:
- **Rational choice (RAT):** Strong Route Consistency (SRC) — $c$ is $<$-consistent for *every* route. $c(A)=M(A,P)$ for a linear order $P$.
- **Endogenous status-quo biased choice (SQB):** Route Consistency on a **Centered** Similarity Structure (RCCSS) — a star network with a single center $d$ (status quo). Defined via $d\in X$, $Q\subseteq X\setminus\{d\}$ and linear order $P$; the *extreme* version sets $c(A)=M(A\cap Q,P)$ when $Q\cap A\neq\emptyset$, the *weak* version sets $c(A)=M(A\setminus\{d\},P)$.
- **Rationalizability by game trees (RGT):** Route Consistency on a **Nested** Similarity Structure (RCNSS), where $A,B\in S$ intersecting implies $A\subset B$ or $B\subset A$ (hierarchical attributes). RGT means $c(A)=SPNE(\Gamma|_A)$ for a binary game tree $\Gamma$ with asymmetric relations at non-terminal nodes.
- **Sequential rationalizability (SR):** Weak Route Consistency (WRC) — existence of *one* route for which $c$ is $<$-consistent. SR means $c(A)=M_{1}^{K}(A)$ for an ordered list of acyclic relations $\{P_1,\dots,P_K\}$.

Proofs are constructive (e.g. building the game tree node-by-node from a nested $S$; splitting each acyclic $P_j$ into single-pair relations to induce a route).

## Data
None — this is a pure axiomatic/theoretical contribution. "Empirical content" enters only as illustrative 3-element choice examples (e.g. the cyclic menu $\{1,2,3\}$) and as counterexample choice functions ($c_1,\dots,c_4$) used to prove strictness of the inclusions.

## Key findings
- **Theorem 1:** $c$ satisfies SRC $\iff$ $c$ is rational (RAT). Rationality = congruence with *all* routes; framing is irrelevant.
- **Theorem 2:** $c$ satisfies RCCSS $\iff$ $c$ is an endogenous status-quo biased choice (extreme or weak). This also delivers the first *endogenous* (status-quo-free domain) formulations of Masatlioglu–Ok-style bias.
- **Theorem 3:** $c$ satisfies RCNSS $\iff$ $c$ is rationalizable by game trees (RGT). Nested similarity = hierarchical binary-attribute perception.
- **Theorem 4:** $c$ satisfies WRC $\iff$ $c$ is sequentially rationalizable (SR) — the least structured case, one route suffices.
- **Proposition 3 (taxonomy):** $C^{RAT}\subset C^{SQB}\subset C^{RGT}\subset C^{SR}$, all strict. SQB is unexpectedly a refinement of RGT (shown by collapsing a centered $S$ into a nested $S'$).
- **Auxiliary results:** $C^{RGT(LO)}\subset C^{RGT}$ (Prop. 1, after Horan — asymmetric node relations strictly extend linear ones); $C^{RSM}\subset C^{SR}\subset C^{SR(As)}$ (Prop. 2 — acyclic vs. asymmetric relations matter, but two-relation Rational Shortlist Methods stay inside SR); $C^{SR(\alpha)}=C^{SR}$ (Cor. 1 — any "at least acyclic" relations give the same class).
- Not everything fits: choosing $1$ from $\{1,2\}$ and $\{1,3\}$ but $2$ from $\{1,2,3\}$ is *not* representable by any route, since $1$ can never be rejected.

## Contribution
Provides a unifying procedural language that subsumes four major choice models as special cases distinguished solely by the admissible class of routes, and derives from it a sharp, previously-implicit refinement hierarchy among them. It reframes "bounded rationality" as a measurable departure from full route-independence, and gives the first endogenous-domain version of status-quo biased choice.

## Limitations & open questions
The authors explicitly flag three forward-looking lines: (1) studying *manipulation of routes* by a marketer or principal in market-interaction settings; (2) using route procedures as a *learning/de-biasing tool* — walking a DM through multiple routes to make her aware of route-dependence and reconsider inconsistent binary comparisons; (3) using *the size and composition of the set of routes consistent with observed behavior as a quantitative measure of rationality* (more consistent routes = less capricious behavior). The framework is also confined to single-valued choice on a finite universal domain with deterministic data; stochastic choice, infinite/continuous alternatives, and limited-domain data are out of scope.

## Connections
The paper sits at the intersection of three literatures it explicitly unifies: status-quo bias (Masatlioglu and Ok 2005, 2010; Thaler 1980; Kahneman, Knetsch and Thaler 1991), rationalizability by game trees / multi-self conflict ([[@Xu2007|Xu and Zhou 2007]]; [[@Kalai2002|Kalai, Rubinstein and Spiegler 2002]]; Horan 2009; de Clippel and Eliaz 2010), and sequential / shortlisting rationalization ([[@Manzini2007|Manzini and Mariotti 2007]] on Rational Shortlist Methods; [[@Salant2008|Salant and Rubinstein 2008]] on choice with frames; Tyson 2011). The "measure of rationality" agenda connects to the authors' own Apesteguia and Ballester (2011) and to revealed-preference-violation measures (Echenique, Lee and Shum 2010; Beatty and Crawford 2010; Choi et al. 2011). Methodologically it belongs to the procedural / heuristic decision-making tradition (Gigerenzer et al. 1999; Manrai and Prabhakant 1989 on elimination-by-cutoffs).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
