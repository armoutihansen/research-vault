---
citekey: Masatlioglu2013
title: Choice by iterative search
authors: ["Masatlioglu, Yusufcan", "Nakajima, Daisuke"]
year: 2013
type: journalArticle
doi: 10.3982/TE1014
zotero: "zotero://select/library/items/PH2LBTUT"
pdf: /Users/jesper/Zotero/storage/C66RNMMN/Masatlioglu2013.pdf
tags: [literature]
keywords: [consideration-sets, bounded-rationality, revealed-preference, search, reference-dependent-choice, choice-theory]
topics: ["[[limited-attention-consideration-sets]]"]
related: [Bernheim2009, Caplin2011, Cherepanov2013, Eliaz2011a, Hauser1990, Manzini2007, Masatlioglu2012, Roberts1991, Salant2008, Sen1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> When making choices, decision makers often either lack information about alternatives or lack the cognitive capacity to analyze every alternative. To capture these situations, we formulate a framework to study behavioral search by utilizing the idea of consideration sets. Consumers engage in a dynamic search process. At each stage, they consider only those options in the current consideration set. We provide behavioral postulates that characterize this model. We illustrate how one can identify both search paths and preferences.

## Summary
This paper develops a decision-theoretic model, *choice by iterative search* (CIS), in which a decision maker (DM) holds a stable preference but explores her budget set dynamically through evolving consideration sets rather than evaluating all alternatives at once. Starting from an observed reference point, the DM repeatedly expands her consideration set, picks the best item seen so far, and stops at a fixed point. The general model is characterized by a single acyclicity-type axiom, but it is behaviorally vacuous about search; imposing a *Markovian* structure—where the next consideration set depends only on the best alternative encountered so far—delivers sharp identification of both the DM's preference and her entire search path from choice data, while still allowing choice reversals, cyclical behavior, and status-quo bias.

## Research question
How can we model the *process* by which a boundedly rational DM forms and updates a consideration set during search, and to what extent can we recover her (stable) underlying preference and her search path purely from observed (extended) choice data—without invoking context-dependent preferences to explain apparent choice anomalies?

## Method / identification
The primitive is an *extended choice function* $c(S,x)\in S$, defined on extended choice problems $(S,x)$ where $S\in\mathcal{K}(X)$ is a finite feasible set and $x\in S$ is an observed *starting point*. A CIS representation is a pair $(\succ,\Gamma)$ of a strict preference $\succ$ and a *consideration set mapping* $\Gamma(A,S)$ with $A\subseteq\Gamma(A,S)\subseteq S$. Search generates a history sequence $A_0=\{x\}, A_1,\dots,A_n$ with $\Gamma(A_k,S)=A_{k+1}$ until a fixed point $\Gamma(A_n,S)=A_n$ is reached; the choice is the $\succ$-best element of $A_n$. Because $\{A_k\}$ is an expanding sequence in a finite set, a fixed point always exists.

The general model is characterized by the **Dominating Anchor** axiom (each $S$ has an alternative $x^*$ that is never abandoned), which is shown equivalent to acyclicity of the revealed relation $x\succ_c y$ defined by $c(S,y)=x$ (Theorem 1). The **Markovian CIS** restriction sets $\Gamma(A,S)=(\Gamma^*(x_A)\cap S)\cup A$, where $x_A$ is the best item in $A$ and $\Gamma^*$ is the Markovian consideration set mapping. It is characterized by four axioms (Theorem 2): A1 *Strong Dominating Anchor*, A2 *Irrelevance*, A3 *Expansion*, and A4 *Replacement*, shown to be independent. The paper also treats the case of *unobservable starting points* by inducing a choice correspondence $C_c(S)=\{y:\exists x,\,y=c(S,x)\}$, characterized via the **Bliss Point** axiom for the general model.

## Data
None—this is a pure axiomatic/revealed-preference theory paper. No empirical data, experiments, or simulations; the "data" are hypothetical extended choice functions. The paper notes that observability of starting points is increasingly plausible given data-mining technologies and discusses how the framework could be tested if search-path data were available.

## Key findings
- **Theorem 1 (general CIS):** $c$ is a CIS iff it satisfies Dominating Anchor; any preference containing the transitive closure of $\succ_c$ represents $c$. But the general model is behaviorally equivalent to a static one-shot model, so it is uninformative about search.
- **Theorem 2 (Markovian CIS):** $c$ is a Markovian CIS iff it satisfies A1–A4.
- **Proposition 1 (revealed preference):** Three observable choice patterns—abandonment of the starting point, choice reversal, and choice over a dominating alternative—generate a relation whose transitive closure $\mathrm{TC}_c$ exactly characterizes revealed preference.
- **Remarks 1–2 (revealed consideration):** $x$ is revealed to be in $y$'s consideration set iff $y=c(\{x,y\},x)$; revealed *not* to be in it under a stated condition.
- **Remark 3 (search-path identification):** Every Markovian representation generates the *same* search path for every problem—the path is fully identified from choices.
- **Behavioral properties:** the model exhibits Starting Point Bias, Starting Point Contraction (a conditional IIA), the Sandwich Property, and Irrelevance of Revealed Inferior Alternatives.
- **Corollary 1 / Proposition 2:** characterizations when preference or the consideration mapping is partially/fully observable.

## Contribution
First general decision-theoretic model of *how* a consideration set forms and evolves dynamically over the course of search, linking consideration-set formation to a search process. It shows that seemingly irrational behavior (choice reversals, cycles) can arise from limited search alone, with *stable* preferences—context-dependent preferences are not necessary to rationalize anomalies. It provides full identification of both preferences and the otherwise-latent search path from enriched choice data, giving firms tools to distinguish "consumers dislike the product" from "consumers never found it."

## Limitations & open questions
- The **general CIS model is behaviorally vacuous** about search (equivalent to a static choose-best-of-$\Gamma(\{x\},S)$ model), motivating the Markovian restriction.
- Identification relies on observing the **starting point**; while Section 4 handles unobservable starting points via induced choice correspondences, inference is weaker there.
- **Open direction 1:** extend the model to *aggregate/market-share* data (e.g., "40% who start at $x$ end up at $y$") and ask how to identify *distributions* of preferences and consideration sets when each individual follows a Markovian CIS.
- **Open direction 2:** incorporate **framing effects** beyond history and feasible set, e.g., consideration sets of the form $\Gamma(A,S,f)$ or $\Gamma^*(x,f)$ with frame $f$ capturing presentation/advertising.
- Reconciling a Markovian representation with *externally observed* preference or consideration data may fail without extra consistency conditions (flagged as work in progress).

## Connections
The revealed-preference-with-multiple-representations approach is taken directly from [[@Masatlioglu2012|Masatlioglu, Nakajima & Ozbay (2012)]] on limited attention, and is related to [[@Cherepanov2013|Cherepanov, Feddersen & Sandroni (2013)]], [[@Manzini2007|Manzini & Mariotti]] (2007, 2012), [[@Caplin2011|Caplin & Dean (2011)]], and Green & Hojman (2007). The extended-domain/reference-point formulation mirrors status-quo and frame-based choice in Masatlioglu & Ok (2005), [[@Salant2008|Salant & Rubinstein (2008)]], and [[@Bernheim2009|Bernheim & Rangel (2009)]]; the starting-point-bias property reproduces the status-quo-bias axiom of Masatlioglu & Ok (2005). The consideration-set primitive draws on the marketing literature ([[@Hauser1990|Hauser & Wernerfelt 1990]], [[@Roberts1991|Roberts & Lattin 1991]], Nedungadi 1990, Hauser 2010) and contrasts with classical search theory (Stigler 1961, McCall 1970, Mortensen 1970). Two special cases of CIS are applied to firm–consumer market interactions by [[@Eliaz2011a|Eliaz & Spiegler]] (2011a, 2011b). The satisficing/bounded-rationality motivation is Simon's, and connects to heuristic search evidence (Gigerenzer & Selten 2001). The choosable-set interpretation under unobserved starting points follows [[@Sen1993|Sen (1993)]] and [[@Salant2008|Salant & Rubinstein (2008)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
