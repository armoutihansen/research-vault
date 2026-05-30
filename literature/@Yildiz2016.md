---
citekey: Yildiz2016
title: List-rationalizable choice
authors: ["Yildiz, Kemal"]
year: 2016
type: journalArticle
doi: 10.3982/TE1298
zotero: "zotero://select/library/items/YBP38UR4"
pdf: /Users/jesper/Zotero/storage/5GUUUPIS/Yildiz2016.pdf
tags: [literature]
keywords: [bounded-rationality, list-rationalizability, stochastic-choice, path-independence, revealed-preference, shortlisting, choice-theory]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> A choice function is list rational(izable) if there is a fixed list such that for each choice set, successive comparison of the alternatives by following the list retrieves the chosen alternative. We extend the formulation of list rationality to stochastic choice setup. We say two alternatives are related if the stochastic path independence condition is violated between these alternatives. We show that a random choice function is list rational if and only if this relation is acyclic. Our characterization for deterministic choice functions follows as a corollary. By using this characterization, we relate list rationality to two-stage choice procedures.

## Summary
Yildiz models a boundedly rational decision maker (DM) who chooses by running a single-elimination "horse race" down a fixed but unobserved list: take the first two alternatives, keep the winner, compare it to the next, and so on until the list is exhausted. The motivation is a DM with a single memory cell who cannot recall all encountered options. The paper provides choice-theoretic foundations for this procedure in both deterministic and stochastic (random choice) settings. The central tool is a "revealed-to-follow" relation built from violations of a (stochastic) path-independence condition; list rationality holds iff this relation is acyclic, which also pins down the identifiable list(s). A parallel acyclicity characterization is given for the shortlisting procedure, enabling a clean comparison of the two procedures.

## Research question
When is observed choice behavior consistent with a DM who orders alternatives by a single subjective list and chooses by sequential pairwise elimination along that list? Concretely: (i) what behavioral conditions characterize list-rational (random) choice functions, (ii) can the unobserved list be recovered from observed choices, and (iii) how does list rationality relate formally to two-stage "shortlisting" procedures?

## Method / identification
The paper is pure axiomatic choice theory (no data, no estimation). Let $X$ be a finite alternative set and $\Omega$ the collection of nonempty choice sets. A list $f$ is an ordering (complete, transitive, antisymmetric) on $X$; $x\mathrel{f}y$ means $x$ follows $y$ in the DM's considerations.

**Deterministic list rationality (Definition 1).** A choice function $c:\Omega\to X$ is list-rational if there is a list $f$ such that for each $S$, with $x$ the $f$-last element of $S$,
$$c(S)=c(\{c(S\setminus x),\,x\}).$$
This recursion encodes carrying the running winner to the next round. Example 1 shows rational (preference-maximizing) choice is list-rational for any list; Example 2 shows choice via a binary game tree (backward induction / subgame-perfect outcomes) is list-rational, by listing alternatives in reverse order of their appearance as end nodes.

**Stochastic list rationality (Definition 2).** Observing repeated choices yields a random choice function (r.c.f.) $C$ assigning each $S$ a probability measure, with $C_x(S)$ the frequency of choosing $x$ from $S$. The list $f$ is deterministic but pairwise comparisons are random. $C$ is list-rational if there is a list $f$ such that, with $x$ the $f$-last element of $S$,
$$C_x(S)=\sum_{z\in S\setminus x} C_z(S\setminus x)\cdot C_x(x,z)\qquad(1)$$
and for each $y\in S\setminus x$,
$$C_y(S)=C_y(S\setminus x)\cdot C_y(x,y).\qquad(2)$$
A deterministic $c$ is the special case where every $C_x(S)\in\{0,1\}$.

**Identification via revealed-to-follow.** The key axiom is Stochastic Path Independence (SPI): $C$ satisfies SPI if for all $S$ with $x\in S$, $y\notin S$, $C_x(S\cup y)=C_x(S)\cdot C_x(x,y)$ (equivalently a splitting property $C_x(S)=C_x(S_1)\cdot C_x(S_2)$ when $S_1\cup S_2=S$, $S_1\cap S_2=\{x\}$). Definition 3 then sets $x\mathrel{f_C}y$ ("$x$ revealed-to-follow $y$") whenever SPI is violated between $x$ and $y$, i.e. $C_x(S\cup y)\neq C_x(S)\cdot C_x(x,y)$ for some such $S$. Definition 4 gives the deterministic counterpart $F_c$ via explicit case conditions on $c(S\cup y)$, $c(S)$, and the binary choice $c(x,y)$.

## Data
None - this is a theoretical paper. It cites experimental motivation (Russo and Rosen 1975 eye-fixation study; Liu and Simonson 2005, where list-guided subjects bought their selected product 45% vs 34% of the time; Shugan 1980 cost-of-thinking; recency-effect evidence from figure-skating and music-contest judging) but does not analyze a dataset.

## Key findings
**Proposition 1 (stochastic characterization).** An r.c.f. $C$ is list-rational if and only if $f_C$ is acyclic. Moreover the identified list is unique up to the completions of the transitive closure $\mathrm{Tr}(f_C)$. The "only-if" direction shows $x\mathrel{f_C}y\Rightarrow x\mathrel{f}y$ (so an acyclic $f_C$ follows from transitivity of $f$); the "if" direction builds $f$ as any completion of $\mathrm{Tr}(f_C)$ and verifies (1)-(2) hold because SPI holds between the last element and everything preceding it.

**Corollary 1 (deterministic characterization).** A choice function $c$ is list-rational iff $F_c$ is acyclic, with the list unique up to completions of $\mathrm{Tr}(F_c)$. It follows directly by specializing Proposition 1 to degenerate r.c.f.s.

**Recency / monotonicity (Example 3).** List rationality can violate (strong) monotonicity. In Debreu's symphony-vs-suite example with equiprobable pairwise comparisons, the list $y\mathrel{f}x_2\mathrel{f}x_1$ yields choice probabilities $0.25,0.25,0.5$ for $x_1,x_2,y$ — recovering the "natural" assignment that the Luce rule cannot, exhibiting a recency effect (the last-listed distinct alternative $y$ is favored).

**Proposition 2 (shortlisting).** Defining $x\mathrel{R_c}y$ by a three-case condition (Definition 5) that is a minimal deviation from $F_c$, a choice function $c$ is a shortlisting — i.e. $c(S)=\max(\max(S,P_1),P_2)$ for a transitive (possibly incomplete) $P_1$ and a preference $P_2$ — if and only if $R_c$ is acyclic. The proof uses a Weak Path Independence lemma (Lemma 1). Example 4 shows shortlisting is observationally equivalent to choice via a Stackelberg game, mirroring the game-tree equivalence for list rationality.

The set of list-rational choice functions is nested by those of Xu and Zhou (2007), Apesteguia and Ballester (2013), and Masatlioglu et al. (2012), and is nonnested with those of Manzini and Mariotti (2007, 2012) and Cherepanov et al. (2013). List rationality and shortlisting are nonnested; expressing both via acyclicity of closely related relations is what makes them comparable.

## Contribution
Provides the first revealed-preference foundation for list-rational choice as a subjective (unobserved-list) procedure, in both deterministic and stochastic settings, with a constructive identification of all consistent lists from the transitive closure of the revealed-to-follow relation. It extends path independence (Plott 1973; cf. Kalai and Megiddo 1980) to stochastic choice (SPI), and recasts shortlisting (Manzini and Mariotti 2007; Au and Kawai 2011) through a parallel acyclicity condition $R_c$ nested in Au and Kawai's relation, sharpening the comparison between sequential procedures. The game-tree (Example 2) and Stackelberg-game (Example 4) equivalences connect these choice procedures to extensive-form solution concepts.

## Limitations & open questions
- **No general duplicates effect.** List-rational random choice handles Debreu's specific example but the paper explicitly notes it "fails to accommodate the general duplicates effect," pointing to Gul, Natenzon, and Pesendorfer (2014) for a model that does — an opening to reconcile list-following with broader similarity effects.
- **Deterministic list, random comparisons only.** Definition 2 fixes a deterministic list while randomizing comparisons. The author flags the deterministic-comparison restriction (same winner regardless of list) as "particularly restrictive" for r.c.f.s and suggests, as an extension of random utility models (Block and Marschak 1960), a model where both the list and the comparisons are random — left open.
- **Monotonicity failures.** Because list-following exhibits recency, standard monotonicity (satisfied by Luce) can fail; the welfare/normative status of such violations is not resolved.
- **Comparability of procedures.** The acyclicity reformulations are offered to "facilitate comparisons," but a full mapping of where list rationality, shortlisting, and other two-stage procedures overlap or diverge is only partially traced.

## Connections
Builds directly on Salant and Rubinstein (2006) "A model of choice from lists" (there the list is an exogenous frame, here it is subjective/unobserved) and Salant (2003, 2011) on single-memory-cell procedures. The game-tree equivalence relates to Xu and Zhou (2007) and Horan (2011) "Choice by tournament," a special case of which is observationally equivalent to list rationality. The shortlisting analysis engages Manzini and Mariotti (2007) rational shortlist methods, Au and Kawai (2011), Lleras et al. (2010), and Horan (2012), and the agenda-voting amendment procedure of Apesteguia, Ballester, and Masatlioglu (2014). SPI extends Plott (1973) path independence and Kalai and Megiddo (1980); Manzini and Mariotti (2014) derive a related stochastic condition from primitive axioms. The recency/duplicates discussion connects to Debreu (1960), the Luce rule (Luce 1959), and Gul, Natenzon, and Pesendorfer (2014). It situates within boundedly rational / sequentially rationalizable choice (Apesteguia and Ballester 2013; Masatlioglu et al. 2012; Cherepanov et al. 2013), with the WPI characterization tracing to the author's thesis Yildiz (2013).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
