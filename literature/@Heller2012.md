---
citekey: Heller2012
title: Justifiable choice
authors: ["Heller, Yuval"]
year: 2012
type: journalArticle
doi: 10.1016/j.geb.2012.07.001
zotero: "zotero://select/library/items/9NVMEYSS"
pdf: /Users/jesper/Zotero/storage/JIYYE3EH/Heller2012.pdf
tags: [literature]
keywords: [justifiable-choice, incomplete-preferences, multiple-utility, multiple-priors, menu-effects, revealed-preference, axiomatic-choice-theory]
topics: ["[[sequential-rationalizability-shortlists]]"]
related: [Bernheim2009, Eliaz2006, Kalai2002, Manzini2007, Salant2008, Sen1971, Simonson1992, Tversky1974]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Most existing decision-making models assume that choice behavior is based on preference maximization even when the preferences are incomplete. In this paper we study an alternative approach – "justifiable choice": each agent has several preference relations ("justifications"), and she can use each justification in every choice problem. We present a new behavioral property that requires an alternative to be chosen if it is not inferior to all mixtures of chosen alternatives, and show that this property characterizes justifiable choice. The main application of this property yields a multiple-utility representation, which substantially differs from existing related representations. In addition, we obtain a multiple-prior representation, and study the notions of indecisiveness and being more decisive.

## Summary
Heller models choice under incomplete preferences not as maximization of one incomplete relation but as *justifiable choice*: the agent holds a set of complete preference relations ("justifications" / rationales), and payoff-irrelevant information selects which one is used in a given problem; an alternative is choosable if it is best under at least one justification. He introduces a single behavioral axiom — the Convex Axiom of Revealed Non-Inferiority (CARNI) — and proves that, together with standard von Neumann–Morgenstern (vN-M) axioms, it characterizes a multiple-utility representation in which $q$ is chosen iff some utility ranks it weakly best in the menu. An Anscombe–Aumann analogue delivers a multiple-prior representation. The model accommodates menu effects (a binary facet of the tradeoff contrast effect) while staying close to WARP and retaining normative appeal.

## Research question
Once the completeness axiom is dropped, why should preference maximization remain the criterion of rational choice? Specifically: what behavioral property characterizes a decision maker who chooses by selecting the best alternative under *one of several* complete rationales (rather than maximizing a single incomplete relation), and what representation does this yield?

## Method / identification
Axiomatic decision theory. The primitive is a choice correspondence $C$ on $\mathcal{Y}$, the closed non-empty subsets of $Y=\Delta(X)$ (lotteries over a finite outcome set $X$); $C(A)$ is the non-empty set of choosable alternatives in $A$.

The central axiom relaxes Eliaz & Ok's WARNI by referring to *mixtures*. Say $q$ is revealed not inferior to $r$ if $q\in C(B)$ for some $B$ with $r\in\mathrm{conv}(B)$. Then:

**CARNI (A4).** Let $q\in A$. If for every $r\in\mathrm{conv}(C(A))$ there is $B$ with $q\in C(B)$ and $r\in\mathrm{conv}(B)$, then $q\in C(A)$.

This is imposed alongside three standard axioms: non-triviality (A1), continuity (A2), and independence (A3). The proof strategy mirrors Eliaz & Ok to obtain
$$q\in C(A)\iff \forall r\in\mathrm{conv}(A),\ \exists u_r\in U,\ u_r(q)\ge u_r(r),$$
rewrites it as $\min_{r\in\mathrm{conv}(A)}\max_{u\in U}\,[u(q)-u(r)]\ge 0$, and — because both $U$ and $\mathrm{conv}(A)$ are convex and the utilities are linear — applies the **minimax theorem** to swap the operators, yielding $\exists u\in U\ \forall r,\ u(q)\ge u(r)$. The convexity baked into CARNI is exactly what licenses the quantifier reversal that turns "best against *some* utility for each rival" into "best against *one fixed* utility."

For uncertainty, the Anscombe–Aumann framework is used: acts $L=Y^S$ over finite states $S$, with axioms B0–B4 (adding monotonicity B0). The same minimax logic delivers a single-prior selection condition.

A companion taxonomy (Fig. 2) decomposes the axioms via Sen's $\alpha,\beta,\gamma$, a new *Convex $\gamma$*, the Aizerman property, and Seidenfeld et al.'s Mixture Invariance.

## Data
None — this is a pure theory paper. The descriptive motivation invokes the experimental tradeoff-contrast literature (Simonson & Tversky), and the author notes separate experimental evidence in Heller (2010) for a moderate contrast effect over lotteries, but no data are analyzed here.

## Key findings
- **Theorem 1 (risk).** $C$ satisfies A1–A4 iff there is a convex compact set $U$ of vN-M utilities, unique up to positive linear transformations, with a non-triviality condition, such that $q\in C(A)\iff \exists u\in U\ \text{s.t.}\ \forall r\in A,\ u(q)\ge u(r)$. An alternative is choosable iff it *maximizes one* of the utilities.
- **Theorem 2 (uncertainty).** $C$ satisfies B0–B4 iff there is a non-constant utility $u$ and a closed convex set of priors $P\subseteq\Delta(S)$, both unique (up to positive linear transformations of $u$), with $f\in C(A)\iff \exists p\in P\ \text{s.t.}\ \forall g\in A,\ E_p[u(f)]\ge E_p[u(g)]$.
- **Contrast with [[@Eliaz2006|Eliaz & Ok (2006)]].** Their WARNI yields $q\in C(A)\iff \forall r\ \exists u_r,\ u_r(q)\ge u_r(r)$ — allowing $q$ to be chosen via *conflicting* rationales (best vs. $r$ under $u_1$, best vs. $r'$ under $u_2$) without maximizing any utility. CARNI rules this out: choice requires a single justifying utility. Example 1 (beef/chicken, near/far) is consistent with CARNI but violates WARNI.
- **Menu effects.** CARNI is logically independent of WARP/WARNI; a CARNI choice correspondence is generally inconsistent with preference maximization (it satisfies Sen's $\alpha$ and *Convex* $\gamma$ but not Sen's $\gamma$), so it accommodates the menu effects that Manzini & Mariotti (2010) found to drive WARP violations. WARP $+$ Mixture Invariance implies CARNI; CARNI decomposes into Sen's $\alpha$, Convex $\gamma$, Aizerman, and Mixture Invariance.
- **Indecisiveness (Sec. 3).** A two-part revealed psychological preference $\succ^*$ (parts I and II of Eq. 5) is defined; part II refines Bernheim & Rangel's (2009) relation into a transitive one. Proposition 1 shows $q\succ^* r\iff \forall u\in U,\ u(q)\ge u(r)$. Preferences are complete iff $U$ (resp. $P$) is a singleton (Lemmas 1–2). "More decisive" is characterized: Alice is more decisive than Bob iff $U_A$ is a singleton, or $U_A\subseteq U_B$, or $U_A\subseteq -U_B$ (Prop. 2; analogue Prop. 4 for priors). Hence an incomplete-preference agent who is more decisive than another must be either fully-consistent or fully-inconsistent with him (Corollaries 2, 4).

## Contribution
A new, single, normatively motivated axiom (CARNI) that characterizes justifiable choice and supplies multiple-utility and multiple-prior representations differing essentially from Eliaz & Ok's: choosability requires maximizing *one* rationale, not piecing together conflicting ones. The model is the first in this family to (i) impose structure on rationales using lottery/act data (convex, closed sets of affine preorders), (ii) accommodate an interesting menu effect while keeping a small, principled deviation from WARP, and (iii) deliver a transitive revealed-psychological-preference notion plus a clean characterization of comparative decisiveness applicable to other incomplete-preference models.

## Limitations & open questions
- CARNI captures only a *binary* facet of the tradeoff contrast effect; it does *not* capture the attraction effect or the compromise effect (de Clippel & Eliaz, 2012, model those).
- The descriptive appeal is limited: experimental evidence for the tradeoff contrast effect concerns multi-attribute products, whereas the model applies it to lotteries; supporting lottery evidence (Heller, 2010) is only "moderate."
- The process by which payoff-irrelevant information selects a justification (framing, availability, anchoring) is *not* explicitly modeled — left as a black box.
- $X$ is taken finite for simplicity; extension to compact metric outcome spaces is noted as feasible (via Evren, 2010; Gilboa et al., 2010) but not carried out.

## Connections
Builds directly on [[@Eliaz2006|Eliaz & Ok (2006)]], whose WARNI and multiple-utility representation are the closest antecedent and the main foil. The justifiable-choice notion follows Lehrer & Teper (2011); the multiple-utility flavor echoes the non-axiomatic representation of Levi (1974). The uncertainty model uses Anscombe & Aumann (1963) (via Fishburn, 1970) and Savage (1954), and its WARNI benchmark coincides with Knightian preferences à la Bewley (2002). The minimax step is in the spirit of Gilboa & Schmeidler (1989). On incomplete preferences and multiple rationales it connects to Aumann (1962), Dubra, Maccheroni & Ok (2004), Nehring (1997), [[@Kalai2002|Kalai, Rubinstein & Spiegler (2002)]], Mandler (2005), [[@Manzini2007|Manzini & Mariotti (2007)]], [[@Salant2008|Salant & Rubinstein (2008)]], and Cherepanov, Feddersen & Sandroni (2010); the empirical menu-effect motivation is Manzini & Mariotti (2010). Descriptively it draws on [[@Simonson1992|Simonson & Tversky]] (1992, 1993) and [[@Tversky1974|Tversky & Kahneman]] (1974, 1981). The axiom taxonomy uses [[@Sen1971|Sen (1971)]], Aizerman & Malishevski (1981), Chernoff (1954), and Seidenfeld, Schervish & Kadane (2010); the revealed-psychological-preference comparison is with [[@Bernheim2009|Bernheim & Rangel (2009)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
