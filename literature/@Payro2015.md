---
citekey: Payro2015
title: Similarity-based mistakes in choice
authors: ["Payró, Fernando", "Ülkü, Levent"]
year: 2015
type: journalArticle
doi: 10.1016/j.jmateco.2015.09.002
zotero: "zotero://select/library/items/HWQ97WT5"
pdf: /Users/jesper/Zotero/storage/FVEIKZ8X/Payro2015.pdf
tags: [literature]
keywords: [bounded-rationality, similarity, choice-theory, revealed-preference, cyclic-choice, rationalizability]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We characterize the following choice procedure. The decision maker is endowed with two binary relations over alternatives, a preference and a similarity. In every choice problem she includes in her choice set all alternatives which are similar to the best feasible alternative. Hence she can, by mistake, choose an inferior option because it is similar to the best. We characterize this boundedly rational behavior by suitably weakening the rationalizability axiom of Arrow (1959). We also characterize a variation where the decision maker chooses alternatives on the basis of their similarities to attractive yet infeasible options. We show that similarity-based mistakes of either kind lead to cyclical behavior. Finally, we reinterpret our procedure as a method for choosing a bundle given a set of individual items, in which the decision maker combines the best feasible item with those that complement it.

## Summary
The paper models a decision maker who is fully rational in her mental attitudes but behaviorally irrational because she sometimes mistakes an inferior alternative for the best one. She is endowed with a preference (linear order) $R$ and a reflexive *similarity* relation $S$; in any menu she deems choosable the best feasible option together with everything similar to it. The authors axiomatize this procedure with a single weakening of Arrow's rationalizability axiom (w-Arrow), characterize a nested variation where mistakes are anchored to attractive *infeasible* alternatives, prove that any such departure from rationalizability must generate binary cycles, and reinterpret the same formal object as a boundedly rational rule for choosing *bundles* via complementarities.

## Research question
When a decision maker's preferences are perfectly rational but she occasionally selects an inferior option merely because it *resembles* the best one, what observable structure does her choice behavior exhibit? Concretely: can deterministic, similarity-driven "mistakes" be characterized by a transparent revealed-preference axiom, and what are their unavoidable behavioral signatures (in particular, do they force choice cycles)?

## Method / identification
The setting is a standard finite choice environment: a finite set $X$, the collection $\Sigma$ of nonempty subsets (menus), and a *choice correspondence* $c:\Sigma\to\Sigma$ with $c(A)\subseteq A$ (allowing indeterminate, multi-valued choice). The benchmark of full rationality is rationalizability by a complete transitive $\succeq$, equivalently **Arrow's axiom**: for all $B\subset A$, if $B\cap c(A)\neq\emptyset$ then $c(B)=c(A)\cap B$.

The primitives of the mistake model are a linear order $R$ (with $\max(A,R)$ its unique best element) and a *similarity* $S$, defined as a merely **reflexive** binary relation (following Tversky 1977, similarity need not be symmetric or transitive). The first procedure, **representation (1)**, is

$$c_{R,S}(A)=\{x\in A : xS\max(A,R)\}.$$

Reflexivity guarantees $\max(A,R)\in c_{R,S}(A)$ always. The identifying axiom is the *existential* weakening of Arrow:

- **w-Arrow:** for every $A$ there exists *some* $a\in c(A)$ such that whenever $a\in B\subset A$, $c(B)=c(A)\cap B$.

Arrow's axiom imposes this on *every* choosable element; w-Arrow asks only for *one* such "anchor." The proof of sufficiency constructs the primitives from data: define $xSy\iff[x=y$ or $c(xy)=xy]$, and a relation $R_0$ by $xR_0y\iff x\neq y$ and removing $x$ from some menu containing $y$ changes choices ($c(A\setminus x)\neq c(A)\setminus x$). w-Arrow forces $R_0$ to be acyclic, so by the **Szpilrajn (1930)** extension theorem it embeds in a linear order $R$, and one verifies $c=c_{R,S}$.

The **variation, representation (2)**, lets mistakes be anchored to *infeasible* superior options. Writing $R(A)=\{x\in X : xRa\ \forall a\in A\}$ (alternatives at least as good as everything in $A$) and $S(x,A)=\{a\in A : aSx\}$,

$$c_{R,S}(A)=\bigcup_{x\in R(A)} S(x,A).$$

An option is choosable iff it is similar to the best feasible alternative *or* to some better infeasible one. The relevant extra axiom is the classical $\alpha$ (Sen's contraction consistency): $x\in c(A),\ x\in B\subset A\Rightarrow x\in c(B)$.

## Data
None - this is a pure axiomatic decision-theory paper. The "data" is the abstract object of a choice correspondence; illustrations are stylized (mistaking adjacent cereal brands, or the knock-off *Transmorphers* for *Transformers*).

## Key findings
- **Theorem 1:** A choice correspondence satisfies Arrow's axiom if and only if it satisfies both **NBC** (no binary cycles: $x\in c(xy)$ and $y\in c(yz)\Rightarrow x\in c(xz)$) and **w-Arrow**. So w-Arrow is exactly the "non-cyclic part" of rationality that survives once cycles are allowed; w-Arrow and NBC are logically independent.
- **Theorem 2:** $c$ has representation (1) **iff** it satisfies w-Arrow. This is the central characterization: similarity-based mistakes are precisely the w-Arrow-consistent correspondences.
- **Corollary 1:** If a representation-(1) correspondence fails rationalizability, it must admit a binary cycle. Mistake-making and cyclicity are inseparable.
- **Theorem 3:** $c$ has representation (2) **iff** it satisfies w-Arrow *and* $\alpha$. Hence (2) is a strict *specialization* of (1): the two models are nested, and (2) is exactly the sub-class that additionally satisfies contraction consistency. **Corollary 2** mirrors Corollary 1 for representation (2).
- **Scope of explainable cycles:** Representation (1) cannot rationalize "robust" cycles built from singletons (e.g. $c(xy)=x,\ c(yz)=y,\ c(xz)=z$ forces no similarities, contradicting the cycle), but it does explain *less robust* cycles involving indeterminate (non-singleton) choice sets.
- Two auxiliary observations (Remarks 1-4): similarity matters only when it relates a *less* preferred to a *more* preferred option, so any $c_{R,S}$ can equally be generated by an asymmetric or by a symmetric similarity; and preferences over two adjacent-and-similar alternatives are *not* revealed by behavior.
- **Reinterpretation (Section 5):** Reading $c(A)$ as a *chosen bundle* and $S$ as a **complementarity** relation $C$, the same formula $c_{R,C}(A)=\{x\in A : xC\max(A,R)\}$ becomes a boundedly rational bundle-choice heuristic - pick your favorite single item, then add everything that complements it - sidestepping the need to rank all of $2^X$. It connects to choice in two-sided matching (Roth-Sotomayor).

## Contribution
The paper offers a clean, single-axiom revealed-preference foundation for a psychologically natural error: choosing the wrong thing because it looks like the right thing. Methodologically it isolates exactly *which* implication of Arrow's axiom (the universal quantifier over anchors) must be relaxed, and shows the residual w-Arrow has bite. It departs sharply from stochastic-choice models of mistakes: the generated data is *deterministic*, and the distortion is the *addition of a reflexive relation* rather than a random utility shock. The procedural transparency yields a bonus interpretation (complementarity-based bundle choice), unifying two seemingly distinct boundedly rational stories under one characterization.

## Limitations & open questions
- The procedure is *deterministic*; the authors explicitly contrast it with stochastic-choice/random-utility error models but do not bridge the two - a stochastic version of similarity-based mistakes is left open.
- Representation (1) provably **cannot** explain all cyclical behavior (singleton-only cycles are excluded); characterizing which cycle structures are generable is only partially done.
- Identification is limited: when two alternatives are *adjacent in preference and similar*, behavior cannot reveal which is better (Remarks 2, 4), so $R$ and $S$ are not uniquely pinned down by choice data.
- Similarity is taken as a fixed exogenous primitive; the paper does not endogenize where similarity (or, in the reinterpretation, complementarity) comes from, nor how it might vary with menus or context.
- The bundle/complementarity reinterpretation is sketched only for representation (1); a parallel development (and matching-theoretic implications) for representation (2) is not pursued.

## Connections
The paper sits in the **boundedly rational / multistage choice** literature but deliberately breaks from it: in **Manzini and Mariotti (2007)** "sequentially rationalizable choice," **Masatlıoğlu, Nakajima and Özbay (2012)** "revealed attention," **Dutta and Horan (2015)**, and **Bajraj and Ülkü (2015)**, alternatives are *eliminated* stage by stage until a single survivor remains; here the first-stage winner survives but *passed-over* alternatives can re-enter the choice set, an opposite movement. The formal backbone is **Arrow (1959)** and the revealed-preference tradition summarized by **Moulin (1985)**, with the linear-extension construction relying on **Szpilrajn (1930)**. The similarity primitive draws on **Tversky (1977)** (non-symmetric, non-transitive similarity) and contrasts with **Rubinstein (1988)**, where similarity *completes* an incomplete preference over lotteries (an Allais-paradox resolution) rather than *causing* behavioral irrationality. The bundle reinterpretation links to choice functions in two-sided **matching** (**Roth and Sotomayor 1990**; **Chambers and Yenmez 2013**).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
