---
citekey: Grinblatt2008
title: "Social Influence and Consumption: Evidence from the Automobile Purchases of Neighbors"
authors: ["Grinblatt, Mark", "Keloharju, Matti", "Ikäheimo, Seppo"]
year: 2008
type: journalArticle
doi: 10.1162/rest.90.4.735
zotero: "zotero://select/library/items/U2SYMBHB"
pdf: /Users/jesper/Zotero/storage/I9D68X4R/Grinblatt2008.pdf
tags: [literature]
keywords: [social-influence, peer-effects, consumption, reflection-problem, nearest-neighbors-identification, conspicuous-consumption, information-diffusion]
topics: ["[[peer-effects-social-interactions]]"]
related: [Glaeser1996, Sacerdote2001]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This study analyzes the automobile purchase behavior of all residents of two Finnish provinces over several years. Using a comprehensive data set with location coordinates at the individual consumer level, it finds that the purchases of neighbors, particularly in the recent past and by those who are geographically most proximate, influence a consumer's purchases of automobiles. There is little evidence that emotional biases, like envy, account for the observed social influence on consumption.

## Summary
Using a comprehensive Finnish administrative panel that geolocates every resident of two provinces (Greater Helsinki and surroundings) to building-level latitude/longitude and records the exact date of every car purchase, the authors show that a neighbor's recent car purchase sharply raises a consumer's own propensity to buy a car. The effect is concentrated in the very nearest neighbors, decays to near-zero within about ten days, is strongest in rural areas and among low-income consumers, and is far larger for the *same make and model* and for used cars. The authors argue this pattern is inconsistent with envy or status signaling and most consistent with localized information transmission (and, secondarily, conformity).

## Research question
Does social influence operate in the consumption of a major visible durable good (automobiles), and if so, what mechanism drives it—emotional biases such as envy/status-seeking ("keeping up with the Joneses"), conformity, or information sharing? A central methodological sub-question is how to credibly identify such a peer effect given the classic omitted-variables and reflection problems.

## Method / identification
The unit of analysis is a binary buy/not-buy decision for subject $i$ in year $t$ (also specialized to new vs. used, and to particular makes/models). Because control variables barely change within a year, each resident contributes one observation per year: purchasers on their actual purchase date, and non-purchasers on a randomly assigned "shadow non-purchase date" drawn so the non-purchase date distribution matches the purchase date distribution (yielding annualized-rate coefficients). This gives 2,520,575 binary observations. Estimation is primarily logit (with OLS and fixed-effects robustness checks).

The identification core is the **nearest neighbors approach**. Linearizing the choice model, the subject's action is
$$a = fA + g_o x_o + g_u x_u,$$
where $A$ is neighborhood car-buying history, $x_o$ observed and $x_u$ unobserved subject attributes. Endogenous sorting makes $x_u$ correlate with $A$, biasing $f$. The authors split the neighborhood into an inner ring (10 nearest) with state $A_1$ and an outer ring (neighbors 11–50) with state $A_2$, and estimate
$$a = f_1\,(A_1 - A_2) + g_o x_o + [\,g_u x_u + (f_1+f_2)A_2\,],$$
where the bracket is the residual. Because $A_2$ proxies the same unobserved common neighborhood attributes as $A_1$, the *difference* $A_1 - A_2$ purges $x_u$; distant neighbors' purchases effectively instrument for the omitted common factors. They validate this by showing the inner–outer ring difference in the prior ten-day purchase rate is uncorrelated with every observable $x_o$ and with the subject's own attributes—inferring the same holds for unobservables. The construction also conservatively biases a positive $f_1$ toward zero since $A_2$ is negatively correlated with $A_1 - A_2$.

The **reflection problem** (Manski) is handled two ways: (i) the regressor uses *lagged* neighbor actions, which a subject's current purchase cannot have caused; (ii) nearest-neighbor proximity is non-commutative—a subject is one of the ten nearest neighbors of his own ten nearest neighbors only ~41% of the time (16% for the single nearest neighbor)—so feedback $h$ on the inner-minus-outer difference is small. They argue this yields at least a threefold (fivefold in urban areas) reduction in reflection bias. Fixed-effects logit/OLS with per-subject dummies confirm the coefficient is stable.

## Data
Two linked Finnish administrative sources for the provinces of Uusimaa and East Uusimaa (Greater Helsinki). The Finnish Vehicle Administration provides ownership and exact purchase dates (new vs. used inferred from registration history); income-tax returns provide income deciles, age, sex, marital status, dependents, homeownership, employment, work-travel costs, and address. Addresses are converted to (anonymized, rotated) lat/long, giving each subject a distance-ranked hierarchy of the 500 nearest neighbors observed daily over 1994–2001, with controls over 1999–2001. Spouses are excluded as neighbors to avoid confounding. Car purchases are rare, seasonal events.

## Key findings
- Neighbors' recent purchases significantly raise own purchase propensity. The nearest neighbor buying on the same day carries a logit coefficient of about 1.3; the surface of 135 time×distance coefficients peaks at near/recent and decays steeply.
- The influence is **short-lived**: purchases more than ~10 days old have negligible effect (average coefficient below 0.01 for days −11 to −30).
- The influence is **hyper-local**: essentially no effect beyond the 50 nearest neighbors; the inner 10 dominate.
- Stronger in **rural areas** than cities (inversely related to population density).
- Strongest among the **lowest income deciles**; influence from a same-income-decile neighbor is largest (multiplies daily buy propensity ~1.16) and from higher-income neighbors larger than from lower-income ones.
- Larger for **used cars** than new cars (used-car coefficient ~50% bigger), and same-type purchases reinforce same-type decisions.
- Strongest of all for **same make** (coefficient ~5× the "other makes" effect) and **same make-and-model** (~10× the other-makes effect).
- Fixed-effects estimates are essentially unchanged (OLS neighborhood coefficient 0.0092 → 0.0096 with neighbor fixed effects), implying ~12% increase in the annualized purchase rate per additional inner-ring purchase.

## Contribution
Provides one of the first credible, micro-level empirical demonstrations of social influence in consumption of a visible durable, using a research design whose location precision, daily frequency, and rich administrative controls jointly address the omitted-variables and reflection problems that had undermined prior neighborhood-effects studies. Beyond establishing the effect, it discriminates among competing mechanisms: the speed of decay, the rural/low-income concentration, and the same-make/used-car patterns are argued to rule out envy and status signaling and to favor localized, time-sensitive information transmission (e.g., dealer pricing/inventory) and conformity.

## Limitations & open questions
- The mechanism is inferred, not directly identified: the authors cannot fully reconcile *why* even an information story would decay to near-zero within ten days; conformity is hard to square with a fast-decaying "emotion."
- They lack data on what triggers the *initial* neighbor purchase, so status signaling as a driver of those first purchases cannot be ruled out.
- The 6-month new/used classification and truncation in the ownership snapshot (cars owned as of June 10, 2002) bias time trends, though the social-influence conclusions are robust.
- In dense urban buildings the exact ten nearest neighbors cannot always be pinpointed, attenuating urban estimates.
- The setting is institutionally specific (high Finnish auto/fuel taxes, strong public transit, luxury status of cars), raising external-validity questions for other goods and countries.

## Connections
The paper situates itself against the theoretical literature on interpersonal consumption effects—Veblen (1899), Duesenberry (1949/1962), Leibenstein (1950), Friedman (1957), Becker (1974), Pollak (1976), Abel (1990), Galí (1994), Bagwell & Bernheim (1996), Campbell & Cochrane (1999), and Hopkins & Kornienko (2004)—and on conformity and fads (Bikhchandani, Hirshleifer & Welch (1992), Bernheim (1994), Pesendorfer (1995)). Its identification confronts the reflection and omitted-variables critiques of Manski (1993), Evans, Oates & Schwab (1992), and Akerlof (1997). Empirically it builds on the neighborhood- and peer-effects literature: [[@Sacerdote2001|Sacerdote (2001)]], Topa (2001), [[@Glaeser1996|Glaeser, Sacerdote & Scheinkman (1996)]], Bayer, Ross & Topa (2005), Kling, Ludwig & Katz (2005), and especially Marmaros & Sacerdote (2006), whose rapid distance-decay of social interaction parallels these results; Goolsbee & Klenow (2002) on local consumption spillovers. The information-mechanism discussion draws on Putsis & Srinivasan (1994) (time to purchase), and Kapteyn et al. (2007) (Dutch Post Code Lottery) provides corroborating evidence that windfall-induced visible consumption does not spread to neighbors.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
