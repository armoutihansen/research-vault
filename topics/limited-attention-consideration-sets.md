---
slug: limited-attention-consideration-sets
title: "Limited Attention & Consideration Sets"
type: topic
scope: "Models in which a DM maximizes a stable preference over an attention-limited or stochastically-formed consideration set, and the identification of preference vs. (in)attention."
area: "[[bounded-rationality-choice]]"
tags: [topic]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This topic collects models in which a decision maker (DM) maximizes a *stable* preference $\succ$ but only over a **consideration set** $\Gamma(A)\subseteq A$ she actually attends to, rather than over the full feasible menu $A$. The defining question is one of **identification**: once the full-attention axiom underpinning classical revealed preference is dropped, when can preference be separated from (in)attention — and how does the consideration set respond to feasibility, salience, menu size, and information cost? The boundary is the consider-then-maximize architecture with a *fixed* welfare-relevant order; menu-dependence driven by genuinely shifting preferences (context effects, reference dependence) lives in neighbouring topics, as do pure shortlisting procedures where the screening criterion is itself a rationale rather than an attention/feasibility primitive.

## Sub-themes

- **Deterministic attention filters and their revealed-preference content.** The MNO program: [[@Masatlioglu2012|Masatlioglu, Nakajima & Ozbay (2012)]] (attention filter, unawareness), [[@Lleras2017|Lleras, Masatlioglu, Nakajima & Ozbay (2017)]] (competition filter, "more is less"), [[@Iwata2018|Iwata (2018)]] (salience-affected attention), and [[@Masatlioglu2013|Masatlioglu & Nakajima (2013)]] (dynamic search paths). All recover preference from *choice reversals*, never from being chosen.
- **Stochastic consideration / feasibility.** [[@Manzini2014|Manzini & Mariotti (2014)]] (independent menu-independent attention probabilities $\gamma(a)$), [[@Brady2016|Brady & Rehbeck (2016)]] (correlated random feasibility via a subset distribution $\pi$), with [[@Dardanoni2020|Dardanoni, Manzini, Mariotti & Tyson (2020)]] inferring the *distribution* of cognitive types from aggregate shares.
- **Optimal / cost-based consideration.** [[@Caplin2019|Caplin, Dean & Leahy (2019)]] (Shannon rational inattention endogenizes the set), and the marketing cost-benefit tradition: [[@Hauser1990|Hauser & Wernerfelt (1990)]], [[@Roberts1991|Roberts & Lattin (1991)]].
- **Threshold / satisficing screens as consideration.** [[@Manzini2013|Manzini, Mariotti & Tyson (2013)]] and [[@Manzini2016|Manzini, Mariotti & Tyson (2016)]] (two-stage threshold representations and partial knowledge), [[@Papi2012|Papi (2012)]] (satisficing under graded observability), [[@Caplin2011|Caplin & Dean (2011)]] (search and choice-process data).
- **Consideration as the observable / as market strategy.** [[@Eliaz2011|Eliaz, Richter & Rubinstein (2011)]] (the shortlist itself is observed), [[@Eliaz2011a|Eliaz & Spiegler (2011)]] (firms compete to enter consideration sets), [[@Lehmann1994|Lehmann & Pan (1994)]] (context effects act on the consideration stage).

## Cross-paper tensions

**The sharpest tension is point identification of preference, and it cleaves the topic.** Deterministic attention models *do not* identify $\succ$: [[@Masatlioglu2012|MNO (2012)]] recover only the partial order $P_R$ (the transitive closure of reversals), and crucially when data satisfy WARP they identify *nothing* — behavior is equally consistent with full attention or with never noticing anything but the chosen item. [[@Lleras2017|Lleras et al. (2017)]] inherit the same partial-identification ceiling under the competition filter. [[@Manzini2014|Manzini & Mariotti (2014)]] turn this into a selling point of *stochastic* consideration: their independence + asymmetry axioms deliver **unique** recovery of both $\succ$ and $\gamma$, something deterministic models provably cannot. So the field disagrees on whether the route to identification is *richer data* (process data, salience manipulations) or *stochasticity itself*.

**Rival filter axioms that are mutually incompatible.** The MNO **attention filter** ($\Gamma(A)=\Gamma(A\setminus x)$ when $x\notin\Gamma(A)$) and the [[@Lleras2017|Lleras et al. (2017)]] **competition filter** ($x\in\Gamma(T),\,S\subseteq T\Rightarrow x\in\Gamma(S)$ — Sen's $\alpha$ on attention) are explicitly *orthogonal*: each rationalizes anomalies the other forbids, and Lleras et al. note that imposing *both* yields no clean characterization (left as an open problem). [[@Iwata2018|Iwata (2018)]] extends MNO with salience but keeps it incompatible with the competition channel.

**The menu-independence knife-edge.** A recurring, almost identical impossibility result appears across the stochastic strand: [[@Manzini2014|Manzini & Mariotti (2014)]] Theorem 2 and [[@Brady2016|Brady & Rehbeck (2016)]] Theorem 3.2 both show that *menu-dependent* attention/feasibility weights make the model vacuous — every rule is rationalizable by every $\succ$. Identification therefore hinges entirely on menu-independence, which Brady–Rehbeck themselves call "hardly defensible for consideration sets." Yet [[@Caplin2019|Caplin, Dean & Leahy (2019)]] derive consideration sets that are *intrinsically* menu/prior-dependent and even *non-monotone* in attention cost $\lambda$ — a direct theoretical clash with the tractability assumption the revealed-preference models lean on.

**Are consideration models even random utility models?** [[@Brady2016|Brady & Rehbeck (2016)]] prove the RCCSR violates regularity, so it is *not* a RUM, and it strictly generalizes [[@Manzini2014|Manzini & Mariotti's]] rule by a single swapped axiom (correlated vs. independent consideration → substitutes/complements). This sits against [[@Caplin2019|Caplin et al. (2019)]], whose Shannon model also produces consideration sets but from optimization, and whose hedging/correlation structure is a feature, not a primitive distribution.

**Vacuity of the bare architecture.** [[@Manzini2013|Manzini, Mariotti & Tyson (2013)]] deliver the deflationary punchline that the two-stage threshold structure is *empirically empty on single-valued data* — all predictive content comes from the supplementary axioms (the attention filter, monotone threshold, expansiveness). [[@Manzini2016|Manzini, Mariotti & Tyson (2016)]] show content reappears only when components $\langle f,\theta,g\rangle$ are externally known. This challenges every model in the topic: how much of its "explanatory power" is the consider-then-maximize template versus the specific filter?

**Marketing realism vs. axiomatic minimalism.** [[@Hauser1990|Hauser & Wernerfelt (1990)]] and [[@Roberts1991|Roberts & Lattin (1991)]] *derive* set size from an explicit cost-benefit log-sum and fit it to scanner data, but assume away inter-brand interactions and impose distributional structure ($\lambda$ lognormal) "not from first principles." [[@Lehmann1994|Lehmann & Pan (1994)]] show context effects (attraction, compromise, extremeness) reshape the consideration set itself with a hard size cap — a behavioral regularity the axiomatic filters do not predict.

## Open questions

- **Which restricted menu-dependence is identified?** Both [[@Manzini2014|Manzini & Mariotti (2014)]] and [[@Brady2016|Brady & Rehbeck (2016)]] leave open exactly which forms of menu-dependent attention stay tractable between the identified (independent) and vacuous (fully dependent) extremes.
- **Hybrid consideration-plus-utility-noise.** [[@Manzini2014|Manzini & Mariotti (2014)]] model only consideration error, not utility noise; is a model with *both* still identified?
- **Removing the default / no-default variants.** [[@Brady2016|Brady & Rehbeck (2016)]] and [[@Manzini2014|Manzini & Mariotti (2014)]] both flag that dropping the outside option $x^*$ breaks identification of the bottom of $\succ$.
- **Cost-function dependence of endogenous consideration.** [[@Caplin2019|Caplin, Dean & Leahy (2019)]] show their closed forms are Shannon-specific (Invariance Under Compression fails for Tsallis); consideration-set predictions under general posterior-separable costs are open.
- **Combining filters / mechanism discrimination.** [[@Lleras2017|Lleras et al. (2017)]] leave the attention-∩-competition filter uncharacterized, and OC is observationally equivalent to categorization and rationalization — separating mechanisms needs non-choice data.
- **Endogenous / variable thresholds.** [[@Papi2012|Papi (2012)]], [[@Manzini2016|Manzini, Mariotti & Tyson (2016)]], and [[@Caplin2011|Caplin & Dean (2011)]] all fix the aspiration/reservation level; making it depend on menu complexity is unaddressed.
- **From individual to aggregate.** [[@Masatlioglu2013|Masatlioglu & Nakajima (2013)]] and [[@Caplin2019|Caplin et al. (2019)]] flag identifying *distributions* of preferences and consideration from market-share data — the gap [[@Dardanoni2020|Dardanoni et al. (2020)]] partially fills with tensor decomposition.

## Candidate ideas

- **Test stochastic vs. deterministic identification head-to-head.** Run a lab choice experiment with both menu variation and eye-tracking, then compare what the unique-identification machinery of [[@Manzini2014|Manzini & Mariotti (2014)]] recovers against the partial order $P_R$ of [[@Masatlioglu2012|MNO (2012)]] and the certified attention of [[@Iwata2018|Iwata (2018)]] — does stochasticity buy real identification, or artefactual precision?
- **Characterize the "identification frontier" of menu-dependence.** Find the maximal class of menu-dependent attention $\delta(a,A)$ that stays uniquely identified, closing the gap between Theorem 1 and Theorem 2 of [[@Manzini2014|Manzini & Mariotti (2014)]] / Theorems 3.1–3.2 of [[@Brady2016|Brady & Rehbeck (2016)]].
- **A consideration model with both attention error and utility noise.** Build and axiomatize a hybrid of [[@Manzini2014|Manzini & Mariotti's (2014)]] $\gamma(a)$ with a Luce/RUM taste shock, testing whether $(\succ,\gamma)$ survive identification — the explicit open question both that paper and [[@Brady2016|Brady & Rehbeck (2016)]] raise.
- **Reconcile rational inattention with menu-independence.** Derive when [[@Caplin2019|Caplin, Dean & Leahy's (2019)]] Shannon consideration sets *approximate* a menu-independent $\gamma$, giving a cost-based microfoundation for the [[@Manzini2014|Manzini–Mariotti]] primitive and a test to distinguish them on prior-variation data.
- **Estimate the cognitive-type distribution on real scanner data.** Implement the [[@Dardanoni2020|Dardanoni et al. (2020)]] tensor-decomposition identification on grocery panel data, using the correlated-feasibility reading of [[@Brady2016|Brady & Rehbeck (2016)]] to recover substitutes/complements alongside the attention distribution.
- **Filter discrimination via salience manipulation.** Use [[@Iwata2018|Iwata's (2018)]] salience reversals to empirically separate the attention filter of [[@Masatlioglu2012|MNO (2012)]] from the competition filter of [[@Lleras2017|Lleras et al. (2017)]] — the combination Lleras et al. could not characterize — and test the consideration-stage context effects of [[@Lehmann1994|Lehmann & Pan (1994)]].

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Manzini2007]] — cited by 12 members
- [[@Salant2008]] — cited by 8 members
- [[@Cherepanov2013]] — cited by 4 members
- [[@Tyson2008]] — cited by 4 members
- [[@Huber1982]] — cited by 3 members
- [[@Rubinstein2006]] — cited by 3 members
- [[@Gabaix2006]] — cited by 2 members
- [[@Apesteguia2013]] — cited by 1 member
- [[@Bagwell2007]] — cited by 1 member
- [[@Bernheim2009]] — cited by 1 member
- [[@Bordalo2013]] — cited by 1 member
- [[@Dutta2015]] — cited by 1 member
- [[@Jeuland1983]] — cited by 1 member
- [[@Kalai2002]] — cited by 1 member
- [[@Loomes1991]] — cited by 1 member
- [[@Mandler2012]] — cited by 1 member
- [[@Manzini2012a]] — cited by 1 member
- [[@May1954]] — cited by 1 member
- [[@Ok2015]] — cited by 1 member
- [[@Rubinstein2012]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
