---
citekey: Melnikov2023
title: A Course of Stochastic Analysis
authors: ["Melnikov, Alexander"]
year: 2023
type: book
doi: 10.1007/978-3-031-25326-3
zotero: "zotero://select/library/items/HSPE7WDC"
pdf: /Users/jesper/Zotero/storage/UIYD5GQV/Melnikov - 2023 - A Course of Stochastic Analysis.pdf
tags: [literature]
keywords: [stochastic-analysis, semimartingales, martingale-theory, stochastic-calculus, mathematical-finance, doob-meyer-decomposition, measure-theory]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary

A graduate textbook (CMS/CAIMS Books in Mathematics, Vol. 6) that builds stochastic analysis from Kolmogorov's measure-theoretic foundations up to the general theory of semimartingales under the "usual conditions," with applications to mathematical finance and statistics of random processes. Coverage note: this is a 214-page text; I read the front matter, preface, full contents, the per-chapter abstracts, and Chapters 1-7 in detail from the extracted text (extraction truncated mid-book), supplementing later chapters (8-12) from their table-of-contents structure and chapter abstracts.

## Research question

Not a research paper but a pedagogical synthesis. The organizing thesis: predictability (conditioning on a filtration $(\mathcal{F}_t)$) is the central driver that extends classical probability and stochastic calculus to the largest possible class of processes — semimartingales — which admit a full description in predictable terms and unify discrete- and continuous-time theory. The book asks how to deliver this unified machinery with enough rigor to support genuine applications.

## Method / identification

The development is axiomatic and constructive. It starts from a probability space $(\Omega,\mathcal{F},P)$, motivating the move from a finite-additive "first-level" model on an algebra to the "second-level" $\sigma$-algebra model via the Carathéodory extension theorem and continuity-of-measure equivalences. The Kolmogorov consistency theorem is used to construct measures on $(\mathbb{R}^\infty,\mathcal{B}(\mathbb{R}^\infty))$ and, via Gaussian transition densities $\varphi_t(y\mid x)=(2\pi t)^{-1/2}\exp(-(y-x)^2/(2t))$, the Wiener measure on path space. Random variables, Lebesgue-integral expectations, convergence modes (a.s., in probability, $L^p$, weak/in-distribution), and the Radon-Nikodym theorem and conditional expectation $E(X\mid\mathcal{A})$ follow.

The core machinery is the stochastic basis $(\Omega,\mathcal{F},(\mathcal{F}_t),P)$. Discrete-time martingale theory is developed first (predictability, optional stopping, convergence on finite and infinite horizons), then the classical continuous-time objects: the Wiener process, the Itô stochastic integral, the Itô change-of-variables formula, the Girsanov theorem, and the martingale representation theorem. Stochastic differential equations and diffusion processes are tied to PDEs. The capstone is the general theory under usual conditions: localization (local and locally square-integrable martingales $M_{\text{loc}}$, $M^2_{\text{loc}}$), the optional and predictable $\sigma$-algebras $\mathcal{O}$, $\mathcal{P}$, semimartingale stochastic calculus, and the Doob-Meyer decomposition (stated and proved).

## Data

None — this is a theory/methods monograph. It includes worked examples and an end-of-book set of supplementary problems with hints and solutions (Chapter 12) rather than empirical data.

## Key findings

These are the classical theorems the book proves and unifies, not new results. Foundational: Carathéodory extension theorem (Thm 1.2), Kolmogorov consistency theorem (Thm 1.3) and the construction of Wiener measure. Limit theory: the Central Limit Theorem via weak convergence; martingale convergence theorems and martingale limit theorems with statistical applications. Measure change: the Radon-Nikodym theorem; the discrete-time Girsanov theorem and its financial application; the continuous-time Girsanov theorem. Itô calculus: the Itô formula and the representation of martingales as stochastic integrals with respect to a Wiener process. SDE/diffusion theory and its link to PDEs, with applications to option pricing via controlled diffusions. General theory: stochastic calculus for semimartingales and the Doob-Meyer decomposition (every submartingale of class D decomposes into a martingale plus a predictable increasing compensator). Applications: stochastic mathematical finance and stochastic regression analysis.

## Contribution

A self-contained, unified route from Kolmogorov's axioms to semimartingale calculus that deliberately foregrounds predictability as the unifying concept and keeps discrete and continuous time in parallel. Its distinctive emphasis is pairing the abstract general theory with concrete payoffs in mathematical finance (Girsanov-based pricing, option pricing through controlled diffusions) and in statistics of random processes (martingale limit theory, stochastic regression). It targets senior undergraduates, graduate students, and practitioners, drawing on the author's courses at Moscow State, the Higher School of Economics, Copenhagen, and Alberta.

## Limitations & open questions

As a textbook it states no research open problems; its "open questions" are pedagogical and structural. The treatment stays within the "usual conditions" (right-continuous, completed filtrations), so questions about analysis without these regularity hypotheses are out of scope. The applications chapters (finance, stochastic regression) are introductory illustrations rather than exhaustive, leaving the modeling extensions — incomplete markets, jump/Lévy-driven semimartingales beyond the worked cases, and inference for partially observed diffusions — as natural directions a reader would pursue elsewhere. The supplementary-problems chapter is the explicit hook for deeper independent work.

## Connections

The lineage is Kolmogorov's Grundbegriffe (1933) for the axiomatic foundation and the mid-twentieth-century general theory of processes associated with Doob, Meyer, Dellacherie, and Itô (the Doob-Meyer decomposition, Itô calculus). It sits alongside standard graduate references such as Shiryaev's Probability and the Jacod & Shiryaev semimartingale program, Karatzas & Shreve and Øksendal on Brownian motion and SDEs, and Protter on stochastic integration. On the finance side it connects to the Girsanov/martingale-measure pricing tradition (Harrison & Kreps, Harrison & Pliska) and Black-Scholes-Merton option pricing via controlled diffusions; on the statistics side to Liptser & Shiryaev on statistics of random processes.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
