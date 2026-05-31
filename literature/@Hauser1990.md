---
citekey: Hauser1990
title: An Evaluation Cost Model of Consideration Sets
authors: ["Hauser, John R.", "Wernerfelt, Birger"]
year: 1990
type: journalArticle
doi: 10.1086/209225
zotero: "zotero://select/library/items/XBBV58LJ"
pdf: /Users/jesper/Zotero/storage/68W5QAPL/Hauser1990.pdf
tags: [literature]
keywords: [consideration-sets, search-costs, bounded-rationality, discrete-choice, consumer-behavior, two-stage-choice]
topics: ["[[limited-attention-consideration-sets]]"]
related: [Manzini2007, Masatlioglu2012, Tversky1974]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> If utility (net of price) varies by consumption occasion, the consideration set of a rational consumer will represent trade-offs between decision costs and the incremental benefits of choosing from a larger set of brands. If evaluating a brand decreases biases and uncertainty in perceived utility, the decision to evaluate a brand for inclusion in a consideration set is different from the decision to consider an evaluated brand. The decision to consume is, in turn, different from the decision to consider. This article provides analytical expressions for these decision criteria and presents four aggregate implications of the model: (1) distributions of consideration set sizes, (2) order-of-entry penalties, (3) dynamic advertising response, and (4) competitive promotion intensity.

## Summary
Hauser and Wernerfelt build a rational, cost/benefit theory of why consumers consider only a handful of brands (a median of two to five) out of dozens available. The key innovation is to treat utility as a random variable that varies by consumption occasion and is partly unknown before evaluation. A consideration set then balances the *expected benefit* of having more options to choose among (via the expected maximum utility) against the *decision cost* of carrying each brand and the *evaluative search cost* of learning about an unevaluated one. The paper derives analytical add/drop/evaluate criteria and shows the resulting model reproduces four aggregate regularities in real package-goods data: lognormal-shaped consideration-set-size distributions, order-of-entry market-share penalties, asymmetric (faster-up-than-down) advertising response, and a positive promotion-intensity–consideration-set-size correlation.

## Research question
Can the empirical fact that consumers consider more than one brand but far fewer than all available brands be explained as the optimal behavior of a rational, utility-maximizing consumer? And what aggregate, testable market-level implications follow from such an individual model?

## Method / identification
The paper is an analytical (theory-driven) modeling exercise validated against published/aggregate data; it runs no controlled experiments. Utility of brand $j$ at occasion $t$ is decomposed into a pre-evaluation belief with mean $v_j$ and variance $\sigma_u^2$, a post-evaluation mean shift $a_j$ (which can be positive, negative, or zero), and an occasion-to-occasion variance $\sigma_e^2 < \sigma_u^2$. The consumer's value of choosing from a set of $n$ considered brands is the expected maximum utility net of per-brand decision costs:
$$E[\max(u_1, u_2, \ldots, u_n)] - \sum_{j=1}^{n} d_j .$$
Three distinct decisions follow. A brand is **added** to (kept in) the consideration set if its incremental expected-max value exceeds its decision cost $d_{n+1}$:
$$E[\max\{u_1,\ldots,u_n,u_{n+1}\}] - E[\max\{u_1,\ldots,u_n\}] - d_{n+1} > 0 .$$
A brand is **dropped** when the symmetric inequality reverses. A brand is **evaluated** only if the discounted stream of incremental benefits exceeds the one-time evaluative search cost $s_{n+1}$; writing $F_n \equiv E[\max\{u_1,\ldots,u_n\}]$ and $F'_{n+1}$ for the pre-evaluation analog,
$$F'_{n+1} - F_n - \gamma s_{n+1} - d_{n+1} > 0 ,$$
where $\gamma > 1$ discounts a cost paid once against an ongoing benefit stream. The model is thus a *mixed sampling* model: consumption is a fixed-sample search over the formed set, while consideration-set formation is sequential. For the aggregate tests the authors impose an i.i.d. normal post-evaluation utility assumption, reducing the add condition to $d \approx \Delta e_n \, \sigma_e$, where $\Delta e_n$ is a tabled increment in the expected maximum of standardized normals. Letting $\lambda = d/\sigma_e$ be lognormally distributed across consumers yields a predicted consideration-set-size distribution $P_n = \Lambda(\Delta e_{n-1}\mid\mu,\Sigma) - \Lambda(\Delta e_n\mid\mu,\Sigma)$.

## Data
None collected first-hand. The authors confront the model with published and publicly available aggregate data: consideration-set-size frequencies for plastic wraps (Hauser and Gaskin 1984), laundry detergents (Campbell 1969), deodorants (Silk and Urban 1978), and refrigerated juices (the Assessor pre-test-market database, ~300–600 per study); order-of-entry share penalties for 129 brands across 36 categories from Urban et al. (1986); and promotion intensity (percent volume sold on promotion) from the Information Resources, Inc. Marketing Factbook (panel of 30,000 consumers, 1986). Price-cost margin tests were attempted but abandoned for lack of data at the right level of aggregation.

## Key findings
1. **Consideration-set-size distribution.** Under the i.i.d.-normal and lognormal-$\lambda$ assumptions, predicted $P_n$ fit observed frequencies in all four categories; contingency (chi-squared) tests do not reject the lognormal fit at the 0.05 level, and the lognormal beats normal and uniform alternatives.
2. **Order-of-entry penalties.** Because the expected-maximum threshold rises as more brands compete, earlier-evaluated brands are considered more often and earn higher share. Predicted penalties (1.00, 0.71, 0.57, 0.50, 0.44, 0.40 for entrants 1–6) closely match Urban et al.'s empirical estimates (1.00, 0.71, 0.58, 0.51, 0.45, 0.41).
3. **Asymmetric advertising response.** Dropping (governed by less-sensitive post-evaluation utility) responds less to advertising than adding/evaluating (governed by more-sensitive pre-evaluation utility), so sales rise faster under advertising increases than they fall under decreases.
4. **Competition.** The relevant competitiveness measure is the average *considered* set size $C$, not the number of brands $N$. Percentage markup is predicted proportional to $(1 + \beta_1/C)^{-1}$, and promotion intensity should correlate positively with average consideration-set size.

## Contribution
The paper provides the first analytical derivation showing that multi-brand-but-not-all-brand consideration sets emerge from rational cost/benefit optimization, by augmenting Stiglerian search theory with (a) occasion-varying utility and (b) pre-evaluation uncertainty. It cleanly separates three decisions—evaluate, consider, consume—that prior search models conflated, and it reframes competition around the number of brands considered rather than the number available. It became a foundational reference for the economics and marketing literatures on consideration sets and two-stage (consider-then-choose) discrete choice.

## Limitations & open questions
The authors are candid about several open problems, each a hook for further work. (1) Decision-cost interactions are assumed negligible—processing one brand neither eases nor hinders processing another; relaxing this is left to "future models." (2) The mixed (fixed + sequential) sampling structure has "no empirical evidence" supporting it yet. (3) The lognormal distribution of $\lambda$ is asserted, not derived; they call for future models to obtain it "from first principles," and note the restricted model mis-fits the tails in categories where many brands are considered (and fails chi-squared at very large samples). (4) The theory is "mute" on how consumers form pre-evaluation beliefs (means/variances) and on how they perform the implied calculations. (5) The order-of-entry fit invites the charge of curve-fitting (weights chosen to match). (6) Price-cost-margin predictions remain empirically untested for want of suitably aggregated data. (7) Throughout, individual-level predictions are only ceteris paribus and assert face validity rather than experimental confirmation.

## Connections
The model extends George Stigler's (1961) economics of search and Phillip Nelson's (1970) search/experience-good distinction, incorporating Louis Wilde (1981) on consumption as search and Richard Schmalensee (1982) on pioneering-brand advantages. It sits within John Payne's (1982) cost/benefit (effort–accuracy) framework for decision rules, and draws on Steven Shugan's (1980) "cost of thinking," Peter Wright (1975) on simplifying choice, George Miller (1956) on processing limits, and [[@Tversky1974|Tversky and Kahneman (1974)]] on heuristics. The behavioral-science framing contrasts the rational benchmark against Kahneman and Tversky's (1979) prospect theory. In transportation science it builds on Robert Meyer (1979) and Anthony Richardson (1982) on choice-set formation, and on Alba and Hutchinson (1987) on consumer expertise. Empirical anchors include Silk and Urban (1978), Campbell (1969), Hauser and Gaskin (1984), and Urban et al. (1986). The consider-then-choose architecture connects to later bounded-rationality and limited-attention choice models in economics, such as [[@Manzini2007|Manzini and Mariotti (2007)]] on sequentially rationalizable choice and [[@Masatlioglu2012|Masatlioglu, Nakajima, and Ozbay (2012)]] on attention filters.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
