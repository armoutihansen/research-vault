---
citekey: Dutta2015
title: "Inferring rationales from choice: Identification for rational shortlist methods"
authors: ["Dutta, Rohan", "Horan, Sean"]
year: 2015
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/Q79WR87S"
pdf: /Users/jesper/Zotero/storage/SU7UNNWD/Dutta2015.pdf
tags: [literature]
keywords: [revealed-preference, bounded-rationality, rational-shortlist-method, choice-theory, identification, two-stage-choice]
topics: []
related: [Au2011, Bernheim2009, Cherepanov2013, Eliaz2011a, Manzini2007, Manzini2012a, Masatlioglu2012, Rubinstein2012, Salant2008, Samuelson1938, Tyson2013]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Dutta and Horan study *identification* in Manzini and Mariotti's (2007) Rational Shortlist Method (RSM), the two-stage choice procedure in which a decision maker applies a first rationale to delete dominated alternatives and then a second rationale to pick from the survivors. Manzini and Mariotti axiomatized *which* behavior the model rationalizes but left open *what the behavior reveals about the rationales*. Because an RSM choice function generally admits many representations, the paper develops a revealed-preference theory: it defines conservative "revealed rationales," characterizes the full class of (minimal) representations consistent with the data, and gives the choice-invariant transformations of any representation. The three results are shown to be exact analogs of revealed preference, the representation theorem, and "uniqueness up to affine transformation" in the classical utility-maximization setting.

## Research question
Given choice behavior that is consistent with the RSM model, to what extent — and exactly how — does observed choice pin down the underlying pair of rationales $(P_1,P_2)$? Equivalently: what is revealed preference for the RSM model, what is the complete set of representations, and which modifications of a representation leave choice unchanged?

## Method / identification
Pure decision-theoretic / revealed-preference analysis. A *rationale* is an asymmetric binary relation on a finite domain $X$. An RSM is a choice function induced by a pair $(P_1,P_2)$ via
$$C_{(P_1,P_2)}(A)=\max\big(\max(A;P_1);P_2\big),$$
where $\max(B;P)=\{a\in B: \text{no } b\in B \text{ with } bPa\}$. The benchmark axiomatization (Theorem 1, MM) is **Expansion** and **WWARP**. Let $\mathcal{R}(c)$ be the set of all rationale pairs representing $c$. The authors define the **revealed 1-rationale** $P_1^*$ and **revealed 2-rationale** $P_2^*$ as the pairs common to *every* representation — a conservative stance in the spirit of [[@Masatlioglu2012|Masatlioglu, Nakajima & Ozbay (2012)]] and Samuelson. A representation is **minimal** if neither rationale duplicates or contradicts the other. The machinery uses the pairwise revealed preference $P^c$ ($aP^cb$ iff $c(a,b)=a$), $P^c$-complements, the lattice structure of representations, and a notion of $(P_1,P_2)$-**redundant** pairs to define choice-invariant moves of preference pairs between rationales.

## Data
None — this is a theory paper. The analysis assumes choice from *every* menu in $2^X\setminus\emptyset$ is observable (complete data); the conclusion sketches extensions to limited data in the sense of de Clippel & Rozen (2014). The motivating Examples I–V (multicriterial choice, forced choice, limited consideration, comparative advertising) are illustrative applications, not empirical data.

## Key findings
- **Proposition 1 (revealed rationales).** For RSM-representable $c$: $aP_1^*b$ iff a choice *switch* occurs — $c(B)=b$ and $c(B\cup\{a\})\notin\{a,b\}$ for some $B$; and $aP_2^*b$ iff a choice *reversal* occurs — $c(A)=a$ and $c(B)=b$ for some $\{b\}\subseteq A\subseteq B$. The revealed 1-rationale coincides with Rubinstein & Salant's (2008) dominance relation and the revealed 2-rationale with Houy's (2008) "progressive knowledge" relation.
- **Proposition 2 (representations).** $P_i^*\subseteq P_i$ so the interval $V_i(c)$ of admissible rationales is nonempty, and $(P_1,P_2)$ is minimal iff $P_i\in V_i(c)$ and $P_{-i}=P^c\setminus P_i$. The minimal representations form a *lattice* (footnote 12). The representation is unique iff $P_1^*\cup P_2^*=P^c$; otherwise an indeterminate part $P^m$ can be assigned to either rationale, generating a range bounded by the two extreme minimal representations.
- **Proposition 3 (choice-invariant transformations).** A pair $(a,b)\in P_2$ can be moved to $P_1$ (and symmetrically) without changing choice iff it is $(P_1,P_2)$-redundant, characterized via $P_1$-chains. This is the RSM analog of "uniqueness up to affine transformation," letting one identify revealed rationales and all minimal representations directly from any representation, without computing choices.
- **Remark 1 (welfare).** The Bernheim–Rangel welfare relation $W$ satisfies $P_1^*\subseteq W=P_1^c$ (it overestimates the first rationale) and $P_2^*\cap W=\emptyset$ (no connection to the second rationale) — so even the "model-free" BR approach implicitly privileges the first rationale.

## Contribution
Provides the first complete identification theory for the RSM model: a tight, easy-to-apply revealed-preference characterization (switches and reversals), an exact description of the entire set of (minimal) representations, and a transformation result. It unifies and clarifies binary relations introduced separately by [[@Salant2008|Rubinstein & Salant (2008)]] and Houy (2008), shows WWARP's role is to keep the revealed rationales disjoint, and reduces the axiomatization of special cases (transitive rationales, acyclic RSM) to finding axioms that reshape minimal representations. It demonstrates that procedural models can support the same identification exercise as utility maximization, with applications to welfare analysis and to the economics of comparative advertising.

## Limitations & open questions
- Results assume **complete data** (choice from every menu). Extension to limited data is sketched, with conditions "available on request," but not fully developed — a hook for a limited-data identification paper.
- The lattice structure of representations is the engine; models *without* it (e.g., Lleras et al. 2010; [[@Masatlioglu2012|Masatlioglu, Nakajima & Ozbay 2012]]) are explicitly **not** amenable to the approach, leaving open how to characterize representations there.
- Extension to **more than two rationales** (Apesteguia & Ballester 2010; [[@Manzini2012a|Manzini & Mariotti 2012b]]) is left open — "not entirely clear whether our approach can be applied."
- Multivalued RSM (Garcia-Sanz & Alcantud 2010) and the negative-transitive special case ([[@Tyson2013|Tyson 2013]]) are flagged as natural targets for extending Propositions 1–2.
- The paper takes **no position** on the model-based vs. model-free welfare debate; which rationale counts as "true" preference (tie-breaking rule vs. consideration set) is left to interpretation.
- The suggested application to comparative advertising and seller "nudging" (Examples IV–V) is proposed as meriting "further investigation."

## Connections
The paper builds directly on [[@Manzini2007|Manzini & Mariotti (2007)]], whose RSM model and axioms (Expansion, WWARP) are the object of study, and on the alternative axiomatization of [[@Salant2008|Rubinstein & Salant (2008)]]. The conservative notion of revealed preference follows [[@Masatlioglu2012|Masatlioglu, Nakajima & Ozbay (2012)]] and the classical revealed-preference program of [[@Samuelson1938|Samuelson]] (1938, 1950). The revealed rationales connect to relations in [[@Salant2008|Rubinstein & Salant (2008)]] (dominance) and Houy (2008) (progressive knowledge), the latter also appearing in the more general model of [[@Cherepanov2013|Cherepanov, Feddersen & Sandroni (2013)]]. Related two-stage identification work includes Lleras et al. (2010), [[@Au2011|Au & Kawai (2011)]], Horan (2013), Matsuki & Tadenuma (2013), Garcia-Sanz & Alcantud (2010), [[@Tyson2013|Tyson (2013)]], and de Clippel & Rozen (2014) (limited data). Welfare connections are to Bernheim & Rangel (2007, 2009), [[@Bernheim2009|Bernheim (2009)]], and [[@Rubinstein2012|Rubinstein & Salant (2012)]]; the advertising/nudging applications relate to [[@Eliaz2011a|Eliaz & Spiegler]] (2011a,b), Piccione & Spiegler, and Thaler & Sunstein (2008).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
