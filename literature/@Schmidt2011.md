---
citekey: Schmidt2011
title: Maß und Wahrscheinlichkeit
authors: ["Schmidt, Klaus D."]
year: 2011
type: book
doi: 10.1007/978-3-642-21026-6
zotero: "zotero://select/library/items/S8FG7PPW"
pdf: /Users/jesper/Zotero/storage/Y3S3ST4U/Schmidt - 2011 - Maß und Wahrscheinlichkeit.pdf
tags: [literature]
keywords: [measure-theory, probability-theory, lebesgue-integration, conditional-expectation, central-limit-theorem, martingales, textbook]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary

Klaus D. Schmidt's *Maß und Wahrscheinlichkeit* (2nd ed., Springer-Lehrbuch, 2011) is a ~480-page German graduate textbook that develops probability theory from its rigorous measure-theoretic foundations. It is explicitly positioned in the tension between theory and application: measure and integration theory (plus a working amount of topology) are treated as the indispensable substrate on which probability — independence, conditional expectation, conditional distributions, and special univariate/multivariate distributions — is then built. The pedagogical credo is *not* to rush to important results, but to "illuminate" each concept together with its typical proof methods before introducing the next, so the reader can later discover and prove new, application-specific results. The book spans five parts: set systems and mappings, measure theory, integration theory, probability theory, and advanced probability (generating functions, weak convergence/CLT, conditional expectation and martingales, Kolmogorov's theorem). Because this is a 489-page reference text, this note is based on a targeted reading: front matter, prefaces, the *Einleitung*, the full table of contents, and chapter-opening framing — not a line-by-line ingestion.

## Research question

Not a research paper but a textbook; its organizing question is pedagogical and architectural: how to present the foundations of probability theory in the field of tension between mathematical generality and the needs of applications (notably statistics and actuarial/insurance mathematics), giving equal weight to *results* and to the *proof techniques* that let a reader extend the theory. The author frames himself as belonging more to "applied pure mathematics" than "pure applied mathematics," and consciously balances the drive toward maximal generality against restriction to the essentials.

## Method / identification

The method is the standard axiomatic–deductive exposition of measure-theoretic probability, with a distinctive structural choice: topologies and $\sigma$-algebras are introduced *in parallel* (Part I), exploiting their analogies, because both are typically defined indirectly via a smaller generating system. The build is strictly bottom-up:

- **Part I — Set systems and mappings:** topologies, $\sigma$-algebras, Dynkin systems, $\cap$-stable systems, semirings and rings; measurable spaces and measurable maps; product spaces and projections.
- **Part II — Measure theory:** set functions (contents, measures, signed measures); extension of measures (uniqueness theorem, outer measures, existence/Carathéodory, approximation, construction of Lebesgue measure); transformation of measures (image measures, translation-invariant measures on $\mathcal{B}(\mathbb{R}^n)$, linear images of Lebesgue measure).
- **Part III — Integration theory:** measurable functions; the Lebesgue integral built from positive simple functions $\to$ positive measurable functions $\to$ integrable functions $\to$ $L^p$-spaces; computation of the integral (measures with densities, absolutely continuous vs. singular measures, image/restricted measures, product measures and Fubini, Lebesgue vs. Riemann integral).
- **Part IV — Probability theory:** probability spaces and random variables, discrete and symmetric spaces, finite and projective families (theorem of Andersen/Jessen); independence of events, event systems, and random variables; univariate and multivariate distributions with moments and central moments; modes of convergence (a.s., stochastic, $L^p$); laws of large numbers (weak, strong, Glivenko/Cantelli, random walks).
- **Part V — Advanced probability:** generating functions (probability-, moment-, cumulant-generating, and characteristic functions); weak convergence, tightness, and the central limit theorem; conditional expectation (as projection) and martingales; conditional probability, conditional independence, conditional distribution and density; regularity and Kolmogorov's extension theorem.

Exposition proceeds by definitions, worked examples, and a large stock of exercises ("Aufgaben") that double as entry points to specialized topics beyond the book's scope.

## Data

None — this is a pure-mathematics textbook. There are no datasets or empirical estimation. The "data" are illustrative examples and exercises, many drawn from statistics and insurance mathematics, used to motivate and exercise the abstract machinery.

## Key findings

As a textbook it presents the canonical theorems of measure-theoretic probability rather than new results. The named landmarks it develops include: the **uniqueness theorem** and **Carathéodory existence/extension theorem** for measures, and the **construction of Lebesgue measure**; the convergence theorems of Lebesgue integration (monotone convergence, Fatou, dominated convergence) and the **Radon–Nikodým** distinction between absolutely continuous and singular measures; **Fubini/Tonelli** for product measures; the **theorem of Andersen/Jessen** on projective families; the **laws of large numbers** including the **Glivenko–Cantelli theorem**; the analytic theory of **characteristic functions** and the **central limit theorem** via weak convergence and tightness; the construction of **conditional expectation as an $L^2$ projection** and the resulting theory of **martingales**; **regular conditional distributions**; and the **Kolmogorov extension theorem** for constructing stochastic processes from consistent finite-dimensional distributions. Two stated conventions are used throughout: $0/0 := 0$ and $0^0 := 1$, and "positive" means $\geq 0$.

## Contribution

A self-contained, carefully sequenced German-language bridge from measure and integration theory to probability, with topology folded in only where genuinely needed (Borel $\sigma$-algebra, Lebesgue measure, construction of stochastic processes). Its distinctive contributions as a teaching text are (i) the parallel treatment of topologies and $\sigma$-algebras, (ii) the deliberate emphasis on proof methods over speed-to-results, and (iii) the unusually thorough treatment of univariate *and* multivariate distributions and of conditional expectation/distribution, oriented toward applications in statistics and actuarial mathematics. It serves as a foundational reference for the probabilistic apparatus underlying econometrics and choice modeling.

## Limitations & open questions

By design the book restricts generality "to the essentials" and stops at the foundations: it explicitly leaves specialized topics and applications to the exercises and to further study, noting these go "beyond the scope of this book." Continuous-time stochastic processes, ergodic theory, and advanced stochastic-process theory are gestured at (via Kolmogorov's theorem) but not developed. The author flags the standing tension — generality vs. essentials — as itself an open editorial judgment rather than a solved problem. For a quantitative researcher the open hooks are thus less "unsolved problems" than pointers: the exercises on insurance/statistics applications, and the construction of stochastic processes, are natural launch points into applied probability.

## Connections

This is a foundational reference rather than a contribution to the social-preference / choice-modeling literature, but it underpins the measure-theoretic machinery those literatures presuppose. It sits alongside standard references such as Billingsley's *Probability and Measure*, Durrett's *Probability: Theory and Examples*, Bauer's *Maß- und Integrationstheorie* and *Wahrscheinlichkeitstheorie*, Klenke's *Wahrscheinlichkeitstheorie*, and Kallenberg's *Foundations of Modern Probability* — all developing the same measure–integration–probability arc (Carathéodory extension, Radon–Nikodým, Fubini, Kolmogorov's theorem, martingales, CLT). The conditional-expectation-as-projection and martingale material connects to the probabilistic foundations used in econometric identification and in random-utility/stochastic-choice models (e.g., the measure-theoretic treatment of distributions over choice underlying work in the tradition of McFadden's random utility framework). The author's actuarial orientation links it to risk and insurance-mathematics applications.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
