---
citekey: deClippel2022
title: "Bounded Rationality in Choice Theory: A Survey"
authors: ["de Clippel, Geoffroy", "Rozen, Kareen"]
year: 2022
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/MI82H6JK"
pdf: /Users/jesper/Zotero/storage/MGYP28R6/deClippel2022.pdf
tags: [literature]
keywords: [bounded-rationality, choice-theory, revealed-preference, axiomatic-characterization, stochastic-choice, welfare-analysis]
topics: ["[[behavioral-welfare-nudge]]"]
related: [Bernheim2009, Lleras2017, Manzini2007, Manzini2012, Masatlioglu2012, Salant2008, Sen1971, Tyson2008]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> A vibrant literature incorporates elements of bounded rationality into choice theory. We survey this work, discussing five central ways in which the literature has modeled departures from the rational choice procedure. We discuss the variety of purposes axiomatic choice characterizations serve for these positive theories; explore the permissiveness of these theories; synthesize the welfare debate; and assess important future directions.

## Summary

A wide-ranging survey of bounded-rationality choice theory, the literature that studies choice patterns that need not be consistent with maximizing a single, stable, complete and transitive preference. The authors organize the field around five conceptual ways the tenets of rationality can be relaxed (imperfect perception, multiple-self aggregation, limited attention/consideration, context/reference dependence, and satisficing), rather than around the specific anomalies models explain. They then step back to ask what axiomatic characterizations are for, how permissive these theories really are (surprisingly, most remain highly discerning as the option space grows), and how — if at all — one can do welfare analysis when choices are not preference-maximizing. The survey is explicitly conceptual and taxonomic, intended to help economists "wade through the maze of models."

## Research question

How should one taxonomize and evaluate the diverse literature that injects bounded rationality into individual choice theory? Three sub-questions recur: (i) what purposes do axiomatic characterizations of boundedly-rational choice procedures serve, given they are not normative; (ii) are these theories too permissive (do they explain everything and thus nothing); and (iii) what normative/welfare inferences are licensed by choices that violate preference maximization?

## Method / identification

This is a theoretical survey, not an empirical paper. The unifying formal framework: a finite set of conceivable options $X$, a menu $S\subseteq X$, and a choice function $c:\mathcal{P}(X)\to X$ (or a choice correspondence $C(S)\subseteq S$, or a stochastic choice function $\sigma:\mathcal{P}(X)\to\Delta(X)$). Rationality is the benchmark: maximization of a strict preference, characterized by IIA on full domains and, on arbitrary observed domains $D$, by the Strong Axiom of Revealed Preference (SARP) — i.e. an acyclic revealed preference. Sen's $\alpha$ (contraction) and $\beta$ (expansion) characterize rational correspondences; GARP characterizes the correspondence case.

The five organizing departures, with representative formal models:
- **Imperfect perception.** Utility-threshold representations: $y\,P\,x \iff u(y)-u(x)>\tau$. Constant $\tau$ yields a semiorder (Luce 1956); variable thresholds give interval orders; sequential application gives lexicographic/shortlist procedures (Tversky 1969; [[@Manzini2012|Manzini–Mariotti 2012b]]). Stochastic version: the Luce rule, $P(x\mid S)=u(x)/\sum_{y\in S}u(y)$, which equals random-utility maximization with Gumbel noise (multinomial logit). Extensions handle the red-bus/blue-bus similarity critique (nested logit; Kovach–Tserenjigmid 2021a), inference after perception (Natenzon's Bayesian probit), and rational inattention (Matějka–McKay 2015).
- **Context / reference dependence.** [[@Salant2008|Salant–Rubinstein (2008)]] extended choice problems $(S,f)$ with a frame $f$; Masatlioglu–Ok status-quo models where the status quo grants a utility "bump" or restricts the consideration set via "psychological constraint sets."
- **Satisficing.** A threshold $u^*$ and search order: pick the first $x$ with $u(x)\ge u^*$. The textbook fixed-order version is behaviorally equivalent to rationality. Menu-dependent thresholds $\theta(S)$ (Aleskerov et al. 2007; [[@Tyson2008|Tyson 2008]]) — equivalently a departure function $\delta(S)$ — relax this; Tyson reinterprets satisficing as only partially forming one's preference.
- **Multiple selves / limited attention** (treated in the un-extracted §3.2–3.3): consideration sets and two-stage "maximize a preference over $\Gamma(S)$" models, shortlisting ([[@Manzini2007|Manzini–Mariotti 2007]]).

For judging permissiveness, the authors introduce three "mild regularity" properties on how a theory $T=\{T_X\}$ behaves as the conceivable set varies — (i) label neutrality, (ii) restriction consistency (consistency on $Y\supset X$ implies consistency on $X$), and (iii) a disjoint-union composition property — and prove Observation 1 below.

## Data

None — this is a survey/theory paper. It draws on a large secondary literature and cites empirical/experimental motivations (Mosteller–Nogee 1951 S-shaped choice frequencies; Besedeš et al. 2015 choice overload; Bouacida–Martin 2021 grocery-purchase welfare cycles) but generates no new data.

## Key findings

- **Behavioral equivalence is pervasive.** Distinct choice processes can be indistinguishable on standard choice data: fixed-order satisficing reproduces exactly the rational choice functions; a cafeteria-line satisficer satisfies IIA; selecting undominated alternatives under an acyclic preference ([[@Sen1971|Sen 1971]], characterized by Condition $\alpha$ plus Condition $\gamma$: $x\in C(R)\cap C(S)\Rightarrow x\in C(R\cup S)$) captures semiorder, interval-order, and Markovian-search models alike.
- **Purposes of characterizations.** Even for non-normative positive theories, axiomatizations (i) clarify the theory's content (IIA $\Leftrightarrow$ rationality), (ii) pinpoint the principle separating two theories or reveal their equivalence, (iii) can carry normative appeal, and (iv) provide choice-based tests — where domain-robust SARP-style axioms beat domain-sensitive IIA-style ones and force the modeler to confront identification.
- **Observation 1 (permissiveness).** For a theory satisfying the regularity properties: (A) if $T$ is nontrivial and satisfies Property (ii), the fraction of choice functions consistent with $T$ on $X_n$ monotonically decreases to zero as $|X_n|\to\infty$; (B) if $T$ is more permissive than rationality and satisfies Property (iii), the fraction of *rational* choice functions among the $T$-consistent ones also converges to zero. The upshot: virtually every theory proposed to date is "infinitely discerning" given enough alternatives, even while being strictly more permissive than rationality — these are not in tension. (Counts dramatize this: rational choice functions are $n!$, but all choice functions on $|X|=5$ exceed 309 billion; weak-WARP places no restriction at $|X|=3$ yet becomes extremely demanding for large $X$.) An analogous convergence holds for stochastic choice: RUM SCFs are a measure-zero-in-the-limit but positive-measure sub-polytope of all SCFs (extreme points cut from 309 billion to 120 when $|X|=5$).
- **Welfare has no consensus.** Even for a single DM, multiple preferences can rationalize the same data (the multiplicity already present in Varian 1982 for incomplete rational data, and worse under bounded rationality). Approaches split philosophically: Sugden's (2004) anti-paternalist "continuing locus of responsibility"; model-based inference (cleanest when there is one acyclic welfare-relevant preference plus an identified confound, e.g. two-stage consideration-set models); and [[@Bernheim2009|Bernheim–Rangel's (2009)]] model-free generalized-choice-situations $(S,d)$ with the unambiguous-choice relation $P^*$ ($x\,P^*y$ iff $y\notin C(S,d)$ whenever $x,y\in S$, over all relevant $(S,d)$), proven acyclic but only given a complete dataset; Nishimura's (2018) transitive core addresses the resulting cyclicity.

## Contribution

Provides a coherent conceptual map of an otherwise sprawling literature, organized by *type of departure from rationality* rather than by anomaly explained or by data format. Beyond synthesis, it contributes an original formal result (Observation 1) showing that the apparent permissiveness of bounded-rationality theories largely evaporates as the option space grows — a reassuring restrictiveness — and it synthesizes the fractured welfare debate into a small set of philosophical positions and their formal commitments.

## Limitations & open questions

The authors flag these explicitly (project-idea hooks):
- **Generating richer distinguishing data.** Because so many processes are behaviorally equivalent on standard menu-choice data, the field needs richer observables — domain enrichments (status quo, presentation order: $\mathcal{P}(X)\times I_D$) and especially DM-generated range enrichments (response times, eye-tracking, intermediate process data: $I_R$). Only a minority of works exploit either; how to systematically design experiments (e.g. redesigning the cafeteria display) to separate equivalent theories is open.
- **Welfare under multiplicity and incompleteness.** No consensus on whether confounds must be modeled, which preference to use under multi-self models, or how to handle $P^*$ cyclicity without exponentially-large complete datasets; whether to interpret an observed correspondence as exhaustive or as a sample is an unresolved "philosophical stand."
- **Which anomalies are the "right" ones (§5.2 "How successful?").** Permissiveness alone is the wrong yardstick; theories should be judged on whether they expand rationality toward empirically prevalent patterns — an open evaluative program.
- **Self-described omissions.** The authors concede the survey likely has "important and inadvertent omissions."

## Connections

Foundational benchmarks: Samuelson–Houthakker revealed preference and SARP/WARP/GARP; [[@Sen1971|Sen (1971)]] on $\alpha$/$\beta$/$\gamma$; Luce (1956, 1959) and McFadden's random-utility/logit tradition. Methodological framing follows Rubinstein (1998) on procedural decision-making and Conlisk (1996) on deliberation costs; it situates choice theory against the "Krepsian" decision-theoretic methodology (Lipman–Pesendorfer 2013; Spiegler 2013). Limited-attention and consideration-set work ([[@Masatlioglu2012|Masatlioglu, Nakajima, Ozbay 2012]]; [[@Manzini2007|Manzini–Mariotti 2007]] shortlists; [[@Lleras2017|Lleras et al. 2017]]), context/framing ([[@Salant2008|Salant–Rubinstein 2008]]; Masatlioglu–Ok 2005, 2014; [[@Bernheim2009|Bernheim–Rangel 2009]]), and stochastic choice (Natenzon 2019; Matějka–McKay 2015; Apesteguia–Ballester 2020) are the principal strands surveyed. The permissiveness result parallels and complements Giarlotta–Petralia–Watson (2021). Directly relevant to anyone modeling social preferences or estimating choice models who must decide how much structure to impose on the choice procedure and how to identify welfare from imperfect choice data.

Coverage note: the §7 conclusion / "future directions" and parts of §3.2–§3.3 and §5.2 fell beyond the PDF extractor's character cap; future directions above are synthesized from the abstract and the explicit open problems the authors raise throughout §§2–6 rather than from §7 verbatim.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
