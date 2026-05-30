---
citekey: Lippman2005
title: C++ Primer
authors: ["Lippman, Stanley B.", "Lajoie, Josée", "Moo, Barbara E."]
year: 2005
type: book
doi: ""
zotero: "zotero://select/library/items/7KLZPV6W"
pdf: /Users/jesper/Zotero/storage/T8JKP7SP/Lippman2005.pdf
tags: [literature]
keywords: [cpp, programming-reference, software-engineering, c++11, scientific-computing, textbook]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
This is *C++ Primer* by Lippman, Lajoie, and Moo — a comprehensive tutorial-and-reference textbook on the C++ programming language, not a research article. The PDF in the library is the Fifth Edition (copyright 2013, covering C++11), despite the `2005` citekey/year metadata in Zotero (likely a mismatch with an earlier edition's date). At 969 pages it teaches modern C++ from first principles through advanced facilities. It is an outlier in this otherwise economics/choice-modeling library and is best treated as a software-engineering reference for implementing computational research code (estimators, simulations, performance-critical tooling). Coverage note: given the 969-page length, this note is based on a targeted read — front matter (title/copyright/Preface), the full table of contents (parts and chapters), and sampled back-matter (Appendix A, the defined-terms glossary); chapter bodies were not ingested exhaustively.

## Research question
None — this is a pedagogical reference text, not an investigation. Its implicit "question" is practical: how does one write correct, idiomatic, efficient modern (C++11) C++, and how do the language's core constructs and standard library compose? It targets readers with some prior programming experience who want a thorough, example-driven path to fluency.

## Method / identification
None in the empirical sense. The book's "method" is its expository structure: a layered curriculum that introduces each construct with motivation, complete compilable examples, "Best Practices," "Warning," and "Note" sidebars, and end-of-chapter "Defined Terms" glossaries and exercises. The organization proceeds in four parts after an introductory Chapter 1 (Getting Started):

- **Part I — The Basics:** Variables and Basic Types (Ch. 2), Strings/Vectors/Arrays (Ch. 3), Expressions (Ch. 4), Statements (Ch. 5), Functions (Ch. 6), Classes (Ch. 7).
- **Part II — The C++ Library:** IO Library (Ch. 8), Sequential Containers (Ch. 9), Generic Algorithms (Ch. 10), Associative Containers (Ch. 11), Dynamic Memory (Ch. 12).
- **Part III — Tools for Class Authors:** Copy Control (Ch. 13), Overloaded Operations and Conversions (Ch. 14), Object-Oriented Programming (Ch. 15), Templates and Generic Programming (Ch. 16).
- **Part IV — Advanced Topics:** Specialized Library Facilities (Ch. 17), Tools for Large Programs (Ch. 18), Specialized Tools and Techniques (Ch. 19).

It closes with appendices (e.g., Appendix A on the library, library names and headers) and a substantial glossary of defined terms.

## Data
None — no datasets. The "data" are illustrative code listings (e.g., the recurring `Sales_item`/`Sales_data` bookstore running example introduced in Chapter 1) used to demonstrate language features.

## Key findings
Not findings but the core pedagogical content. The Fifth Edition is built around C++11 and emphasizes modern idioms throughout, including: `auto` type deduction and `decltype`; range-based `for`; uniform `{}` initialization and initializer lists; `constexpr` and constant expressions; smart pointers (`shared_ptr`, `unique_ptr`, `weak_ptr`) for dynamic memory management; move semantics and rvalue references; `nullptr`; the standard containers and the generic-algorithm/iterator model; lambda expressions; templates and variadic templates; and the rule that copy control (copy/move constructors, assignment, destructor) be designed coherently. It stresses safe, library-first style (preferring `string`/`vector` over C-style arrays, smart pointers over raw `new`/`delete`).

## Contribution
A widely used, authoritative introduction to standard C++ co-authored by Lippman (a member of the original C++ team) and Moo. Its contribution is didactic and practical rather than scholarly: it lowers the barrier to writing correct, idiomatic C++11 and serves as a durable desk reference. For this vault, its relevance is instrumental — supporting the implementation of performance-sensitive research software (e.g., maximum-likelihood estimation routines, agent-based or Monte Carlo simulations of choice/social-preference models) where C++ is chosen over R/Python for speed.

## Limitations & open questions
As a textbook it states no open research problems. Practical limitations worth flagging: (1) it predates C++14/17/20/23, so newer language and library features are absent; (2) it is a language reference, not a guide to numerical methods, econometrics, or scientific-computing libraries (no Eigen, BLAS/LAPACK, or statistical tooling) — those must be sourced elsewhere; (3) the Zotero entry has no abstract and a `2005` year that conflicts with the Fifth Edition's 2013 content, so the citation metadata should be corrected. Project-idea hook: this is the natural reference if a project decides to push a bottleneck estimator or simulation into compiled C++ (potentially via Rcpp or pybind11 bindings).

## Connections
This title sits outside the substantive research literature of the vault and connects instead to the computational-tooling layer. Within the C++ canon it is a companion to Stroustrup's *The C++ Programming Language* and *A Tour of C++*, and to Meyers' *Effective C++* / *Effective Modern C++*; the standard-library coverage parallels Josuttis' *The C++ Standard Library*. For research applications it would interface with R via Eddelbuettel & François' Rcpp and with Python via pybind11. No direct intellectual link to the social-preference or stochastic-choice papers in this library; its role is methodological/infrastructural.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
