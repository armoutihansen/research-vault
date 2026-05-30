---
citekey: Manzini2007
title: Sequentially Rationalizable Choice
authors: ["Manzini, Paola", "Mariotti, Marco"]
year: 2007
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/KNGI6WI4"
pdf: /Users/jesper/Zotero/storage/DM9X9GD4/Manzini2007.pdf
tags: [literature]
keywords: [bounded-rationality, revealed-preference, choice-theory, heuristics, sequential-rationalizability, axiomatic-choice]
topics: []
related: [Kalai2002, Loomes1991, Rubinstein2006, Samuelson1938]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> A sequentially rationalizable choice function is a choice function that can be retrieved by applying sequentially to each choice problem the same fixed set of asymmetric binary relations (rationales) to remove inferior alternatives. These concepts translate into economic language some human choice heuristics studied in psychology and explain cyclical patterns of choice observed in experiments. We study some properties of sequential rationalizability and provide a full characterization of choice functions rationalizable by two and three rationales. (JEL D01).

## Summary
Manzini and Mariotti propose a family of boundedly rational choice procedures in which a decision maker screens alternatives by applying a fixed, ordered list of asymmetric binary relations ("rationales"), each removing dominated alternatives, until one survives. The two-rationale case — a "Rational Shortlist Method" (RSM) — is fully characterized by two observable axioms (Expansion and Weak WARP). These procedures rationalize cyclical and menu-dependent choice that violates the classical single-preference model, yet remain testable via revealed-preference data. The paper also extends to $K$ rationales, shows that not every choice function is sequentially rationalizable, and gives a full characterization of 3-rationalizability.

## Research question
When are observed choices — including persistent pairwise cycles and WARP violations seen in experiments — compatible with a decision maker who applies a *fixed sequence of fixed rationales* to eliminate inferior alternatives? What observable, revealed-preference conditions characterize such behavior for two and three rationales, and what kinds of "irrationality" can and cannot be explained this way?

## Method / identification
The framework is axiomatic decision theory over a finite set of alternatives $X$ with $|X|\ge 2$. A choice function $\gamma:\mathcal{P}(X)\to X$ selects one alternative from each nonempty $S\subseteq X$. For an asymmetric relation $P$, the $P$-maximal set is $\max(S;P)=\{x\in S\mid \neg\exists\, y\in S \text{ with } (y,x)\in P\}$.

A choice function is a **Rational Shortlist Method (RSM)** if there is an ordered pair $(P_1,P_2)$ of asymmetric relations such that
$$\{\gamma(S)\}=\max(\max(S;P_1);P_2)\quad\text{for all } S\in\mathcal{P}(X).$$
The first rationale $P_1$ produces a shortlist; the second $P_2$ selects from it. The general notion, **sequential rationalizability**, uses an ordered list $P_1,\dots,P_K$ applied recursively ($M_0(S)=S$, $M_i(S)=\max(M_{i-1}(S);P_i)$), with $\{\gamma(S)\}=M_K(S)$; $\gamma$ is $K$-sequentially rationalizable if $K$ rationales suffice.

Identification rests on two axioms. **Expansion**: an alternative chosen from each of two sets is chosen from their union. **Weak WARP**: if $x=\gamma(\{x,y\})=\gamma(T)$ with $\{x,y\}\subseteq S\subseteq T$, then $y\neq\gamma(S)$ — a menu-dependence-permitting weakening of Samuelson's WARP. The constructive sufficiency proof defines $P_1=\{(x,y)\mid y$ is never chosen when $x$ is present$\}$ and $(x,y)\in P_2 \iff x=\gamma(\{x,y\})$. For restricted subdomains the combined axiom **WWE** is used. The 3-rationalizability result leans on Sen's (1970) binariness theorem applied to an auxiliary choice *correspondence* $\gamma^*$, via a "Recursion Lemma" that peels off the last two rationales.

## Data
None — this is a pure theory paper. Experimental evidence on cyclical choice is cited motivationally (Tversky 1969; [[@Loomes1991|Loomes, Starmer & Sugden 1991]]; Roelofsma & Read 2000; Blavatskyy 2003; Waite 2001 on gray jays), with reported cycle rates sometimes near or above 50 percent, but no original data are analyzed.

## Key findings
- **Theorem 1 (RSM characterization):** A choice function on any set $X$ is an RSM if and only if it satisfies Expansion and Weak WARP. Corollary 1 restates this on subdomains via the single axiom WWE.
- **Proposition 1:** Every choice function that violates WARP also violates **Always Chosen** (if an alternative beats all others pairwise it is chosen from the set) or **No Binary Cycles** — so violations of standard rationality partition into just these two elementary "pathologies."
- **Lemma 1 / Theorem 2:** Any sequentially rationalizable choice function satisfies Always Chosen; hence a sequentially rationalizable function violates WARP if and only if it exhibits binary cycles. Sequential rationalizability thus *excludes* the Always-Chosen pathology while accommodating cyclical choice.
- **Not universal:** Even with unboundedly many rationales, some choice functions on as few as three alternatives are *not* sequentially rationalizable.
- **Theorem 3 (3-rationalizability):** Full characterization via existence of a choice correspondence $\gamma^*$ satisfying $\gamma(\gamma^*(S))=\gamma(S)$, WWE on the induced subdomain, and binariness; the proof yields a concrete checking algorithm.
- **Application (Section III):** Preference reversal in intertemporal choice is generated by an RSM with a discounted-value rationale (with threshold $\sigma$) followed by outcome/time tie-breakers, compatible even with exponential discounting.

## Contribution
The paper gives economic, revealed-preference foundations to "noncompensatory," sequential elimination heuristics from psychology and marketing (Tversky's Elimination by Aspects; Gigerenzer–Todd's fast-and-frugal heuristics; two-stage consideration-and-choice models). Its key insight is that a limited, structured form of menu-dependence — captured by Weak WARP plus Expansion — is *equivalent* to two-stage rationale-based screening, providing simple, testable axioms where prior approaches relied on indirect estimation algorithms.

## Limitations & open questions
- A **full characterization of general sequential rationalizability** (arbitrary $K$) "remains a nontrivial open problem"; only partial results plus the 3-rationale case are given.
- General observable conditions characterizing sequential rationalizability of choice *correspondences* are lacking (needed to iterate the Recursion Lemma beyond the one-rationale base case).
- **Menu-dependent RSMs** (rationales applied in a problem-varying order) can rationalize many more functions, but "we do not know at present which choice functions can be rationalized in this way."
- The order of rationales is treated as fixed/hardwired; how it depends on context or decision-maker type is left open.

## Connections
The paper is the journal version of work previously circulated as "Rationalizing Boundedly Rational Choice," and builds directly on the authors' related Manzini & Mariotti (2006a) on intertemporal choice. It formalizes psychological heuristics from Tversky (1969, 1972) and Gigerenzer, Todd & the ABC Research Group (1999), and marketing evidence in Yee et al. and Kohli (forthcoming). It extends [[@Samuelson1938|Samuelson's (1938)]] revealed-preference program and the WARP/IIA tradition surveyed in Moulin (1985) and Suzumura (1983), using Sen (1970) on binariness and Varian (2005) on revealed preference. It contrasts with [[@Kalai2002|Kalai, Rubinstein & Spiegler (2002)]], where a single but menu-varying rationalizing order is used; with Ok & Masatlioglu (forthcoming) on intertemporal choice without a second partial order; and relates to Tadenuma (2002) in social choice, Rubinstein (2003) on similarity-based multistage procedures, Salant (2003) and [[@Rubinstein2006|Rubinstein & Salant (2006)]] on computational simplicity and behavioral revealed preference.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
