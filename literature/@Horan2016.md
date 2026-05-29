---
citekey: Horan2016
title: A simple model of two-stage choice
authors: ["Horan, Sean"]
year: 2016
type: journalArticle
doi: 10.1016/j.jet.2016.01.002
zotero: "zotero://select/library/items/Z23APJVF"
pdf: /Users/jesper/Zotero/storage/J9M27C42/Horan2016.pdf
tags: [literature]
keywords: [bounded-rationality, shortlist-methods, revealed-preference, axiomatization, choice-reversals, two-stage-choice, context-effects]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> I provide choice-theoretic foundations for a simple two-stage model, called transitive shortlist methods, where choices are made by sequentially by applying a pair of transitive preferences (or rationales) to eliminate inferior alternatives. Despite its simplicity, the model accommodates a wide range of choice phenomena including the status quo bias, framing, homophily, compromise, and limited willpower. I establish that the model can be succinctly characterized in terms of some well-documented context effects in choice. I also show that the underlying rationales are straightforward to determine from readily observable reversals in choice. Finally, I highlight the usefulness of these results in a variety of applications.

## Summary
Horan axiomatizes the *transitive shortlist method* (TSM): a boundedly-rational decision maker who sequentially maximizes a pair $(P_1,P_2)$ of transitive (but possibly incomplete) "rationales", first shortlisting the $P_1$-maximal alternatives and then picking the unique $P_2$-maximum. The central insight is that the entire model is pinned down by a single behavioral axiom, **Strong Exclusivity**, which forbids a menu from simultaneously exhibiting two empirically prevalent context effects (the *attraction effect* and *limited-attention* style reversals) for the same pair of alternatives. The two rationales are shown to be cleanly identified from "small-menu" choice reversals, and the framework unifies and re-characterizes a family of two-stage models (RSM, $T_1$SM, $T_2$SM, transitive RSM) along a single exclusivity dimension.

## Research question
Can the two-stage shortlisting model with *two transitive rationales* be given choice-theoretic foundations in terms of *interpretable, directly observable* behavior, rather than the opaque acyclicity conditions (SARP-like) used in prior work? And can the underlying rationales be uniquely recovered from choice data collected on small menus, so the model is usable in applications?

## Method / identification
The primitive is a single-valued choice function $c:2^X\to X$ on a finite domain $X$. A *rationale* $P$ is an asymmetric binary relation; a TSM is a pair of transitive rationales (quasi-transitive preferences) inducing
$$c_{(P_1,P_2)}(B)\equiv\max(\max(B;P_1);P_2)\quad\text{for all }B\subseteq X,$$
where $\max(A;P)\equiv\{x\in A:\text{no }y\in A\text{ s.t. }yPx\}$.

The analysis is built on two canonical *choice reversals* that violate IIA. A **direct** $x,y$ reversal: $c(B)=y$ but $c(B\cup\{x\})\notin\{x,y\}$ (the attraction effect). A **weak** $x,y$ reversal: $c(x,y)=x$ yet $c(B)=c(B\setminus\{y\})$ for $B\supseteq\{x,y\}$ (limited attention). Theorem 1 shows IIA fails iff *both* reversal types appear. The key construct is an **indirect** $x,y$ reversal — a configuration $c(B)=y$, $c(B\cup\{x\})=x$, $c(B\cup\{w,x\})=w$, $c(B\cup\{w\})=z\notin\{y,w\}$ — in which the alternative $x$ "obscures" that $w$ directly reverses $y$; equivalently, a chain of three connected weak reversals.

**Strong Exclusivity**: for every pair $x,y$, either (i) $c$ displays no weak $x,y$ reversal, or (ii) $c$ displays no direct *or indirect* $x,y$ reversal. Identification rests on revealed rationales defined purely from 3-cycles and overlapping 3-cycles (Definition 1): $xR_1^c y$ and $xR_2^c y$, with $P_i^c\equiv\operatorname{tc}(R_i^c)$ the transitive closures. The proofs (Appendix A) reduce sufficiency of Strong Exclusivity to showing the revealed second-rationale relation $R_2^c$ is acyclic, exploiting a **"small-menu" feature**: choices on pairs and 3-cycles determine all behavior (Corollary 1).

## Data
None — this is a pure decision-theory / revealed-preference paper. There is no empirical dataset; "data" means abstract choice functions. The applications (monopolistic screening, implementation, house allocation) are theoretical illustrations, not estimations.

## Key findings
- **Theorem 1**: IIA $\iff$ no direct reversals $\iff$ no weak reversals.
- **Lemmas 1–3**: among RSM-representable $c$, Exclusivity $\iff$ transitivity of $P_1$ ($T_1$SM); Strong Exclusivity $\iff$ transitivity of both ($T$SM); and, given Expansion, Weak Exclusivity $\iff$ Manzini–Mariotti's Weak WARP.
- **Theorem 2** (characterization): $c$ is TSM-representable $\iff$ it satisfies **Expansion** (Sen's $\gamma$) **and Strong Exclusivity**.
- **Theorem 3** (revealed preference): $xP_i^c y$ iff $xP_i y$ in *every* TSM-representation — the revealed rationales capture exactly the choice-relevant content.
- **Theorem 4**: large-menu reversals reduce to small-menu ones — $xR_1^c y$ iff a direct/indirect reversal occurs; $x\widehat{R}_2^c y$ iff a weak reversal occurs ($\widehat{R}_2^c$ handling irreducible weak reversals, with $\operatorname{tc}(\widehat{R}_2^c)=P_2^c$).
- **Theorem 5** (representation class): $(P_1,P_2)$ represents $c$ iff $P_1^c\subseteq P_1\subseteq\widehat{Q}_1^c$ and $P_2\supseteq\operatorname{tc}(\succeq^c\setminus P_1)$ — exposing a conservative/liberal trade-off between the two rationales and characterizing *minimal* representations.
- **Theorem 6**: $T_1$SM $\iff$ Expansion + Exclusivity; RSM $\iff$ Expansion + Weak Exclusivity — a unified exclusivity ladder.
- **Theorem 7** (testability): for RSM-representable $c$, Strong Exclusivity $\iff$ $\widehat{R}_2^c$ is quadruple-acyclic; Exclusivity $\iff$ triple-acyclic — testing needs only one reversal type, on small menus, over "short" cycles.
- **Applications**: Remark 1 characterizes the extreme-status-quo model via "ESQ Exclusivity"; Remark 2 shows framing and compromise models display no indirect reversals; Remark 3 shows that with biased TSM consumers $(P_1,P_2^i)$ the optimal screening menu contains at most one decoy product.

## Contribution
The paper replaces the technical $R_2^c$-acyclicity conditions of prior TSM characterizations (Au–Kawai, Lleras et al., Yildiz) with a single, interpretable axiom grounded in two well-documented context effects, and shows the rationales are recoverable from readily observable small-menu reversals. By recasting RSM, $T_1$SM, and $T$SM as successive strengthenings of an *exclusivity* requirement, it offers a unified comparative lens on shortlist methods — analogous to how independence conditions organize models of choice under uncertainty. The identification and testability results (small-menu, single-reversal-type, short-cycle) make the model practically usable, which the author leverages to derive non-parametric features of optimal contracts and mechanisms.

## Limitations & open questions
- The TSM model rules out **multi-valued choice** (single-valued $c$ throughout); accommodating it requires dropping totality assumptions per application.
- **Theorem 5's representation trade-off** forces the analyst to take a position on assigning preferences not in either revealed rationale — viewed as a possible shortcoming when no application pins down the interpretation.
- The $T_2$SM model **lacks the small-menu feature**, so whether it admits a "simple" exclusivity characterization (rather than acyclicity) is left open.
- For the more general RSM model, identification may require observing choices from **arbitrarily large menus** — a sharp contrast highlighting what transitivity buys.
- Open application threads: extending Salant–Siegel screening results using the framing-model insights; systematically checking Korpela/de Clippel's *Weak* $\mu$ implementation condition for TSM agents; and characterizing the outcomes of serial dictatorship vs. top trading cycles (Bade) when agents are TSM-rational.
- Computational caveat: tested *on its own* (not jointly with Expansion/Weak WARP), Strong Exclusivity's complexity is comparable to the acyclicity conditions it replaces — its testing advantage is conditional.

## Connections
Directly extends Manzini and Mariotti (2007) *rational shortlist methods* (RSM), reusing their Expansion + Weak WARP characterization and the Weak WARP $\leftrightarrow$ Weak Exclusivity bridge; the TSM model itself was suggested in Manzini and Mariotti (2006). It supersedes the acyclicity-based TSM characterizations of Au and Kawai (2011), Lleras et al. (2011), and Yildiz (2015), and complements Matsuki and Tadenuma (2013) ($T_1$SM via "Elimination") and Houy (2008) ($T_2$SM). The revealed-preference results build on Dutta and Horan (2015) for the RSM model. The behavioral phenomena it organizes trace to the attraction effect (Huber, Payne, Puto 1982) and limited attention (Masatlioglu, Nakajima, Ozbay 2012). Applications connect to Apesteguia and Ballester (2013) and Masatlioglu–Ok (2005) on status quo, Salant and Siegel (2013) on framing, Cuhadaroglu (2015) on homophily, Chandrasekher (2015) on compromise, Masatlioglu et al. (2011) on willpower, and to Spiegler's and Koszegi's programs of embedding bounded rationality in industrial organization and contract theory, plus Korpela (2012), de Clippel (2014), and Bade (2008, 2013) on implementation. The historical roots of shortlist methods are credited to Soviet mathematicians (Aizerman 1985).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
