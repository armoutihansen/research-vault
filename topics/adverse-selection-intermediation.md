---
slug: adverse-selection-intermediation
title: "Adverse Selection, Quality & Intermediation"
type: topic
scope: "Markets with privately-known quality: lemons, certification, and middlemen as expert information intermediaries."
area: "[[industrial-organization-markets]]"
tags: [topic]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This topic covers markets where one side privately knows a good's vertical quality and a common price for heterogeneous units threatens to unravel trade — the lemons problem — together with the institutions that restore it: certification, warranties, reputation, and middlemen acting as expert information intermediaries. It spans the foundational adverse-selection mechanism, the formal "good news" apparatus (MLRP) that orders the signals such institutions emit, and a sequence of models in which an inspecting/certifying middleman either resolves or reshapes the inefficiency. Its boundary: quality is *exogenously held* or *chosen by the seller*, and the friction is hidden quality (adverse selection / quality moral hazard), not search frictions per se or pure persuasive communication — those border on the intermediation-via-search and advertising topics.

## Sub-themes

- **The lemons mechanism and its welfare logic.** [[@Akerlof1970|Akerlof (1970)]] is the source: a common price for hidden, heterogeneous quality makes average supplied quality fall with price, so trade shrinks or vanishes, and private/social returns to quality diverge. This is the unraveling that every other member tries to undo or re-derive.
- **Middlemen as quality-validating experts.** [[@Biglaiser1993|Biglaiser (1993)]], [[@Biglaiser1999|Biglaiser & Friedman (1999)]], and [[@Biglaiser2018|Biglaiser & Li (2018)]] form the program's spine: an infinitely-lived, reputation-backed dealer who sinks an inspection investment and offers warranties, restoring (or distorting) trade where atomistic sellers cannot signal.
- **The formal grammar of signals.** [[@Milgrom1981|Milgrom (1981)]] supplies the favorableness/MLRP language and the unraveling-via-disclosure result that underpin both the contingent contracts and the "good news raises price" mechanics the middleman models rely on.
- **Learning as an alternative to certification.** [[@Crawford2005|Crawford & Shum (2005)]] and the disintermediation channel of [[@Hendershott2006|Hendershott & Zhang (2006)]] handle hidden match-quality through Bayesian experience and consumer self-selection/search rather than an expert certifier — a complementary, sometimes rival, resolution.

## Cross-paper tensions

The sharpest tension is internal to the middleman program: **does the expert intermediary cure adverse selection or weaponize it?** [[@Biglaiser1993|Biglaiser (1993)]] proves a welfare *ceiling*-raising middleman in *all* equilibria when transaction costs are low and the quality gap large — the dealer's volume justifies inspection and his infinite horizon makes reputation credible. But [[@Biglaiser1999|Biglaiser & Friedman (1999)]] shows, in a competitive version, that middlemen "typically" *over-inspect* and that eliminating search costs can *lower* welfare; intermediation's sign becomes ambiguous once entry $F$ is a resource cost. [[@Biglaiser2018|Biglaiser & Li (2018)]] then inverts the 1993 optimism entirely: when quality is the seller's *endogenous, sunk* effort, a perfectly informative middleman ($\phi_m=1$), or many competing ones ($K\to\infty$), drives effort to its *minimum* $\underline q$ via hold-up and a misidentification externality. So the three papers, sharing authorship and apparatus, disagree on the basic comparative static $\partial(\text{quality})/\partial(\text{middleman precision})$ — positive in 1993, ambiguous in 1999, perversely negative in 2018. The hinge is whether quality is *given* (1993/99) or *chosen under hold-up* (2018), and whether the middleman can *commit* to a price.

A second tension concerns **what is hidden and how it is resolved.** Akerlof and the Biglaiser line treat quality as a fixed seller type cured by certification/inspection. [[@Crawford2005|Crawford & Shum (2005)]] dissolves the lemons logic differently: match-quality is idiosyncratic and learned, and they find learning recovers $\sim$90% of first-best utility *without* any certifier — diagnostic matching by an expert doctor does most of the work. This is a rival resolution: experience and a benevolent expert-agent vs. a self-interested certifying middleman. Crucially, Crawford & Shum *assume* the doctor is a perfect agent and flag agency/detailing as unidentified — exactly the hold-up/conflict that [[@Biglaiser2018|Biglaiser & Li (2018)]] makes central. The two literatures thus make opposite maintained assumptions about the intermediary's incentives.

A third tension is about **signal credibility and unraveling.** [[@Milgrom1981|Milgrom (1981)]]'s disclosure result predicts full unraveling — skeptical buyers infer withheld news is the worst, forcing complete disclosure — which would *make certifying middlemen redundant*. The Biglaiser models survive only by breaking Milgrom's verifiability: signalling-by-delay fails the single-crossing/Spence–Mirrlees condition (1993), or the middleman's signal is noisy and his report non-verifiable (2018). The tension: under what conditions does Grossman–Milgrom unraveling *not* obtain, leaving room for a paid expert? Relatedly, [[@Hendershott2006|Hendershott & Zhang (2006)]] sidesteps quality certification altogether — disintermediation via a direct channel raises welfare by price-discriminating on search cost — suggesting the *value* the middleman adds may be sorting/search, not quality validation, contradicting Biglaiser's quality-guarantor rationale.

## Open questions

- **Free entry and the number of middlemen.** [[@Biglaiser1993|Biglaiser (1993)]] solves only the single middleman; [[@Biglaiser1999|Biglaiser & Friedman (1999)]] leaves the endogenous number/differentiation of competitive middlemen open; [[@Biglaiser2018|Biglaiser & Li (2018)]] finds competition *destroys* effort under no-recall but *reverses* with recall. The welfare sign of middleman entry is unsettled.
- **Continuous signals and general distributions.** Biglaiser & Li only *conjecture* their misidentification/market-premium decomposition survives a continuous MLRP signal; Biglaiser & Friedman assume uniform distributions. The robustness of unraveling to concave utility was already flagged open by Akerlof.
- **Endogenous, dynamic reputation.** Every middleman model invokes reputation-as-bond informally with pessimistic off-path beliefs; none solves the explicit dynamic monitoring game that keeps the certifier honest.
- **Agency inside the expert.** Crawford & Shum cannot identify doctor agency/detailing effects; the whole intermediation line lacks empirical discrimination between the quality-guarantor and search/sorting rationales.

## Candidate ideas

- **Endogenous-quality middleman with commitment.** Re-solve [[@Biglaiser2018|Biglaiser & Li (2018)]] allowing the middleman to *post a price schedule before* the seller's effort choice; test whether commitment converts the perverse $\phi_m=1$ effort-collapse back into the welfare gain of [[@Biglaiser1993|Biglaiser (1993)]] — pinning down commitment as the knife-edge.
- **Certification vs. learning, structurally.** Embed a self-interested certifier into the [[@Crawford2005|Crawford & Shum (2005)]] match-learning framework and estimate whether observed expert markups reflect quality-validation rents or sorting, using their unidentified "doctor agency" channel as the target parameter.
- **When does unraveling spare the expert?** Map the verifiability/cost conditions under which [[@Milgrom1981|Milgrom (1981)]] disclosure unraveling fails, formalizing the parameter region in which a *paid* certifying middleman (à la [[@Biglaiser1999|Biglaiser & Friedman (1999)]]) is strictly value-adding rather than redundant.
- **Quality-guarantor or search-reducer?** Build a model nesting the [[@Hendershott2006|Hendershott & Zhang (2006)]] search/price-discrimination channel and the [[@Biglaiser1993|Biglaiser (1993)]] inspection channel to derive testable predictions (price vs. quality dispersion) that separate the two rationales empirically.
- **Over-inspection and competition policy.** Use the [[@Biglaiser1999|Biglaiser & Friedman (1999)]] "too much inspection" result plus the [[@Biglaiser2018|Biglaiser & Li (2018)]] competition-degrades-quality result to ask whether entry of certifiers/rating agencies should be *restricted* — a behavioral-IO normative on credence/certification markets.
- **Securitization as adverse-selection externality.** Take the [[@Biglaiser2018|Biglaiser & Li (2018)]] misidentification externality to data on loan securitization, testing whether more core-dealer screening precision lowered originator effort, operationalizing their pre-2008 narrative.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Nelson1970]] — cited by 2 members
- [[@Choi1991]] — cited by 1 member
- [[@Coughlan1985]] — cited by 1 member
- [[@Jeuland1983]] — cited by 1 member
- [[@McGuire1983]] — cited by 1 member
- [[@Milgrom1986]] — cited by 1 member
- [[@Moorthy1987]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
