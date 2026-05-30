---
citekey: Gerasimou2018
title: "Indecisiveness, Undesirability and Overload Revealed Through Rational Choice Deferral"
authors: ["Gerasimou, Georgios"]
year: 2018
type: journalArticle
doi: 10.1111/ecoj.12500
zotero: "zotero://select/library/items/GSL38PZY"
pdf: /Users/jesper/Zotero/storage/97VJE3C8/Gerasimou2018.pdf
tags: [literature]
keywords: [choice-deferral, incomplete-preferences, revealed-preference, choice-overload, bounded-rationality, axiomatic-choice-theory]
topics: []
related: [Bernheim2009, Eliaz2006, Gerasimou2016a, Iyengar2000, Manzini2007, Salant2008, Samuelson1938, Samuelson1988, Sen1971, Shafir1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Three reasons why decision-makers may defer choice are indecisiveness between various feasible options, unattractiveness of these options and choice overload. This article provides a choice-theoretic explanation for each of these phenomena by means of three deferral-permitting models of decision-making that are driven by preference incompleteness, undesirability and complexity constraints, respectively. These models feature rational choice deferral in the sense that whenever the individual does not defer, he chooses a most preferred feasible option. Active choices are therefore always consistent with the Weak Axiom of Revealed Preference. The three models suggest novel ways in which observable data can be used to recover preferences as well as their indecisiveness, desirability and complexity components or thresholds.

## Summary
Gerasimou provides revealed-preference (axiomatic) foundations for three distinct reasons a decision-maker might decline to choose any feasible market option and instead opt for an unmodelled outside option ("defer"): indecisiveness (incomplete preferences), undesirability (all options below a desirability threshold), and choice overload (menu too complex). The unifying theme is *rational* deferral: deferral never reflects inconsistent or context-dependent preferences, and whenever the agent does make an active choice it maximizes a stable, menu-independent (pre)order and so satisfies WARP. Each source of deferral is characterized by a distinct, falsifiable set of axioms on observable choice-and-deferral data, and each yields a different degree to which preferences and the relevant threshold can be recovered.

## Research question
When an agent's status quo is a *non-market outside option* (e.g. remaining uninsured) rather than a concrete feasible alternative, choosing "nothing" is a deferral rather than a choice of a feasible option. What observable axioms characterize the three leading behavioral explanations for such deferral — indecisiveness, undesirability, overload — and what can each reveal about the agent's underlying preferences and thresholds?

## Method / identification
Pure revealed-preference / axiomatic choice theory on a finite alternative set $X$ with menu collection $\mathcal{M}$ (all subsets) and a possibly multi- and empty-valued choice correspondence $C:\mathcal{M}\to\mathcal{M}$ with $C(A)\subseteq A$. The interpretive innovation is that $C(A)=\varnothing$ is read as deferral to the outside option, so the usual **Non-emptiness** assumption is dropped and treated as an explicit axiom. The applicable consistency principle is a Samuelson-style **WARP**: if $x\in C(A)$, $y\in A\setminus C(A)$ and $y\in C(B)$, then $x\notin B$. Because Non-emptiness is not imposed, axioms that are normally equivalent (Contraction Consistency, Strong Expansion / Sen's property $\gamma$, WARP) become logically distinct, and the paper exploits these separations. Each model is a representation theorem (necessary and sufficient axioms), with proofs and tightness shown in appendices. Writing $B_\succeq(A):=\{x\in A: x\succeq y\ \forall y\in A\}$ for the set of greatest elements:

- **MDC (indecisiveness):** characterized by **Desirability** ($C(\{x\})=\{x\}$), **Contraction Consistency**, and **Strong Expansion**. Representation: a unique preorder $\succeq$ (transitive, possibly incomplete) with $C(A)=B_\succeq(A)$ if non-empty, else $\varnothing$.
- **DCR (undesirability):** characterized by **WARP**, **Contraction Consistency**, **Undesirability** ($\exists x: C(\{x\})=\varnothing$), and **Contractive Undesirability** ($C(A)=\varnothing,\ B\subset A\Rightarrow C(B)=\varnothing$). Representation: a weak order $\succeq$ (utility $u$) and a threshold alternative $x^\ast$ with $C(A)=\arg\max_{x\in A}u(x)$ if $\max_{x\in A}u(x)>u(x^\ast)$, else $\varnothing$.
- **OCR (overload):** characterized by **Desirability**, **WARP**, **Deferral Monotonicity** ($B\supset A\neq\varnothing,\ C(A)=\varnothing\Rightarrow C(B)=\varnothing$, *novel*), and **Binary Choice Consistency**. Representation: a complexity function $w:\mathcal{M}\to\mathbb{R}$ (monotone in set inclusion) and integer threshold $n$ with $C(A)=\arg\max_{x\in A}u(x)$ if $w(A)\le n$, else $\varnothing$; when $w(A)=|A|$ this is a simple menu-size cutoff.

## Data
None — this is a theory paper. It cites lab and field evidence ([[@Iyengar2000|Iyengar & Lepper 2000]]; Tversky & Shafir 1992; Dhar & Sherman 1996; Costa-Gomes et al. 2016; Chernev et al. 2015 meta-analysis) to motivate the models, but estimates nothing.

## Key findings
- **Proposition 1 (MDC).** Desirability + Contraction Consistency + Strong Expansion $\iff$ maximally-dominant-choice representation by a unique preorder. The agent chooses the (set of) greatest element(s) when one exists and defers when his incomplete preferences leave no most-preferred option.
- **Novel indifference-vs-indecisiveness criterion.** Under MDC, $x$ and $y$ are revealed *indifferent* iff both are always choosable whenever both feasible and one is chosen; revealed *indecisive* iff neither is ever chosen in the other's presence. This is the first behavioral split between indifference and indecisiveness that applies to WARP-consistent agents with incomplete preferences and needs no a priori "regularity" restriction (contrast [[@Eliaz2006|Eliaz & Ok 2006]], whose indecisiveness criterion forces a WARP violation). The MDC revealed-incomparability relation coincides with non-comparability under the [[@Bernheim2009|Bernheim–Rangel (2009)]] revealed-preference relation.
- **Proposition 2 (DCR).** The four DCR axioms $\iff$ desirability-constrained utility maximization with threshold $x^\ast$; $\succeq$ is quasi-rationalized uniquely up to $x^\ast$. Preferences are *almost* fully recoverable — everything above the threshold is pinned down; the ranking among undesirable (never-chosen) options is unrecoverable. The threshold $x^\ast$ is generally infeasible yet shapes behavior, paralleling reference-dependent loss aversion (Tversky & Kahneman 1991).
- **Proposition 3 (OCR).** The four OCR axioms $\iff$ overload-constrained utility maximization $(w,n)$, with $u$ and $(w,n)$ unique up to strictly increasing transformations. Recovery of preferences is only *partial*: pairs that are too complex to ever appear in a non-deferred menu remain unranked.
- **Choice overload, two mechanisms.** MDC explains overload via growing incompleteness (more options $\Rightarrow$ more incomparable pairs $\Rightarrow$ no dominant option) *and* explains its breakdown when a dominant option is inserted into a large menu. OCR explains overload via a complexity cutoff but *cannot* explain that breakdown — distinguishing the two theories empirically.
- A two-period extension of MDC (Appendix B) supplies choice-theoretic foundations for Bewley (2002) "objectively rational" incomplete preferences under uncertainty.

## Contribution
Supplies the first unified axiomatic taxonomy that separates three behaviorally and economically distinct sources of choice deferral, each with falsifiable foundations and explicit preference/threshold recovery. It shows that deferral need not signal irrationality: by reinterpreting empty-valued choice as an outside option and limiting WARP to active choices, standard rationality (full WARP consistency of chosen options) coexists with deferral. It also delivers the new indifference/indecisiveness criterion and links the framework to Bewley preferences, reference dependence, and Simon's bounded-rationality program.

## Limitations & open questions
- **Menu-independent thresholds.** DCR and OCR both impose context-independent desirability/complexity criteria; the paper explicitly notes that context-dependent undesirability (Dhar & Sherman 1996, where framing of good/bad features flips deferral) violates these axioms and flags such models as a benchmark-relative extension.
- **Deferral Monotonicity can fail descriptively** when a clearly superior option overrides complexity; defended only on normative cost-benefit grounds.
- **Partial recoverability** under OCR (and the unranked undesirable tail under DCR) leaves open how to identify the full preorder.
- **Modelling the outside option explicitly** (Section 6) and the static-vs-dynamic interpretation of deferral are raised as further directions; the WARP restriction to active choices presumes choices across decisions may violate it.
- Empirical implementation across the suggested domains (choice datasets with deferral, IO, robust social choice, choice under uncertainty) is left to future work.

## Connections
Builds directly on incomplete-preference choice theory — [[@Eliaz2006|Eliaz & Ok (2006)]] on revealed indecisiveness, Mandler (2009) and Danan (2010) on indifference vs. indecisiveness via sequential trades and money pumps, and Bewley (2002) on objectively rational preferences. The revealed-preference machinery extends [[@Samuelson1938|Samuelson (1938)]], [[@Sen1971|Sen]] (1971, property $\gamma$), [[@Salant2008|Salant & Rubinstein]] (2008, property $c+$ / Strong Expansion), and the model-free relation of [[@Bernheim2009|Bernheim & Rangel (2009)]]. It sits beside status-quo and reference-dependence models — [[@Samuelson1988|Samuelson & Zeckhauser (1988)]], Knetsch (1989), Tversky & Kahneman (1991), Masatlioglu & Ok (2005, 2015), Apesteguia & Ballester (2009, 2013), Ortoleva (2010), [[@Gerasimou2016a|Gerasimou (2016)]] — and the bounded-rationality tradition of Simon (1957) and Miller (1956). Motivating evidence comes from Tversky & Shafir (1992), [[@Shafir1993|Shafir et al. (1993)]], Dhar & Sherman (1996), [[@Iyengar2000|Iyengar & Lepper (2000)]], Chernev et al. (2015), and Costa-Gomes et al. (2016). The "menu-dependent attention/consideration" agenda of [[@Manzini2007|Manzini & Mariotti (2007)]] and related limited-attention models offer a contrasting account of why options go unchosen.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
