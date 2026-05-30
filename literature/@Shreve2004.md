---
citekey: Shreve2004
title: "Stochastic calculus for finance II: Continuous-time models"
authors: ["Shreve, Steven E."]
year: 2004
type: book
doi: ""
zotero: "zotero://select/library/items/9KT7K5A8"
pdf: /Users/jesper/Zotero/storage/W3WJBKND/Shreve2004.pdf
tags: [literature]
keywords: [stochastic-calculus, risk-neutral-pricing, brownian-motion, ito-formula, option-pricing, mathematical-finance]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
This is the second volume of Steven Shreve's two-volume graduate text on the mathematics of derivative-security pricing, covering the continuous-time theory. It builds the measure-theoretic probability, Brownian motion, Itô (Itô–Doeblin) stochastic calculus, risk-neutral pricing via Girsanov's theorem, and the partial-differential-equation connections needed to price and hedge options, then applies this machinery to exotic options, American (early-exercise) options, change of numéraire, term-structure/interest-rate models, and jump processes. Because the source is a 518-page textbook, I read it in targeted fashion: the front matter and preface, the chapter-by-chapter "Summary of Volume II," and Chapter 1 (General Probability Theory) in detail, sampling later chapters via the table of contents rather than ingesting every page.

## Research question
Not a research paper but a pedagogical synthesis. The organizing question is: how does one rigorously price and hedge derivative securities in continuous time? Concretely, how do the no-arbitrage and risk-neutral-pricing ideas first seen in the discrete binomial model (Volume I) generalize to continuous-time models driven by Brownian motion (and later by jump processes), and what is the minimal measure-theoretic apparatus required to state and prove the central results (Itô's formula, Girsanov's theorem, the Black–Scholes–Merton equation, the Fundamental Theorems of Asset Pricing)?

## Method / identification
The "method" is the formal mathematical development of stochastic calculus and its application to finance. The text proceeds axiomatically and constructively:

- **Measure-theoretic foundation (Ch. 1–2):** Probability spaces $(\Omega,\mathcal{F},\mathbb{P})$ are built on possibly uncountable sample spaces, with $\sigma$-algebras, Lebesgue integration, and the Radon–Nikodým change of measure. Information is modeled by filtrations and conditioning by conditional expectation.
- **Brownian motion (Ch. 3):** Standard Brownian motion $W_t$ is introduced; its defining property for calculus is the quadratic variation $[W,W]_t=t$, i.e. $(dW_t)^2=dt$.
- **Stochastic calculus (Ch. 4 — the core):** The Itô integral $\int_0^t \Delta_s\,dW_s$ is constructed as a limit of integrals of simple integrands, and the Itô–Doeblin formula is derived: for a $C^{1,2}$ function $f$,
$$df(t,W_t)=f_t\,dt+f_x\,dW_t+\tfrac{1}{2}f_{xx}\,dt.$$
Consequences include Lévy's characterization of Brownian motion via quadratic variation and the Black–Scholes–Merton PDE for a European call.
- **Risk-neutral pricing (Ch. 5):** Girsanov's theorem provides the change from the physical measure $\mathbb{P}$ to an equivalent martingale (risk-neutral) measure $\widetilde{\mathbb{P}}$ under which discounted asset prices are martingales; this yields the two Fundamental Theorems of Asset Pricing (no arbitrage $\Leftrightarrow$ existence of a risk-neutral measure; market completeness $\Leftrightarrow$ uniqueness).
- **PDE connections (Ch. 6):** The Feynman–Kac representation links conditional expectations of diffusions to solutions of parabolic PDEs.
- **Applications (Ch. 7–11):** Exotic options, early exercise/American options (optimal stopping), change of numéraire, Heath–Jarrow–Morton and forward-LIBOR term-structure models, and Poisson/compound-Poisson jump processes with an Itô–Doeblin formula for jump processes and change of measure for jumps.

## Data
None — this is a theoretical/pedagogical text. Empirical material is limited to illustrative examples and end-of-chapter exercises, some drawn from practical quantitative-finance problems.

## Key findings
The central named results developed and proved are: the **Itô–Doeblin formula** (Itô's formula, single and multidimensional, plus a version for jump processes); **Lévy's theorem** characterizing Brownian motion by continuity and quadratic variation $[W,W]_t=t$; the **Black–Scholes–Merton equation** and option-pricing formula; **Girsanov's theorem** for change of measure; the **Martingale Representation Theorem**; the **First and Second Fundamental Theorems of Asset Pricing**; the **Feynman–Kac theorem** connecting diffusions and PDEs; and the construction and properties of **Poisson and compound-Poisson processes** with their moment-generating functions and martingale properties.

## Contribution
The book's contribution is expository rather than original research: it distills the modern theory of continuous-time finance — risk-neutral pricing and stochastic calculus — into a self-contained course requiring only calculus and calculus-based probability as prerequisites, providing precise statements, plausibility arguments, and selected proofs alongside the intuition refined through Carnegie Mellon's Master of Science in Computational Finance program. It is a standard reference for hedging, the Fundamental Theorems of Asset Pricing, and the Itô calculus underpinning quantitative finance.

## Limitations & open questions
As a textbook there are no "open problems" in the research sense; the explicit scoping caveats are pedagogical. The author notes which sections are non-load-bearing and can be skipped (e.g. the Brownian Bridge in Section 4.7, Dividend-Paying Stocks in 5.5), and that Chapters 7 (Exotic Options), 8 (Early Exercise), 10 (Term Structure), and 11 (Jump Processes) are largely self-contained and not used elsewhere. The deeper open directions implicit in the material — incomplete markets, non-uniqueness of the pricing measure under jumps, calibration of term-structure models, and numerical/Monte-Carlo methods — are gestured at but left to specialized literature.

## Connections
The text sits within the lineage opened by Markowitz's *Portfolio Selection* (1952), Sharpe's CAPM, and the work of Merton, who introduced stochastic calculus to finance (1969). Its centerpiece is the option-pricing theory of Black & Scholes (1973) and Merton (1973). The risk-neutral-pricing apparatus rests on Girsanov's theorem and on the Fundamental Theorems of Asset Pricing associated with Harrison & Kreps (1979) and Harrison & Pliska (1981). The PDE link is the Feynman–Kac formula. Volume II is the continuous-time companion to Volume I's binomial model in the spirit of Cox, Ross & Rubinstein (1979). The term-structure chapters draw on Heath, Jarrow & Morton (1992) and the forward-LIBOR (BGM) market models, while the jump-process chapter connects to the broader Lévy-process literature. As a reference it is comparable to Karatzas & Shreve's *Brownian Motion and Stochastic Calculus* and Øksendal's *Stochastic Differential Equations*.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
