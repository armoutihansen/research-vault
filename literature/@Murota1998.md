---
citekey: Murota1998
title: Discrete convex analysis
authors: ["Murota, Kazuo"]
year: 1998
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/TAHGLD96"
pdf: /Users/jesper/Zotero/storage/ERLSLWFQ/Murota - 1998 - Discrete convex analysis.pdf
tags: [literature]
keywords: [discrete-convex-analysis, m-convexity, l-convexity, submodular-functions, fenchel-duality, integer-programming, matroid-theory, gross-substitutes]
topics: []
related: []
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> A theory of "discrete convex analysis" is developed for integer-valued functions defined on integer lattice points. The theory parallels the ordinary convex analysis, covering discrete analogues of the fundamental concepts such as conjugacy, subgradients, the Fenchel min-max duality, separation theorems and the Lagrange duality framework for convex/nonconvex optimization. The technical development is based on matroid-theoretic concepts, in particular, submodular functions and exchange axioms. Sections 1-4 extend the conjugacy relationship between submodularity and exchangeability, deepening our understanding of the relationship between convexity and submodularity investigated in the eighties by A. Frank, S. Fujishige, L. Lovász and others. Sections 5 and 6 establish duality theorems for M- and L-convex functions, namely, the Fenchel min-max duality and separation theorems. These are the generalizations of the discrete separation theorem for submodular functions due to A. Frank and the optimality criteria for the submodular flow problem due to M. Iri-N. Tomizawa, S. Fujishige, and A. Frank. A novel Lagrange duality framework is also developed in integer programming. We follow Rockafellar's conjugate duality approach to convex/nonconvex programs in nonlinear optimization, while technically relying on the fundamental theorems of matroid-theoretic nature.

## Summary
This is the foundational paper that launches *discrete convex analysis* — a theory of "convexity" for integer-valued functions $f:\mathbb{Z}^V\to\mathbb{Z}\cup\{+\infty\}$ defined on the integer lattice. The motivating problem is nonlinear integer programming, $\min f(x)$ s.t. $x\in B\subseteq\mathbb{Z}^V$, for which Murota wants a Lagrange/Fenchel duality theory mirroring the continuous case. The paper first shows (Examples 1.1–1.3) that the naive transcription of convex analysis to the lattice fails: the integer Fenchel transform $f^\bullet(p)=\sup\{\langle p,x\rangle-f(x)\mid x\in\mathbb{Z}^V\}$ does not satisfy biconjugacy ($f^{\bullet\bullet}\neq f$), the integer subdifferential can be empty, and the discrete separation theorem fails for arbitrary lattice-convex functions. The fix is to restrict to two well-behaved, mutually conjugate classes — **M-convex** and **L-convex** functions — built from matroid-theoretic exchange/submodularity axioms. On these classes all the pillars of convex analysis (conjugacy, subgradients, Fenchel min-max, separation, Lagrange duality) hold *with integrality*. Coverage here is **targeted** (59-page article): I read the abstract, full introduction, the M-/L-convexity definitions and conjugacy theorem (§4), the duality theorems (§5), the Lagrange duality scheme (§6), and the concluding remarks; intermediate lemma proofs were sampled rather than fully ingested.

## Research question
Can the entire apparatus of convex analysis — conjugacy, the Fenchel min-max duality, separation theorems, and the Rockafellar-style perturbation/Lagrange duality framework — be reconstructed *exactly* (with integrality assertions) for functions on the integer lattice, by identifying the "right" discrete analogue of a convex function? Equivalently: which subclass of lattice functions is closed under conjugacy and supports a strong duality theory?

## Method / identification
This is a pure mathematics / optimization-theory paper; the "method" is the axiomatic construction of two function classes and the proof of their duality.

- **M-convexity.** $f:\mathbb{Z}^V\to\mathbb{Z}\cup\{+\infty\}$ with $\mathrm{dom}\,f\neq\emptyset$ is *M-convex* if it satisfies the **exchange axiom (M-EXC)**: for all $x,y\in\mathrm{dom}\,f$ and all $u\in\mathrm{supp}^+(x-y)$ there exists $v\in\mathrm{supp}^-(x-y)$ with
$$f(x)+f(y)\ \succeq\ f(x-\chi_u+\chi_v)+f(y+\chi_u-\chi_v),$$
where $\chi_u$ is the characteristic vector of $u$ (here read $\succeq$ as $\geq$). This is the quantitative generalization of the simultaneous-exchange property (B-EXC) of integral base sets / base polyhedra of submodular systems; an M-concave function with $\mathrm{dom}\subseteq\{0,1\}^V$ is exactly a *valuated matroid* of Dress–Wenzel.
- **L-convexity.** $f$ is *L-convex* if it is submodular on the vector lattice, $f(p)+f(q)\succeq f(p\vee q)+f(p\wedge q)$, and is linear along the all-ones direction: $\exists r\in\mathbb{Z}$ with $f(p+\mathbf{1})=f(p)+r$. The restriction to $\mathbb{Z}^V$ of the Lovász extension of a submodular set function is L-convex.
- **Conjugacy.** The integer Fenchel transform is $f^\bullet(p)=\sup\{\langle p,x\rangle-f(x)\mid x\in\mathbb{Z}^V\}$; the integer subdifferential is $\partial_{\mathbb{Z}} f(x)=\{p\in\mathbb{Z}^V\mid f(y)-f(x)\succeq\langle p,y-x\rangle\ \forall y\}$. The central structural result (Theorem 4.24) is that **M- and L-convexity are conjugate**: $\mathcal{M}^\bullet=\mathcal{L}$, $\mathcal{L}^\bullet=\mathcal{M}$, and $f^{\bullet\bullet}=f$ on each class — biconjugacy that *fails* in general. An Extension Theorem (4.11) characterizes M-convex $f$ as exactly those extending to a convex function whose every $\mathrm{arg\,min}$ of $f[-p](x)=f(x)+\langle p,x\rangle$ is an integral base polyhedron.
- **Lagrange duality (§6).** Following Rockafellar's conjugate-duality / perturbation scheme, the primal $\min c(x)$ s.t. $x\in B$ is rewritten $\min f(x)$ with $f=c+\delta_B$, embedded in a perturbation family $F(x,u)$ with $F(x,0)=f(x)$ and per-$x$ biconjugacy in $u$. The optimal-value function $\varphi(u)=\inf_x F(x,u)$, Lagrangian $K(x,y)=\inf_u\{F(x,u)+\langle u,y\rangle\}$, and dual $g(y)=\inf_x K(x,y)$ yield the dual $\max g(y)$. An *augmented Lagrangian* $F_r(x,u)=c(x)+\delta_B(x+u)+r(u)$ with M-convex $r$, $r(0)=0$, handles the nonconvex case.

## Data
None. This is a theory paper; there is no empirical data, estimation, or simulation. All results are theorems and worked counterexamples on the integer lattice.

## Key findings
- **Failure of the naive theory** (Examples 1.1–1.3): for general lattice-extendable functions, $f^{\bullet\bullet}\neq f$, $\partial_{\mathbb{Z}}(f_1+f_2)\neq\partial_{\mathbb{Z}}f_1+\partial_{\mathbb{Z}}f_2$, and discrete separation can fail — motivating the restriction to M-/L-convexity.
- **Conjugacy duality (Theorem 4.24):** the integer Fenchel transform is an involutive bijection between the M-convex and L-convex classes, summarized in the paper's Table 1; this extends the eighties-era $\mathcal{M}_0/\mathcal{L}_0$ conjugacy between integral base sets and Lovász extensions.
- **Fenchel-type min-max duality (Theorem 5.2):** for M-convex $f$ and M-concave $g$ with a domain-intersection condition,
$$\inf\{f(x)-g(x)\mid x\in\mathbb{Z}^V\}=\sup\{g^\circ(p)-f^\bullet(p)\mid p\in\mathbb{Z}^V\},$$
with both extrema *attained* — a discrete, integral analogue of the classical Fenchel duality. (The supporting Theorem 5.1, proved in Appendix A, is the optimality criterion for the M-convex intersection problem.)
- **Separation theorems:** the **M-separation theorem** (5.3) and the conjugate **L-separation theorem** (5.4): an M-convex $f\geq$ M-concave $g$ can be separated by an *integral* affine function $\alpha^\ast+\langle p^\ast,x\rangle$. These specialize to Frank's discrete separation theorem and to Iri–Tomizawa / Fujishige optimality criteria for submodular-flow and matroid-intersection problems.
- **Lagrange duality:** weak duality $\inf(P)\geq\sup(D)$ (Thm 6.2) always holds; strong duality $\min(P)=\max(D)$ holds iff $\partial_{\mathbb{Z}}\varphi(0)\neq\emptyset$ (Thm 6.4), characterized by the *saddle-point theorem* (6.5). For the canonical case (B an integral base set, $c$ M-convex), the dual objective is L-concave and **strong duality holds**, as a consequence of M–L conjugacy and the Fenchel duality. The augmented Lagrangian extends this to nonconvex programs via the larger M$_2$/L$_2$ classes.

## Contribution
The paper unifies, under one roof, three previously separate strands — convex analysis, matroid/submodular-function theory, and integer programming duality — by isolating M-convexity and L-convexity as *the* lattice analogues of convex functions and proving they are conjugate. It generalizes the eighties results of Frank, Fujishige, and Lovász (which concerned only convex *sets* and their support functions) to genuine convex *functions*, and supplies a Rockafellar-style perturbation duality for nonlinear integer programming that is distinct from subadditive duality in being convexity-driven. It is the founding reference for the field of discrete convex analysis.

## Limitations & open questions
The author (§7) explicitly confines the paper to *structural* aspects (conjugacy, duality) and leaves several problems open: (i) **algorithms** — whether minimization algorithms for nonlinear integer objectives and matroid valuations extend to general M-convex functions (later realized; cf. Shioura's result, noted in the paper); (ii) **continuous/polyhedral generalization** — extending M-/L-convexity to piecewise-linear functions $f:\mathbb{R}^V\to\mathbb{R}\cup\{+\infty\}$ on real space (Remark 7.2); (iii) **g-polymatroid version** — replacing "base polyhedron" by "generalized polymatroid" in the Extension Theorem (Remark 7.3, taken up by Murota–Shioura). For an empirical/economics reader, the open hook is computational tractability: which structured optimization or equilibrium problems can be cast as M-/L-convex programs so that integral strong duality is automatic.

## Connections
The construction generalizes the *valuated matroids* of Dress & Wenzel (1990, 1992) and the submodular-function/convexity link of Lovász (1983) and Frank (1982), whose discrete separation theorem is recovered as a special case; Fujishige's (1984) Fenchel-type duality for submodular flows is likewise subsumed. The Lagrange/perturbation machinery is a direct lattice adaptation of Rockafellar's (1970, 1974) conjugate-duality theory for convex/nonconvex programs. Within economics, M-concavity (gross substitutes) underlies the discrete-convexity treatment of equilibrium and matching markets — connecting to Kelso & Crawford (1982) on gross substitutes and to later work by Murota & Tamura on competitive equilibria in indivisible-goods economies. Methodologically the paper sits with the broader literature on submodularity and discrete optimization in operations research and combinatorial optimization.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
