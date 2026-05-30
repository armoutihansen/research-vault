---
citekey: Bernheim2009
title: "Beyond Revealed Preference: Choice-Theoretic Foundations for Behavioral Welfare Economics"
authors: ["Bernheim, B. Douglas", "Rangel, Antonio"]
year: 2009
type: journalArticle
doi: 10.1162/qjec.2009.124.1.51
zotero: "zotero://select/library/items/VC2HEA7N"
pdf: /Users/jesper/Zotero/storage/LUZUE8JE/Bernheim2009.pdf
tags: [literature]
keywords: [behavioral-welfare-economics, revealed-preference, choice-theory, time-inconsistency, pareto-efficiency, libertarian-paternalism]
topics: []
related: [Iyengar2000, Kahneman1997, Salant2008, Thaler2003]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We propose a broad generalization of standard choice-theoretic welfare economics that encompasses a wide variety of nonstandard behavioral models. Our approach exploits the coherent aspects of choice that those positive models typically attempt to capture. It replaces the standard revealed preference relation with an unambiguous choice relation: roughly, x is (strictly) unambiguously chosen over y (written xP*y) iff y is never chosen when x is available. Under weak assumptions, P* is acyclic and therefore suitable for welfare analysis; it is also the most discerning welfare criterion that never overrules choice. The resulting framework generates natural counterparts for the standard tools of applied welfare economics and is easily applied in the context of specific behavioral theories, with novel implications. Though not universally discerning, it lends itself to principled refinements.

## Summary
Bernheim and Rangel build a welfare framework for behavioral economics that stays anchored in choice rather than in any postulated "true" or "experienced" utility. The trick is to keep welfare comparisons only where choice is unambiguous: $x$ is judged better than $y$ iff $y$ is never chosen whenever $x$ is available. This "unambiguous choice relation" $P^{*}$ is acyclic (hence usable for welfare analysis) even when behavior violates every standard axiom, it is the most discerning criterion that never overrules a choice, and it reduces to ordinary revealed preference when choices are consistent. The paper then rebuilds compensating variation, consumer surplus, Pareto optimality, and the first welfare theorem on this foundation, shows that small anomalies imply small welfare errors, and lays out principled ways to refine (sharpen) the criterion by pruning suspect choice situations.

## Research question
How can applied welfare economics be conducted for agents whose behavior departs from standard rationality (framing effects, status-quo bias, anchoring, time inconsistency) *without* committing to a contested notion of true/experienced utility, and *without* abandoning choice as the normative foundation? Equivalently: what is the right generalization of revealed preference when choices conflict?

## Method / identification
The paper is pure choice theory; the central primitive is a **generalized choice situation (GCS)** $G=(X,d)$, a constraint set $X\subseteq\mathcal{X}$ paired with an **ancillary condition** $d$ (a feature that may affect behavior but that the planner deems normatively irrelevant: time of choice, framing, default/anchor, presentation). A positive theory delivers a **generalized choice correspondence** $C:\mathcal{G}^{*}\rightrightarrows\mathcal{X}$ with $C(X,d)\subseteq X$. The analyst designates a **welfare-relevant domain** $\mathcal{G}\subseteq\mathcal{G}^{*}$ (allowing "pruning"). Two weak assumptions: every finite subset of $\mathcal{X}$ is some constraint set, and $C(G)$ is nonempty.

A key conceptual move distinguishes conditions of *experience* (do not change when a decision is delegated to a planner; treat as object characteristics) from conditions of *choice* (change under delegation; treat as ancillary). This is how the framework decides what counts as an ancillary condition versus a property of the good.

Welfare is then carried by binary relations defined directly on choices, generalizing weak ($R$) and strict ($P$) revealed preference:

$$x\,R'\,y \iff \forall (X,d)\in\mathcal{G}\text{ with }x,y\in X,\ y\in C(X,d)\Rightarrow x\in C(X,d).$$

$$x\,P^{*}\,y \iff \forall (X,d)\in\mathcal{G}\text{ with }x,y\in X,\ y\notin C(X,d).$$

So $xP^{*}y$ means $y$ is *never* chosen when $x$ is available. $P'$ is the asymmetric part of $R'$; $R^{*}$ is the finest relation whose asymmetric part is $P^{*}$ ($xR^{*}y \iff \sim yP^{*}x$). One shows $xP^{*}y \Rightarrow xP'y \Rightarrow xR'y \Rightarrow xR^{*}y$, and that all four collapse to standard $R,P$ when choice is ancillary-invariant and axiom-consistent. Welfare optima are defined as $P^{*}$- (or $P'$-) maximal elements. Applied tools (compensating/equivalent variation, consumer surplus, generalized Pareto optima, competitive equilibrium) are constructed as direct analogues using these relations.

## Data
None. This is a theoretical paper; illustrations use stylized models (coherent arbitrariness with decision utility $U(y,z\mid d)=u(y)+d\,v(z)$; the $\beta,\delta$ quasi-hyperbolic model; a two-person Edgeworth-box example; a jam-variety example based on [[@Iyengar2000|Iyengar and Lepper 2000]]). The authors note applications by others to real data (e.g., sales-tax salience in Chetty, Looney, and Kroft 2008).

## Key findings
- **Theorem 1 (no money pump):** any chain $x_1 R' x_2 \cdots R' x_N$ containing at least one strict link $x_k P^{*} x_{k+1}$ cannot close ($\sim x_N R' x_1$).
- **Corollary 1 (acyclicity):** $P^{*}$ is acyclic, so maximal elements exist on finite sets and improvements can be identified and measured even absent transitivity. ($P'$, by contrast, can cycle.)
- **Observations 1-2 (libertarian property):** anything chosen from $X$ in some welfare-relevant condition is a weak optimum in $X$; an option can be a welfare optimum without being chosen from that set.
- **Theorem 2 (most discerning):** among all asymmetric *inclusive libertarian* relations (those that never declare a chosen object improvable), $P^{*}$ is the finest; $mP^{*}(X)\subseteq mQ(X)$ for any such $Q$. Hence $P^{*}$ rationalizes choice whenever any relation does.
- **Theorem 3 (multiself Pareto):** if $\mathcal{G}$ is rectangular and each $d$ maximizes a utility $u_d$, then $P^{*}$ equals strict multiself Pareto dominance ($M^{*}$) and $P'$ equals weak ($M$). This gives a choice-based (non-psychological) justification of the multiself Pareto criterion for *coherent arbitrariness* but **not** for $\beta,\delta$ (whose domain is non-rectangular).
- **Theorem 4 ($\beta,\delta$ model):** with $W_t(C_t)\equiv\sum_{k=t}^{T}(\beta\delta)^{k-t}u(c_k)$, $C_1' P^{*} C_1 \iff W_1(C_1')>U_1(C_1)$, and $R',P^{*}$ are transitive here. As $\beta\to1$ the criterion converges to the standard one (unlike conventional multiself Pareto).
- **Theorem 5:** closed-form CV as an analogue of consumer surplus; CV-A and CV-B (two compensation standards) *bracket* Marshallian surplus and converge to it as the anchor range shrinks.
- **Theorems 6-7 (multi-agent):** generalized Pareto optima exist; the **first welfare theorem generalizes** to "behavioral competitive equilibria," which are weak generalized Pareto optima when $\mathcal{G}_n=\mathcal{G}_n^{*}$. Efficiency is driven by firm profit-maximization, not consumer rationality.
- **Theorems 8-10, Corollaries 3 (limiting case):** as choice correspondences converge to a standard (utility-maximizing) one, welfare optima, CV-A/CV-B, and the generalized Pareto set converge to their standard counterparts. Small anomalies have only minor welfare implications.
- **Theorems 11-12 (refinements):** restricting to "coherent" single-choice GCSs ($R_c,P_c^{*}$) for the $\beta,\delta$ consumer makes the $t=1$ perspective decisive and is equivalent to a novel **robust multiself Pareto** criterion (robust to unknown backward-looking preferences), reconciling the long-run criterion with multiself Pareto.

## Contribution
Provides the first general, axiom-free choice-theoretic foundation for behavioral welfare economics: a single welfare relation ($P^{*}$) that (i) requires only the environment-to-choice mapping, (ii) applies to any positive model (preference-based, algorithmic, heuristic, neuroeconomic), (iii) nests standard welfare economics exactly when axioms hold and approximately when anomalies are small, and (iv) supplies generalized versions of the applied welfare toolkit and the first welfare theorem. It reframes "mistakes," paternalism, and the use of nonchoice (psychological/neuro) evidence as disciplined operations on the welfare-relevant domain rather than appeals to true utility.

## Limitations & open questions
- **Non-discernment under severe conflict:** $P^{*}$ can be very coarse (large optimum sets) when choice conflicts are pervasive; the framework "lives with" the resulting ambiguity rather than resolving it.
- **Line-drawing is not pinned down:** distinguishing object characteristics from ancillary conditions, and choosing what to prune from $\mathcal{G}^{*}$, is left to the analyst; the framework only "pinpoints the source of disagreement."
- **Justifying refinements:** the paper explicitly flags the need for principled criteria to prune GCSs (information-processing failures, coherence, simplicity, preponderance). It argues *against* self-officiating via metachoices (infinite regress; metachoices may cycle), and notes the simplicity criterion built from binary choices need not yield acyclicity.
- **Identifying perceived choice sets / mistakes:** recovering an individual's actually-perceived set $Y\neq X$ is "beyond the current capabilities of economics, neuroscience, and psychology" in most cases; provisional "suspect" classifications and sensitivity analysis are proposed instead.
- **Existence gaps:** strict individual welfare optima and strict generalized Pareto optima need not exist; CV may not be finite without further structure; CVs are generally non-additive across sequential changes.
- **Backward-looking preferences** for the $\beta,\delta$ self are untestable from choice, motivating (but not fully settling) the robust multiself Pareto refinement.

## Connections
The paper positions itself against the "experienced/true utility" program ([[@Kahneman1997|Kahneman, Wakker, and Sarin 1997]]; Kahneman 1999) and against rejecting choice as a normative basis (Sugden 2004). It contrasts with Green and Hojman (2007), who rationalize anomalies via conflicting preferences and evaluate by unanimity (and need not coincide with standard welfare under rationality). The unambiguous-choice relation is closely related to independent work by [[@Salant2008|Rubinstein and Salant (2008)]] on "frames" and to Mandler (2006) and Salant-Rubinstein on status-quo bias; the multi-agent efficiency results lean on Fon and Otani (1979), Rigotti and Shannon (2005), and Mandler (2006) for economies with incomplete/intransitive preferences. Applications to time inconsistency engage the $\beta,\delta$ literature (Laibson, Repetto, and Tobacman 1998) and to addiction the authors' own Bernheim and Rangel (2004). Empirically the framework is operationalized by Chetty, Looney, and Kroft (2008) on tax salience and Burghart, Cameron, and Gerdes (2007). It connects to the broader debate on nonchoice evidence (Gul and Pesendorfer 2008; Caplin and Schotter 2008) and to libertarian-paternalist policy proposals ([[@Thaler2003|Thaler and Sunstein 2003]]).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
