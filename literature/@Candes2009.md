---
citekey: Candes2009
title: Exact Matrix Completion via Convex Optimization
authors: ["Candès, Emmanuel J.", "Recht, Benjamin"]
year: 2009
type: journalArticle
doi: 10.1007/s10208-009-9045-5
zotero: "zotero://select/library/items/BYI58HWY"
pdf: /Users/jesper/Zotero/storage/ATI48PAP/Candes2009.pdf
tags: [literature]
keywords: [matrix-completion, nuclear-norm-minimization, low-rank-recovery, convex-optimization, compressed-sensing, incoherence, dual-certificate]
topics: ["[[recommender-systems-matrix-factorization]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We consider a problem of considerable practical interest: the recovery of a data matrix from a sampling of its entries. Suppose that we observe m entries selected uniformly at random from a matrix M. Can we complete the matrix and recover the entries that we have not seen? We show that one can perfectly recover most low-rank matrices from what appears to be an incomplete set of entries. We prove that if the number m of sampled entries obeys m ≥ C n^1.2 r log n for some positive numerical constant C, then with very high probability, most n × n matrices of rank r can be perfectly recovered by solving a simple convex optimization program. This program finds the matrix with minimum nuclear norm that fits the data. The condition above assumes that the rank is not too large. However, if one replaces the 1.2 exponent with 1.25, then the result holds for all values of the rank. Similar results hold for arbitrary rectangular matrices as well. Our results are connected with the recent literature on compressed sensing, and show that objects other than signals and images can be perfectly reconstructed from very limited information.

## Summary
This is the foundational paper of low-rank matrix completion. Candès and Recht show that an unknown $n_1\times n_2$ matrix $M$ of rank $r$, observed only on a small uniformly-random subset $\Omega$ of its entries, can—under an *incoherence* condition on its singular vectors—be recovered *exactly* with high probability by solving a tractable convex program: minimize the nuclear norm subject to agreement on the observed entries. The headline guarantee is that $m\gtrsim n^{6/5}r\log n$ observed entries suffice (improving to a $5/4$ exponent for arbitrary rank), far below the $n^2$ ambient count. The nuclear norm acts as the matrix analogue of the $\ell_1$ relaxation of sparsity in compressed sensing, and the proof builds an explicit dual certificate via a randomized golfing/least-squares construction.

## Research question
Given only $m\ll n_1 n_2$ entries of a matrix $M$, observed at locations sampled uniformly at random, when and how can one recover *all* the missing entries exactly? Specifically: can the combinatorially hard rank-minimization problem be replaced by a tractable convex relaxation that still achieves *exact* recovery, and how many samples does that relaxation require?

## Method / identification
The ideal estimator would solve $\min \operatorname{rank}(X)$ subject to $X_{ij}=M_{ij}$ for $(i,j)\in\Omega$, but this is NP-hard. The paper studies instead the **nuclear norm minimization** convex relaxation
$$\min_{X}\ \lVert X\rVert_*\quad\text{subject to } X_{ij}=M_{ij},\ (i,j)\in\Omega,$$
where $\lVert X\rVert_* = \sum_{k} \sigma_k(X)$ is the sum of singular values. This is the matrix counterpart of the $\ell_1$-vs-$\ell_0$ relaxation in sparse recovery, and it is a semidefinite program, hence efficiently solvable.

Recovery requires the singular vectors to be spread out, formalized by the **coherence** of an $r$-dimensional subspace $U\subseteq\mathbb{R}^n$:
$$\mu(U)\equiv\frac{n}{r}\max_{1\le i\le n}\lVert P_U e_i\rVert^2,$$
with $1\le\mu(U)\le n/r$. The two structural assumptions are: **A0** $\max(\mu(U),\mu(V))\le\mu_0$ for the column/row spaces $U,V$; and **A1** the matrix $\sum_{k\le r}u_k v_k^*$ has entries bounded by $\mu_1\sqrt{r/(n_1 n_2)}$.

The identification strategy is a **dual certificate** argument. By a subgradient/duality lemma, $M$ is the unique minimizer if the sampling operator is injective on the tangent space $T$ of the rank-$r$ manifold and there exists a matrix $Y$ supported on $\Omega$ whose projection onto $T$ equals $\sum_k u_k v_k^*$ and with $\lVert P_{T^\perp}(Y)\rVert<1$ in spectral norm. The authors construct $Y$ as the minimum-Frobenius-norm solution to $(P_T P_\Omega)(X)=\sum_k u_k v_k^*$, giving the closed form $Y=A_T(A_T^* A_T)^{-1}(E)$ with $A_T=P_\Omega P_T$. Sampling is analyzed under the **Bernoulli model** ($\delta_{ij}\sim\text{Bern}(p)$, $p=m/(n_1 n_2)$), which upper-bounds the uniform-model failure probability by a factor of two. Injectivity of $P_T P_\Omega P_T$ near its mean $pP_T$ follows from **Rudelson's selection theorem** and a noncommutative Khintchine inequality; the spectral-norm bound on $P_{T^\perp}(Y)$ uses a Neumann series, **decoupling** inequalities for $U$-statistics, and **Talagrand's** concentration inequality for empirical processes.

## Data
None—this is a theoretical paper. Motivating applications (not analyzed empirically) are the Netflix collaborative-filtering problem (users × movies ratings matrix, assumed approximately low-rank) and sensor-network triangulation/localization from a partial distance matrix.

## Key findings
- **Theorem 1.1 (random orthogonal model).** If $M$'s singular vector families are drawn uniformly among orthonormal sets, then $m\ge C\,n^{5/4}r\log n$ random entries guarantee exact recovery by the SDP with probability $\ge 1-cn^{-3}\log n$; if additionally $r\le n^{1/5}$, the bound improves to $m\ge C\,n^{6/5}r\log n$.
- **Theorem 1.3 (general incoherent matrices, main result).** Under A0 and A1, if $m\ge C\max(\mu_1^2,\mu_0\mu_1,\mu_0 n^{1/4})\,nr(\beta\log n)$ for $\beta>2$, the minimizer is unique and equal to $M$ with probability $\ge 1-cn^{-\beta}$. Under A0 alone and $r\le\mu_0^{-1}n^{1/5}$, this improves to $m\ge C\mu_0 n^{6/5}r(\beta\log n)$. Theorem 1.1 is the special case $\mu_0=O(1)$, $\mu_1=O(\log n)$.
- **Corollary.** For $\mu_0=O(1)$ and modest rank, $m\ge C\,n^{6/5}r\log n$ suffices—dramatically below the $n^2$ entries, and approaching the $(2n-r)r$ degrees of freedom.
- **Theorem 4.1 / 4.2 (injectivity).** $\lVert p^{-1}P_T P_\Omega P_T - pP_T\rVert\le C_R\sqrt{\mu_0 nr(\beta\log n)/m}$ with high probability, establishing both injectivity of the sampling operator on $T$ and concentration of $P_T P_\Omega P_T$ around its mean.
- The nuclear norm relaxation is, for most problems, *formally equivalent* to the intractable rank-minimization program.

## Contribution
The paper launches the field of **matrix completion**, providing the first rigorous *exact-recovery* guarantees for a *tractable* algorithm under random sampling, and porting the compressed-sensing paradigm ($\ell_1$ for sparse vectors) to the matrix setting (nuclear norm for low rank). It introduces the **incoherence** condition as the right structural assumption ruling out spiky, unrecoverable matrices, and develops a dual-certificate construction (a precursor to the later "golfing scheme") that became the standard proof technique for completion and related low-rank recovery problems.

## Limitations & open questions
The authors explicitly flag several open problems:
- **Optimal sample complexity.** Can the exponent on $n$ be driven down toward the information-theoretic $nr$ (up to logs)? They note bounding successive terms $(P_{T^\perp}P_\Omega P_T)H_k(E)$ in the Neumann series would lower the exponent from $6/5$ to $7/6$, then $8/7$, etc., needing $k\sim\log n$ terms—at the cost of growing decoupling constants.
- **Approximately low-rank matrices.** Extend exact recovery to matrices that are only *close* to low-rank: is $\lVert M'-M\rVert_*$ comparable to the truncation error $\lVert M-M_r\rVert_*$?
- **Noise robustness.** For observations $Y_{ij}=M_{ij}+z_{ij}$, relax the equality constraint to $\lVert P_\Omega(X-Y)\rVert_F\le\delta$; is the reconstruction error proportional to the noise level?
- **Scalable solvers.** Interior-point SDP methods are impractical beyond a few hundred dimensions; specialized solvers (singular value thresholding, Bregman/fixed-point continuation) are needed for large instances.

## Connections
The work is the matrix analogue of compressed sensing for sparse signals—Donoho (2006) and Candès, Romberg & Tao (2006) on exact signal reconstruction from incomplete frequency information, and Candès & Tao (2005) on decoding by linear programming. The nuclear norm heuristic for rank minimization originates with Fazel (2002) and Recht, Fazel & Parrilo (2010, then a 2007 preprint), who established it for generic linear measurements; the present paper handles the harder *entry-sampling* operator. The injectivity analysis rests on Rudelson (1999) and Rudelson & Vershynin (2007) on random vectors in isotropic position, the noncommutative Khintchine inequalities of Lust-Picquard (1986) and Buchholz (2001), decoupling for $U$-statistics from de la Peña (1992) and de la Peña & Montgomery-Smith (1995), and Talagrand's (1996) concentration inequality. Motivating applications connect to collaborative filtering—Srebro (2004) and Rennie & Srebro (2005) on maximum-margin matrix factorization, and the Netflix Prize—and to sensor-network localization via So & Ye (2007) and Linial, London & Rabinovich (1995). Solver directions point to Cai, Candès & Shen (2010) on singular value thresholding and Ma, Goldfarb & Chen (2011) on fixed-point/Bregman methods. The noise-robustness question was subsequently taken up by Candès & Plan and by Keshavan, Montanari & Oh.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
