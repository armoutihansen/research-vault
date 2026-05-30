---
citekey: Stewart2012
title: "Calculus: early transcendentals"
authors: ["Stewart, James"]
year: 2012
type: book
doi: ""
zotero: "zotero://select/library/items/M5NBKNBL"
pdf: /Users/jesper/Zotero/storage/3UY5HPSG/Stewart - 2012 - Calculus early transcendentals.pdf
tags: [literature]
keywords: [calculus, mathematics-reference, optimization, integration, differentiation, taylor-series]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
This is James Stewart's *Calculus: Early Transcendentals* (7th ed., Cengage Learning, 2012), the standard one-/two-semester university calculus textbook rather than a research paper. It develops the full single-variable and multivariable calculus sequence — limits, differentiation, integration, sequences and series, vector geometry, partial derivatives, multiple integrals, and vector calculus — in the "early transcendentals" ordering, where exponential, logarithmic, and inverse-trigonometric functions are introduced near the start so they can be used throughout. The text is reference material in the vault, not a primary research source; this note characterizes its scope and the results most relevant to applied/economic modeling.

## Research question
Not a research paper. The pedagogical goal is to teach the concepts, techniques, and applications of differential and integral calculus, building mathematical literacy and the analytic toolkit (rates of change, accumulation, optimization, approximation, infinite series) used across the quantitative sciences and economics.

## Method / identification
Expository and constructive. Concepts are introduced informally (the "rule of four": numerical, graphical, algebraic, verbal) and then formalized. Core machinery developed in order:
- **Limits and continuity** via the $\varepsilon$-$\delta$ definition: $\lim_{x\to a} f(x)=L$ iff for every $\varepsilon>0$ there is $\delta>0$ with $0<|x-a|<\delta \Rightarrow |f(x)-L|<\varepsilon$.
- **Derivative** as a limit of difference quotients, $f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$, with the product, quotient, and chain rules, implicit and logarithmic differentiation.
- **Definite integral** as a limit of Riemann sums, $\int_a^b f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^n f(x_i^*)\,\Delta x$.
- **Series convergence** tests (integral, comparison, alternating, ratio, root) and power/Taylor expansions.
- **Multivariable** extension: partial derivatives, gradients, constrained optimization, and the integral theorems of vector calculus.
Each technique is stated as a rule/theorem, justified, and drilled through worked examples and exercises.

## Data
None — it is a textbook. Applications use stylized or illustrative datasets and modeling vignettes (population growth, predator–prey dynamics, the Gini index, economics-and-biology applications) rather than empirical data.

## Key findings
Named theorems and results, by area:
- **Fundamental Theorem of Calculus (FTC):** if $f$ is continuous on $[a,b]$ and $g(x)=\int_a^x f(t)\,dt$, then $g'(x)=f(x)$; and $\int_a^b f(x)\,dx=F(b)-F(a)$ for any antiderivative $F$.
- **Mean Value Theorem:** for $f$ continuous on $[a,b]$ and differentiable on $(a,b)$, there is $c$ with $f'(c)=\frac{f(b)-f(a)}{b-a}$.
- **Chain Rule** and **l'Hospital's Rule** for indeterminate forms.
- **Taylor / Maclaurin series:** $f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n$, with convergence criteria and the binomial series.
- **Lagrange multipliers** for constrained optimization: extremize $f$ subject to $g=k$ where $\nabla f=\lambda\nabla g$.
- **Vector-calculus integral theorems:** Green's Theorem, Stokes' Theorem, and the Divergence Theorem, unifying line, surface, and volume integrals.

## Contribution
A comprehensive, widely adopted reference and pedagogical standard. For this vault its value is as a lookup for the calculus underlying economic theory and choice/structural modeling — derivatives and gradients for optimization and comparative statics, integrals for expected-utility and welfare computations (e.g., the Gini index appears as an application), Taylor approximation for local analysis, and Lagrange multipliers for constrained-optimization problems pervasive in microeconomics and estimation.

## Limitations & open questions
As a textbook it poses no research open problems. Scope limits worth noting for vault use: it stays at the calculus level and does not develop measure theory, real analysis rigor beyond $\varepsilon$-$\delta$, or the probability/optimization theory needed for econometrics and structural estimation; those require dedicated analysis, probability, and convex-optimization references. The "Problems Plus" and applied-project sections are the closest thing to open-ended hooks.

## Connections
This title is a reference rather than part of the social-preferences / choice-modeling literature that dominates the vault, so it has no direct citation neighbors there. It is the mathematical prerequisite layer beneath that work: the optimization and approximation tools it teaches (gradients, Lagrange multipliers, Taylor expansion) underlie utility maximization and comparative statics, and connect naturally to dedicated treatments of convex optimization (Boyd & Vandenberghe) and mathematics-for-economists references (e.g., Simon & Blume). Its probability application section is a primitive precursor to the probability and measure-theoretic foundations used in choice modeling and econometrics.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
