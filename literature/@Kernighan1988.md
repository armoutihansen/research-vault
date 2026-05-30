---
citekey: Kernighan1988
title: The C programming language
authors: ["Kernighan, Brian W.", "Ritchie, Dennis M."]
year: 1988
type: book
doi: ""
zotero: "zotero://select/library/items/AGTG7IN2"
pdf: /Users/jesper/Zotero/storage/IBU6H3L4/Kernighan1988.pdf
tags: [literature]
keywords: [c-programming-language, ansi-c, systems-programming, reference-manual, programming-pedagogy, unix]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
The C Programming Language, 2nd edition ("K&R"), is the canonical tutorial-plus-reference for the C programming language, revised by its creators to track the then-new ANSI C standard (C89). It teaches C through complete, tested example programs spanning a tutorial introduction, chapter-by-chapter treatment of every major language feature (types, control flow, functions, pointers, structures, I/O), an authoritative reference manual, and a standard-library summary. Concise and example-driven, it doubles as both a learning text and a working programmer's reference.

## Research question
This is a technical/instructional book rather than a research paper, so it poses no empirical research question. Its organizing aim is pedagogical and normative: how to write correct, idiomatic, portable C, and how to specify the language precisely. The 2nd edition's specific motivating problem is to reconcile the original 1978 description of C with the formal ANSI standard, presenting "C as defined by the ANSI standard" while preserving the brevity of the first edition.

## Method / identification
The exposition is built on reading, writing, and revising complete, machine-tested example programs rather than on bare statements of rules ("Most of the treatment is based on reading, writing and revising examples"). The structure proceeds in three layers:
- Chapter 1, a tutorial introduction that deliberately omits pointers, structures, and most operators to get the reader writing useful programs quickly;
- Chapters 2-8, systematic treatment of one feature family at a time — types/operators/expressions, control flow, functions and program structure, pointers and arrays, structures, input/output, and the UNIX system interface;
- Appendix A, a reference manual presenting "the essentials of the standard in a smaller space" (explicitly not the standard itself), Appendix B summarizing the standard library, and Appendix C cataloguing changes from the first edition.
The book assumes familiarity with basic programming concepts (variables, assignment, loops, functions) and is not an introductory programming manual.

## Data
None — this is a programming-language text. Its "data" are worked example programs (e.g., character counting, word counting, a storage allocator, an implementation of `fopen`/`getc`, directory listing, a declaration-to-words translator), all stated to have been "tested directly from the text, which is in machine-readable form."

## Key findings
There are no theorems; the durable "results" are language-design and exposition decisions:
- C is positioned as a small, general-purpose language — "not a 'very high level' language, nor a 'big' one" — whose absence of restrictions and generality make it effective across tasks despite a compact feature set.
- The 2nd edition writes exclusively in the ANSI form; the most visible change is the new function declaration/definition syntax (prototypes), e.g. the shift from old-style parameter lists to typed prototypes.
- It canonizes idioms that became C culture: the `while ((c = getchar()) != EOF)` input loop, pointer arithmetic equivalence with arrays, `argc`/`argv` command-line handling, and the reading of complicated declarations via the right-left rule.
- Appendix A and B function as a programmer-facing distillation of the standard and standard library, deliberately distinct from a compiler-writer's definition.

## Contribution
K&R is the foundational and most influential text on C, and arguably one of the most influential programming books written. Its terse, example-first style set a template for technical writing in computing. By rewriting the canonical description to match ANSI C, the 2nd edition aligned the language's most-read introduction with its first formal standard, smoothing the community's transition to standardized, portable C. The example programs (and the codebase conventions they embody) shaped decades of systems programming style, and the book remains a reference long after publication.

## Limitations & open questions
The authors are explicit about the book's scope limits:
- The tutorial chapter is, by design, incomplete and "may also be misleading" because it omits major features and does not give the full story on any one of them.
- The reference manual (Appendix A) is deliberately not authoritative: "Appendix A, the reference manual, is not the standard, but our attempt to convey the essentials of the standard in a smaller space," meant for programmer comprehension, not as a definition for compiler writers — that role "properly belongs to the standard itself."
- The library appendix (Appendix B) is likewise for reference by programmers, "not implementers."
- The book pre-supposes prior programming experience and so is not self-contained for true novices.
These scoping choices implicitly hand off precise semantics to the ANSI document and leave implementation-defined and machine-dependent behaviors (noted in the text) as caveats for the reader.

## Connections
The 2nd edition is the direct revision of Kernighan & Ritchie (1978), the first edition, and tracks the ANSI X3.159 C standard (C89/C90) that superseded the informal 1978 description. C itself descends from Ritchie's earlier work on B and BCPL and is intertwined with Thompson & Ritchie's UNIX system, for which it was originally implemented on the DEC PDP-11. The example-driven, style-conscious approach is continued in Kernighan & Pike, The Practice of Programming (1999), and complements Kernighan & Plauger, The Elements of Programming Style. The reference manual relates to the contemporaneous formal standardization effort and to compiler-construction texts such as Aho, Sethi & Ullman (Al Aho is acknowledged in the prefaces). Bjarne Stroustrup's C++ — used here as a translator for local testing — is C's most prominent descendant.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
