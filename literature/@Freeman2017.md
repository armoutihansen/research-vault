---
citekey: Freeman2017
title: Preferred personal equilibrium and simple choices
authors: ["Freeman, David J."]
year: 2017
type: journalArticle
doi: 10.1016/j.jebo.2017.08.016
zotero: "zotero://select/library/items/SQHBHZ9R"
pdf: /Users/jesper/Zotero/storage/2JGLRKSZ/Freeman2017.pdf
tags: [literature]
keywords: [reference-dependent-preferences, personal-equilibrium, rational-shortlist-method, revealed-preference, axiomatization, loss-aversion]
topics: []
related: [Abeler2011, Au2011, Crawford2011, Dutta2015, Freeman2016, Heidhues2008, Horan2016, Kalai2002, Koszegi2006b, Koszegi2010, Manzini2007, Masatlioglu2016, Ok2015, Sen1971, Tyson2013, deClippel2012]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper studies choices under the preferred personal equilibrium concept introduced by [[@Koszegi2006b|Koszegi and Rabin (2006)]] for modeling choice given expectations-based reference-dependent preferences. The main result of this paper shows that when expectations are not observed and parametric assumptions on utility are not made, preferred personal equilibrium choice is a special case of the rational shortlist method of [[@Manzini2007|Manzini and Mariotti (2007)]]. Building on this connection, the paper provides an axiomatization of preferred personal equilibrium choice behavior and discusses the implications of these results for how choices can be used to test and identify the model, and for the relationship between preferred personal equilibrium and other models of behavior.

## Summary
Freeman asks what observable content the Koszegi-Rabin preferred personal equilibrium (PPE) model has when reference points, expectations, and the reference-dependent utility function are all unobserved and no functional form is assumed. The central result is a representation equivalence: PPE choice behavior is observationally indistinguishable from the rational shortlist method (RSM) of [[@Manzini2007|Manzini and Mariotti (2007)]] with a transitive second rationale. This connection yields a clean revealed-preference axiomatization (Expansion plus Weak Congruence), pins down exactly which choice patterns the model rules out (e.g. attraction and compromise effects), and clarifies how PPE relates to status-quo-bias models and other non-transitive theories.

## Research question
Reference points are not naturally observable, so any application of reference-dependent preferences must assume how they form. Given that PPE imposes that the reference point equals the chosen option (rational expectations), the paper asks: what is the behavioral content of reference-dependence under the PPE solution concept, expressed purely in terms of an observed choice correspondence, without observing expectations and without parametric assumptions on utility?

## Method / identification
The primitive is a finite alternative set $X$, the collection $\mathcal{D}$ of nonempty subsets ("choice sets"), and an observed choice correspondence $c:\mathcal{D}\to\mathcal{D}$ with $\emptyset\neq c(D)\subseteq D$. A reference-dependent utility is $v:X\times X\to\mathbb{R}$, where $v(\cdot\mid x)$ is utility when the reference point is $x$. The Koszegi-Rabin solution concepts restrict the general model:
- Personal equilibrium: $\mathrm{PE}_v(D)=\{x\in D: v(x\mid x)\ge v(y\mid x)\ \forall y\in D\}$ (reference point consistent with rational expectations about choice).
- Preferred personal equilibrium: $\mathrm{PPE}_v(D)=\arg\max_{x\in\mathrm{PE}_v(D)} v(x\mid x)$ (the decision-maker selects her best PE according to the self-referential ranking).
- Choice-acclimating PE: $\mathrm{CPE}_v(D)=\arg\max_{x\in D} v(x\mid x)$.

The rational shortlist method applies two binary rationales sequentially: $\mathrm{RSM}_{P_1,P_2}(D)=m(m(D,P_1),P_2)$, where $m(D,P)=\{x\in D:\forall y\in D,\ yPx\Rightarrow xPy\}$ is the set of undominated elements. The identification strategy is constructive: build $P_1$ from "wanting to deviate from the reference point" and $P_2$ from the self-referential CPE ranking, then show the two procedures coincide. The axiomatization extends Manzini-Mariotti's axioms to multi-valued correspondences via an Expansion axiom and a Weak Congruence axiom (a weakening of Richter's Congruence).

## Data
None - this is a pure choice-theoretic / decision-theoretic paper. Identification is in terms of an abstract observed choice correspondence; no experimental or empirical data are used, though Example 1 calibrates linear loss aversion ($\lambda=3$) to the experimental range.

## Key findings
- **Observation 1**: Without restrictions, the general reference-dependent model rationalizes *any* choice correspondence (set $\eta(D)=c(D)$ and indicator utilities) - reference-dependence per se has no testable content.
- **Proposition 1** (main result): There exist an asymmetric $P_1$ and a complete, transitive $P_2$ with $c=\mathrm{RSM}_{P_1,P_2}$ if and only if there exists $v$ with $c=\mathrm{PPE}_v$. The construction uses $v(y\mid x)>v(x\mid x)\Leftrightarrow yP_1 x$ and $v(x\mid x)\ge v(y\mid y)\Leftrightarrow xP_2 y$.
- **Corollary 1**: $c=\mathrm{PE}_v$ iff $c$ is induced by a complete binary relation (recovering Gul-Pesendorfer 2008); $c=\mathrm{CPE}_v$ iff induced by a complete *and transitive* relation. Hence PE is the special case of PPE where the CPE ranking is indifferent everywhere, and CPE the case where PE never eliminates anything.
- **Proposition 2**: $c$ satisfies Expansion and Weak Congruence iff it has an RSM representation with transitive $P_2$ iff it is a PPE. **Observation 3**: PE is characterized by Expansion and Sen's $\alpha$.
- **Proposition 3**: Adding a No Cycle Condition (pairwise transitivity, required by Ok-Ortoleva-Riella's attraction-effect model) to Expansion and Weak Congruence/Sen's $\alpha$ forces full WARP. So PPE and the Ok et al. endogenous-reference model intersect only at standard rational choice; the PPE model cannot produce attraction or compromise effects, since Expansion rules out $\{x\}=c(\{x,y\})=c(\{x,z\})$ yet $\{y\}=c(\{x,y,z\})$.

## Contribution
The paper gives the first non-parametric revealed-preference foundation for the widely-applied PPE concept, mapping it onto a well-understood boundedly-rational procedure (the RSM). This lets PPE be tested and identified from choices alone, without committing to the gain-loss functional form, and provides a precise vocabulary for comparing it to PE, CPE, status-quo-bias models, and non-transitive theories. It also subsumes Gul-Pesendorfer's PE characterization as a corollary and extends Manzini-Mariotti to multi-valued correspondences.

## Limitations & open questions
- The analysis is confined to a **static, riskless** abstract domain; the distinctive dynamic-choice implications of PE that [[@Koszegi2010|Koszegi (2010)]] identifies - multiple stable equilibria, dynamic inconsistency, informational preferences - are absent here. Extending the revealed-preference program to rich risk/multi-stage settings is open.
- Identification is **partial**: an intransitive cycle $\{x\}=c(\{x,y\}),\{y\}=c(\{y,z\}),\{z\}=c(\{x,z\})$ alone does not reveal which comparisons come from the PE set versus the CPE ranking. Under risk (companion paper [[@Freeman2016|Freeman 2016]]) preferences can be uniquely identified; doing so in general is open.
- The analysis assumes $\mathrm{PE}_v(D)$ is always nonempty; this is equivalent to $v$ satisfying the **limited cycle inequalities** (equivalent to Munro-Sugden's C7). General nonemptiness conditions for the RSM are deferred to [[@Dutta2015|Dutta and Horan (2015)]].
- Comparison with regret theory and other non-transitive models is contingent on a specific extension of those models to arbitrary (non-binary) choice sets.

## Connections
The paper is built directly on [[@Koszegi2006b|Koszegi & Rabin]] (2006, 2007, 2009) for the PE/PPE/CPE concepts and [[@Manzini2007|Manzini & Mariotti (2007)]] for the rational shortlist method; the PE characterization recovers Gul & Pesendorfer (2008). The multi-valued axiomatization relates to [[@Tyson2013|Tyson (2013)]] and to single-valued RSM axiomatizations by [[@Au2011|Au & Kawai (2011)]] and [[@Horan2016|Horan (2016)]], with foundational revealed-preference axioms from Arrow (1959), Richter (1966), and [[@Sen1971|Sen (1971)]]. The "many rationales" intuition behind Observation 1 connects to [[@Kalai2002|Kalai, Rubinstein & Spiegler (2002)]]. On reference-dependence and status-quo bias it contrasts with Masatlioglu & Ok (2005, 2014), Sagi (2006), Sugden (2003), Munro & Sugden (2003), and Apesteguia & Ballester (2009, 2013); the attraction-effect model of [[@Ok2015|Ok, Ortoleva & Riella (2015)]] is the key foil for Proposition 3, alongside de [[@deClippel2012|Clippel & Eliaz (2012)]]. Non-transitive precedent is Loomes & Sugden's (1982) regret theory, and the risk extension is [[@Freeman2016|Freeman (2016)]], with [[@Masatlioglu2016|Masatlioglu & Raymond (2016)]] and Blow, Crawford & Crawford (2015) on related functional-form and revealed-preference questions. Applications motivating the PPE focus include [[@Crawford2011|Crawford & Meng (2011)]], [[@Heidhues2008|Heidhues & Koszegi]] (2008, 2014), Karle et al. (2015), and Pagel (2016); experimental tests include [[@Abeler2011|Abeler et al. (2011)]] and Ericson & Fuster (2011).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
