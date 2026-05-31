---
citekey: Garcia-Sanz2015
title: Sequential rationalization of multivalued choice
authors: ["García-Sanz, María D.", "Alcantud, José Carlos R."]
year: 2015
type: journalArticle
doi: 10.1016/j.mathsocsci.2014.12.006
zotero: "zotero://select/library/items/Z5FKVUAD"
pdf: /Users/jesper/Zotero/storage/IYGSGJZD/Garcia-Sanz2015.pdf
tags: [literature]
keywords: [sequential-rationalizability, choice-correspondences, revealed-preference, rational-shortlist-method, bounded-rationality, axiomatic-characterization]
topics: ["[[sequential-rationalizability-shortlists]]"]
related: [Apesteguia2013, Au2011, Cherepanov2013, Houy2009, Kalai2002, Manzini2007, Manzini2012, Masatlioglu2012, Rubinstein2006, Sen1971, Tyson2013]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper contributes to the theory of rational choice under sequential criteria. Following the approach initiated by [[@Manzini2007|Manzini and Mariotti (2007)]] for single-valued choice functions, we characterize choice correspondences that are rational by two sequential criteria under a mild consistency axiom. Rationales ensuring the sequential rationalization are explicitly constructed and a uniquely determined, canonical solution is provided.

## Summary
This is a pure choice-theory paper that extends the Manzini–Mariotti Rational Shortlist Method (RSM) from single-valued choice *functions* to multivalued choice *correspondences*. The authors show that compounding two rational choice correspondences need not be rational, and they identify exactly when a correspondence can be decomposed as the sequential application of two rational criteria. The key is a new consistency axiom, "choosing without dominated elements" (CWDE); on the class of correspondences satisfying it, the testable conditions Expansion ($E$) and a generalized Weak WARP characterize two-stage sequential rationalizability. They further construct an explicit, uniquely determined canonical pair of rationales.

## Research question
For multivalued choice (choice correspondences rather than functions), when can observed choice behavior be explained as the sequential application of two rational criteria $C = C_2 \circ C_1$? And when such a representation exists, can one pin down a unique canonical pair of rationalizing relations?

## Method / identification
Purely axiomatic revealed-preference analysis. Let $X$ be a set of alternatives and $\mathcal{D}$ the domain of all finite nonempty subsets. A *decisive choice correspondence* is a map $C:\mathcal{D}\to\mathcal{P}(X)$ with $\emptyset\neq C(S)\subseteq S$. $C$ is *rational* if some binary relation $R$ yields $C(S)=C_R(S)=\{x\in S: (x,y)\in R\ \forall y\in S\}$; on this domain rational and acyclic-rational coincide, and rationalizing relations are reflexive and complete. The *composition* is $(C_2\circ C_1)(A)=C_2(C_1(A))$.

The relevant axioms: Chernoff ($CH$, i.e. $C(T)\cap S\subseteq C(S)$ for $S\subseteq T$); Direct Condorcet ($Con^+$); Expansion ($E$, Sen's $\gamma$: $x\in C(M_i)\ \forall i \Rightarrow x\in C(\bigcup_i M_i)$); and Weak WARP ($WWARP$): for $\{x,y\}\subseteq S\subseteq T$, if $C(\{x,y\})=\{x\}$ and $x\in C(T)$ then $y\notin C(S)$. The novel axiom is CWDE: $x$ is *dominated* by $y$ if $x\notin C(S)$ whenever $\{x,y\}\subseteq S$; $C$ satisfies CWDE if $C(S)=C(S\setminus\{x\})$ whenever $x$ is dominated by some $y\in S$. The proof constructs two explicit complete relations: $xR_1 y \Leftrightarrow \exists S'\in\mathcal{D}: x,y\in S'$ and $x\in C(S')$; and $xR_2 y \Leftrightarrow x\in C(\{x,y\})$.

## Data
None - this is a theoretical paper. No experiments or empirical datasets; "data" here are abstract choice correspondences over finite menus, illustrated by two worked counterexample tables in the Appendix on $X=\{x,y,z\}$ and $X=\{x,y,z,t,s\}$.

## Key findings
- **Proposition 1**: If $C_1, C_2$ are rational choice correspondences on $\mathcal{D}$, then the compound $C=C_2\circ C_1$ satisfies $E$ and $WWARP$ (necessity, no recourse to CWDE).
- The translation from functions is *not* faithful: $E$ and $WWARP$ alone do **not** suffice to characterize correspondences rational by two sequential criteria (Example 2), and $E$ plus $WWARP$ do not even imply $CH$ (Example 1).
- **Theorem 1** (main result): For a choice correspondence $C$ satisfying CWDE, $C$ is rational by two sequential criteria **if and only if** $C$ satisfies $E$ and $WWARP$. This exactly replicates the Manzini–Mariotti characterization, now in the multivalued domain restricted by CWDE.
- **Canonical representation**: With $R_1, R_2$ defined as above, $C_{R_2}(S)\subseteq C(S)\subseteq C_{R_1}(S)$ for all $S$, where $C_{R_1}$ is the *smallest* rational correspondence containing $C$ and $C_{R_2}$ is the *greatest* rational correspondence contained in $C$ (linking to Aizerman–Aleskerov approximation). The rationalizing relations are not unique, but this nested construction delivers a uniquely determined, economically interpretable canonical solution.

## Contribution
Generalizes the RSM program ([[@Manzini2007|Manzini & Mariotti 2007]]) from single-valued to multivalued choice, isolating exactly the consistency requirement (CWDE) under which the original two-axiom characterization survives. CWDE imports the spirit of IIA: the DM considers everything but chooses as if dominated alternatives had been eliminated. The paper also supplies a constructive, canonical pair of rationales tied to revealed-preference primitives, situating sequential rationalizability within the broader literature on bounded rationality, limited consideration, and multiple rationales.

## Limitations & open questions
- **Uniqueness of rationales is not established** - the authors can only offer a canonical *representation* (the nested $C_{R_2}\subseteq C\subseteq C_{R_1}$), not unique rationalizing relations. They explicitly defer the full identification problem to Dutta and Horan (2014), noting that the latter's uniqueness argument "crucially hinges on the property that choices are univalued," so extending exact identification of all representing rationale pairs to correspondences is open.
- **Restriction to CWDE**: the characterization holds only on the CWDE class; outside it (Example 2) $E$ and $WWARP$ fail to characterize. Whether a clean characterization exists for the full domain is left open.
- **Two criteria only**: like Manzini–Mariotti's complete analysis of two and three relations, this treats two sequential criteria; the $k$-criteria multivalued case is not resolved.
- **Exhaustive-data assumption**: the analysis assumes choices from every menu are observed; the authors cite de Clippel and Rozen (2012) on the empirical implausibility of full datasets as a standing concern.

## Connections
The paper is built directly on [[@Manzini2007|Manzini & Mariotti (2007)]] "Sequentially rationalizable choice" (RSM) and explicitly replicates its Expansion + Weak WARP characterization for the multivalued setting. It contrasts with [[@Apesteguia2013|Apesteguia & Ballester (2013)]] on choice by sequential procedures and status-quo-bias refinements (Masatlioglu & Ok 2005), [[@Au2011|Au & Kawai (2011)]] on transitive-RSMs, and Houy (2007) on order-dependence of sequential rationality. The identification gap is framed against Dutta & Horan (2014). Foundational revealed-preference roots include Arrow (1959), Richter (1966, 1971), [[@Sen1971|Sen (1971)]], Suzumura (1976, 1983), Blair et al. (1976), and Tversky (1969) on intransitivity. The canonical approximation construction draws on Aizerman & Aleskerov (1995) and Aizerman & Malishevski (1986). The limited-consideration literature it relates to includes [[@Masatlioglu2012|Masatlioglu, Nakajima & Ozbay (2012)]] on revealed attention, Lleras et al. (2011) on limited consideration, [[@Cherepanov2013|Cherepanov, Feddersen & Sandroni (2013)]] on rationalization, and [[@Kalai2002|Kalai, Rubinstein & Spiegler (2002)]] on rationalization by multiple rationales. Other neighbors: [[@Rubinstein2006|Rubinstein & Salant (2006)]] on choice from lists, [[@Manzini2012|Manzini & Mariotti (2012)]] on lexicographic semiorders, [[@Houy2009|Houy & Tadenuma (2009)]], [[@Tyson2013|Tyson (2013)]] on shortlisting procedures, and Bossert & Sprumont (2013) on backwards-induction rationalizability (extended to correspondences by Rehbeck 2014 and Xiong 2014).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
