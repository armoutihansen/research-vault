---
citekey: Manzini2012
title: Choice by lexicographic semiorders
authors: ["Manzini, Paola", "Mariotti, Marco"]
year: 2012
type: journalArticle
doi: 10.3982/TE679
zotero: "zotero://select/library/items/J9DR2LV9"
pdf: /Users/jesper/Zotero/storage/DYATAI5V/Manzini2012a.pdf
tags: [literature]
keywords: [lexicographic-semiorders, bounded-rationality, revealed-preference, choice-functions, sequential-rationalizability, axiomatic-characterization]
topics: ["[[sequential-rationalizability-shortlists]]"]
related: [Ehlers2008, Mandler2012, Manzini2007, Salant2008, Tyson2008]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> In Tversky's (1969) model of a lexicographic semiorder, a preference is generated via the sequential application of numerical criteria by declaring an alternative x better than an alternative y if the first criterion that distinguishes between x and y ranks x higher than y by an amount exceeding a fixed threshold. We generalize this idea to a fully fledged model of boundedly rational choice. We explore the connection with sequential rationalizability of choice (Apesteguia and Ballester 2010, [[@Manzini2007|Manzini and Mariotti 2007]]) and we provide axiomatic characterizations of both models in terms of observable choice data.

## Summary
The paper extends Tversky's (1969) lexicographic semiorder, originally a model of cyclical *binary* preference, into a full theory of choice from arbitrary (including non-binary) menus. The decision maker applies an ordered list of threshold criteria (semiorders); at each stage he discards alternatives that are beaten on that criterion by more than a fixed threshold $\sigma$, iterating on the survivors until a single alternative remains. The authors characterize this "choice by lexicographic semiorder" (cles) via a single contraction-consistency axiom, **Reducibility**, give a constructive algorithm for the criteria, locate the model precisely relative to sequential rationalizability / rational shortlist methods, and use the same machinery to settle the previously-open axiomatic characterization of sequential rationalizability.

## Research question
How can Tversky's noncompensatory, threshold-based lexicographic heuristic—which produces possibly cyclic binary preferences—be turned into a well-defined, single-valued *choice function* over rich menus, and what are its exact observable (revealed-preference) implications? Secondarily: how does this model relate to the more general boundedly rational notions of sequential rationalizability and rational shortlist methods?

## Method / identification
Pure axiomatic decision theory; no data. Fix a set $X$. A **semiorder** (Luce 1956) is an irreflexive binary relation $P$ satisfying two interval conditions, representable on suitable domains by $(x,y)\in P \iff f(x) > f(y) + \sigma$ for a value function $f$ and a *fixed* threshold $\sigma\ge 0$. A **lexicographic semiorder** is an ordered sequence $(f_i,\sigma)_{i\in I}$ (with $I$ finite or all of $\mathbb{N}$).

The choice rule operates by sequential elimination via "survivor sets":
$$M_0(S)=S,\qquad M_i(S)=\{s\in M_{i-1}(S)\mid \forall s'\in M_{i-1}(S),\ f_i(s)+\sigma \ge f_i(s')\}.$$
A choice function $c$ is a **choice by lexicographic semiorder (cles)** if some $(f_i,\sigma)_{i\in I}$ yields, for every menu $S$, a $j$ with $\{c(S)\}=M_j(S)=M_k(S)$ for all $k\ge j$ (finite termination on each menu, though no uniform bound across menus is required). A **basic** semiorder has $f_i$ ranging only in $\{-1,0,1\}$ with $\sigma=1$: alternatives are merely classed good/neutral/bad on each dimension.

The central axiom: **Reducibility**. For every nonempty subcollection $C\subseteq\Sigma$ there exist $S\in C$ and $x,y\in S$ such that for all $T\in C$ with $(T\setminus\{y\})\in C$ and $x\in T$, $c(T)=c(T\setminus\{y\})$ — i.e. on any subdomain some $x$ makes some $y$ "$C$-irrelevant" (removing $y$ never changes the choice whenever $x$ is present). This is a weakening of standard IIA: IIA demands *every* unchosen alternative be removable on every menu; Reducibility demands only *some* pair on *some* menus. The comparison model, **sequential rationalizability** ([[@Manzini2007|Manzini & Mariotti 2007]]), replaces the threshold criteria $f_i$ with arbitrary asymmetric **rationales** $P_i$ applied in order; a **rational shortlist method (RSM)** uses two rationales; **acyclic** sequential rationalizability restricts rationales to be acyclic.

## Data
None — this is a theoretical paper. The "data" are abstract choice functions $c:\Sigma\to X$ over a domain $\Sigma$ of menus; results concern which such functions are representable. An Appendix works through a worked example (from Apesteguia & Ballester 2010) applying the constructive algorithm.

## Key findings
- **Proposition 1.** On a purely binary domain with $X$ countable, the basic cles model is *completely unrestrictive* — any binary choice pattern is induced by a basic lexicographic semiorder.
- **Proposition 2.** If $c$ satisfies WARP and $X$ is countable, a basic lexicographic semiorder induces it. Since WARP does not imply SARP on general domains, cles can generate strict revealed-preference *cycles* ("irrational" data).
- **Proposition 3 (finite-domain equivalence).** For finite $X$, $c$ is acyclic sequentially rationalizable iff it is induced by a *basic* lexicographic semiorder. Basic discrimination already exhausts the acyclic-rationale model. (Relatedly, on full domains this connects to Apesteguia & Ballester's equivalence of acyclic and *simple* rationales.)
- **Proposition 4 (separation on infinite domains).** There exist RSMs with acyclic rationales (e.g. $P_1=\{(i,i+1)\}$, $P_2=\{(j,i)\mid j>i+1\}$ on $X=\{1,2,\dots\}$) that are induced by *no* lexicographic semiorder, regardless of discriminatory power. So the finite-domain clause in Proposition 3 is essential: moving from acyclicity to transitivity (semiorders) is a genuine behavioral threshold on larger domains.
- **Theorem 1.** For finite $X$ and $\Sigma$ = all finite subsets, the following are equivalent: (i) $c$ is a cles; (ii) $c$ is reducible; (iii) $c$ is a basic cles. Reducibility captures *all* observable implications, and basic semiorders cover exactly the same ground as general ones. The proof is constructive (an algorithm building the semiorders).
- **Theorem 2.** A natural relaxation of Reducibility characterizes sequential rationalizability *tout court* — resolving a problem the authors left open in [[@Manzini2007|Manzini & Mariotti (2007)]].

## Contribution
Three contributions: (1) it converts Tversky's binary lexicographic semiorder into a procedurally faithful, single-valued choice function that handles arbitrary menus and naturally accommodates cyclical revealed preference; (2) it gives a clean revealed-preference characterization (Reducibility) plus a constructive algorithm, and pins down the surprising fact that *basic* (three-valued) discrimination loses nothing on finite domains; (3) it maps the model's exact position within the bounded-rationality landscape (sequential rationalizability, RSMs, acyclic rationales, the Mandler–Manzini–Mariotti checklist model) and, as a byproduct, supplies the missing axiomatic characterization of sequential rationalizability.

## Limitations & open questions
- Theorem 1's full equivalence is stated for **finite $X$ with $\Sigma$ = all finite subsets**; behavior on restricted or infinite domains is only partially mapped (Propositions 1–4), leaving the general-domain characterization incomplete.
- The authors explicitly **decline to defend Reducibility as an a priori compelling rationality property**, resting the model's appeal on psychological plausibility, tractability, and testability rather than normative grounds — inviting work on its empirical content.
- They float (in the concluding remarks) but do not develop an application to **choice under uncertainty via sequential quantile maximization** (sequentially discarding gambles by quantiles, then applying a mean-based criterion on the reduced set) — an explicit hook for future modeling.
- The relation to the **checklist model** (basic cles as a three-valued weakening of a checklist, hence a "minimal departure from rational choice") is sketched conceptually but not fully formalized.

## Connections
Directly builds on and reinterprets Tversky (1969) on lexicographic semiorders, and on Luce (1956) for semiorders / Fishburn (1970, 1985) for interval orders. It is the choice-theoretic companion to the authors' own [[@Manzini2007|Manzini & Mariotti (2007)]] on sequential rationalizability and rational shortlist methods, and to Manzini & Mariotti (2006) on multicriterion intertemporal choice. It engages closely with Apesteguia & Ballester (2010) on acyclic and simple rationales, and with [[@Mandler2012|Mandler, Manzini & Mariotti (2012)]] on the checklist model (plus Mandler 2009 on the minimum number of rationales). Other heuristic-choice antecedents include Rubinstein (1988) and Leland (1994) on similarity-based binary choice (experimentally probed by Binmore et al. 2008), Gigerenzer & Todd (1999) on fast-and-frugal heuristics, and Kohli & Jedidi (2007) / Yee et al. (2007) in marketing. The revealed-preference, axiomatic-on-choice-data methodology aligns it with the broader boundedly rational choice program: Masatlioglu & Ok (2005, 2006), Cherepanov, Feldman & Sanjurjo / Cherepanov et al. (2008), Masatlioglu & Nakajima (2011), [[@Tyson2008|Tyson (2008)]], [[@Salant2008|Salant & Rubinstein (2008)]], Eliaz, Richter & Rubinstein (2009), [[@Ehlers2008|Ehlers & Sprumont (2008)]] and Lombardi (2008) on tournament-based choice, and Kalandrakis (2010) on rationalizing voting choices.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
