---
citekey: Mayzlin2014
title: "Promotional Reviews: An Empirical Investigation of Online Review Manipulation"
authors: ["Mayzlin, Dina", "Dover, Yaniv", "Chevalier, Judith"]
year: 2014
type: journalArticle
doi: 10.1257/aer.104.8.2421
zotero: "zotero://select/library/items/DBNIY7HW"
pdf: /Users/jesper/Zotero/storage/SIWGNQ76/Mayzlin2014.pdf
tags: [literature]
keywords: [online-reviews, review-manipulation, organizational-form, reputation, difference-in-differences, signal-jamming, platform-design]
topics: []
related: [Milgrom1986, Nelson1974]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Online reviews could, in principle, greatly improve consumers' ability to evaluate products. However, the authenticity of online user reviews remains a concern; firms have an incentive to manufacture positive reviews for their own products and negative reviews for their rivals. In this paper, we marry the diverse literature on economic subterfuge with the literature on organizational form. We undertake an empirical analysis of promotional reviews, examining both the extent to which fakery occurs and the market conditions that encourage or discourage promotional reviewing activity. Specifically, we examine hotel reviews, exploiting the organizational differences between two travel websites: Expedia.com and TripAdvisor.com. While anyone can post a review on TripAdvisor, a consumer can only post a review of a hotel on Expedia if she actually booked at least one night at the hotel through the website. We examine differences in the distribution of reviews for a given hotel between TripAdvisor and Expedia. We exploit the characteristics of a hotel's neighbor. We show that hotels with a nearby neighbor have more one- and two-star (negative) reviews on TripAdvisor relative to Expedia. We argue that the net gains from promotional reviewing are likely to be highest for independent hotels that are owned by single-unit owners and lowest for branded chain hotels that are owned by multi-unit owners. Our methodology thus isolates hotels with a disproportionate incentive to engage in promotional reviewing activity. We show that the hotel neighbors of hotels with a high incentive to fake have more one- and two-star (negative) reviews on TripAdvisor relative to Expedia than do hotels whose neighbors have a low incentive to fake. Furthermore, we show that hotels with a high incentive to fake have a greater share of five-star (positive) reviews on TripAdvisor relative to Expedia.

## Summary
The paper detects online review manipulation indirectly, without ever classifying any individual review as fake. It exploits an organizational-form discontinuity between TripAdvisor (anyone can post) and Expedia (only verified bookers can post), so faking is cheap on the former and expensive on the latter. Comparing the same hotel's review distribution across the two sites, and interacting that gap with neighbor and ownership characteristics, the authors show that hotels with a disproportionate economic incentive to fake (independents, single-unit owners) and the neighbors of such hotels exhibit exactly the review patterns a manipulation model predicts. A stylized Hotelling/signal-jamming model in the appendix ties the empirics to reputational cost of being caught.

## Research question
Does promotional (fake) reviewing occur at economically meaningful scale on open review platforms, and is its intensity governed by the firm's reputational cost of manipulation as determined by competitive proximity and organizational form (affiliation, ownership, management)?

## Method / identification
The empirical strategy is a non-standard differences-in-differences in which neither difference is temporal. For each hotel $i$ in city $j$ the outcome is the within-hotel gap in the share of $N$-star reviews across the two platforms, estimated as
$$\frac{N\text{StarReviews}^{TA}_{ij}}{\text{TotalReviews}^{TA}_{ij}}-\frac{N\text{StarReviews}^{Exp}_{ij}}{\text{TotalReviews}^{Exp}_{ij}}=X_{ij}B_1+\text{OwnAf}_{ij}B_2+\text{Nei}_{ij}B_3+\text{NeiOwnAf}_{ij}B_4+\sum_j\gamma_j+\varepsilon_{ij}.$$
Attention focuses on the extremes: $1$- and $2$-star reviews (negative manipulation, predicted to be driven by *neighbor* characteristics) and $5$-star reviews (positive manipulation, driven by *own* characteristics). $X_{ij}$ is a rich set of observable hotel controls (official star rating, STR tier dummies, age, location type, all-suites/convention/restaurant indicators), $\gamma_j$ are city fixed effects, and standard errors are heteroskedasticity-robust. The identifying assumption is that TripAdvisor and Expedia users do not differentially value the (largely unobservable) ownership/affiliation characteristics of a hotel or its neighbors. The design mirrors the indirect-cheating-detection literature (Duggan & Levitt; Jacob & Levitt; DellaVigna & La Ferrara), with the innovation that two platforms of differing fakery cost provide a benchmark.

The appendix presents a four-stage signal-jamming Hotelling model. Two firms $A,B$ have unobservable qualities $q_i\sim N(q_0,\sigma_q^2)$; each firm exerts effort $e_{i,i}$ on positive self-promotion and $e_{i,j}$ on negative reviews of its rival, generating signals $s_A=q_A+e_{A,A}-e_{B,A}$ and $s_B=q_B+e_{B,B}-e_{A,B}$. Manipulation is convexly costly, $C(e_{i,i},e_{i,j})=\frac{\delta_i}{2}(e_{i,i})^2+\frac{\gamma_i}{2}(e_{i,j})^2$, where $\delta_i$ and $\gamma_i$ are the reputational damages from being caught self-promoting or attacking, respectively. Consumers Bayes-update with weight $\mu_s=\sigma_q^2/(\sigma_q^2+\sigma_\varepsilon^2)$ and choose via a Hotelling indifference condition.

## Data
Hotel reviews scraped in October 2011 from TripAdvisor and Expedia for the 25th-75th largest US cities (Las Vegas dropped), matched by name and address to Smith Travel Research (STR) industry data on official rating, location, age, and—crucially—affiliation, ownership, and management structure. The base sample is 2,931 hotels with reviews on both sites (350,485 TripAdvisor and 123,569 Expedia reviews). TripAdvisor averages ~3x more reviews per hotel and is more critical (mean 3.52 vs 3.95 stars). A robustness sample uses TripAdvisor vs. Orbitz (verified/unverified flags) for 2,512 hotels collected January 2013.

## Key findings
- **Negative manipulation (Table 4):** Having any neighbor within 0.5 km raises the cross-site gap in $1$- and $2$-star share by ~1.9-3.0 percentage points; an *independent* neighbor adds a further 1.7 pp; a *multi-unit-owner* neighbor reduces it by 2.5 pp. Own ownership characteristics are insignificant for negative reviews—as the manipulation hypothesis (but not a taste-difference story) predicts.
- **Positive manipulation (Table 4):** Independent hotels show a 2.4 pp larger cross-site gap in $5$-star share than chains; multi-unit-owner hotels show a 3.1 pp smaller gap (~4 fewer 5-star reviews). Neighbor characteristics are insignificant here, again as predicted.
- **Magnitudes:** An independent, single-unit-owned hotel generates ~7 more fake positive TripAdvisor reviews than a chain hotel with a large owner; a hotel next to such a hotel gets ~6 more fake negative reviews than an isolated hotel.
- **Model (Proposition 1):** optimal efforts $e^*_{A,A}=\frac{p_A\mu_s}{2\delta_A t}$, $e^*_{A,B}=\frac{p_A\mu_s}{2\gamma_A t}$ (symmetrically for $B$). **Corollary 1:** lower reputational cost raises manipulation ($\partial e^*/\partial\gamma<0$ in cost), and firms always do positive *and* negative manipulation in equilibrium. Strikingly, in the symmetric-information benchmark consumers perfectly discount fakery, so manipulation does not change choices—yet firms still fake, because abstaining would be (mis)read as terrible quality.

## Contribution
First paper to empirically identify review manipulation via a platform-design discontinuity rather than textual markers, and to show manipulation responds to economic incentives shaped by organizational form. It bridges the strategic-communication/persuasion literature with the organizational-form and reputational-spillover literature, demonstrating that larger entities curb cheating because the cost of detection spills over many units while the benefit accrues to one. It also offers practical input to fakery-detection algorithms (organizational form is hard to alter, unlike text) and to review-system design (verification cuts fakery but also cuts review volume).

## Limitations & open questions
The authors explicitly flag: (1) manipulation is inferred, never observed directly; (2) the measure ignores review *content*, so it misses text-intensive attacks (e.g., a fabricated bed-bug claim)—"an interesting issue for future work"; (3) they cannot measure manipulation's *impact on consumer purchase behavior*—do consumers detect and discount fakes, discount all reviews, or make poor choices? These are "left for future work." The verified-vs-unverified compromise (Orbitz, Amazon) is noted as not fully solving the platform's problem of whether to aggregate unverified reviews.

## Connections
The theoretical backbone is Mayzlin (2006) on promotional chat and Dellarocas (2006), which reach opposite welfare conclusions about whether high- or low-quality firms manipulate more; this paper extends them by letting manipulation cost differ across firms. It sits within strategic communication and persuasion—Crawford & Sobel (1982), Kamenica & Gentzkow (2011), [[@Milgrom1986|Milgrom & Roberts (1986)]], [[@Nelson1974|Nelson (1974)]]—but departs by making the sender's identity *uncertain* rather than common knowledge. On reviews and demand it builds on Chevalier & Mayzlin (2006), Luca (2012), Anderson & Magruder (2012). On organizational form and reputational spillovers it connects to Jin & Leslie (2009), Blair & Lafontaine (2005), Pierce & Snyder (2008), Bennett et al., and Ji & Weil (2009). Methodologically it parallels indirect cheating detection in Duggan & Levitt (2002), Jacob & Levitt (2003), and DellaVigna & La Ferrara (2010). Textual-detection alternatives it critiques include Ott et al. (2011) and Kornish (2009).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
