---
citekey: Melnikov2023
title: A Course of Stochastic Analysis
authors: ["Melnikov, Alexander"]
year: 2023
type: book
doi: 10.1007/978-3-031-25326-3
zotero: "zotero://select/library/items/HSPE7WDC"
pdf: /Users/jesper/Zotero/storage/PBXBVB94/Melnikov - 2023 - A Course of Stochastic Analysis.pdf
tags: [literature]
keywords: [stochastic-analysis, martingales, semimartingales, stochastic-calculus, mathematical-finance, change-of-measure, martingale-limit-theory]
topics: []
related: []
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> _No abstract in source metadata; see Summary below._

## Summary

*Coverage: targeted reading of a 214-page graduate monograph — front matter, preface, the full table of contents and per-chapter abstracts, plus a TOC-led sample of the discrete-time martingale core (Ch. 6–7), the continuous-time / semimartingale culmination (Ch. 8–10), and the two applications chapters (mathematical finance and stochastic regression). Not a page-by-page ingest.*

This is a self-contained graduate textbook (CMS/CAIMS Books in Mathematics, Vol. 6) that builds *stochastic analysis* from Kolmogorov's axioms up to the general theory of semimartingales, organized around a single unifying object: the *stochastic basis* $(\Omega,\mathcal{F},(\mathcal{F}_t),P)$, a probability space equipped with an information flow (filtration) $(\mathcal{F}_t)$. Melnikov's pedagogical thesis is that once deterministic numerical characteristics (mean, variance) are replaced by their conditional versions with respect to $(\mathcal{F}_t)$, *predictability* becomes the driver that extends stochastic calculus to the largest tractable process class — semimartingales — which simultaneously unify discrete- and continuous-time processes and admit a full description in predictable terms. The book deliberately develops the discrete-time martingale theory first (so all key ideas appear without measure-theoretic heavy machinery), then re-derives them in continuous time, and closes with applications in mathematical finance and statistics of random processes.

## Research question

This is a textbook, not a research paper, so there is no single hypothesis. Its organizing question is methodological: *what is the minimal unified apparatus that captures both discrete- and continuous-time stochastic dynamics, and how far does the martingale/semimartingale framework extend before it breaks?* The answer it develops: filtration + predictability + the martingale property, generalized via localization to local martingales and then to semimartingales.

## Method / identification

The book is theorem–proof mathematics. The backbone constructs, in order:

- **Stochastic basis and stopping times.** A filtration $(\mathcal{F}_n)$ with $\mathcal{F}_\infty=\sigma(\cup_n\mathcal{F}_n)$; a random time $\tau$ is a *stopping time* if $\{\tau\le n\}\in\mathcal{F}_n$ for all $n$, with the pre-$\tau$ $\sigma$-algebra $\mathcal{F}_\tau=\{A\in\mathcal{F}_\infty: A\cap\{\tau\le n\}\in\mathcal{F}_n\}$.
- **Martingales and predictability.** $(X_n)$ adapted with $X_n\in\mathcal{F}_n$; martingale, sub- and supermartingale defined via $E(X_n\mid\mathcal{F}_{n-1})$.
- **Change of measure machinery.** For $\tilde{P}\ll P$ with restrictions $\tilde{P}_n\ll P_n$, the *local density* $Z_n=\mathrm{d}\tilde{P}_n/\mathrm{d}P_n$ is itself a martingale, $E(Z_n\mid\mathcal{F}_{n-1})=Z_{n-1}$, and conditional expectations transform by the rule $\tilde{E}(Y\mid\mathcal{F}_{n-1})=Z_{n-1}^{-1}E(YZ_n\mid\mathcal{F}_{n-1})$ — the discrete prototype of Girsanov.
- **Doob decomposition** of a submartingale $X_n=X_0+A_n+M_n$ into a predictable increasing $A_n$ and a martingale $M_n$; its continuous-time analogue is the *Doob–Meyer decomposition* (Ch. 10), proved in full.
- **Quadratic characteristic / compensator** $\langle X,X\rangle$ and quadratic bracket $[X,Y]$, the predictable objects in terms of which limit behavior is characterized.
- **Continuous-time layer (Ch. 8–9):** the Wiener process, the Itô stochastic integral, the Itô change-of-variables formula, the (continuous) Girsanov theorem, martingale representation, stochastic differential equations, diffusion processes and their link to PDEs, and controlled diffusions for option pricing.
- **General theory (Ch. 10):** localization extends martingale theory to *local martingales* $\mathcal{M}_{\mathrm{loc}}$ and *locally square-integrable* $\mathcal{M}^2_{\mathrm{loc}}$, then to semimartingales and stochastic calculus for them; the optional $\mathcal{O}$ and predictable $\mathcal{P}$ $\sigma$-algebras supply the regularity scaffolding under the "usual conditions."

A representative formal result is the **Strong Law of Large Numbers for martingales** (Theorem 7.1): for a non-negative predictable non-decreasing $(A_n)$ with $A_\infty=\infty$ (a.s.) and a square-integrable martingale $(M_n)$, $M_0=0$, satisfying $\sum_{n\ge1}\Delta\langle M,M\rangle_n / A_n^2<\infty$ (a.s.), one has $A_n^{-1}M_n\to 0$ (a.s.). It is proved via a *stochastic Kronecker lemma* (Lemma 7.2) and the convergence-set lemma $\{\langle X,X\rangle_\infty<\infty\}\subseteq\{X_n\to\}$ (Lemma 7.1).

## Data

No empirical data. This is a pure theory/methodology textbook; the only "data" are illustrative worked examples and an end-of-book set of supplementary problems with hints and solutions (Ch. 12).

## Key findings

The "findings" are the catalogued and unified classical results, not new theorems. Notable named results and their content:

- **Strong LLN for martingales** (Thm 7.1) and its corollary recovering **Kolmogorov's strong LLN** for independent summands as the special case $A_n=n$, $M_n=\sum_{i=1}^n Y_i$, under the variance condition $\sum_n\sigma_n^2/n^2<\infty$.
- **Convergence-set characterization** in predictable terms: for $C^+$-class submartingales with Doob decomposition $X_n=X_0+A_n+M_n$, $\{X_n\to\}=\{\sup_n X_n<\infty\}=\{A_\infty<\infty\}$ (a.s.) (Thm 7.2).
- **Statistical application:** strong consistency of the least-squares estimate $\theta_n=(\sum_{i=0}^n f_i^2)^{-1}\sum_{i=0}^n f_i x_i$ in the regression $x_n=f_n\theta+e_n$ with martingale-difference errors and predictable regressor — recovering, for $f_n=x_{n-1}$, the classical AR(1) consistency condition $\sum x_{i-1}^2=\infty$. Ch. 11 extends this via a CLT for martingales to asymptotic normality of *martingale stochastic-approximation* procedures.
- **Discrete-time Girsanov theorem** and its use to derive a **discrete-time Bachelier option-pricing formula**; the continuous-time chapters give the Itô formula, the Girsanov/Cameron–Martin change of drift, the martingale representation theorem, and arbitrage-free pricing of options via controlled diffusions.
- **Foundational results:** Carathéodory extension theorem, Kolmogorov consistency theorem and the construction of Wiener measure (Ch. 1), the Radon–Nikodym theorem (Ch. 5), and the **Doob–Meyer decomposition** (Ch. 10) as the continuous-time culmination supplying the compensator that underlies semimartingale calculus.

## Contribution

A unified, classroom-tested account that threads one methodology (filtration + predictability + martingale localization) from elementary probability to semimartingales, and crucially keeps mathematical finance and statistics of random processes as first-class applications rather than afterthoughts. Its distinctive pedagogy is the discrete-time-first scaffolding: every analytic idea (densities/Girsanov, Doob decomposition, quadratic characteristic, convergence sets, LLN/CLT) appears first as an elementary discrete statement, then is lifted to continuous time. It draws on the author's courses at Moscow State, the Higher School of Economics, Copenhagen, and Alberta, and targets senior undergraduates through practitioners.

## Limitations & open questions

By design a consolidating textbook, it does not advance the frontier and is a *reference/methods source* only loosely tied to the vault's core program (social/other-regarding preferences, discrete-choice and structural choice modelling, belief elicitation and proper scoring rules, ML-for-theory). Its closest legitimate hook is methodological infrastructure for *dynamic/sequential models*: the martingale CLT and martingale stochastic-approximation results bear on the asymptotics of recursive estimators and online learning, and the change-of-measure (Girsanov) apparatus underlies likelihood-ratio and importance-sampling arguments. The treatment stays within the "usual conditions" (right-continuous, completed filtrations), so analysis without these regularity hypotheses is out of scope. Directions the text flags but does not pursue: sharper martingale-convergence conditions beyond the square-integrable case; the §7.3 extensions (asymptotic martingales, martingale transforms, generalized martingales); and the gap between the discrete Bachelier pricing it derives and full continuous semimartingale market models (incomplete markets, jump/Lévy drivers, inference for partially observed diffusions).

## Connections

The lineage is canonical stochastic analysis: Kolmogorov's *Grundbegriffe* (1933) for the axioms, Doob for the martingale convergence and decomposition theory, Meyer and Dellacherie for the "general theory" and the Doob–Meyer decomposition and semimartingales, and Itô for the stochastic integral and change-of-variables formula; change of measure traces to Girsanov and Cameron & Martin. It sits alongside standard graduate references — Shiryaev's *Probability*, the Jacod & Shiryaev semimartingale program, Karatzas & Shreve and Øksendal on Brownian motion and SDEs, and Protter on stochastic integration. On the finance side it connects to Black, Scholes & Merton (1973) option pricing and the martingale-measure pricing tradition of Harrison & Kreps and Harrison & Pliska; on the statistics side to Liptser & Shiryaev on statistics of random processes and the Robbins & Monro stochastic-approximation lineage. Within the vault it is methods-adjacent to any work using martingale-difference asymptotics, recursive/stochastic-approximation estimators, or likelihood-ratio change-of-measure arguments.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
