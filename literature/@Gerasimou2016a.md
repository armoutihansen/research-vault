---
citekey: Gerasimou2016a
title: "Asymmetric dominance, deferral, and status quo bias in a behavioral model of choice"
authors: ["Gerasimou, Georgios"]
year: 2016
type: journalArticle
doi: 10.1007/s11238-015-9499-7
zotero: "zotero://select/library/items/LTZ5PVKE"
pdf: /Users/jesper/Zotero/storage/7SPXJWXR/Gerasimou2016.pdf
tags: [literature]
keywords: [incomplete-preferences, choice-deferral, status-quo-bias, attraction-effect, partial-dominance, revealed-preference, bounded-rationality]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> This paper proposes and axiomatically characterizes a model of choice that builds on the criterion of partial dominance and allows for two types of avoidant behavior: choice deferral and status quo bias. These phenomena are explained in a unified way that allows for a clear theoretical distinction between them to be made. The model also explains the strengthening of the attraction effect that has been observed when deferral is permissible. Unlike other models of status quo biased behavior, the one analyzed in this paper builds on a unique, reference-independent preference relation that is acyclic and generally incomplete. When this relation is complete, the model reduces to rational choice.

## Summary
Gerasimou extends his "partially dominant choice" model to an expanded choice domain (à la Masatlioglu and Ok) in which decision problems may carry a non-specific status quo (deferral is possible) or a specific status quo (a default option $s$). A single, reference-independent, acyclic but generally incomplete strict preference relation $\succ$ governs behavior in both settings. The decision maker chooses an option iff it is undominated and partially dominant (it beats something); when no such option exists he either defers (non-specific status quo) or sticks with the default (specific status quo). The model thereby gives a unified, deterministic account of choice deferral, status-quo/default bias, the strengthening of the attraction (asymmetric-dominance) effect, and the weakening of the compromise effect when deferral is allowed — and collapses to rational utility maximization when $\succ$ is complete.

## Research question
Can choice deferral and status-quo bias — two distinct "avoidant" behaviors usually modeled separately, with reference-dependent preferences or multiple rationales — be derived from a single, reference-independent, incomplete preference relation, and can such a model simultaneously explain the experimentally documented strengthening of the attraction effect (and weakening of the compromise effect) when not choosing is an option?

## Method / identification
The approach is axiomatic decision theory (revealed-preference characterization), not estimation. Let $X$ be a finite set of alternatives and $\mathcal{M}$ its menus. The domain of decision problems $S \subset \mathcal{M}\times\mathcal{M}$ consists of pairs $(A,\diamond)$ — a menu $A$ with a **non-specific** status quo, where deferral is permitted — and $(A,s)$ with $s\in A$ — a menu with a **specific** status quo (default). A choice correspondence $C:S\rightrightarrows X$ satisfies $C(A,p)\subseteq A$, with $C(A,s)\neq\emptyset$ always required but $C(A,\diamond)=\emptyset$ permitted (this empty-set device formalizes deferral).

The central object (Definition 1) is the **Extended Partial Dominance (EPD) procedure**: there is a unique acyclic relation $\succ$ on $X$ such that for all problems,
$$C(A,\diamond)=\{x\in A: z\not\succ x \text{ for all } z\in A \text{ and } x\succ y \text{ for some } y\in A\},$$
$$C(A,s)=\{x\in A\setminus\{s\}: z\not\succ x \text{ for all } z\in A \text{ and } x\succ s\}\ \text{ if nonempty, else } s.$$
Equivalently, deferral occurs exactly when no two options are comparable: $C(A,\diamond)=\emptyset \iff x\not\succ y$ and $y\not\succ x$ for all $x,y\in A$. The default is kept exactly when it is undominated: $C(A,s)=s \iff z\not\succ s$ for all $z\in A$. A striking structural feature is that abandoning the default is itself a *restricted* application of the partial-dominance rule (dominance must hold against $s$ specifically), linking the two phenomena.

Five axioms characterize EPD (Proposition 1): **A1 Bounded Status Quo Bias** (a default cannot overturn strict pairwise preference; an upper bound on bias); **A2 a-WARP** (a weak consistency condition relaxing WARP across problems with the same status quo); **A3 Choice Implies Rejection** (something is always rejected from non-singleton menus); **A4 Restricted Expansion** (a Sen-$\gamma$-type expansion property accommodating deferral); **A5 Partial b-WARP** (choosing $x$ reveals pairwise dominance of $x$ over some rejected option). The preference relation is recovered from binary problems: $x\succ y \iff C(\{x,y\},\diamond)=x$.

## Data
None — this is a pure theory paper. It is, however, calibrated against published experimental findings (Tversky and Shafir 1992; Dhar 1997; Dhar and Simonson 2003; Huber et al. 1982; Knetsch 1989; reported deferral rates of 20–45%), which the model is shown to rationalize qualitatively/deterministically.

## Key findings
**Proposition 1 (representation):** $C$ satisfies A1–A5 if and only if $C$ is generated by an EPD procedure with a unique acyclic $\succ$. **Proposition 2 (rationality as a special case):** $C$ satisfies A0 (Decisiveness: $C(A,\diamond)\neq\emptyset$ always) together with A1–A3 iff there is a unique strict linear order $\succ$ with $C(A,p)=\{x\in A: y\not\succ x \ \forall y\in A\}$ — i.e., standard utility maximization. Under A0, axioms A4 and A5 become redundant. Substantively: (i) deferral is explained purely by incomparability/decision conflict, not undesirability; (ii) the model *rules out* choice-overload-type deferral (adding a partially dominant option to an all-incomparable menu induces choice rather than more deferral); (iii) it gives a deterministic account of the Dhar–Simonson (2003) strengthening of the attraction effect and weakening of the compromise effect under permissible deferral; (iv) status-quo bias arises from incompleteness — the default is kept whenever nothing is revealed-superior to it. Appendix B establishes logical independence of A1–A5.

## Contribution
This is claimed to be the first model to (a) explain choice deferral and status-quo bias in a *unified* way while keeping them theoretically distinct; (b) do so with a *single*, reference-independent, acyclic, generally incomplete preference relation — avoiding multi-valued correspondences (Masatlioglu–Ok 2005), reference-dependent/loss-averse utilities (Tversky–Kahneman 1991; Apesteguia–Ballester 2009), or two separate rationales (a utility $U$ plus a constraint correspondence $Q$ as in Masatlioglu–Ok 2015); and (c) suggest a common behavioral mechanism behind the attraction effect, status-quo bias, and avoidant behavior. It nests rational choice as the complete-preference limit, framing the behavior as "boundedly irrational" rather than irrational.

## Limitations & open questions
The author flags several explicit boundaries. The EPD model is **deterministic**, whereas much attraction/compromise-effect evidence is probabilistic — Gerasimou points to Echenique et al. (2014)'s perception-adjusted Luce (random-choice) model as the stochastic complement. Unlike Tversky–Kahneman, EPD does **not allow non-feasible reference points** to influence choice (it is context-dependent in choices but not in preferences). It deliberately **excludes choice-overload behavior** (more deferral from larger menus), which competing models (Costa-Gomes et al. 2014; Dean 2008) accommodate. A1 places only an *upper bound* on status-quo bias, ruling out preference-overturning biases — whether this is descriptively too strong is left open. The empty-set vs. explicit "no-choice option $d$" modeling debate (Sect. 4.3) is discussed but not resolved: he argues the empty-set approach is right when deferral is conflict-driven and an explicit $d$ is right when it is undesirability-driven, noting preferences can only be elicited *up to a desirability threshold*. Reconciling deterministic and stochastic accounts, and empirically distinguishing incompleteness-driven from overload-driven deferral, are natural follow-ups.

## Connections
The paper builds directly on Gerasimou (2015) "Partially dominant choice" and the expanded-domain framework of Masatlioglu and Ok (2005, 2015). Its incompleteness-based reading of status-quo bias descends from Bewley (2002, Knightian uncertainty) and Mandler (2004). It contrasts sharply with the reference-dependent, loss-aversion tradition of Tversky and Kahneman (1991), Bleichrodt (2007), and Apesteguia and Ballester (2009). On conflict-induced deferral it sits beside Costa-Gomes, Cueva and Gerasimou (2014, "maximally dominant" rule with transitive incomplete preferences), Dean (2008), and Buturak and Evren (2014). The attraction/compromise effects trace to Huber, Payne and Puto (1982) and Simonson (1989), with reason-based interpretations in Shafir, Simonson and Tversky (1993); related bounded-rationality choice models include Lombardi (2009), de Clippel and Eliaz (2012), Ok, Ortoleva and Riella (2015, revealed (p)reference), and the salience model of Bordalo, Gennaioli and Shleifer (2013). The empty-set modeling of deferral connects to Hurwicz (1986), Clark (1995, indecisive choice), and Kreps (2012).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
