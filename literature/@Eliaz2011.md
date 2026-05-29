---
citekey: Eliaz2011
title: Choosing the two finalists
authors: ["Eliaz, Kfir", "Richter, Michael", "Rubinstein, Ariel"]
year: 2011
type: journalArticle
doi: 10.1007/s00199-009-0516-3
zotero: "zotero://select/library/items/GP2NQ5UB"
pdf: /Users/jesper/Zotero/storage/K9Z68K8T/Eliaz2011a.pdf
tags: [literature]
keywords: [choice-correspondence, consideration-sets, axiomatization, bounded-rationality, revealed-preference, shortlisting]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> This paper studies a decision maker who for each choice set selects a subset of (at most) two alternatives. We axiomatize three types of procedures: (i) The top two: the decision maker has in mind an ordering and chooses the two maximal alternatives. (ii) The two extremes: the decision maker has in mind an ordering and chooses the maximal and the minimal alternatives. (iii) The top and the top: the decision maker has in mind two orderings and he chooses the maximal element from each.

## Summary
A short revealed-preference theory note. Instead of the usual single-valued choice function, the decision maker maps each menu to a *small* set — here, at most two alternatives — interpreted either as a consideration set feeding a second (unmodeled) stage or as a final "team" of two. The authors give clean axiomatic characterizations of three intuitive shortlisting procedures: pick the top two by one ordering; pick the extremes (top and bottom) of one ordering; or pick the top of each of two orderings. The contribution is the precise behavioral signature (a small bundle of Sen-$\alpha$-style consistency axioms) that distinguishes these procedures from one another.

## Research question
What observable restrictions on a two-valued choice correspondence $D$ characterize each of three "choose the finalists" heuristics: (i) the **top two** of a single ordering, (ii) the **two extremes** (max and min) of a single ordering, and (iii) the **top-and-the-top** — the maximizers of two (possibly distinct) orderings? Equivalently, given only the observed shortlists, when can behavior be rationalized by each procedure, and what axioms separate them?

## Method / identification
Pure axiomatic choice theory, no data. The primitive is a **choice correspondence** $D$ on a finite alternative set $X$: a function assigning to every non-empty $A\subseteq X$ a non-empty subset $D(A)\subseteq A$ with $|D(A)|\le 2$. The authors interpret a multi-element $D(A)$ as "any of these could be the ultimately consumed element" (a consideration set, à la Kreps 1979 preference-for-flexibility), explicitly *not* a bundle. Each representation theorem proceeds by isolating axioms and then constructing the rationalizing ordering(s) by induction on $|X|$.

Axioms used:
- $A0$: $|A|\ge 2 \Rightarrow |D(A)|=2$ (always exactly two finalists).
- $A1$ (Sen's $\alpha$): $a\in D(A)$ and $a\in B\subset A \Rightarrow a\in D(B)$.
- $A2$ (expansion-consistency on removals): for $a\notin D(A)=\{x,y\}$, if $a\in D(A\setminus\{x\})$ then $a\in D(A\setminus\{y\})$.
- $A3$: for $x,y\in A$, if $a\in D(A\cup\{x\})$ and $a\in D(A\cup\{y\})$ then $a\in D(A\cup\{x,y\})$.
- $A0'$: $|D(A)|\le 2$ (relaxes $A0$ so the two orderings may agree on the top).
- $A4$ (weak IIA): if $D(A)=\{a\}$ and $a\in B\subseteq A$ then $D(B)=D(A)$.
- $A5$: if $a\in D(A_1)\cap D(A_2)\cap D(A_1\cap A_2)$ and $|D(A_1\cap A_2)|=2$, then $a\in D(A_1\cup A_2)$.

For top-and-the-top the construction is algorithmic: two rankings $a_1\succ_1\cdots\succ_1 a_n$ and $b_1\succ_2\cdots\succ_2 b_n$ are built element-by-element by repeatedly inspecting $D(X\setminus A_{1,m})$ and splitting into three cases depending on whether that set is a singleton and whether the partial orderings have so far coincided.

## Data
None — this is a theoretical paper. No experiment, dataset, or estimation; all "tests" are the verifications that each candidate procedure satisfies the relevant axioms and that the axioms are mutually independent (each shown by an explicit counterexample correspondence).

## Key findings
Three representation theorems, each an iff.

1. **The top two.** $D$ satisfies $A0,A1,A2$ iff there is an ordering $\succ$ on $X$ with $D(A)=$ the two $\succ$-top elements of $A$. The three axioms are independent (e.g., the two-extremes rule satisfies $A0,A1$ but violates $A2$). A stated extension generalizes this to a "top $M$" correspondence under $A1$, $A2$, and an $M$-element version of $A0$.

2. **The two extremes.** $D$ satisfies $A0,A3$ iff there is an ordering $\succ$ with $D(A)=\{\max(A,\succ),\min(A,\succ)\}$. A **lemma** first shows $A0+A3\Rightarrow A1$. The construction defines a "to the left of" relation: $a\to b$ iff $D(\{a,b,R\})=\{a,R\}$ and $D(\{L,a,b\})=\{L,b\}$ (where $D(X)=\{L,R\}$), then proves $\to$ is asymmetric, total, and transitive, so it is an ordering whose extremes $D$ selects. Notably the two-extremes procedure is the special case of top-and-the-top where the second ordering is the inverse of the first.

3. **The top-and-the-top.** $D$ satisfies $A0',A1,A4,A5$ iff there are orderings $\succ_1,\succ_2$ (possibly identical) with $D(A)=\{\max(A,\succ_1),\max(A,\succ_2)\}$. Under the "two reasons" reading, $a$ is chosen from $A$ if some reason $R_i$ ranks $a$ above all of $A$; $A5$ encodes that a jointly-chosen pair forces a single reason to carry an element across the union. The four axioms are independent (e.g., the top-two procedure satisfies $A0',A1,A4$ but violates $A5$ once $|X|\ge 4$).

## Contribution
Supplies the missing behavioral characterizations for *small-set* (specifically two-element) choice, a natural object when one observes shortlists, finalist pairs, or two-member teams rather than final picks. It cleanly separates three superficially similar shortlisting heuristics by minimal consistency axioms, and links them: every two-extremes rule is a top-and-the-top rule, and a top-and-the-top rule that always returns a pair must in fact be a two-extremes rule (its two orderings are inverses). It thereby extends the Sen-$\alpha$/IIA toolkit and the menu-choice tradition (Kreps) to correspondences whose output is interpreted as a consideration set.

## Limitations & open questions
- **Explicit open problem:** how to extend the top-and-the-top procedure to selecting the tops of $M>2$ orderings (stated verbatim in the closing comment). The top-*two* "top $M$" extension is given, but the multi-ordering version is open.
- The framework fixes the cap at (at most) two; the authors note but do not fully develop the case of an arbitrary fixed bound $M$, and only the single-ordering extension is proved.
- It axiomatizes **only the first stage** (the shortlist). The actual second-stage choice from the consideration set is unmodeled — by design, in the Kreps tradition — so the procedures say nothing about which finalist is ultimately consumed.
- For the team interpretation the model is silent on within-pair structure (e.g., president vs. vice-president roles); it treats the pair as unordered.

## Connections
Squarely in the bounded-rationality / two-stage choice literature. It contrasts itself with **Manzini & Mariotti** (sequentially rationalizable choice, 2007; consumer choice and revealed bounded rationality, 2009) and **Masatlioglu, Nakajima & Ozbay** (revealed attention, 2008): those papers observe the *final* choice and *infer* the shortlist/attention filter, whereas here the shortlist itself is the observable. The consideration-set reading draws on **Kreps (1979)** on preference for flexibility and on the authors' own **Eliaz & Spiegler (2009)** on consideration sets and competitive marketing. The top-and-the-top connects to multi-rationale rationalization (**Aizerman & Malishevski 1981**) and, via the Pareto interpretation of two individuals' orderings, to testable implications of collective choice (**Sprumont 2000**). The two-agent organizational reading (a screener plus a top manager) cites **García-Sanz (2008)**.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
