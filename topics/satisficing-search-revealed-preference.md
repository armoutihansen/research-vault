---
slug: satisficing-search-revealed-preference
title: "Satisficing, Search & Threshold Choice"
type: topic
scope: "Revealed-preference and search-theoretic formalizations of Simon's satisficing, aspiration thresholds, and choice-process data."
tags: [topic]
created: 2026-05-31
generated: 2026-05-31
area: "[[bounded-rationality-choice]]"
---

## Scope

This topic gathers the revealed-preference and search-theoretic formalizations of Herbert Simon's satisficing: choice procedures in which a cognitively constrained decision-maker stops once an option clears a *good-enough* threshold rather than maximizing globally. The members axiomatize the resulting behavior — threshold/aspiration representations, sequential search with a stopping rule, and the *choice-process data* needed to identify search — and ask what observable content these procedures carry. The boundary is sharp: this is about the *threshold/stopping* architecture of bounded rationality and its identification, not about limited-attention consideration sets per se (those models border this topic but are anchored elsewhere), and not about optimization-under-information-cost à la rational inattention.

## Sub-themes

- **Aspiration/threshold representations (static).** A primary criterion $f$ is kept above a menu-dependent bar $\theta(A)$, with no explicit search. [[@Tyson2008|Tyson (2008)]] gives the canonical *satisficing representation* $C(A)=\{x:f(x)\ge\theta(A)\}$ as a relaxation of contraction consistency; [[@Tyson2015|Tyson (2015)]] adds a fixed secondary criterion to break residual pseudo-indifference, $C(A)=\arg\max_{f_1(x)\ge\theta_1(A)} f_2(x)$; [[@Manzini2013|Manzini, Mariotti & Tyson (2013)]] abstracts both into the general *two-stage threshold* (TST) class $\langle f,\theta,g\rangle$.
- **Sequential search & stopping rules.** The threshold is the *reason search halts*, not just a filter on a fixed menu. [[@Papi2012|Papi (2012)]] models discovery along a nested menu sequence with a fixed aspiration $x_s$ and a first-satisfactory stopping stage; [[@Caplin2011|Caplin & Dean (2011)]] characterizes alternative-based search (ABS) and its reservation-stopping refinement (RBS), where search halts the instant an option clears reservation utility $\rho$.
- **Choice-process / satisficing data.** What the analyst must observe to identify search and aspiration. [[@Caplin2011|Caplin & Dean (2011)]] enriches the data to the trajectory of provisional choices over contemplation time $C_A(t)$; [[@Papi2012|Papi (2012)]] grades identification across three informational structures (search order fully observable / partially / unobservable), trading inference power against data volume.

## Cross-paper tensions

- **Static threshold vs. sequential search.** The threshold does very different work across members. In [[@Tyson2008|Tyson (2008)]] and the TST umbrella of [[@Manzini2013|Manzini, Mariotti & Tyson (2013)]], $\theta(A)$ is an *atemporal filter* on a fully-perceived menu — the agent never "stops early," and there is no notion of an unsearched option. In [[@Papi2012|Papi (2012)]] and [[@Caplin2011|Caplin & Dean (2011)]] the threshold is a *stopping rule*: the agent quits the moment a satisfactory/above-reservation alternative is found, so options exist that were never examined. These are observationally different — the search models predict that an *inferior* option can be chosen out of unawareness, which the static threshold models, reading non-choice as below-threshold, cannot represent.
- **What choice-process data reveals that final-choice data cannot.** This is the heart of the topic. [[@Caplin2011|Caplin & Dean (2011)]] show that with incomplete search *any* final-choice pattern is rationalizable — final choices alone have no testable content for search models. Enriching to the choice process $C_A(t)$ (switches from $y$ to a later $x$ reveal $x\succ y$; co-selection reveals indifference) yields a single sharp acyclicity axiom (OWC). [[@Papi2012|Papi (2012)]] reaches the same conclusion from the other side: under his unobservable-search domain $D_3$, satisficing collapses to weak-order maximization and preference *above* the aspiration is unidentified — recovering it requires observing (some of) the search order. By contrast [[@Tyson2008|Tyson (2008)]] and [[@Tyson2015|Tyson (2015)]] extract content from *standard menu-variation* data alone, by exploiting menu-dependence rather than time — a fundamentally different data enrichment for the same underlying Simon story.
- **Menu-dependence of the threshold.** [[@Tyson2008|Tyson (2008)]] makes $\theta(A)$ explicitly menu-dependent and ties it to complexity via *nestedness* / *expansiveness* ($A\subseteq B,\ \max f[A]\ge\theta(B)\Rightarrow\theta(A)\ge\theta(B)$ — larger menus carry weakly lower bars), grounding menu-dependence in *perception* degrading with complexity. [[@Papi2012|Papi (2012)]] deliberately fixes the aspiration $x_s$ and flags an endogenous, problem-dependent threshold as future work. [[@Caplin2011|Caplin & Dean (2011)]] fix a single reservation $\rho$ across menus and likewise gesture at context-dependent stopping (citing Tyson) as open. So the members disagree on whether the bar moves with the menu, and Tyson's complexity-driven $\theta(A)$ is exactly the ingredient the search models leave out.
- **How much content the threshold architecture actually buys.** [[@Manzini2013|Manzini, Mariotti & Tyson (2013)]] deliver the deflationary verdict: the bare TST representation is characterized by mere acyclicity of the first-stage separation relation $F$, and is *vacuous for single-valued choice*. The predictive force of [[@Tyson2008|Tyson (2008)]] (Base Acyclicity + Strong Expansion) and [[@Tyson2015|Tyson (2015)]] (Weak Congruence + Base Transitivity) comes from their *extra* axioms — i.e., from expansiveness/nestedness — not from the threshold form itself. There is also an interpretive split TST exposes: in the satisficing reading the *primary* criterion $f$ is welfare-relevant, whereas in the limited-consideration readings the *secondary* criterion $g$ is — the same algebra, opposite welfare object.
- **Where welfare lives.** [[@Tyson2015|Tyson (2015)]] argues binary (small-menu) choices are the reliable welfare arbiter, since perception is finest on small menus. [[@Caplin2011|Caplin & Dean (2011)]] instead locate welfare in revealed preference recovered *along the search path* (and in below-reservation menus, which must have been fully searched). These are competing answers to "which observations carry welfare-significant preference" when behavior departs from maximization.

## Open questions

- **Endogenous / complexity-dependent thresholds.** [[@Papi2012|Papi (2012)]] fixes $x_s$ and [[@Caplin2011|Caplin & Dean (2011)]] fix $\rho$; both flag a threshold that varies with the choice problem (size, complexity, cost of search) as unresolved. [[@Tyson2008|Tyson (2008)]] supplies menu-dependent $\theta(A)$ but explicitly *declines* to micro-found it — leaving open the cognitive budget constraint that would generate it.
- **Reconciling time-based and menu-based identification.** [[@Caplin2011|Caplin & Dean (2011)]] identify search from contemplation-time data; the Tyson line and [[@Manzini2013|Manzini, Mariotti & Tyson (2013)]] identify from menu variation. No member offers a representation whose threshold/stopping rule is jointly disciplined by *both* data types, nor a statement of when one dominates the other.
- **Stopping rules beyond fixed reservation.** [[@Caplin2011|Caplin & Dean (2011)]] explicitly leave cardinality-dependent, context-dependent, and optimal/learning-based stopping uncharacterized — and point at [[@Tyson2008|Tyson (2008)]]-style context-dependence as the natural generalization.
- **Search style and the holistic-vs-dimensional boundary.** ABS/RBS assume alternative-based (not attribute-by-attribute) search; [[@Caplin2011|Caplin & Dean (2011)]] leave open *which environments* induce which search style. [[@Tyson2008|Tyson (2008)]] notes nestedness fails for menu-holistic effects (extremeness aversion, asymmetric dominance) — so both the static and search branches are restricted to pairwise/alternative-based evaluation, with the holistic case open.
- **Identification under incomplete sequence/process coverage.** [[@Papi2012|Papi (2012)]] notes satisficing DMs can appear to violate WARP merely because certain key menu sequences are never observed; [[@Caplin2011|Caplin & Dean (2011)]] note never-chosen items are indeterminate (searched or not). How robust is identification to realistically sparse process data?
- **Relaxing the perception structure.** [[@Tyson2015|Tyson (2015)]] flags relaxing complete-preorder perceived preferences (incomplete $R^1_A$, intransitive pseudo-indifference) and the infinite-$X$ numerical case as open; [[@Manzini2013|Manzini, Mariotti & Tyson (2013)]] leave the general map from "extra axioms" to "threshold properties" unsolved.

## Candidate ideas

- **Unified menu-and-time threshold representation.** Build a single satisficing model whose stopping/threshold is disciplined jointly by choice-process data ([[@Caplin2011|Caplin & Dean (2011)]]) *and* menu variation ([[@Tyson2008|Tyson (2008)]]), and characterize when the two data sources give overlapping vs. independent identifying restrictions — closing the time-vs-menu identification gap.
- **Complexity-indexed reservation utility.** Endogenize the aspiration/reservation as $\theta = \theta(\text{complexity}(A))$ by importing Tyson's nestedness/expansiveness ([[@Tyson2008|Tyson (2008)]]) into Caplin–Dean RBS ([[@Caplin2011|Caplin & Dean (2011)]]), then test the comparative static "larger/more-complex menus lower the bar" on choice-process data — directly answering Papi's fixed-$x_s$ open question ([[@Papi2012|Papi (2012)]]).
- **Empirically locating where the TST content comes from.** Use the [[@Caplin2011|Caplin & Dean (2011)]] elicitation paradigm to test the *extra* axioms ([[@Tyson2008|Tyson (2008)]] expansiveness, [[@Tyson2015|Tyson (2015)]] Weak Congruence) that [[@Manzini2013|Manzini, Mariotti & Tyson (2013)]] show carry all the predictive force beyond vacuous $F$-acyclicity — turning their logical-gap diagnosis into a falsification programme.
- **Welfare arbiter shoot-out.** Design choices where Tyson's "trust the small menu" criterion ([[@Tyson2015|Tyson (2015)]]) and Caplin–Dean's "trust the search path" criterion ([[@Caplin2011|Caplin & Dean (2011)]]) make *opposite* welfare assignments, and measure which better predicts incentivized later choice — adjudicating where welfare-relevant preference actually lives under satisficing.
- **Robustness of identification to sparse process data.** Quantify how Papi's WARP-appearance pathologies under partial sequence coverage ([[@Papi2012|Papi (2012)]]) and Caplin–Dean's never-chosen indeterminacy ([[@Caplin2011|Caplin & Dean (2011)]]) degrade recovery of preference and aspiration as observation thins — a bridge to designing minimally-sufficient satisficing experiments.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Manzini2007]] — cited by 4 members
- [[@Salant2008]] — cited by 4 members
- [[@Masatlioglu2012]] — cited by 2 members
- [[@Rubinstein2006]] — cited by 2 members
- [[@Bernheim2009]] — cited by 1 member
- [[@Cherepanov2013]] — cited by 1 member
- [[@Gabaix2006]] — cited by 1 member
- [[@Samuelson1938]] — cited by 1 member
- [[@Samuelson1988]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
