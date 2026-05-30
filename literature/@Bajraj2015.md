---
citekey: Bajraj2015
title: Choosing two finalists and the winner
authors: ["Bajraj, Gent", "Ülkü, Levent"]
year: 2015
type: journalArticle
doi: 10.1007/s00355-015-0878-3
zotero: "zotero://select/library/items/6TMQA4D8"
pdf: /Users/jesper/Zotero/storage/FXZHHAN8/Bajraj2015.pdf
tags: [literature]
keywords: [bounded-rationality, choice-theory, revealed-preference, axiomatic-characterization, sequential-choice, limited-consideration, shortlisting]
topics: []
related: [Eliaz2011, Manzini2007, Rubinstein2006, deClippel2012]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We study a class of boundedly rational choice functions which operate as follows. The decision maker uses two criteria in two stages to make a choice. First, she shortlists the top two alternatives, i.e. two finalists, according to one criterion. Next, she chooses the winner in this binary shortlist using the second criterion. The criteria are linear orders that rank the alternatives. Only the winner is observable. We study the behavior exhibited by this choice procedure and provide an axiomatic characterization of it. We leave as an open question the characterization of a generalization to larger shortlists.

## Summary
The paper axiomatizes a two-stage boundedly rational choice procedure that the authors call a *two-stage chooser* (TSC). The decision maker has two linear orders. From any feasible set she keeps the top two alternatives under the first criterion (the "two finalists"), then picks the winner among them under the second criterion. Crucially, only the winner (the choice) is observable, not the shortlist — this single observability constraint is what makes the characterization hard. The main result (Theorem 2) is that a choice function is a TSC if and only if it satisfies four novel axioms (A1–A4) phrased entirely in terms of *choice reversers* and a *hidden choice*. The procedure rationalizes a specific, intuitive failure of rationality (the "fries vs. salad" anomaly) and is shown to coincide with violations of the Always Chosen axiom.

## Research question
When can observed choice behavior — i.e. a choice function $c$ that returns a single winner from each set — be explained by a two-criterion, two-stage filtering procedure in which the analyst sees only the winner and never the runner-up? What is the exact axiomatic content of such behavior, and how does its non-rationalizability differ from other sequential procedures (notably Manzini–Mariotti)?

## Method / identification
The setting is standard finite choice theory. $X$ is a finite set of alternatives, $\Sigma$ the nonempty subsets, and a choice function is $c:\Sigma\to X$ with $c(A)\in A$. The object of interest is defined as: $c$ is a **two-stage chooser** if there exist linear orders $(\succ_1,\succ_2)$ with
$$c(A)=\max_{\succ_2}\big(T^{2}_{\succ_1}(A)\big),$$
where $T^{k}_{\succ}(A)$ is the set of top-$k$ elements of $A$ under $\succ$ (so $T^2_{\succ_1}(A)$ is the binary shortlist). The identification engine is built from two derived objects: the **reverser set** $R(A)=\{x\in A: c(A)\neq c(A\setminus x)\}$ (alternatives whose removal changes the choice) and the **hidden choice** $h(A)=c(A\setminus c(A))$ (what is chosen once the winner is deleted). A set has "choice reversal" if $\Sigma^{*}=\{A:|R(A)|\neq 1\}$, i.e. it contains a non-trivial reverser $y\neq c(A)$.

The four characterizing axioms are: **A1** for every $x\in R(A)$, $c(A\setminus x)=h(A)$ (removing any reverser yields the hidden choice); **A2** if $c(c(A)h(A))=h(A)$ then $A\in\Sigma^{*}$ (if the hidden choice beats the winner in a pairwise comparison, the set must exhibit reversal); **A3** if $x\in R(A)$, $x\in B\subset A$ and $B\in\Sigma^{*}$, then $x\in R(B)$ (reversers persist downward into reversing subsets); **A4** if $A\in\Sigma^{*}$ then $|R(A)|=2$ (at most one non-trivial reverser per set).

The proof of sufficiency is the technical core. From A1–A4 the authors derive four consequences B1–B4 (B1 is the no-binary-cycle condition; B2–B4 impose persistence of the reversal structure). They then construct an auxiliary asymmetric, transitive relation $P_0$ ($xP_0y$ iff some reversing set has $x$ as a reverser and $y$ not), and define the two criteria: $P_2$ from doubleton choices ($xP_2y\iff c(xy)=x$) and $P_1$ as a particular completion of $P_0$. Lemmas 1–6 establish that $P_1,P_2$ are linear orders, and a final case analysis shows $c(A)=\max_{P_2}(T^2_{P_1}(A))$ for every $A$. The hardest lemma (asymmetry of $P_0$, Lemma 2) requires reasoning about six-element sets.

## Data
None — this is a pure axiomatic / revealed-preference theory paper. The only "data" are illustrative choice tables (Example 1) and the counterexamples in the appendices.

## Key findings
- **Theorem 1** (warm-up): $c$ is rationalizable iff no set contains a non-trivial choice reverser, equivalently iff it satisfies IIA. Non-rational behavior always takes the form $c(A\setminus y)\neq c(A)\neq y$.
- **Theorem 2** (main characterization): $c$ is a two-stage chooser iff it satisfies A1–A4. The four axioms are shown to be independent (Appendix 1: four choice functions, no three axioms imply the fourth) and every rationalizable choice function satisfies them.
- **Corollary 1**: a non-rationalizable TSC necessarily violates the **Always Chosen** axiom (if $x=c(xa)$ for all $a\in A\setminus x$ then $x=c(A)$). Because a TSC contains no binary cycles, AC is the *only* extra ingredient separating TSCs from full rationality (via Manzini–Mariotti's Proposition 1). This pins down precisely the anomaly the model captures: an alternative that wins every pairwise contest can still lose in a large set because it fails to be shortlisted.
- **Theorem 3** (identification from small sets): distinct two-stage choosers must already differ on sets of at most three alternatives ($c|_{\Sigma_3}\neq\hat c|_{\Sigma_3}$). Behavior on triples determines a TSC, the analogue of the rational-choice fact that doubletons suffice under IIA. Note the first criterion is *not* uniquely revealed — swapping the top two of $\succ_1$ in the grand set leaves choices unchanged — whereas $\succ_2$ is exactly pinned down by doubleton choices.

## Contribution
The paper completes a natural step left open by [[@Eliaz2011|Eliaz, Richter and Rubinstein (2011)]], who characterized selection of the *two* finalists when both are observable; here a final winner is selected and only that winner is seen. It provides a clean revealed-preference foundation for a "shortlist-then-choose-with-a-different-criterion" heuristic, situating it within the limited-consideration literature (Masatlıoğlu, Nakajima, Özbay 2012; Lleras et al. 2011) as the special case where all but the first criterion's top two are filtered out, and within the list-based/limited-attention literature (Rubinstein–Salant) as the $k=2$ case of attention-constrained choice from a list. The technical contribution is the machinery (reversers, hidden choice, the $P_0$ completion) for recovering an unobservable shortlisting order from winner-only data.

## Limitations & open questions
- **The central open problem** (stated in the introduction and Conclusion): characterize the generalization to top-$k$ shortlists, $c(A)=\max_{\succ_2}(T^{k}_{\succ_1}(A))$ for $k>2$. The authors **conjecture** that an analogue of Theorem 2 holds with A1–A3 unchanged and A4 replaced by **A4\***: for every $A\in\Sigma^{*}$, $|R(A)|=k$. They flag that larger shortlists generate more reversers and hence a combinatorial explosion of cases in the sufficiency proof; even the binary case is described as "a challenging starting point."
- The model assumes the two criteria are **strict linear orders** (no indifferences) and that the *order of application* and identity of the criteria are **fixed** across all problems — relaxing either is unaddressed.
- The first criterion is only partially identified, so the model does not deliver unique welfare/structural recovery of the shortlisting order from choice data.

## Connections
The paper is most directly a sequel to **[[@Eliaz2011|Eliaz, Richter & Rubinstein (2011)]]**, "Choosing the two finalists," differing only in the observability of the runner-up. The benchmark for the *type* of irrationality is **[[@Manzini2007|Manzini & Mariotti (2007)]]**, "Sequentially rationalizable choice": both are two-stage, but the authors stress the anomalies differ, and they borrow Manzini–Mariotti's proposition linking no-binary-cycles plus Always Chosen to rationalizability. The limited-consideration framing draws on **Masatlıoğlu, Nakajima & Özbay (2012)** (revealed attention) and **Lleras, Masatlıoğlu, Nakajima & Özbay (2011)** (choice by limited consideration). The list/frame interpretation connects to **[[@Rubinstein2006|Rubinstein & Salant]] (2006, 2008)** (choice from lists; $(A,f)$ choice with frames) — the TSC is the $k=2$ instance of their limited-attention chooser, though restricted to standard (non-extended) choice functions. Related shortlisting and identification work cited includes **de [[@deClippel2012|Clippel & Eliaz (2012)]]** (reason-based choice), **Dutta & Horan (2013)** (inferring rationales from rational shortlist methods), and **Yıldız (2012)** (list-rationalizable choice, whose weak path independence implies axiom A2). The rationalizability/IIA backbone follows **Moulin (1985)**.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
