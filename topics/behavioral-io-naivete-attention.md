---
slug: behavioral-io-naivete-attention
title: "Behavioral IO: Naivete, Shrouding & Attention"
type: topic
scope: "Firms exploiting consumer mistakes: shrouded add-on prices, naivete-based discrimination, steering, and attention/salience shocks in markets."
area: "[[industrial-organization-markets]]"
tags: [topic]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This topic covers markets in which rational, profit-maximizing firms (or intermediaries) interact with *fallible* consumers — those who ignore part of what they pay, mispredict their own future behavior, or attend to only a slice of their choice set. The unifying object is the **hidden/additional price** that a naive or inattentive consumer fails to internalize at the point of choice but pays anyway, and the central question is whether competition disciplines its exploitation. The boundary is deliberately market-level and supply-aware: the cognitive primitive (myopia, present bias, forgetting, limited attention) is taken as given from Layer-1 choice theory; what is in scope is how firms *price against* it, *discriminate on* it, *steer* with it, and how attention shocks move equilibrium behavior. Pure individual-choice models of consideration sets live in the limited-attention topic; here attention is a market force.

## Sub-themes

- **Shrouding and add-on pricing (theory).** The foundational engine: [[@Gabaix2006|Gabaix & Laibson (2006)]] on shrouded add-on prices surviving competition via the curse of debiasing, generalized into a field-defining reduced-form "additional price" scaffold by the [[@Heidhues2018|Heidhues et al. (2018)]] survey.
- **Naivete-based discrimination and steering.** Conditioning offers on *who is naive* rather than on preferences — [[@Heidhues2017|Heidhues & Kőszegi (2017)]] — and its dynamic extension to recommender systems, where intermediaries steer fallible consumers using information about their *mistakes*: [[@Heidhues2023|Heidhues et al. (2023)]].
- **Lapse- and forgetting-based contracts.** Firms designing contracts that profit from predictable consumer failure to follow through: [[@Gottlieb2021|Gottlieb & Smetters (2021)]] on lapse-supported life insurance driven by forgetfulness and underweighted liquidity shocks.
- **Attention as a market force (field evidence).** Limited attention shaping which assets/products enter the consideration set and how salience shocks move behavior: [[@Barber2008|Barber & Odean (2008)]] and its out-of-sample replication [[@Seasholes2007|Seasholes & Wu (2007)]] on attention-driven buying, and [[@Stango2014|Stango & Zinman (2014)]] on uninformative salience shocks cutting overdraft fees.

## Cross-paper tensions

**Does competition protect naive consumers? The sharpest fault line.** [[@Gabaix2006|Gabaix & Laibson (2006)]] and [[@Heidhues2018|Heidhues et al. (2018)]]' "safety-in-markets" benchmark deliver a *reassuring* result: with $v>c$ and imperfect competition, naive consumers' equilibrium welfare is *unaffected* by naivete — firms set the additional price to $a_{\max}$ but compete it back through lower anticipated prices $f_l$. [[@Heidhues2017|Heidhues & Kőszegi (2017)]] then weaponizes the same model to deliver the *opposite* verdict: once firms can discriminate on naivete, the total welfare distortion $\mathrm{DWL}(\alpha)=k(a(\alpha))$ is invariant to market power $t$, so competition only redistributes and sharper targeting strictly lowers welfare (strictly so iff $k'/k''$ is increasing, weaker than prudence in the credit case). The tension is not a contradiction but a knife-edge: *whose information* and *which trades are distorted* flips the welfare sign. [[@Heidhues2023|Heidhues et al. (2023)]] pushes the reversal furthest — value-based steering helps, but mistake-based and perceived-value-based steering harm *unboundedly* whenever the consumer does not "buy reasonably," and they argue real-world ML steering is exactly the harmful type.

**Are sophisticates a check on exploitation, or accomplices?** In [[@Gabaix2006|Gabaix & Laibson (2006)]], sophisticates *cannot* discipline shrouding — the curse of debiasing means they prefer to stay at high-markup firms and free-ride on myope-targeted loss leaders. [[@Seasholes2007|Seasholes & Wu (2007)]] gives the empirical counterpart: identified "smart traders" do not debias individuals; they *profit* from the attention bias at 1.16% per day, their investment *predicting* next-day naive buying. So both papers agree sophistication arbitrages rather than corrects — but [[@Heidhues2017|Heidhues & Kőszegi (2017)]]'s cross-subsidy runs the other way (naive *subsidize* sophisticates via competition on $f_l$), raising the unresolved question of when sophisticates are subsidized versus when they are the residual claimants on others' mistakes.

**Disclosure/education: futile, or potent?** The theory wing is pessimistic by construction: [[@Gabaix2006|Gabaix & Laibson (2006)]]'s no-firm-unshrouds result and [[@Heidhues2018|Heidhues et al. (2018)]]'s "soft interventions fail in equilibrium" both say information remedies backfire or are unavailable. Yet [[@Stango2014|Stango & Zinman (2014)]] shows *uninformative* salience shocks — reminders carrying zero account-specific information — durably cut overdraft fees by ~3.7 p.p. for up to two years, strongest for the low-literacy consumers the theory says are most exploited. The reconciliation hinges on a primitive the theory leaves fixed: is the problem *information* (which shrouding theory says firms suppress) or *attention* (a buildable, decaying stock that third-party reminders can replenish)? The two literatures model the same overdraft market with incompatible levers.

**Naive vs. sophisticated as a behavioral primitive — and is it even identified?** The discrete naive/sophisticated split is load-bearing in [[@Gabaix2006|Gabaix & Laibson (2006)]] and [[@Heidhues2017|Heidhues & Kőszegi (2017)]], but [[@Gottlieb2021|Gottlieb & Smetters (2021)]] needs a *different* primitive — forgetting (37.8% of lapses) and narrowly-framed liquidity underweighting (15.4%) — and explicitly dispatches present bias as the wrong microfoundation. Meanwhile [[@Heidhues2017|Heidhues & Kőszegi (2017)]] concedes its central identification gap: the *same* demand data admit a preference-based and a naivete-based reading, and direct evidence that firms discriminate on naivete is thin. [[@Barber2008|Barber & Odean (2008)]] is candid that none of its three attention proxies is clean. Across the topic, the behavioral driver is rarely separately identified from rational alternatives (search costs, short-sale constraints, reclassification risk).

## Open questions

- **Participation distortions and the perfect-competition limit.** [[@Heidhues2017|Heidhues & Kőszegi (2017)]] flags that as $t\to 0$ the perceived price falls below marginal cost, generating possibly massive *over*participation — yet the safety-in-markets result assumes participation is fixed. When does naivete inflate the *extensive* margin rather than just redistribute on the intensive one?
- **Strategic naivete.** Every model here assumes consumers do not infer their own naivete from suspiciously attractive offers ([[@Heidhues2018|Heidhues et al. (2018)]]; the exogenous $\tilde v(\cdot)$ in [[@Heidhues2023|Heidhues et al. (2023)]]). What survives if consumers grow suspicious?
- **Attention substitution and welfare.** [[@Stango2014|Stango & Zinman (2014)]] cannot sign welfare (does vigilance on overdrafts crowd out attention to credit-card balances?) and cannot disentangle attention from fee-paying *learning*. [[@Barber2008|Barber & Odean (2008)]] takes the attention process as exogenous.
- **Multidimensional heterogeneity and coexisting distortions.** Naivete-plus-taste, and homogeneous/sophisticated-side/naive-side distortions coexisting in one market (e.g. insurance), are "relatively unexplored" ([[@Heidhues2018|Heidhues et al. (2018)]]; [[@Heidhues2017|Heidhues & Kőszegi (2017)]]).
- **What technology implements *value-based* steering?** [[@Heidhues2023|Heidhues et al. (2023)]] cannot say what real practice yields the benign type — an open design/regulation problem.
- **Empirical BIO is in its infancy.** The survey explicitly notes theory is far ahead of evidence; identifying hidden prices and discrimination from market data, and the residual unexplained lapses in [[@Gottlieb2021|Gottlieb & Smetters (2021)]], remain open.

## Candidate ideas

- **Identify naivete-based discrimination in the wild.** Use targeted-offer data (mortgage/credit-card mailers) to test whether firms condition the *additional* price $a(\alpha)$ on proxies for naivete, separating it from preference-based discrimination — closing the identification gap [[@Heidhues2017|Heidhues & Kőszegi (2017)]] concedes and the empirical-BIO call in [[@Heidhues2018|Heidhues et al. (2018)]].
- **Reminders vs. shrouding, head-to-head.** Field-experiment whether ongoing third-party salience shocks ([[@Stango2014|Stango & Zinman (2014)]]) actually unwind the no-debiasing equilibrium of [[@Gabaix2006|Gabaix & Laibson (2006)]], measuring whether attention replenishment substitutes for the disclosure that firms suppress.
- **Test the welfare knife-edge of steering.** Audit recommender outputs to classify steering as value- vs. mistake- vs. perceived-value-based and estimate the "buys/refrains reasonably" statistics from [[@Heidhues2023|Heidhues et al. (2023)]], turning its unbounded-harm prediction into a regulatable diagnostic.
- **Attention substitution as a welfare test.** Use linked multi-account data to check whether overdraft vigilance ([[@Stango2014|Stango & Zinman (2014)]]) crowds out attention on credit cards, resolving the welfare indeterminacy and the [[@Barber2008|Barber & Odean (2008)]] attention-budget conjecture.
- **Strategic naivete under exploitative offers.** Build (and lab-test) a model where consumers Bayes-update their own naivete from offer attractiveness, asking whether the [[@Gabaix2006|Gabaix & Laibson (2006)]] shrouding and [[@Heidhues2017|Heidhues & Kőszegi (2017)]] discrimination equilibria survive — the unstudied hook both flag.
- **Mandatory reminders as lapse policy.** Quantify, in the [[@Gottlieb2021|Gottlieb & Smetters (2021)]] structure, whether forced payment reminders (which forgetting-exploiting insurers will never send voluntarily) raise consumer welfare net of the lost lapse cross-subsidy.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Milgrom1981]] — cited by 3 members
- [[@Bordalo2013]] — cited by 1 member
- [[@Eliaz2011a]] — cited by 1 member
- [[@Inderst2012]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
