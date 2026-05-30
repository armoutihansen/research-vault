---
citekey: Stroustrup2013
title: The C++ Programming Language
authors: ["Stroustrup, Bjarne"]
year: 2013
type: book
doi: ""
zotero: "zotero://select/library/items/9GQUXWDB"
pdf: /Users/jesper/Zotero/storage/C4MI3WVY/Stroustrup2013.pdf
tags: [literature]
keywords: [cpp, programming-language, zero-overhead-principle, generic-programming, object-oriented-programming, standard-template-library, language-design]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
This is Bjarne Stroustrup's definitive fourth-edition reference and tutorial for the C++ programming language, updated to cover the C++11 standard (ISO/IEC 14882:2011). It is a 1366-page book by the language's designer, not a research paper. It combines a tutorial "Tour of C++" with an exhaustive reference manual for both the core language and the standard library. The book articulates C++'s design philosophy — multi-paradigm support (procedural, data-abstraction, object-oriented, and generic programming) governed by a "zero-overhead" principle — and serves as a near-authoritative description of the language alongside the ISO standard itself. Coverage note: as a reference work of this length, I read targeted material (front matter, Introduction/Notes-to-the-Reader, the §1.2 "Design of C++" discussion, and the References) rather than the full text.

## Research question
None in the academic sense. As a designer's reference, the book's organizing question is pragmatic and didactic: how should a working programmer understand and use C++11's facilities, and what design rationale ("ideas in code") underlies them? Stroustrup frames the purpose of a programming language as performing two tasks — providing a vehicle to specify machine actions and providing a set of concepts for thinking about what can be done.

## Method / identification
Not applicable — there is no formal model, estimator, or experimental design. The "method" is expository. The book deliberately blends two genres that Stroustrup contrasts explicitly: a pure tutorial (topics ordered so no concept is used before introduction, readable linearly from page one) and a pure reference manual (accessible at any point, each topic described succinctly with forward/backward cross-references). It opens with a four-chapter "A Tour of C++" (basics; abstraction mechanisms; containers and algorithms; concurrency and utilities), then proceeds to detailed language chapters and standard-library chapters (e.g., Chapter 30 Standard-Library Overview, Chapter 31 STL Containers). The exposition is driven by worked code examples and design rationale rather than by proofs or data.

## Data
None — this is a language reference and tutorial. Its "evidence" is illustrative code and accumulated design experience, not empirical data.

## Key findings
There are no theorems or empirical results; instead the book advances a coherent set of design positions that function as its core claims:
- **Multi-paradigm synthesis.** C++ supports procedural, data-abstraction (class-oriented), object-oriented, and generic programming styles, and these are meant to be used together; focusing exclusively on one (e.g., calling C++ "an object-oriented language") is characterized as a mistake leading to inflexible, verbose, poorly performing, or unmaintainable code.
- **Zero-overhead principle.** Abstractions should impose no runtime cost relative to equivalent hand-written code, and unused features should cost nothing. Stroustrup describes this and related "Draconian" principles as repeatedly pushing C++ toward simpler, more elegant, and more powerful facilities — citing the STL as a prime example.
- **Close to the machine, high in expressiveness.** Inheriting C's machine-level efficiency, C++ aims to let programmers express ideas at a high level (via classes, hierarchies, templates) while remaining efficient — targeting systems programming and resource-constrained, high-performance contexts.
- **Features serve styles.** Language features exist to support programming techniques (memory, mutability, abstraction, resource management, algorithm expression, error handling, modularity), not as standalone solutions.
- **C++11 modernization.** The edition adopts C++11 idioms throughout (e.g., {}-style brace initializers, `using` type aliases, move semantics, concurrency support), presenting them as the most elegant expression of fundamental ideas rather than novelty for its own sake.

## Contribution
The book's contribution is canonical documentation and pedagogy: it is the standard, designer-authored account of C++11, widely treated as the practical companion to the ISO standard. It consolidates the language's evolution, design rationale, and the full standard library into a single authoritative volume, shaping how a generation of practitioners learns and reasons about C++.

## Limitations & open questions
The book states no formal open problems. Its self-described scope limits, however, function as the natural hooks:
- It explicitly does not aim to teach low-level details exhaustively in the introductory chapters and directs readers to cross-references and the index, acknowledging the tension between tutorial completeness and reference accessibility.
- It targets pre-C++11 compilers as a real-world constraint, noting that some readers/customers may not have upgraded — an implicit portability and adoption gap.
- As a snapshot of C++11, it predates later standards (C++14/17/20/23), so its coverage of the evolving language and library is inherently bounded.
- Stroustrup notes C++ is the work of many contributors via the ISO process, leaving the ongoing standardization and design trade-offs as a living, open-ended endeavor rather than a closed result.

## Connections
The work sits within Stroustrup's own corpus, including his earlier "Classes: An Abstract Data Type Facility for the C Language" (1982, the first description of "C with Classes") and his account of the language's design and evolution. Its standard-library material rests on Stepanov & Lee's "The Standard Template Library" (1994) and the generic-programming tradition, with concept-checking work by Siek & Lumsdaine (2000). The concurrency chapters build on Boehm & Adve's "Foundations of the C++ concurrency memory model" (2008). It is anchored to the ISO/IEC 14882:2011 C++ standard and the underlying C standards (ISO/IEC 9899). Foundational language lineage traces to Barron et al.'s CPL (1963). For pattern-level idioms it references Coplien's "Curiously Recurring Template Patterns" (1995). The book is unrelated to the economics and choice-modeling literature that otherwise populates this vault; it appears here as a software-engineering reference rather than a research paper.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
