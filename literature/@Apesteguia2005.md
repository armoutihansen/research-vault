---
citekey: Apesteguia2005
title: Minimal books of rationales
authors: ["Apesteguía, José", "Ballester, Miguel A."]
year: 2005
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/6T28Y9W9"
pdf: /Users/jesper/Zotero/storage/P8K2PGLL/Apesteguia2005.pdf
tags: [literature]
keywords: [rationalization, independence-of-irrelevant-alternatives, bounded-rationality, choice-functions, revealed-preference, combinatorial-optimization]
topics: ["[[sequential-rationalizability-shortlists]]"]
related: [Baigent1996, Kalai2002, Sen1993]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
When a choice function violates the "independence of irrelevant alternatives" (IIA) axiom it cannot be explained by a single preference order, but [[@Kalai2002|Kalai, Rubinstein and Spiegler (2002)]] show it can always be explained by a *book of rationales* — a collection of linear orders such that every choice is maximal in the chosen set for at least one "page." This paper supplies a constructive **algorithm** that, for any finite choice problem $(X,c)$, returns (i) the minimal number of rationales, (ii) the explicit composition of each rationale, and (iii) a map from choice problems to the rationale that explains them. The trick is to recast the minimization as a graph/partition problem on a small derived set of "c-maximal" choice sets. The authors then characterize the structure of $M_c$ and the minimal book for three benchmark procedures (rational, second-best, median) and conjecture the general problem is NP-complete.

## Research question
Kalai–Rubinstein–Spiegler establish *existence* of a minimal book of rationales but compute the minimal number only for specific procedures. The question here is fully constructive and general: for an arbitrary $(X,c)$, how do we actually find the minimal number of rationales, the contents of each rationale, and the association between choice problems and rationales — so that the choice function and its minimal book carry exactly the same behavioral information (as is automatic in the classical IIA case, where the book has one page)?

## Method / identification
The objects are a finite set of alternatives $X$ and a choice function $c$ assigning to each non-empty $A\subseteq X$ a unique $c(A)\in A$. A **rationalization by multiple rationales (RMR)** is a tuple of strict orders $(\succ_k)_{k=1,\dots,K}$ such that for every $A$, $c(A)$ is $\succ_k$-maximal in $A$ for some $k$. A *minimal RMR* additionally records the composition of each order and the problem-to-rationale map.

The core reduction restricts attention to **c-maximal sets**: $S$ is c-maximal if no strict superset $T\supset S$ has $c(T)=c(S)$; let $M_c$ denote this family. Every other choice set inherits its explanation from a c-maximal set via IIA, so only $M_c$ "makes a difference." On $M_c$ define the binary relation $R$ by
$$A\,R\,B \iff c(A)\notin B\setminus\{c(B)\},$$
i.e. $A$ and $B$ can share a page because putting $c(A)$ at the top does not disturb the choice in $B$. A **complete preorder partition (CPP)** of $(M_c,R)$ is a partition whose every class, restricted to $R$, is a complete preorder; it is minimal if no CPP has fewer classes.

**Proposition 2.5** (the identification result) proves that solving the minimal RMR problem on $(X,c)$ is *equivalent* to solving the minimal CPP problem on $(M_c,R)$, with equal minimal counts — the proof explicitly constructs a rationale $\succ_p^*$ from each class and vice versa, so no behavioral information is lost.

**Algorithm 1** then operates on $(M_c,R)$: compute $M_c$ and $R$; for each linear order $<$ on $M_c$ greedily assign each set to an *admissible class* (one all of whose members $R$-dominate the new set) or open a new class; keep the order yielding the fewest classes. **Proposition 3.1** shows the algorithm returns a minimal CPP regardless of the rule used to pick among admissible classes. For the second-best procedure the authors enlarge the notion to *admissible-2* classes (Def. 4.2) and a specific selection rule (Def. 4.4), giving **Algorithm 2** (Prop. 4.3).

## Data
None — this is a pure decision-theory paper. The only "data" are constructed example choice functions (e.g. the $X=\{1,2,3,4,5\}$ instance used in Proposition 4.8).

## Key findings
- **Proposition 2.5 (equivalence).** Minimal RMR on $(X,c)$ $\equiv$ minimal CPP on $(M_c,R)$; minimal numbers of rationales and classes coincide. This is the paper's foundational result and formalizes the KRS intuition that the decision maker partitions the space of choice problems into "states of the world," applying one rationale per state.
- **Proposition 3.1 / 4.3 (correctness).** Algorithm 1 (and its second-best variant Algorithm 2) always produces a minimal CPP, hence a minimal RMR.
- **Proposition 4.1 (rational procedure).** If $c$ satisfies IIA, then $|M_c|=|X|-1$, and ordering $M_c$ by decreasing cardinality lets the algorithm produce a single class (one rationale) in $|X|-1$ steps — recovering the classical result.
- **Proposition 4.5 (second-best).** For the second-best procedure, $|M_c|=|X|\times(|X|-1)/2$ (polynomial), and an explicit ordering yields a CPP with $\lceil\log_2|X|\rceil$ classes, matching the KRS bound; the proof is a three-stage induction building $M_c^{n+1}$ from $M_c^{n}$.
- **Proposition 4.6 (median).** For the median procedure $|M_c|$ is **not** polynomially bounded in $|X|=N$; for odd $N$,
$$|M_c|=\sum_{j=1}^{(N-1)/2}\left[\binom{(N-1)/2+j}{2j-1}+\binom{(N-1)/2+j}{2j}\right],$$
so the c-maximal reduction gives little traction and the minimal book remains hard to pin down — mirroring KRS's bounded-only result for the median.
- **Proposition 4.7 (pruning).** It suffices to consider linear orders that place the full set $X$ first, because $R$ is tied to set inclusion ($A\subset B \Rightarrow \lnot(A\,R\,B)$), forcing $X$ to top its class.
- **Proposition 4.8 (negative result).** Restricting to orders that *extend* the inclusion partial order $\subset$ does **not** always yield a minimal CPP (counterexample on $X=\{1,2,3,4,5\}$ where inclusion-respecting orders give 3 classes but the minimum is 2); a corollary kills the analogous "order by cardinality" heuristic.

## Contribution
The paper turns the existence theorem of Kalai–Rubinstein–Spiegler into an operational, information-preserving procedure: it gives the *complete* minimal book — count, contents, and the choice-problem-to-rationale assignment — for any finite choice function, restoring the behavioral equivalence between a choice function and its rationalization that holds in the classical IIA world. Methodologically, recasting rationalization as a complete-preorder partition of c-maximal sets under $R$ is a reusable bridge between revealed-preference theory and combinatorial optimization, and the per-procedure cardinality results ($|X|-1$, $|X|(|X|-1)/2$, exponential) cleanly explain why some bounded-rationality procedures are tractable and others are not.

## Limitations & open questions
- **Computational cost / NP-completeness.** The algorithm sweeps over linear orders of $M_c$, which can be a heavy computation. The authors *conjecture* the general minimal-RMR problem is NP-complete: they prove it lies in NP, that partitioning a directed graph into complete-and-transitive subgraphs (PICTSG) is NP-complete, and that their problem is a subproblem of PICTSG — but the reduction closing the conjecture is left open.
- **Pruning the search space.** Beyond fixing $X$ first (Prop. 4.7), restricting which linear orders over $M_c$ must be examined "remains open"; the natural inclusion-extension and cardinality heuristics are shown to fail (Prop. 4.8).
- **Median procedure.** Because $|M_c|$ is exponential, computing a minimal CPP for the median rule is still complicated; only its $M_c$ is characterized, not a closed-form minimal book.
- **Behavioral interpretation.** The authors flag as a research program *why* a decision maker turns to one page versus another — understanding the substantive meaning of the partition/states-of-the-world as a route to understanding individual behavior.

## Connections
The paper is a direct constructive sequel to **[[@Kalai2002|Kalai, Rubinstein and Spiegler]] (2002, Econometrica)**, "Rationalizing Choice Functions by Multiple Rationales," whose book-of-rationales notion and second-best/median results it extends. It sits in the bounded-rationality and revealed-preference tradition descending from **Arrow (1959)** on rational choice functions and **[[@Sen1993|Sen (1993)]]** on internal consistency of choice; the **second-best** procedure traces to Sen and to [[@Baigent1996|Baigent–Gaertner (1996)]], Gaertner–Xu (1999a), and McFadden (1999), while the **median** procedure is characterized by Gaertner–Xu (1999b). In the conclusion the authors connect to **Salant (2003)** (memory and computational power favor rationality), **Manzini and Mariotti (2004)** on sequential rationalizability / rational shortlist methods (which notably *cannot* sequentially rationalize the second-best or median procedures), and **Ok (2004)** on axiomatic IIA for choice correspondences. The NP-completeness discussion leans on **Garey and Johnson (1979)**.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
