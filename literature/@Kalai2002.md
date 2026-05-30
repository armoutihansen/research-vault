---
citekey: Kalai2002
title: Rationalizing Choice Functions by Multiple Rationales
authors: ["Kalai, Gil", "Rubinstein, Ariel", "Spiegler, Ran"]
year: 2002
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/RYIDWNYF"
pdf: /Users/jesper/Zotero/storage/LFQIGEBT/Kalai2002.pdf
tags: [literature]
keywords: [revealed-preference, bounded-rationality, multiple-rationales, iia-violations, choice-functions, rationalizability]
topics: []
related: [Baigent1996, Cherepanov2013, Manzini2007, Sen1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary

This short note (Econometrica "Notes and Comments") proposes a way to extend the economist's standard rationality test to choice functions that violate the Independence of Irrelevant Alternatives (IIA). Instead of demanding a single rationalizing ordering, the authors allow a *small collection* of strict orderings (rationales) and ask that each choice be maximal with respect to *some* ordering in the collection. The key object is $r(c)$, the minimal number of orderings needed. The paper bounds $r(c)$ in general and computes it for several behavioral choice procedures, showing that some intuitively "almost rational" procedures (e.g. the second-best procedure) actually require many rationales, while others coincide with their intuitive descriptions.

## Research question

When a decision maker's choice function violates IIA (and so cannot be explained by a single preference ordering), how many distinct preference orderings are needed to explain the behavior, and what does this minimal number reveal about the "rationality" of various well-known choice procedures? In short: can we measure how far a choice function is from rationality by the minimal size of a multi-rationale explanation?

## Method / identification

Let $X$ be a finite set of alternatives with $|X|=N$, and let $\mathcal{P}(X)$ be the nonempty subsets. A choice function $c$ assigns to each $A\in\mathcal{P}(X)$ a unique $c(A)\in A$. The central concept: a $K$-tuple of strict preference relations $(\succ_k)_{k=1}^{K}$ is a **rationalization by multiple rationales (RMR)** of $c$ if for every $A$, $c(A)$ is $\succ_k$-maximal in $A$ for *some* $k$. Interpretation: the DM holds a partition of $\mathcal{P}(X)$ (cells are "states of the world") and applies one ordering per cell; behavior is rationalized once the state is appended to the description of alternatives.

Every choice function trivially has an RMR (give each set its own rationale), so the authors focus on the *minimal* number $r(c)$. When $r(c)=1$, $c$ is rational in the standard sense (IIA holds). The larger $r(c)$, the less meaningful the multi-rationale explanation. The method is entirely *context-free*: it uses only observed choices, no information about the content of alternatives or the DM's motives. The paper is pure theory — the analytical work is combinatorial counting and inductive constructions over orderings, supported by a key lemma (Lemma 0): if $r(c)=K$ then there is an RMR with $K$ orderings whose top elements are all distinct (move shared top elements to the bottom without breaking the RMR).

## Data

None — this is a theoretical note. No empirical data or experiments; the "examples" (Luce-Raiffa's dinner, the $(u,v)$ procedure, "best from the popular field," second-best, median) are illustrative choice procedures, not datasets.

## Key findings

- **Proposition 1 (upper bound):** $r(c)\le N-1$ for every choice function $c$. Proof: fix $b\ne c(X)$; for each $a\ne b$ use an ordering ranking $a$ first and $b$ second.
- **Proposition 2 (generic tightness):** the proportion of choice functions rationalizable by fewer than $N-1$ orderings tends to $0$ as $N\to\infty$. So "almost all" choice functions need the maximal $N-1$ rationales. The counting argument shows the bound $(1-1/N)^{2u}N^2 2^N<1$ for $N>19$, implying existence of $c$ with $r(c)=N-1$ (an explicit construction for $N=p^2+p+1$ used projective geometry in an earlier draft).
- **Worked examples:** Luce-Raiffa's dinner needs exactly $2$ orderings; the $(u,v)$ procedure needs $2$; its "twin" ($u$-then-$v$ thresholded on $u$) collapses to a *single* lexicographic ordering; "the best from among the popular" with $J$ categories gives $r(c)=J$.
- **Proposition 3 (second-best procedure):** if the DM always picks the $\succ$-second-best element, then $r(c)=\lceil\log_2 N\rceil$. Proven by an inductive construction (split $X$ into top/bottom halves) plus a lower-bound argument assigning each element a distinct proper subset of orderings ranking it above the $\succ$-minimal element.
- **Proposition 4 (median procedure):** for the left-right "median" voter procedure, $N-6\sqrt{N}<r(\mathrm{med})<N-\sqrt{N}+1$, i.e. close to the $N-1$ maximum and far above the second-best's $\log_2 N$. Supported by Lemma 1: a minimal RMR can be taken with adjacent top elements.

## Contribution

The paper introduces RMR and the complexity measure $r(c)$ as a graded extension of the binary rational/irrational classification, generalizing the single-ordering rationalizability test (IIA) to a quantitative one. It demonstrates that intuitive closeness to rationality and the context-free $r(c)$ can diverge sharply: the second-best procedure, which *feels* nearly rational and has an appealing context-laden story (greediness, wine quality), needs only $\log_2 N$ rationales, while the median procedure needs nearly $N$, even though it too has a simple two-pole intuition. This decouples the *number* of rationales from the *structure* of the explanation.

## Limitations & open questions

The authors are explicit about the crudeness of the measure. They note that the appeal of the Luce-Raiffa RMR comes not only from the small number of orderings but from the *simple description* of when each applies (governed by a single pivotal alternative $x^*$): "More research is needed to define and investigate 'structured' forms of rationalization." This is the main open hook — a complexity measure that penalizes not just the count of rationales but the descriptive complexity of the partition assigning rationales to choice sets. They also stress the limits of the context-free stance: where motives/values/conventions exist (Sen's critique), one should instead enrich the consequence space, and an RMR explanation may be inappropriate even when $r(c)$ is low. The median procedure is flagged as better explained by two *fixed* opposed rationales balanced against each other, rather than by a partition-based RMR — suggesting alternative "balancing" models outside the RMR framework.

## Connections

The work sits in the bounded-rationality / revealed-preference tradition built on [[@Sen1993|Sen (1993)]], "Internal Consistency of Choice," whose context-dependence critique frames the paper's context-free caveat. The illustrative procedures draw on Luce & Raiffa (1957) (the dinner example) and McFadden (1999) (second-cheapest wine). The second-best and median procedures have axiomatic characterizations in [[@Baigent1996|Baigent & Gaertner (1996)]] and Gaertner & Xu (1999). The RMR idea anticipates later multi-self / sequential-rationale models of choice, notably [[@Manzini2007|Manzini & Mariotti (2007)]] on "sequentially rationalizable choice," [[@Cherepanov2013|Cherepanov, Feddersen & Sandroni (2013)]] on rationalization, and Kalai-style menu-dependent and categorization models (e.g. Manzini & Mariotti's categorize-then-choose). It is foundational reference material for the literature on rationalizing IIA violations through multiple orderings and on complexity measures of departures from rationality.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
