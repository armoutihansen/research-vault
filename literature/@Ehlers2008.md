---
citekey: Ehlers2008
title: Weakened WARP and top-cycle choice rules
authors: ["Ehlers, Lars", "Sprumont, Yves"]
year: 2008
type: journalArticle
doi: 10.1016/j.jmateco.2007.05.004
zotero: "zotero://select/library/items/BG997WPQ"
pdf: /Users/jesper/Zotero/storage/WIQGGD6W/Ehlers2008.pdf
tags: [literature]
keywords: [revealed-preference, warp, top-cycle, tournament-solutions, choice-theory, cyclic-choice, context-independence]
topics: []
related: [Kalai2002, Loomes1991, Manzini2007, Xu2007]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We propose the following weakened version of WARP: if the decision maker selects an alternative x and rejects another alternative y in some context, he cannot select y and reject x in another context. This axiom is consistent with cyclic choices. It is necessary and sufficient for the choice from every subset A of a (finite) universal set X to coincide with the weak upper-contour set of the transitive closure of some fixed complete relation at some alternative in A. Adding further simple axioms forces the choice from each subset to coincide with the top cycle (in that subset) of some fixed tournament over the universal set.

## Summary
Standard rationality (preference maximization) imposes two regularities that are routinely violated in practice: choices are context-independent and acyclic. Ehlers and Sprumont separate these by weakening the weak axiom of revealed preference (WARP) just enough to permit cyclic choices while still forbidding *unambiguous* context dependence. Their weakened axiom (WWARP) characterizes the class of "upper-class" choice rules, and three further mild conditions pin down the **top-cycle rules**: choosing in each feasible set the top cycle of a fixed tournament. The headline message is that a coherent account of cyclic choice need not invoke multiple preference relations — a single (possibly cyclic) complete binary relation suffices.

## Research question
Can one axiomatically isolate context independence from acyclicity, so that a decision maker may exhibit cyclic choices yet still be "rational" in a single-relation sense? Specifically, what behavioral axiom permits cycles but rules out genuine context dependence, and which choice rules does it characterize? Can additional WARP-implied conditions then force the choice to be the top cycle of a fixed tournament?

## Method / identification
The setting is abstract choice theory à la Arrow (1959): $X$ is a finite universal set with $|X|\ge 3$, $\mathcal{X}$ the nonempty subsets, and a choice rule is a map $f:\mathcal{X}\to\mathcal{X}$ with $\emptyset\neq f(A)\subseteq A$. The full-domain assumption (choice defined on *all* subsets) is used for the tournament results but not for the WWARP characterization itself.

The standard **WARP** says: if $x\in f(A)$ and $y\in A\setminus f(A)$ for some $A$, then there is no $B$ with $y\in f(B)$ and $x\in B$. The authors weaken the conclusion's last clause to require that $x$ be *rejected*:

**WWARP.** If $x\in f(A)$ and $y\in A\setminus f(A)$ for some $A$, then there is no $B$ with $y\in f(B)$ and $x\in B\setminus f(B)$.

WWARP only excludes choices that are *unambiguously* context-dependent. It is consistent with cycles (e.g. choosing only $x$ from $\{x,y\}$, only $y$ from $\{y,z\}$, only $z$ from $\{x,z\}$, but all three from $\{x,y,z\}$).

For a complete relation $R$ on $X$, $\overline{R|_A}$ denotes the transitive closure of the restriction $R|_A$ (which is complete and transitive, and need not equal $R|_X$ restricted). The **weak upper-contour set** is $uc(x,\overline{R|_A})=\{y\in A: y\overline{R|_A}x \text{ or } y=x\}$. A **selection** is $s:\mathcal{X}\to\mathcal{X}$ with $s(A)\in A$. A rule is an **upper-class rule** if there exist $R$ and $s$ with $f(A)=uc(s(A),\overline{R|_A})$ for all $A$.

A **tournament** is a complete, asymmetric $R$. The **top cycle** $t(R|_A)$ is the set of maximal elements of $\overline{R|_A}$ in $A$ — equivalently the unique inclusion-minimal nonempty $C\subseteq A$ with $xRy$ for all $x\in C,\ y\in A\setminus C$ (Lemma 2). The proofs proceed by constructing the revealed relation $xRy\Leftrightarrow \exists A:\ x\in f(A),\ y\in A\setminus f(A)$, showing asymmetry/completeness from the axioms, and using induction on $|A|$ together with the strong superset property (Bordes, 1976).

## Data
None — this is a pure axiomatic / theoretical paper in revealed-preference and tournament theory. The behavioral motivation cites experimental evidence of cyclic and context-dependent choice (Loomes, Starmer & Sugden, 1991; Camerer, 1995).

## Key findings
- **Lemma 1.** A choice rule satisfies WWARP **if and only if** it is an upper-class rule, i.e. $f(A)=uc(s(A),\overline{R|_A})$ for some fixed complete $R$ and selection $s$. The relation $R$ is built as the co-dual of the revealed strict relation $P$, with asymmetry of $P$ delivering completeness and reflexivity of $R$. This characterization survives on arbitrary sub-domains.
- Two WARP-implied conditions are introduced: **Binary dominance consistency (BDC)** — a Condorcet-winner principle: if $f(\{x,y\})=\{x\}$ for all $y\in A\setminus\{x\}$ then $f(A)=\{x\}$; and **weak contraction consistency (WCC)** — $f(A)\subseteq\bigcup_{x\in A}f(A\setminus\{x\})$ (from Lahiri, 2001; weaker than Chernoff's contraction).
- **Theorem 1.** A choice rule is *resolute* and satisfies WWARP, BDC, and WCC **if and only if** it is a top-cycle rule, $f(A)=t(R|_A)$ for a fixed tournament $R$. The four conditions are shown independent via explicit counterexamples.
- **Corollary 1.** Replacing WWARP with the stronger **weak choice axiom (WCA)** (a dual Chernoff condition, Bordes 1976) gives the same top-cycle characterization.
- **Theorem 2.** Dropping resoluteness, $f$ satisfies WCA, BDC, and WCC **if and only if** it is a *weak* top-cycle rule (GETCHA/Schwartz set, $wt(R|_A)$, for a complete possibly-non-asymmetric $R$). WWARP cannot replace WCA here (a counterexample shows WWARP is strictly weaker), but weak top-cycle rules are the *minimal* rules satisfying WWARP: any WWARP rule has $f(A)\supseteq wt(R|_A)$.

## Contribution
The paper cleanly disentangles context independence from acyclicity, showing that the former alone (WWARP) is exactly the property describing upper-class rules, and that a single fixed binary relation — not a collection of preferences — can rationalize cyclic choice. It supplies an "exact" axiomatization of top-cycle choice using only inter-feasible-set properties (no cross-tournament axioms like neutrality), which distinguishes it from the social-choice tradition that obtains only minimality results. It also positions sequential and game-tree rationalizability as refinements of top-cycle rationalizability.

## Limitations & open questions
- The exact (Theorem 1) characterization requires **resoluteness** (singleton choice from pairs); without it one only obtains the weak top-cycle rules via the stronger WCA (Theorem 2), and WWARP alone yields just minimality. Closing the gap between WWARP and an exact non-resolute top-cycle characterization is left open.
- The full-domain assumption is invoked for the tournament results; behavior on restricted/observable domains is not fully characterized beyond Lemma 1.
- The framework is purely structural: it offers no account of *which* tournament or selection a decision maker uses, nor any stochastic/empirical content for estimation.
- Relation to **uncovered-set** rules (Lombardi, 2006) — a refinement of the top cycle that may violate WWARP — is noted but not reconciled.

## Connections
The paper builds directly on Arrow (1959) on rational choice functions and the equivalence of WARP with the choice axiom. The multiple-rationales tradition it argues against includes [[@Kalai2002|Kalai, Rubinstein & Spiegler (2002)]] and [[@Manzini2007|Manzini & Mariotti (2007)]] on sequential rationalizability / rational shortlist methods, as well as the game-theoretic revealed-preference approaches of Ray & Zhou (2001) and [[@Xu2007|Xu & Zhou (2007)]]; the authors show these are refinements of top-cycle rationalizability. The contraction-type axioms derive from Chernoff (1954), Bordes (1976), and Lahiri (2001); Duggan (1997) characterizes WCA via pseudo-rationalizability, of which Lemma 1 is a single-relation analogue. The tournament and top-cycle machinery draws on Moon (1968), Schwartz (1972, 1986), Deb (1977), Kalai, Pazner & Schmeidler (1976), Kalai & Schmeidler (1977), Moulin (1984, 1986), Dutta (1988), Fishburn (1977), Miller (1980), and Laslier (1997). Empirical motivation comes from [[@Loomes1991|Loomes, Starmer & Sugden (1991)]] and Camerer (1995).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
