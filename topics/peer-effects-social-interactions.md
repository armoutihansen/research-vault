---
slug: peer-effects-social-interactions
title: "Peer Effects & Social Interactions"
type: topic
scope: "Identifying causal peer/neighborhood effects (reflection problem) in education, crime, health, work, and consumption."
area: "[[social-other-regarding-preferences]]"
tags: [topic]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This topic covers the empirical identification of *causal* peer and neighborhood effects — how one agent's behavior responds to the behavior or composition of a reference group — across education, crime, adolescent health, the workplace, and consumption. Every member confronts Manski's reflection problem and its companions (the separation of **endogenous** effects from **contextual** and **correlated/selection** effects), and the methods used to escape them (random assignment, fixed effects, instruments, network geometry, variance decomposition, real-effort experiments). The boundary is methodological-and-causal: structural status-signaling models of *why* visible consumption spreads live in conspicuous-consumption; pure reciprocity/social-preference theory lives in its own topics; this topic is where those forces are *measured* as spillovers.

## Sub-themes

- **Random/quasi-random assignment of peers or neighborhoods.** The cleanest selection-free designs: roommate randomization ([[@Sacerdote2001|Sacerdote (2001)]], [[@Zimmerman2003|Zimmerman (2003)]]) and refugee dispersal ([[@Damm2014|Damm & Dustmann (2014)]]).
- **Observational identification under sorting + reflection.** Linear-in-means with peer-background instruments and mover-stayer / fixed-effects discipline: [[@Gaviria2001|Gaviria & Raphael (2001)]], [[@Lundborg2006|Lundborg (2006)]], [[@Trogdon2008|Trogdon et al. (2008)]].
- **Structural network and variance-based identification.** Deriving the estimating equation from a model — Nash-Katz-Bonacich centrality ([[@Calvo-Armengol2009|Calvó-Armengol et al. (2009)]]) and the cross-city variance index ([[@Glaeser1996|Glaeser et al. (1996)]]).
- **Workplace productivity spillovers and mechanism.** Real-effort experiment ([[@Falk2006a|Falk & Ichino (2006)]]), scanner-data cashiers ([[@Mas2009|Mas & Moretti (2009)]]), and economy-wide wage spillovers ([[@Cornelissen2017|Cornelissen et al. (2017)]]).
- **Consumption and context-moderated effects.** Hyper-local consumption diffusion ([[@Grinblatt2008|Grinblatt et al. (2008)]]) and gender-by-neighborhood moderation of peer susceptibility ([[@Zimmerman2010|Zimmerman & Messner (2010)]]).

## Cross-paper tensions

**Sign of the bias in naive estimates — the sharpest disagreement.** The reflexive presumption is that uncorrected OLS peer effects are *upward*-biased by sorting. Yet [[@Lundborg2006|Lundborg (2006)]] finds instrumenting *more than doubles* the marginal effect (binge drinking $0.23\to0.56$), and [[@Trogdon2008|Trogdon et al. (2008)]] and [[@Gaviria2001|Gaviria & Raphael (2001)]] also report 2SLS $\geq$ OLS — implying *downward* bias, which they attribute to attenuation from mismeasured peer behavior. [[@Cornelissen2017|Cornelissen et al. (2017)]] sit on the opposite pole: stacking fixed effects collapses $\gamma$ from $0.148$ to $0.011$, and they argue any residual bias is *upward*. Whether IV estimates that exceed OLS reflect cured attenuation or failed exclusion restrictions is unresolved across the corpus.

**Reflection-problem solutions are mutually distrusting.** [[@Calvo-Armengol2009|Calvó-Armengol et al. (2009)]] argue overlapping individual-specific reference groups (friend-of-friend structure) *identify* the effect through network geometry — precisely the structure absent from the common-group linear-in-means designs of [[@Gaviria2001|Gaviria & Raphael]] and [[@Lundborg2006|Lundborg]], whose peer-background instruments are valid *only if* contextual effects are exactly zero (an assumption the authors themselves doubt). [[@Falk2006a|Falk & Ichino (2006)]] sidestep the whole problem by design, but at $N=24$ with one observation per subject.

**Are the variance-index magnitudes credible?** [[@Glaeser1996|Glaeser et al. (1996)]] turn the cross-city second moment into a social-interaction index (implied group sizes >200 for larceny). [[@Gaviria2001|Gaviria & Raphael (2001)]] apply the *same* nonparametric test and find indices an order of magnitude smaller, explicitly "casting doubt on the structural interpretation of those [crime] indices." The index is only separable from unobserved heterogeneity under a normality or magnitude assumption [[@Glaeser1996|Glaeser et al.]] concede a skeptic can reject.

**Mechanism is contested and under-identified.** [[@Mas2009|Mas & Moretti (2009)]] pin productivity spillovers on social pressure / mutual monitoring (effort rises only for workers *in the entrant's line of vision*); [[@Cornelissen2017|Cornelissen et al. (2017)]] corroborate pressure over knowledge spillover by occupation type; but [[@Grinblatt2008|Grinblatt et al. (2008)]] argue *against* envy/status and *for* fast-decaying information in consumption, while conceding they cannot explain why even information decays within ten days. [[@Damm2014|Damm & Dustmann (2014)]] and [[@Sacerdote2001|Sacerdote (2001)]] both invoke Manski's point that even a cleanly identified endogenous effect leaves the *channel* (constraints, expectations, preferences) unidentified.

**Where is the reference group, and is the technology linear?** [[@Sacerdote2001|Sacerdote (2001)]] finds GPA effects at the room level but fraternity effects at the dorm level; [[@Grinblatt2008|Grinblatt et al.]] find consumption effects vanish beyond the 10 nearest neighbors; [[@Cornelissen2017|Cornelissen et al.]] define peers as occupation$\times$firm$\times$year. Linearity-in-means is also contested: [[@Zimmerman2003|Zimmerman (2003)]], [[@Falk2006a|Falk & Ichino]], and [[@Mas2009|Mas & Moretti]] all find the *low*-ability worker gains most (favoring skill-diverse mixing), and [[@Trogdon2008|Trogdon et al.]] find higher peer-BMI moments matter — directly challenging the single-mean specification most identification strategies assume.

## Open questions

- **Symmetry of multipliers.** [[@Trogdon2008|Trogdon et al. (2008)]] flag that no study shows peer effects are symmetric (does weight *loss* spread like weight gain?) — decisive for whether policy multipliers actually operate, and untested for crime, substance use, and consumption too.
- **Separating contextual from endogenous effects.** The IV designs ([[@Gaviria2001|Gaviria & Raphael]], [[@Lundborg2006|Lundborg]]) *assume* contextual effects away; [[@Sacerdote2001|Sacerdote]] cannot split $\beta$ (contextual) from $\gamma$ (endogenous) without heroic assumptions. No member jointly identifies all three.
- **Mechanism behind heterogeneity.** Why verbal > math ([[@Zimmerman2003|Zimmerman]]), why females are *more* peer-susceptible in violence but *less* in drinking ([[@Zimmerman2010|Zimmerman & Messner]], [[@Lundborg2006|Lundborg]]), and why effects concentrate in the lower ability/income tail ([[@Falk2006a|Falk & Ichino]], [[@Grinblatt2008|Grinblatt et al.]]) are all documented but unexplained.
- **Dynamics.** Almost every design is contemporaneous or cross-sectional ([[@Trogdon2008|Trogdon et al.]], [[@Mas2009|Mas & Moretti]], [[@Falk2006a|Falk & Ichino]]); the build-up, persistence (the freshman-roommate GPA effect fades by senior year in [[@Sacerdote2001|Sacerdote]]), and decay of peer effects are largely open.
- **Beyond linear-quadratic / linear-in-means.** [[@Calvo-Armengol2009|Calvó-Armengol et al.]] flag that the Katz-Bonacich linkage is proven only for linear-quadratic utility, and local-*average* (conformism) vs. local-*aggregate* peer effects are not adjudicated.

## Candidate ideas

- **Resolve the bias-sign puzzle.** Build a measurement-error-vs-exclusion-violation decomposition that explains *when* IV exceeds OLS, calibrated to the conflicting evidence in [[@Lundborg2006|Lundborg (2006)]], [[@Trogdon2008|Trogdon et al. (2008)]], and [[@Cornelissen2017|Cornelissen et al. (2017)]]; ML predicted-peer-quality as an attenuation correction.
- **Test multiplier symmetry directly.** Use a setting with both peer increases and decreases (e.g. workplace entry/exit as in [[@Mas2009|Mas & Moretti]], where exit effects already look smaller than entry) to estimate sign-asymmetry, settling the symmetry question [[@Trogdon2008|Trogdon et al.]] raise.
- **Reconcile variance indices with micro estimates.** Re-run the [[@Glaeser1996|Glaeser et al. (1996)]] index on a setting with credibly identified micro peer effects ([[@Damm2014|Damm & Dustmann]] refugee-dispersal crime) to calibrate how much "excess variance" is interaction vs. heterogeneity, addressing [[@Gaviria2001|Gaviria & Raphael]]'s skepticism.
- **Network structure as the mechanism discriminator.** Estimate the [[@Calvo-Armengol2009|Calvó-Armengol et al. (2009)]] centrality model on data with observed line-of-sight / monitoring ([[@Mas2009|Mas & Moretti]]) to test whether structural centrality predicts where social-pressure spillovers bite.
- **Nonlinearity and optimal mixing.** Estimate a flexible (non-linear-in-means) peer technology using the lower-tail gains in [[@Falk2006a|Falk & Ichino]], [[@Zimmerman2003|Zimmerman]], and [[@Mas2009|Mas & Moretti]] to derive welfare-maximizing assignment rules, contrasting skill-diversity vs. tracking.
- **Context-moderated susceptibility.** Generalize the cross-level interaction of [[@Zimmerman2010|Zimmerman & Messner (2010)]] into a structural model where the peer-effect coefficient itself depends on environment and friendship intimacy, testing whether "stable traits" (gender, ability) have context-dependent behavioral mappings.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Charness2002]] — cited by 1 member
- [[@Fehr1993]] — cited by 1 member
- [[@Fehr1997]] — cited by 1 member
- [[@Jones2009]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
