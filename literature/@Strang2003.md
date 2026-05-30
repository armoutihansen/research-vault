---
citekey: Strang2003
title: Lineare Algebra
authors: ["Strang, Gilbert"]
year: 2003
type: book
doi: 10.1007/978-3-642-55631-9
zotero: "zotero://select/library/items/H4MJNBG3"
pdf: /Users/jesper/Zotero/storage/TQZMM7MS/Strang - 2003 - Lineare Algebra.pdf
tags: [literature]
keywords: [linear-algebra, matrix-factorization, eigenvalues, singular-value-decomposition, least-squares, textbook, vector-spaces]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
This is the German translation (2003) of Gilbert Strang's *Introduction to Linear Algebra* (Wellesley-Cambridge Press, 1998), a comprehensive introductory textbook rather than a research paper. The book organizes the entire subject around two central equations: the linear system $Ax=b$ and the eigenvalue problem $Ax=\lambda x$. Strang's pedagogy emphasizes the "column picture" — viewing $Ax$ as a linear combination of the columns of $A$ — and the four fundamental subspaces, building geometric intuition first and computation (with MATLAB teaching codes) throughout. Coverage here is targeted: I read the preface (Vorwort), the table of contents, and representative sections (Ch. 1 vectors, Ch. 2 elimination), then summarized the remaining chapters from the contents; I did not ingest all 664 pages.

## Research question
None in the research sense. As a textbook, its organizing question is pedagogical: how can the whole of introductory linear algebra be understood through the two equations $Ax=b$ (solving linear systems) and $Ax=\lambda x$ (the eigenvalue problem), and how can students be brought from concrete $2$- and $3$-dimensional vectors to the full structure of $n$-dimensional vector spaces?

## Method / identification
Not applicable — this is an expository textbook. The didactic "method" is a layered approach to solving $Ax=b$ at three levels Strang treats as equally important: (1) direct solution by forward elimination and back-substitution; (2) the matrix solution $x=A^{-1}b$ via the inverse; and (3) the vector-space solution, characterizing all linear combinations of the columns (the column space) and all solutions of $Ax=0$ (the nullspace/kernel). The book foregrounds matrix factorizations as the unifying device: $LU$ from elimination, $QR$ from orthogonalization, the diagonalization $S^{-1}AS$ for general square matrices, $Q^{T}AQ$ for symmetric matrices, and the singular value decomposition $U^{T}AV$ (equivalently $A=U\Sigma V^{T}$) for general rectangular matrices. MATLAB is the primary computational vehicle, with teaching codes (by Cleve Moler and Steven Lee) and parallel Maple/Mathematica collections.

## Data
None — a textbook. Worked examples, exercises, MATLAB teaching codes, solutions to selected problems, a sample final exam, and an index are included instead of empirical data.

## Key findings
The "results" are the standard theorems of linear algebra, presented constructively:
- **Elimination and $LU$:** Gaussian elimination reduces $Ax=b$ to an upper-triangular system solved by back-substitution; encoded as the factorization $A=LU$ (with pivoting, $PA=LU$).
- **Four fundamental subspaces:** column space, nullspace, row space, and left nullspace, with their dimensions governed by the rank and the rank–nullity relation.
- **Orthogonality and least squares:** projections, the normal equations, and Gram–Schmidt yielding $A=QR$.
- **Determinants:** their properties and the cofactor/permutation formulas.
- **Eigenvalues and diagonalization:** $Ax=\lambda x$, the factorization $A=S\Lambda S^{-1}$, the spectral theorem for symmetric matrices $A=Q\Lambda Q^{T}$, positive-definite matrices, similarity, and the SVD.
- **Linear maps:** matrices as representations of linear transformations, change of basis, and the pseudoinverse.
- **Applications (Ch. 8):** graphs and networks, Markov matrices and economic models, linear programming, Fourier series as linear algebra for functions, and computer graphics.
- **Numerical and complex linear algebra (Ch. 9–10):** practical elimination, norms and condition numbers, iterative methods, Hermitian/unitary matrices, and the fast Fourier transform.

## Contribution
Its contribution is pedagogical and field-shaping rather than novel research: Strang reframed the introductory linear-algebra curriculum (his MIT 18.06 course) around intuition — the column picture, the four subspaces, and matrix factorizations — rather than around abstract axioms or rote computation. The accompanying MIT OpenCourseWare materials made this approach one of the most widely adopted treatments of the subject worldwide. The German edition extends this reach to German-language instruction.

## Limitations & open questions
As a textbook there are no open research problems. Scope boundaries Strang himself notes: Chapters 1–6 are the core of a one-semester course (theory plus applications); the deeper view of matrices as linear maps (Ch. 7) is deliberately deferred until after subspaces are understood; the full text is pitched at a two-semester course. The treatment is concrete and computational, so readers seeking abstract module/field-theoretic generality or measure-theoretic/functional-analytic extensions must look elsewhere.

## Connections
This is the German rendering of Strang's *Introduction to Linear Algebra*; it sits alongside his other texts, notably *Linear Algebra and Its Applications* and the later *Linear Algebra and Learning from Data*, which carries the same factorization-centered philosophy into machine learning. The numerical material connects to Golub & Van Loan's *Matrix Computations* and to Trefethen & Bau's *Numerical Linear Algebra*; the abstract counterpart is Axler's *Linear Algebra Done Right*. For an economist working in choice modeling and machine learning, the relevant hooks are the SVD and least-squares chapters (underpinning PCA, regression, and dimensionality reduction), Markov matrices (stochastic choice and dynamics), and positive-definite matrices (covariance structures and optimization).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
