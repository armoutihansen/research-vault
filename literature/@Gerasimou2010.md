---
citekey: Gerasimou2010
title: Consumer theory with bounded rational preferences
authors: ["Gerasímou, Georgios"]
year: 2010
type: journalArticle
doi: 10.1016/j.jmateco.2010.08.015
zotero: "zotero://select/library/items/89773BKE"
pdf: /Users/jesper/Zotero/storage/9WV9EFWX/Gerasimou2010.pdf
tags: [literature]
keywords: [incomplete-preferences, intransitive-preferences, preference-representation, consumer-demand, bounded-rationality, warp, ambivalence-aversion]
topics: ["[[incomplete-preferences-choice-deferral]]"]
related: [Manzini2007, Simonson1989]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Building on the work of Shafer (1974), this paper provides a continuous bivariate representation theorem for preferences that need not be complete or transitive. Applying this result to the problem of choice from competitive budget sets allows for a proof of the existence of a demand correspondence for a consumer who has preferences within this class that are also convex. Similarly to the textbook theory of utility maximization, this proof also uses the Maximum Theorem. With an additional mild convexity axiom that conceptually parallels uncertainty aversion, the correspondence reduces to a function that satisfies WARP.

## Summary
Gerasímou rebuilds the two pillars of neoclassical consumer theory — preference representation and demand existence — for a consumer whose strict preference $\succ$ is neither complete nor transitive ("bounded rational" preferences). The key device is a continuous, odd (skew-symmetric) bivariate *preference function* $P:X\times X\to\mathbb{R}$ that fully characterizes strict preference. Maximizing $P$ over competitive budget sets via Berge's Maximum Theorem yields a demand correspondence of maximal (undominated) bundles; a mild "ambivalence aversion" convexity axiom — a choice-theoretic analogue of Schmeidler's uncertainty aversion — collapses it to a single-valued demand function satisfying WARP.

## Research question
Can the textbook existence theory of consumer demand — built on utility maximization plus the Maximum Theorem — be reconstructed when the consumer's preferences violate both completeness and transitivity, the two axioms most challenged by experimental evidence on indecisiveness and inconsistency? And under what additional behavioral condition does the resulting (generically set-valued) demand reduce to a well-behaved, WARP-consistent demand function?

## Method / identification
Purely theoretical (axiomatic decision/demand theory). Primitives: a metric space $X$ with an asymmetric strict relation $\succ$, a reflexive-symmetric indifference $\sim$, and weak preference $\succsim:=\succ\cup\sim$. Completeness and transitivity are *not* assumed. Incompleteness makes the *incomparability* relation $\bowtie:=\{(x,y): x\not\succ y \text{ and } y\not\succ x\}$ nonempty; the author defines the **ambivalence** relation $\hat\sim:=\sim\cup\bowtie$ (reflexive, symmetric), the maximal reflexive-symmetric relation compatible with $\succ$. $\succ$ is *continuous* iff it has an open graph in $X\times X$.

The central construction (Theorem 1) defines, via the product metric $d$,
$$P(x,y):=\begin{cases} d((x,y),\hat\sim) & \text{if } x\succ y \text{ or } x\hat\sim y\\ -d((y,x),\hat\sim) & \text{if } y\succ x \text{ or } y\hat\sim x\end{cases}$$
where $d((x,y),\hat\sim)=\inf_{(w,z)\in\hat\sim} d((x,y),(w,z))$. Open-graph of $\succ$ makes $\hat\sim$ closed, hence $P$ continuous and odd.

For demand, the consumption set is fixed to $X=\mathbb{R}^n_+$, price–income ratios $Y=\mathbb{R}^n_{++}$, and the budget correspondence $B(p)=\{x: px\le 1\}$ (continuous, convex- and compact-valued). Two axioms are imposed: **Axiom 1 (Hemicontinuity)** — upper and lower contour sets $U_\succ(x),L_\succ(x)$ are open; **Axiom 2 (Convexity)** — $U_\succ(x)$ convex. Existence (Theorem 2) is proved by feeding generalized Shafer lemmas into Berge's Maximum Theorem; the appendix uses Weierstrass, Kakutani's fixed-point and Carathéodory's theorems. **Axiom 3 (Ambivalence Aversion)** delivers single-valuedness: if $x\hat\sim y$ then some convex combination $z=\alpha x+(1-\alpha)y$ satisfies $z\succ x$ or $z\succ y$.

## Data
None — this is a pure theory paper. It cites experimental/behavioral evidence (Anderson 2003; Kivetz & Simonson 2000; Simonson's 1989 compromise effect; Ellsberg-type findings) only as motivation, not as data analyzed.

## Key findings
- **Theorem 1 (representation).** $\succ$ on a metric space $X$ is asymmetric and continuous iff there exists a continuous $P:X\times X\to\mathbb{R}$, unique up to odd strictly-increasing transformations, with $P(x,y)>0\Leftrightarrow x\succ y$, $P(x,y)=0\Leftrightarrow x\hat\sim y$, and $P(x,y)=-P(y,x)$. This generalizes Shafer (1974) (who kept completeness) to incomplete preferences and supersedes Vind's (1991) definition of a preference function.
- **Theorem 2 (demand correspondence).** Under Axioms 1–2 there is an upper-hemicontinuous, nonempty, compact-valued $x:Y\rightrightarrows X$ with $x(p)=\{x\in B(p): P(x,y)\ge 0\ \forall y\in B(p)\}$ — the maximal elements. The proof builds a price-dependent $h(p,x)=\min\{P(x,y):y\in B(p)\}$ whose maximizers coincide with $\succ$-maximal bundles; the optimal-value function $m(p)\equiv 0$, so it cannot serve as an "indirect utility."
- **Corollary 1 (WARP diagnosis).** If choices over two budgets violate WARP via $x,y$, then necessarily $x\hat\sim y$: violations are *caused by ambivalence* (indifference or incomparability).
- **Theorem 3 (demand function + WARP).** Under Axioms 1–3 the correspondence is single-valued, yielding a continuous demand function that satisfies WARP. Notably, this needs neither budget-exhaustion nor local non-satiation (unlike Shafer 1975).

## Contribution
Provides the first tractable, single-function representation that *fully characterizes* strict preference without completeness or transitivity, and shows it dominates weak-utility (Peleg 1970), the Shafer–Sonnenschein non-negative distance function, and multi-utility (Kochov 2007; Evren & Ok 2007) representations on the joint criteria of generality, tractability, and characterization of $\succ$. It re-derives Sonnenschein's (1971) demand-existence result through a neoclassical-style "maximize a function + Maximum Theorem" argument, and introduces *ambivalence aversion* as a behaviorally interpretable selection axiom paralleling Schmeidler's (1989) ambiguity aversion, linking it to the compromise effect.

## Limitations & open questions
- The single-valued demand requires Axiom 3; without it, behavior is genuinely set-valued and WARP fails in general — the welfare/comparative-statics content of the correspondence is left open.
- The "indirect utility" function $m(p)\equiv 0$ is degenerate, so standard duality (Roy's identity, etc.) has no obvious analogue here — an open structural gap.
- The ice-cream / computer narratives motivating ambivalence aversion involve indivisible alternatives where no convex combinations strictly exist; the author concedes these are heuristics, not formal examples, leaving empirical testability of the axiom open.
- Continuity is via open-graph of $\succ$; the author flags (citing his own "On continuity of incomplete preferences," 2010) that closed-graph preorder continuity raises separate difficulties — relating the two notions is unresolved.
- Uniqueness of $P$ is only up to odd-monotonic transformations (richer than Fishburn's 1982 skew-symmetric bilinear case), so cardinal/measurement content of $P$ is not pinned down.

## Connections
The direct lineage is Shafer (1974) "The nontransitive consumer," whose constructive distance representation (for complete-but-intransitive preferences) is generalized here, and Sonnenschein (1971), whose demand-existence result (also noted by Mas-Colell 1974 and Kim & Richter 1986) is re-proved. Alternative representations contrasted are Peleg (1970) weak utility, Shafer & Sonnenschein (1975) and Bergstrom, Parks & Rader (1976) on open-graph preferences, and the multi-utility theorems of Evren & Ok (2007) and Kochov (2007); Vind (1991) and Fishburn (1982, nontransitive measurable utility) supply earlier bivariate notions. The ambivalence-aversion axiom is explicitly modeled on Schmeidler's (1989) uncertainty aversion and connects to Ellsberg-paradox behavior. The WARP/SARP rationalizability angle relates to Shafer (1975) and Quah (2006) on weak axiomatic demand. The behavioral motivation draws on [[@Simonson1989|Simonson (1989)]] compromise effect, Kivetz & Simonson (2000), and Anderson (2003). More broadly this sits alongside the incomplete-preference program (Aumann; Dubra–Maccheroni–Ok expected multi-utility) and bounded-rationality choice models in the spirit of [[@Manzini2007|Manzini & Mariotti (2007)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
