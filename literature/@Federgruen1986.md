---
citekey: Federgruen1986
title: "The Greedy Procedure for Resource Allocation Problems: Necessary and Sufficient Conditions for Optimality"
authors: ["Federgruen, Awi", "Groenevelt, Henri"]
year: 1986
type: journalArticle
doi: 10.1287/opre.34.6.909
zotero: "zotero://select/library/items/NNHPAMMZ"
pdf: /Users/jesper/Zotero/storage/5HCNE85G/Federgruen and Groenevelt - 1986 - The Greedy Procedure for Resource Allocation Problems Necessary and Sufficient Conditions for Optim.pdf
tags: [literature]
keywords: [resource-allocation, polymatroids, greedy-algorithm, submodularity, combinatorial-optimization, marginal-analysis, integer-programming]
topics: []
related: [Fox1966]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> In many resource allocation problems, the objective is to allocate discrete resource units to a set of activities so as to maximize a concave objective function subject to upper bounds on the total amounts allotted to certain groups of activities. If the constraints determine a polymatroid and the objective is linear, it is well known that the greedy procedure results in an optimal solution. In this paper we extend this result to objectives that are "weakly concave," a property generalizing separable concavity. We exhibit large classes of models for which the set of feasible solutions is a polymatroid and for which efficient implementations of the greedy procedure can be given.

## Summary
This combinatorial-optimization theory paper studies the discrete resource-allocation problem: assign integer resource units to activities to maximize a concave objective under upper-bound (knapsack-style) constraints on totals allotted to designated activity subsets. The classical Edmonds (1970) result says the *greedy* (marginal allocation) procedure is optimal for a **linear** objective iff the feasible region is the independence polytope of a **polymatroid**. Federgruen and Groenevelt push this equivalence past linearity: they identify the exact concavity class — "weakly concave" complete orders — for which greed stays optimal over every polymatroid, and show the polymatroid property is also necessary. They then make the result usable by enumerating easily-checkable polymatroid model classes and giving polynomial feasibility tests so the greedy steps can be executed. Coverage is full across Sections 1-6.

## Research question
For the integer program $P(R,F)$ — find $z\in F\subseteq\mathbf{N}^E$ maximal with respect to a complete order $R$ on $\mathbf{N}^E$ — *under what necessary and sufficient conditions on the objective $R$ and the feasible region $F$ does the greedy/marginal allocation procedure return a global optimum?* Two practical sub-questions follow: which model families have a polymatroid feasible region (so the theory applies), and how can the per-iteration feasibility check be implemented efficiently.

## Method / identification
This is pure combinatorial-optimization theory; the "identification" is a chain of structural lemmas and three main theorems. Setup: $E$ is a finite groundset, $\mathbf{A}\subseteq 2^E$, and a set function $V$ on $\mathbf{A}$ defines the feasible region
$$F(\mathbf{A},V)=\{z\in\mathbf{N}^E : z(S)\le V(S)\ \text{for all}\ S\in\mathbf{A}\}.$$
The region is characterized by three properties: (F1) $0\in F$; (F2) downward closure ($z\in F,\ 0\le y<z\Rightarrow y\in F$); and an exchange property (F3). The authors prove $F$ is a polymatroid iff it satisfies (F1)-(F3) — equivalently $F$ is the independence polytope of a rank function $V$ obeying normalization (V1), monotonicity (V2), and submodularity (V3, $V(S)+V(T)\ge V(S\cup T)+V(S\cap T)$).

The objective is a complete order $R$ graded by nested concavity axioms: $R$ is **concave** if it satisfies (R1)-(R4), **weakly concave** if it satisfies just (R1) and (R3), **strongly concave** if it adds (R5)-(R6). Key relation (R1): if $y\ge x$ and $x\succeq_R x+e^i$ then $y\succeq_R y+e^i$ — a diminishing-returns/monotone-marginal condition. Orders induced by separable concave functions are strongly concave, but the weakly concave class also captures nonseparable objectives such as lexicographic ("sharing problem") orders and threshold orders (Examples 1-2).

The **Marginal Allocation Algorithm (MAA)** starts at $z=0$, repeatedly picks the feasible unit increment $z+e^i\in F$ that is $R$-best, and stops when no feasible improving increment exists. The analysis proves (Theorem 1) the MAA halts at a local optimum (conditions (L1)-(L3)); (Theorem 2, sufficiency) for any weakly concave $R$ and any (F1)-(F3) region, the MAA solves $P(R,F)$, by induction on $m(F)=\max\{z(E):z\in F\}$; and (Corollary 1, the Main Result) the equivalence $F$ polymatroid $\Leftrightarrow$ (F1)-(F3) $\Leftrightarrow$ MAA optimal for *every* weakly concave order. Theorem 3 adds that when $R$ is fully concave and $F$ a polymatroid, **every local optimum is global** — a stronger property that can fail for merely weakly concave orders.

## Data
None. This is a theory paper with no empirical dataset. The "data" of a problem instance is the pair $(\mathbf{A},V)$ specifying the constraint structure; the worked model families (single budget, generalized upper bounds, nested/tree-structured constraints, generalized symmetric models, polymatroidal network flows, an oil-and-gas lease investment model) are illustrative instances, not estimated objects.

## Key findings
- **Main equivalence (Corollary 1):** greed is optimal for *all* weakly concave objectives exactly when $F$ is a polymatroid; otherwise a linear (hence weakly concave) objective exists on which the MAA fails — the necessary-and-sufficient generalization of Edmonds.
- **Theorem 2:** for weakly concave $R$ over any (F1)-(F3) region the MAA is optimal — the sufficiency half, reaching nonseparable objectives no separable-equivalence argument covers.
- **Theorem 3:** under full concavity over a polymatroid, local optimality $\Rightarrow$ global optimality, so any improving-direction search converges.
- **Model catalogue (Section 4):** easily-verified polymatroid classes — single resource constraint, simple/generalized upper bounds, nested constraints, tree-structured models, intersecting/crossing families, generalized symmetric models $V(S)=f(w(S))$ with $f$ nondecreasing concave.
- **Efficient implementations (Section 5):** polynomial feasibility tests for tree-structured, network-based and generalized symmetric models (Lemma 9 / Proposition 2 give an $O(|E|\log V(E))$-style membership test via a parametric/sorting argument).
- **Boundary (Section 6):** the general class $P$ with linear objective equals the multiple set covering problem and is strongly NP-complete (via Karp 1972), where greed is only logarithmically approximate (Chvátal 1979, Dobson 1982); results do **not** extend to general supermodular objectives.

## Contribution
The paper closes the gap between Edmonds' linear-objective polymatroid theory and the nonlinear, nonseparable resource-allocation problems arising in operations research. It pinpoints *weakly concave orders* as the precise objective class preserving greedy optimality, supplies the matching necessary condition, and bridges theory to practice with verifiable polymatroid model classes and polynomial feasibility oracles. It thereby unifies a scattered prior literature on incremental/marginal allocation (Gross 1956; [[@Fox1966|Fox 1966]]; Veinott 1964; and rediscoveries by Shih 1974, Mjelde 1975, Hartley 1976, Kao 1976, Proll 1976, Einbu 1977) and the nested/tree extensions of Tamir (1980) and Brucker (1982).

## Limitations & open questions
- The theory stops at concavity/submodularity: results explicitly **fail for general supermodular objectives** and for non-weakly-concave restrictions of concave functions on $\mathbf{R}^E$ — characterizing greedy-amenable objectives beyond this boundary is open.
- The weak-vs-full concavity gap: Theorem 3's local-implies-global property can fail for weakly concave orders, leaving open which intermediate conditions guarantee it.
- Efficient feasibility (membership) testing is shown only for *specific* structured classes; for general polymatroids it reduces to the membership problem solvable only via the ellipsoid method — a combinatorial polynomial oracle for broader classes is unresolved.
- Where $F$ is not a polymatroid (transportation with nonpositive costs, set covering), the problem is NP-hard with only logarithmic greedy approximation; tighter guarantees remain open.

## Connections
The foundational antecedent is Edmonds (1970) on submodular functions, matroids and polyhedra, with the framework surveyed in Lovász (1982) and Welsh (1976) and the membership/ellipsoid machinery in Grötschel, Lovász & Schrijver (1981). The single-constraint marginal-analysis lineage runs through Gross (1956), [[@Fox1966|Fox (1966)]] and Veinott (1964); structured extensions appear in Tamir (1980), Brucker (1982), and the authors' companion work Federgruen & Groenevelt (1986) and Federgruen & Zipkin (1983). Polymatroidal network-flow generalizations connect to Megiddo (1974), Fujishige (1980), Lawler & Martel (1982) and Hassin (1978). On hardness, the multiple set covering reduction ties to Karp (1972) and Garey & Johnson (1979), with greedy-approximation analyses by Chvátal (1979) and Dobson (1982); Topkis (1978) is the submodular-minimization counterpoint. Conceptually, the diminishing-returns structure linking concavity to greedy optimality prefigures the submodular-maximization tradition later central to machine learning.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
