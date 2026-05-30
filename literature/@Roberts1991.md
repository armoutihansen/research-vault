---
citekey: Roberts1991
title: Development and Testing of a Model of Consideration Set Composition
authors: ["Roberts, John H.", "Lattin, James M."]
year: 1991
type: journalArticle
doi: 10.2307/3172783
zotero: "zotero://select/library/items/AQNKBM42"
pdf: /Users/jesper/Zotero/storage/XL2ZWWEC/Roberts1991.pdf
tags: [literature]
keywords: [consideration-set, choice-modeling, multinomial-logit, multiattribute-utility, search-costs, two-stage-choice]
topics: []
related: [Hauser1990]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The authors develop a model of consideration set composition. The approach taken is to compare the marginal expected benefits of including an additional brand in the consideration set with its associated costs of consideration. From an expression of the utility that a brand needs to gain membership in an existing consideration set, the authors derive an expression for set composition and optimal set size. They develop a measurement method to test the model at the individual level and apply it to the ready-to-eat cereal market. The model is tested in two ways. First, the utility function is calibrated at the individual level and the model is used to predict consideration of existing brands. The calibrated model also is used to forecast individual consideration of three new product concepts. Second, the predictive ability of a two-stage model of consideration and choice is tested against a traditional one-stage choice model. The authors conclude with a discussion of management implications of the model in terms of auditing currently available brands and new product management.

## Summary
Roberts and Lattin model the consumer's consideration set as the outcome of a cost-benefit calculation: each additional brand raises the expected maximum utility obtainable from the set, but at a fixed "consideration cost" (search, thinking, mental storage). Under a logit utility framework, this yields a closed-form expression for which brands enter the set, the threshold utility a brand must clear, and the optimal set size $n$. The model is calibrated at the individual level on Australian ready-to-eat cereal data and used both to predict consideration of existing brands and to forecast consideration (and choice) of new product concepts, outperforming naive one-stage benchmarks.

## Research question
How is a consumer's consideration set composed, and what determines its size? Specifically: given awareness of $N$ brands, which brands does a utility-maximizing consumer include in the set she actually deliberates over, and how does that composition depend on brand utilities and the costs of consideration? The paper focuses on individual-level decision making (in contrast to Hauser and Wernerfelt's aggregate, market-level treatment) and on modeling the full composition of the set rather than just whether a single brand joins an existing set.

## Method / identification
The model assumes additive multiattribute utility $u_i=\sum_k w_k y_{ki}$, with brands indexed by decreasing utility. Utility on a given choice occasion carries an i.i.d. double-exponential error $\varepsilon_i$, so choice from a consideration set $C$ follows multinomial logit, $p_i=\exp(u_i)/\sum_{j\in C}\exp(u_j)$. Under the logit assumptions the expected maximum utility of choosing from $C$ is the log-sum
$$EU(C)=\ln\Big(\sum_{j\in C}\exp(u_j)\Big).$$
Brand $i$ enters the set if its marginal benefit exceeds its incremental consideration cost: $EU(C\cup\{i\})-EU(C)>c_i$. Assuming equal costs across brands ($c_j=c$), the optimal set is the first $n$ highest-utility brands, where $n$ satisfies
$$u_n>EU(C_{n-1})+\ln(\exp(c)-1)\quad\text{and}\quad u_{n+1}<EU(C_n)+\ln(\exp(c)-1).$$
Because $EU(C_n)$ is increasing in $n$, each additional brand faces a higher inclusion threshold (an order-of-entry effect). Assuming utility decays linearly across the awareness set, $u_i=u-i\alpha$, they derive a closed-form bound on optimal set size:
$$n<1+\frac{1}{\alpha}\ln\!\left[\frac{\exp(c)-1-\exp(-\alpha)}{\exp(c)\,(1-\exp(\alpha))}\right],\quad \alpha>0,$$
with the degenerate case $\alpha=0$ giving $n<\exp(c)/(\exp(c)-1)$. Calibration: because the analyst's multiattribute model has specification error (distinct from $\varepsilon_i$), a brand with true utility $u_i>u^\ast$ is considered only with probability $F(\sum_k w_k y_{ki}-u^\ast)$. Treating $F$ as double-exponential, the weights $w_k$ and threshold $u^\ast$ are estimated per consumer by maximizing
$$LL=\sum_{i\in A}\Big[z_i\ln F(\textstyle\sum_k w_k y_{ki}-u^\ast)+(1-z_i)\ln\big(1-F(\textstyle\sum_k w_k y_{ki}-u^\ast)\big)\Big],$$
where $z_i=1$ if brand $i$ is considered and $A$ is the awareness set, fit by nonlinear gradient search. The full two-stage choice model multiplies logit choice probabilities over the fitted consideration set $C=\{i:u_i>u^\ast\}$.

## Data
Survey of 121 households in two Sydney suburbs (111 women, 10 men; the primary shopper), screened to have children aged 2–11 and at least one of three brands at home; $10 incentive, in-home interviews. Respondents reported aided/unaided awareness, consideration ("would you consider buying this brand in the next 12 months?"), usage, value (100-point thermometer) and familiarity (5-point) for 26 major cereal brands, and rated their top three brands on 25 descriptive attributes. The 25 attributes were reduced via principal components to four factors (53.3% of variance): healthful, artificial, interesting, nonadult. Only 60 respondents gave enough non-considered-brand data for calibration; the other half supplied factor loadings/scores. Three new product concepts (with color photographs and price) were also evaluated.

## Key findings
- The log-sum benefit and equal-cost assumption yield a simple greedy rule: the optimal consideration set is the top-$n$ utility brands, with $n$ falling as brand heterogeneity $\alpha$ rises and (more sharply) as cost $c$ rises (e.g., with $u=1$: $n=14$ at $\alpha=c=.05$; $n=9$ at $\alpha=.20$; $n=5$ at $c=.20$).
- Calibration fit is strong: average individual log-likelihood $LL=-8.88$, average $\rho^2>.50$. Jackknife (leave-one-brand-out) discriminant validation gives a 73% hit rate predicting consideration of existing brands, well above the ~50% random-rule baseline.
- For the three new product concepts the model attains a 61% hit rate forecasting consideration out of sample.
- The two-stage PROPOSED model predicts aggregate choice shares better than the CONSID and CHOICE single-realistic-stage benchmarks, and is competitive with the C&C model — notable because PROPOSED is calibrated on consideration data alone, whereas C&C requires actual choice data to estimate its logit parameter.
- Estimated average weights: healthful $.618$, artificial $-.800$, interesting $.251$, nonadult $.405$, familiarity $.599$ — sign-consistent across most of the 60 respondents.

## Contribution
The paper supplies one of the first closed-form, individual-level models of consideration-set *composition* (not just single-brand entry) grounded in a utility/cost tradeoff, plus a practical measurement and calibration method requiring only consideration data. It links the marketing consideration-set literature to the economics of information search (Stigler, Weitzman) and to phased/two-stage decision processes, and demonstrates managerial uses: auditing existing brands, forecasting consideration and choice of new products, and guiding marketing-mix effort around the consideration threshold $u^\ast$ (large share rewards for brands "just missing out" by $\delta$, and value to targeted positioning when preferences are heterogeneous).

## Limitations & open questions
The authors explicitly flag: (1) Consideration of a brand is assumed independent of its *similarity* to other brands already in the set, so nothing can be said about the "shape" of the set; remedies suggested include structuring the market into homogeneous groups, nested MNL (cf. Bechtel 1990 on IIA), or a generalized-logit model of the choice of consideration set from all possible sets. (2) The model is static — composition at a point in time — and cannot describe how the set evolves as search proceeds. (3) Only the *compensatory* aspect of consideration is modeled; directly modeling the conjunctive (noncompensatory screening) aspect warrants further attention. (4) There is no consensus on operationalizing "consideration"; a fuzzy-set approach allowing degrees of consideration may have more process validity than the discrete in/out treatment. (5) New-product share forecasts ignore dynamic adjustment of the set after a new brand enters (incumbents are not allowed to leave).

## Connections
The consideration component builds directly on Roberts (1989), "A Grounded Model of Consideration Set Size and Composition," from which the single-brand entry criterion and log-sum benefit are adapted. It positions itself against [[@Hauser1990|Hauser and Wernerfelt (1990)]], whose evoked-set/evaluation-cost model is aggregate and market-structural, whereas this paper is individual-level. The choice machinery rests on McFadden (1973) MNL and the log-sum expected-maximum-utility result of Ben-Akiva and Lerman (1985). The cost-of-thinking foundation comes from Shugan (1980) and the information-search economics of Stigler (1961), Ratchford (1980), and Weitzman (1979). The two-stage screen-then-choose architecture echoes Wright and Barbour (1977) and Gensch (1987b); probabilistic consideration-set models include Swait and Ben-Akiva (1987). The compensatory-vs-noncompensatory debate references Gensch, Johnson and Meyer (1984), and Nedungadi (1990) on salience/recall in consideration.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
