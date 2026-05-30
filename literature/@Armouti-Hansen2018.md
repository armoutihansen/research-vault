---
citekey: Armouti-Hansen2018
title: This or that? Sequential rationalization of indecisive choice behavior
authors: ["Armouti-Hansen, Jesper", "Kops, Christopher"]
year: 2018
type: journalArticle
doi: 10.1007/s11238-017-9634-8
zotero: "zotero://select/library/items/2IXDHEPB"
pdf: /Users/jesper/Zotero/storage/V5N9AI35/Armouti-Hansen2018.pdf
tags: [literature]
keywords: [bounded-rationality, choice-correspondence, rational-shortlist-method, categorize-then-choose, indecisiveness, revealed-preference, sequential-rationalization]
topics: []
related: [Apesteguia2005, Au2011, Cherepanov2013, Eliaz2006, Kalai2002, Manzini2007, Manzini2012a, Masatlioglu2012, Rubinstein2006, Rubinstein2012, Salant2008, Sen1993, Shafir1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Decision-makers frequently struggle to base their choices on an exhaustive evaluation of all options at stake. This is particularly so when the choice problem at hand is complex, because the available alternatives are hard (if not impossible) to compare. Rather than striving to choose the most valuable alternative, in such situations decision-makers often settle for the choice of an alternative which is not inferior to any other available alternative instead. In this paper, we extend two established models of boundedly rational choice, the categorize then choose heuristic and the rational shortlist method, to incorporate this kind of "indecisive" choice behavior. We study some properties of these extensions and provide full behavioral characterizations.

## Summary

The paper generalizes two workhorse models of sequential boundedly rational choice — the Rational Shortlist Method (RSM) and the Categorize Then Choose (CTC) heuristic of [[@Manzini2007|Manzini & Mariotti]] (2007, 2012) — from single-valued choice *functions* to set-valued choice *correspondences*. The motivating phenomenon is **indecisiveness**: after a decision-maker (DM) sequentially eliminates dominated options, several mutually incomparable alternatives may survive, and the DM is content to settle for any of them rather than force a unique winner. The authors provide full behavioral characterizations of both generalized procedures via revealed-preference axioms, thereby filling a gap that Manzini & Mariotti themselves flagged for the correspondence domain.

## Research question

Can the sequential-elimination logic of the RSM and CTC be extended so that the terminal stage need not be *decisive* (need not single out one maximal element), and what observable (revealed-preference) restrictions on a choice correspondence are then necessary and sufficient for representability? Equivalently: what does "indecisive" sequential rationalization look like axiomatically, and how does indecisiveness differ from indifference?

## Method / identification

The framework is axiomatic revealed-preference theory. Let $X$ be a finite set of alternatives with $|X|>2$ and let $\mathcal{P}(X)$ be its nonempty subsets. A **choice correspondence** is a map $C_c:\mathcal{P}(X)\to\mathcal{P}(X)$ with $C_c(S)\subseteq S$. For an asymmetric binary relation (rationale) $P\subseteq X\times X$, the $P$-maximal set is $\max(S;P)=\{x\in S\mid \nexists\, y\in S \text{ with } (y,x)\in P\}$; for an asymmetric *shading* relation $\rhd$ on $\mathcal{P}(X)$, maximality is defined analogously over set-pairs.

Two procedures are defined. A correspondence is a **generalized RSM** if there is an ordered pair $(P_1,P_2)$ of asymmetric relations with
$$C_c(S)=\max(\max(S;P_1);P_2)\quad\text{for all }S\in\mathcal{P}(X).$$
It is a **generalized CTC** if there is a shading relation $\rhd$ on $\mathcal{P}(X)$ and an asymmetric rationale $P$ with
$$C_c(S)=\max(\max(S;\rhd);P)\quad\text{for all }S\in\mathcal{P}(X).$$
Crucially the second-stage relation need *not* be decisive on the survivors of stage one, so $C_c(S)$ may be non-singleton. The identifying axioms are correspondence transforms of the originals: **Weak WARP\*** (WWARP\*) rules out choice *re*-reversals — if $x$ is the unique choice in $\{x,y\}$ and $x\in C_c(T)$ with $y\in T$, then $y\notin C_c(S)$ for every $S$ with $\{x,y\}\subset S\subseteq T$ — and **Expansion\*** — if $x\in C_c(S)\cap C_c(T)$ then $x\in C_c(S\cup T)$. The constructive sufficiency proofs build the rationales explicitly from observed choices (e.g. $(x,y)\in P_2 \iff y\notin C_c(x,y)$), and for the CTC reconstruct the shading relation from upper/lower contour sets of $C_c$.

## Data

None — this is a pure decision-theory paper. Illustrations are a running restaurant-choice vignette and a stylized stock-market example over three shares $\{A,B,C\}$, with no empirical estimation.

## Key findings

- **Theorem 4.1 (RSM characterization):** A choice correspondence $C_c$ on a finite $X$ is a generalized RSM if and only if it satisfies **Expansion\*** and **WWARP\***. This parallels [[@Manzini2007|Manzini & Mariotti (2007)]], whose function-domain RSM required WWARP plus an expansion axiom.
- **Theorem 4.2 (CTC characterization):** $C_c$ is a generalized CTC if and only if it satisfies **WWARP\*** alone — mirroring the function-domain result that CTC is characterized by WWARP. Since every RSM is a special case of a CTC, the CTC class is strictly larger (Expansion\* is the additional bite of the RSM).
- The stock-market cases show the procedures' separating power: "default share" patterns (Case 3) are rationalizable by CTC but **not** by any RSM, and "**reversed Condorcet inconsistency**" patterns (Case 4) are rationalizable by **neither**, exhibiting a peculiarity unique to indecisive choice.
- Indecisiveness is genuinely distinct from indifference: under these procedures it can happen that both $x$ and $y$ survive from $\{x,y\}$ yet only $x$ survives from $\{x,y,z\}$, which indifference could not produce.

## Contribution

The paper closes a gap explicitly left open by [[@Manzini2007|Manzini & Mariotti]] (2007, p. 1833), who noted the lack of conditions for general choice *correspondences*. By transforming WARP-style axioms from functions to correspondences while preserving their intuition (no choice re-reversals; expansion consistency), it delivers clean necessary-and-sufficient characterizations that nest the original decisive models as special cases, and it gives a precise revealed-preference home to "settling for any non-inferior option" behavior.

## Limitations & open questions

- **Indecisiveness vs. indifference is not always separable from choice data.** Building on Mandler (2009), the authors concede that with multiple elimination criteria the boundary becomes fluid; if only choices (not preference judgments) are observable, distinguishing the two is "difficult, if not impossible." Allowing weak rationales $P'$ creates two non-coinciding maximization notions (only one of which preserves scope for indecisiveness, per Danan 2003).
- **Frame-based singleton selection is sketched but not characterized.** They suggest viewing $C_c$ as induced by frame-sensitive RSM choice functions, $\gamma(S,f)=\max(\max(\max(S;P_1);P_2);f)$ (à la [[@Salant2008|Salant & Rubinstein 2008]]), and relate it to behavioral data sets and distortion functions ([[@Rubinstein2012|Rubinstein & Salant 2012]]), but leave a full account of how DMs resolve indecisiveness as open.
- The two-stage / single-shading structure is fixed; longer elimination sequences and the welfare implications of indecisive choice are not pursued.

## Connections

Directly generalizes [[@Manzini2007|Manzini & Mariotti (2007)]] (Rational Shortlist Method) and [[@Manzini2012a|Manzini & Mariotti (2012)]] (Categorize Then Choose). The indifference-vs-indecisiveness theme draws on [[@Eliaz2006|Eliaz & Ok (2006)]], [[@Sen1993|Sen (1993)]], Kreps (1988), Danan (2003), Mandler (2009), Hill (2012), and Savage (1954). Related sequential-rationalization and multiple-rationales work includes [[@Kalai2002|Kalai, Rubinstein & Spiegler (2002)]], [[@Apesteguia2005|Apesteguia & Ballester (2005)]], [[@Au2011|Au & Kawai (2011)]], and [[@Cherepanov2013|Cherepanov, Feddersen & Sandroni (2013)]]; limited-attention/consideration models include [[@Masatlioglu2012|Masatlioglu, Nakajima & Ozbay (2012)]] and Lleras, Masatlioglu, Nakajima & Ozbay (2014). Frame- and list-based choice connects to [[@Salant2008|Salant & Rubinstein (2008)]], [[@Rubinstein2006|Rubinstein & Salant]] (2006, 2012). The behavioral motivation (hard-to-resolve conflict) cites [[@Shafir1993|Shafir, Simonson & Tversky (1993)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
