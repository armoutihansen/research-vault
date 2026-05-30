---
citekey: Drukker2006
title: Generating Halton Sequences using Mata
authors: ["Drukker, David M.", "Gates, Richard"]
year: 2006
type: journalArticle
doi: 10.1177/1536867X0600600204
zotero: "zotero://select/library/items/RJSNSZ4G"
pdf: /Users/jesper/Zotero/storage/L7Q6SREL/Drukker2006.pdf
tags: [literature]
keywords: [halton-sequences, quasi-monte-carlo, low-discrepancy, maximum-simulated-likelihood, multinomial-probit, ghk-simulator, numerical-integration]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper discusses the advantages of Halton sequences over pseudorandom uniform numbers when using simulation to approximate integrals numerically. We describe two types of sequences and give Mata examples. Finally, we document the Mata function halton(), currently in release 9.1 of Stata, which computes both a Halton sequence and its Hammersley variant. Options to use these point sets are available in the Stata 9 program asmprobit, a multinomial-probit estimator, and in the Stata 9.1 Mata function ghk(), the Geweke–Hajivassiliou–Keane multivariate-normal simulator.

## Summary
This is a Stata Journal software-documentation article that explains why *quasirandom* Halton and Hammersley point sets give more accurate quasi-Monte Carlo (QMC) approximations to multidimensional integrals than pseudorandom uniform draws — but only in low dimensions. It reviews the number-theoretic construction of the sequences, derives the discrepancy bounds that govern integration error, documents the Mata functions `halton()` and `ghalton()` (used internally by `asmprobit` and `ghk()`), and runs simulations showing that pseudorandom draws overtake Halton/Hammersley somewhere around dimension $d=10$.

## Research question
When approximating a high-dimensional integral by simulation (e.g., the multivariate-normal integral in a multinomial probit likelihood), which point set gives the most accurate approximation for a given number of draws $n$ and dimension $d$? Specifically: when do low-discrepancy Halton/Hammersley sequences beat ordinary pseudorandom uniform draws, and where does that advantage break down?

## Method / identification
The paper is grounded in QMC integration theory. To integrate $g(x)$ over $x\in\mathbb{R}^d$, the domain is transformed to the unit cube $C^d=[0,1)^d$ and the integral $\int_{C^d} f(y)\,dy$ is approximated by the sample mean $\frac{1}{n}\sum_{i=1}^n f(u_i)$ over a point set $\{u_i\}$. Approximation accuracy is governed not by randomness but by *uniform coverage*, measured by the **star discrepancy**. In one dimension, for $\chi_n=\{x_i\in[0,1)\}$ and $N(u,\chi_n)$ counting points $\le u$,
$$D(n,\chi_n)=\sup_{u\in[0,1)}\left|\frac{N(u,\chi_n)}{n}-u\right|,$$
generalized in $d$ dimensions using the box volume $\nu(u)=\prod_{i=1}^d u_i$. The **Koksma–Hlawka-type bound** ties integration error to discrepancy:
$$\left|\frac{1}{n}\sum_{i=1}^n f(x_i)-\int_{C^d} f(y)\,dy\right|\le V(f)\,D(n,\chi_n^d),$$
where $V(f)$ is the total variation of $f$.

Construction: the $i$th Halton point in base $p$ (prime) is the **radical inverse** of $i$'s base-$p$ digit expansion $i=\sum_{j=1}^q b_{j,p}(i)\,p^{j-1}$,
$$r_p(i)=\sum_{j=1}^{q}\frac{b_{j,p}(i)}{p^{j}}.$$
A $d$-dimensional Halton set uses the first $d$ primes: $h_i=\{r_{p_1}(i),\dots,r_{p_d}(i)\}$. The **Hammersley** variant replaces the first dimension with the minimal-discrepancy evenly spaced sequence $(2i-1)/(2n)$ and uses the first $d-1$ Halton sequences for the remaining dimensions. The paper gives two Mata algorithms: (1) a direct digit-expansion loop, and (2) an incremental "rightward carry" recursion from Wang & Hickernell (2000) computing $r_p(i+1)$ from $r_p(i)$ via $r_p(i+1)=r_p(i)+(1+p)/p^k-1$ for the appropriate $k$. Randomized Halton sequences are produced by shifting with a uniform draw $u$, e.g., $\{r_p(i)+u\}$ (Train 2003).

## Data
None — no empirical dataset. Evidence comes from Monte Carlo simulation experiments. The authors estimate discrepancy by partitioning $C^d$ into $q^d$ subintervals (using $q=10$), generating uniform vectors within each grid cell, and performing a randomized local search of width $2/n$ for the discrepancy-maximizing vector. Experiments run for $n\in\{50,\dots,500\}$ and $d=2,\dots,6$, with up to hundreds of millions of uniform vectors generated per estimate at $d=6$.

## Key findings
- **Discrepancy bounds.** Uniform point sets satisfy $D(n,U_n^d)\le K\sqrt{\log\log n / n}$, a bound *independent of $d$*. Halton and Hammersley sets satisfy $D(n,H_n^d)\le C_H(d)(\log n)^d/n$ and $D(n,\tilde H_n^d)\le C_{\tilde H}(d)(\log n)^{d-1}/n$, where the constants $C_H(d),C_{\tilde H}(d)$ grow *exponentially* in $d$. Hence low-discrepancy sequences help only for small $d$.
- **Simulated crossover.** For $d\le 6$ and moderate $n$, Halton and Hammersley discrepancies are well below uniform (e.g., at $d=4,n=200$: Halton $\approx0.051$, Hammersley $\approx0.038$, uniform $\approx0.108$). Hammersley edges out Halton in most cases. The authors *conjecture* pseudorandom sets overtake both for $d>10$.
- **Large-prime correlation.** Halton sequences from large primes (those used for dimensions $13$–$16$, i.e., $41,43,47,53$) become highly correlated due to long periods — e.g., a correlation of $0.4442$ between the primes-41/43 dimensions — degrading coverage below that of pseudorandom draws. This is why `asmprobit` defaults to Hammersley and why pseudorandom draws are recommended for more than ~10 alternatives.

## Contribution
Provides an accessible, self-contained exposition of QMC integration and the number-theoretic construction of Halton and Hammersley point sets, plus production Mata implementations (`halton()`, the in-place `_halton()`, and `ghalton()`) shipped in Stata 9.1. It documents the practical rationale behind Stata's `asmprobit` defaults and gives applied econometricians using maximum simulated likelihood concrete guidance on point-set choice as a function of integral dimension.

## Limitations & open questions
- The simulated-discrepancy algorithm "works only moderately well" — estimates vary noticeably between replications, and the authors caution it is good enough only to *illustrate* the theory, not to pin down the bounds precisely.
- The crossover dimension ($d\approx10$) is a **conjecture**, not established: simulating beyond $d=6$ at fixed $q$ becomes computationally intractable because the grid count $q^d$ explodes.
- The authors explicitly flag two directions for **future work**: (1) seeking stronger evidence for the $d>10$ crossover conjecture, and (2) finding *other* low-discrepancy/quasirandom sequences whose point sets remain well-behaved in higher dimensions (where Halton's large-prime correlation problem bites).

## Connections
The QMC and discrepancy theory rests on Niederreiter (1992) and Fang & Wang (1994); the minimal-discrepancy $(2i-1)/2n$ sequence feeding the Hammersley first dimension comes from the latter. The incremental radical-inverse recursion and the randomization scheme are from Wang & Hickernell (2000), with an alternative shift-based randomization from Train (2003), the standard reference for simulation-based discrete choice and maximum simulated likelihood. The motivating application — approximating the multivariate-normal integral via the Geweke–Hajivassiliou–Keane (GHK) simulator inside a multinomial probit estimator — connects to Genz (1992) on numerical computation of multivariate normal probabilities. The paper is methodologically upstream of any structural choice-estimation work that relies on simulated likelihood, including mixed logit and multinomial probit applications in the discrete-choice and social-preference estimation literatures.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
