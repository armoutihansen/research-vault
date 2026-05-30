---
citekey: Heidhues2023
title: Steering fallible consumers
authors: ["Heidhues, Paul", "Köster, Mats", "K\\Hoszegi, Botond"]
year: 2023
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/T58N9WY5"
pdf: /Users/jesper/Zotero/storage/L6B8NCHV/Heidhues2023.pdf
tags: [literature]
keywords: [steering, behavioral-io, naivete-based-discrimination, consumer-protection, recommender-systems, welfare-analysis]
topics: []
related: [Bordalo2013, Gabaix2006, Inderst2012, Milgrom1981]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Online intermediaries (Google, Facebook, Amazon) "steer" consumers toward products they are more likely to buy. The classic result is that, holding prices fixed, steering helps consumers by improving the selection of products they consider. Heidhues, Köster and Kőszegi overturn this for *fallible* consumers who make statistical and strategic mistakes when evaluating offers. They show the welfare effect of steering hinges on (i) the *type* of information the intermediary uses — the consumer's true values, her mistakes, or her perceived values — and (ii) two novel behavioural properties they call "buying reasonably" and "refraining reasonably." Steering based on high-quality information about a consumer's mistakes is typically harmful, sometimes unboundedly so, and they argue much real-world steering (A/B testing of frames, ML targeting) is exactly of this type — building an economic case for regulating recommender systems.

## Research question
When an intermediary steers a consumer toward a product using private information about her, does steering raise or lower consumer welfare once we allow the consumer to be *fallible* (to misjudge values) rather than rational, and once we allow steering to exploit her *mistakes* rather than only her preferences?

## Method / identification
A stylised theoretical welfare model. There are $I$ ex ante identical products with fixed price normalised to zero. True values $v_i$ are drawn from CDF $G$ (density $g$); mistakes $m_i$ from CDF $F$ (density $f$); both log-concave, full support on $\mathbb{R}$, independent, with hazard rates going to infinity. For the recommended product $i^*$ the consumer observes a signal $w_{i^*}=v_{i^*}+m_{i^*}$ and forms a subjective value $\tilde v_{i^*}=\tilde v(w_{i^*})$ via a fixed, strictly increasing $\tilde v(\cdot)$ that does *not* depend on the intermediary (this exogeneity encodes *strategic naivete*; the shape of $\tilde v(\cdot)$ encodes *statistical errors*). The consumer buys iff $\tilde v_{i^*}\ge 0$, equivalently iff $v_{i^*}+m_{i^*}\ge\bar w$ for a threshold $\bar w$.

The intermediary maximises purchase probability using an informative signal $s_i$ satisfying the monotone likelihood ratio property (MLRP), so a higher $s_i$ is "good news"; it optimally recommends the product with the highest signal. Three steering types are defined by what $s_i$ is about: **value-based** ($s_i$ about $v_i$), **mistake-based** ($s_i$ about $m_i$), and **perceived-value-based** ($s_i$ about $\tilde v_i$). Two technologies: *binary* steering (observe whether the parameter exceeds a cutoff) and *perfect* steering (observe the parameter exactly). Welfare is the consumer's expected utility relative to the no-steering benchmark (random recommendation).

The two central definitions: the consumer **buys reasonably** if the average value of a random product conditional on purchase is positive, i.e. $\int_{-\infty}^{\infty} v\,[1-F(\bar w - v)]\,dG(v) > 0$; she **refrains reasonably** if the average value conditional on no purchase is negative, $\int_{-\infty}^{\infty} v\,F(\bar w - v)\,dG(v) < 0$; she is **always reasonable** if $\tilde v_i(w_i)=E[v_i\mid w_i]$. Steering is *weak* (binary with low cutoff, barely raises purchase probability) versus *strong* (purchase probability near 1, requires large $I$). The endogenous-price extension (Section 7) lets the intermediary, after recommending, set the seller's profit-maximising price.

## Data
None — this is a pure theory paper. Welfare results are illustrated with numerical examples (binary steering, $\tilde v(w_i)=w_i$, $I=\infty$, $m_i\sim N(0,1)$, and various $v_i\sim N(\mu,1)$). Real-world steering claims in Section 8 draw on secondary/anecdotal evidence (Kohavi et al. A/B-testing cases, Bing ad experiments, Hannak et al. on Expedia, audit studies of life insurance and financial advice).

## Key findings
- **Remark 1 / Proposition 2 (rational benchmark):** With no noise, value-based steering strictly raises welfare. With noise, a rational consumer benefits from value-based and perceived-value-based steering, and — for large $I$ — even from perfect mistake-based steering (she can heavily discount her signal to recover near-perfect value information).
- **Proposition 1:** With a large enough hidden price $M$ (so $F=F_M$, $F_M(m)=F_0(m-M)$) and $E[v_i]<0$, the consumer refrains reasonably but does *not* buy reasonably — the empirically motivated case.
- **Proposition 3 (value-based):** Strong steering benefits any consumer; weak steering harms her if she does not buy reasonably. Steering benefits her *for any* signal structure iff she buys reasonably.
- **Proposition 4 (mistake-based):** Mistake-based steering harms her for any signal structure iff she does *not* buy reasonably; weak steering helps if she buys reasonably; it benefits her for any structure iff she does not refrain reasonably; strong steering harms a consumer who refrains reasonably (hence harms an always-reasonable consumer).
- **Proposition 5 (perceived-value-based):** Benefits her for any structure iff she buys reasonably; benefits her if she does not refrain reasonably or is always reasonable.
- **Proposition 6 (perfect steering, endogenous prices):** Value-based steering still benefits her (the intermediary prices below value to avert non-purchase); mistake-based steering harms her (prices aggressively against the overvaluation, even when she does not refrain reasonably); perceived-value-based steering harms her (extracts all perceived value). Harm can be unbounded.
- Table 1 summarises: weak steering of any type is beneficial iff she buys reasonably; not refraining reasonably is sufficient for any steering to help.

## Contribution
First analysis of the welfare effects of steering when consumers make mistakes and when steering exploits those mistakes rather than preferences. It separates the roles of strategic naivete and statistical error, introduces the "buys/refrains reasonably" conditions as the pivotal welfare statistics, and shows the standard "steering helps with fixed prices" conclusion fails — reversing it precisely for the empirically dominant case (strong, mistake- or perceived-value-based steering with violated reasonability in buying). It thereby supplies economic foundations for regulating recommender systems and dark patterns.

## Limitations & open questions
- Endogenous pricing is only partially analysed (Section 7 treats one special case: perfect steering, many products, intermediary sets profit-maximising price); a full equilibrium pricing analysis is left open.
- The model abstracts from consumer search and its costs; steering that lowers search costs could benefit consumers independently of type (Footnote 25), a channel not modelled.
- It is "difficult to imagine" how an algorithm would implement value-based steering; the authors explicitly note they "do not currently know what practices would result in value-based steering" — an open empirical/design problem and a hook for regulation directing steering toward value-based.
- Conclusions about which real-life practices map to which steering type are "somewhat speculative" given scant evidence on actual steering technologies.
- Enforcing restrictions (e.g., steering only on self-declared interests / self-initiated search) requires verifying no other information is used — a measurement challenge ("controlled browsing" experiments are only a partial tool).

## Connections
The model of mistake-exploiting differential treatment builds on naivete-based discrimination — Eliaz & Spiegler (2006), Heidhues & Kőszegi (2010, 2017), Johnen (2020), Bar-Gill (2021) — but departs by making steering shape *which* products are considered rather than pricing within a full consideration set. It sits against the rational steering literature (Varian (1996), Bergemann & Bonatti (2011), Hagiu & Jullien (2011), [[@Inderst2012|Inderst & Ottaviani (2012a)]], de Corniere (2016), Marotta et al. (2018), Hidir & Vellodi (2021), Teh & Wright (2022)) and policy reports (ACCC (2019), Furman et al. (2019), CMA (2020)) that conclude fixed-price steering helps consumers. The mistakes draw on projection bias (Loewenstein, O'Donoghue & Rabin (2003)), overinference from small samples (Rabin & Vayanos (2010)), hidden/shrouded prices ([[@Gabaix2006|Gabaix & Laibson (2006)]], Heidhues & Kőszegi (2018)), context-dependent choice ([[@Bordalo2013|Bordalo, Gennaioli & Shleifer (2013)]]), and persuasive models (Schwartzstein & Sunderam (2021)). MLRP good-news structure follows [[@Milgrom1981|Milgrom (1981)]]. Empirical anchors include Anagol et al. (2017) and Mullainathan et al. (2011) on advisor steering, Gottlieb (2012) on life-insurance underpurchase, Hannak et al. (2014) on Expedia, Kohavi et al. (2020) on A/B testing, and the Digital Services Act proposal (European Commission, 2020) and Fletcher et al. (2023) on regulation.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
