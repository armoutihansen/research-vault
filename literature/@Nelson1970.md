---
citekey: Nelson1970
title: Information and Consumer Behavior
authors: ["Nelson, Phillip"]
year: 1970
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/LYEVZRHV"
pdf: /Users/jesper/Zotero/storage/WUUGUDVY/Nelson1970.pdf
tags: [literature]
keywords: [search-goods, experience-goods, information-economics, monopoly-power, consumer-search, advertising]
topics: []
related: [Akerlof1970, Nelson1974]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary

Nelson introduces the now-foundational distinction between **search goods** (qualities a consumer can evaluate by inspection prior to purchase) and **experience goods** (qualities knowable only after purchase and use). He builds a simple optimal-sampling model of the consumer's quest for quality information and derives a battery of testable predictions linking the search/experience classification and frequency of purchase to monopoly power, the use of recommendations, retail store clustering, the retail-to-national advertising ratio, and inventory/sales ratios. Twelve empirical tests across five domains all come out in the predicted direction.

## Research question

How do limitations on consumer information about product *quality* (as distinct from price) shape market structure and firm behavior? Specifically, when should a consumer acquire quality information by pre-purchase **search** versus by post-purchase **experience**, and what does that choice imply for monopoly power, advertising, retail location, and inventory holdings?

## Method / identification

The core is an optimal-stopping (prior-decision) sampling model adapted from Stigler's economics of information, applied separately to search and experience. A consumer samples brands until marginal expected cost equals marginal expected return. The marginal return to the $i$-th sample is the gain in the expected utility of the best option observed:
$$MR_i = E_p(B_i) - E_p(B_{i-1})$$
where $E_p(B_i)$ is the expected present value (in utility terms) of the best of $i$ options. For **search**, cost is the direct cost of an inspection and is independent of the utility distribution. For **experience**, the only way to sample a brand is to buy and consume it, so the marginal cost is the foregone utility from consuming a random brand instead of the best already discovered:
$$MC_i = E(B_{i-1}) - \mu$$
with $\mu$ the mean of the utility distribution. Because experience yields a repeated stream of future consumption, the present-value marginal return is rescaled by purchase frequency $f$, horizon $t$, and the per-purchase interest rate $s = (1+a)^{1/f} - 1$ (with $a$ the annual rate):
$$MR_i = [E(B_i) - E(B_{i-1})]\, f \sum (1+s)^{-(\cdot)}$$
The equilibrium number of experiments is the largest $i$ for which $MC_i \le MR_i$. Nelson solves this for rectangular and normal utility distributions (e.g., for the rectangular case with $t \to \infty$, $i$ is the largest integer satisfying a closed-form bound), tabulating sample sizes for both prior-decision and sequential-decision variants across frequencies (Table 1). A key derived object is the weight $w_E$ on the (zero-elasticity) experimental period in overall demand elasticity:
$$w_E = 1 - (1+a)^{-n/f}$$
with $n$ the sample size; since $n/f$ falls as frequency rises, the zero-elasticity experimental period matters more for low-frequency goods. Empirically, goods are classified into search vs. experience using the ratio of repair (non-merchandise) receipts to sales for durables (Table 2), and via destructibility of sampling for nondurables; predictions are tested with two-sample $t$-tests and binomial/hypergeometric tests against null distributions built from consumer-expenditure shares.

## Data

Multiple secondary U.S. datasets: 1958 Census concentration ratios (value added of the eight largest firms) for monopoly tests; *Consumer Reports* articles 1963-64 for guidance; Van Handel's (1969) central-business-district sales shares for location/clustering; *New York Times* advertisements over seven scattered days in 1966-67 for the retail/national advertising ratio; and the 1929 Census of Retailing (the only year with inventory data) for inventory/sales ratios. Repair-expenditure ratios are from 1963 Census of Business data.

## Key findings

1. **Monopoly power.** Concentration ratios are higher for experience goods than search goods and higher for durables than nondurables, holding frequency constant (Table 3); all differences significant at the 5% level or better. The mechanism: smaller equilibrium sample sizes concentrate demand among fewer brands, and the zero-elasticity experimental period further lowers measured elasticity for experience goods.
2. **Sample-size ordering.** Search yields larger sample sizes than experience for the same good, and sample size rises with purchase frequency.
3. **Guidance.** Recommendations (friends, *Consumer Reports*) are used more for experience than search goods and more for low-frequency goods; rejected null at the .001 level in most tests.
4. **Location.** Stores selling search goods cluster more in central business districts than experience-good stores (Van Handel), since multi-store search makes inter-store travel time matter.
5. **Advertising.** The retail-to-national-brand advertising ratio is far higher for search goods (probabilities .0028 and .0032 under the hypergeometric null).
6. **Inventory.** Inventory/sales ratios are higher for search-good stores, because search-good markets support more brands and stores cannot specialize as narrowly.

Twelve tests across five areas all point in the predicted direction; treating biases as independent with zero expected value, the joint probability under the null is at most about $1/32$.

## Contribution

Establishes the search/experience taxonomy as a primitive of information economics and demonstrates that *consumer* information-acquisition behavior — not only production functions or market size — is a determinant of monopoly power and of advertising, location, and inventory patterns. It operationalizes Stigler's search theory for quality and extends it to the experience case where sampling requires purchase. The framework seeded a vast literature on advertising as a quality signal, reputation, and (later, with Darby and Karni) credence goods.

## Limitations & open questions

- The model uses **prior-decision** sampling for tractability; Nelson notes sequential (optimal-stopping) sampling is "more appropriate" and reports it only in tabulated form — a fuller sequential treatment is left open.
- Random sampling is assumed; **guided sampling** is handled only heuristically, with the "detailed theory of guidance" omitted for space.
- Classification is admittedly **crude** (repair-expenditure proxies, destructibility), biasing estimated effects toward zero; better quality-variance measures are needed.
- Standard significance tests are invalid under **bias of unknown direction/magnitude**, the pervasive problem with testing economic propositions; the multi-domain design is a partial workaround, not a solution.
- The price-quality relationship that would guide experience sampling is left unmodeled ("the roughest sort of guide to choice").

## Connections

The search apparatus builds directly on Stigler (1961, 1962) "The Economics of Information," narrowing Stigler's notion to pre-purchase inspection. Van Handel (1969) supplies the location-clustering test. The taxonomy was completed by Darby & Karni (1973), who added **credence goods**, and the experience-good logic underpins Nelson's own later work on advertising as a signal ([[@Nelson1974|Nelson 1974]]) and the signaling literature of Spence (1973). It connects to reputation models such as Klein & Leffler (1981) and Shapiro (1983), and to the broader information-economics tradition of [[@Akerlof1970|Akerlof (1970)]] on quality uncertainty. Within consumer choice modeling, the sampling/optimal-stopping structure relates to later rational-inattention and costly-information accounts of choice (e.g., Caplin & Dean 2015).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
