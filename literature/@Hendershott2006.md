---
citekey: Hendershott2006
title: A Model of Direct and Intermediated Sales
authors: ["Hendershott, Terrence", "Zhang, Jie"]
year: 2006
type: journalArticle
doi: 10.1111/j.1530-9134.2006.00101.x
zotero: "zotero://select/library/items/7GLQYK7R"
pdf: /Users/jesper/Zotero/storage/UZRD9RTY/Hendershott2006.pdf
tags: [literature]
keywords: [intermediation, direct-sales, consumer-search, price-discrimination, vertical-channels, disintermediation, e-commerce]
topics: []
related: [Biglaiser1993, Choi1991, Coughlan1985, Jeuland1983, McGuire1983, Moorthy1987, Nelson1970]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We examine a model in which an upstream firm can sell directly online and through heterogeneous intermediaries to heterogeneous consumers engaging in time-consuming search. Direct online sales may be more or less convenient and involve costly returns if the good fits consumers poorly. Direct selling appeals to higher-value consumers and increases the upstream firm's profits by allowing price discrimination. Competition and segmentation due to direct sales results in lower intermediary prices, making all consumers better off. Thus, entry by an upstream firm increases consumer surplus at the expense of intermediaries with the net result being an increase in social welfare.

## Summary
This is a theory paper on disintermediation in vertical channels. An upstream monopolist sells a single good either through a competitive fringe of heterogeneous intermediaries (retailers/dealers/middlemen) to searching consumers, directly online, or through both channels in parallel (the "hybrid" structure). The model embeds a sequential-search market (closely following Spulber, 1996a) inside a channel-management problem. The central economic mechanism is that discounting links consumer value to search cost: high-value consumers search less, so the direct channel can skim them at a premium price. Direct sales thus serve as a price-discrimination device that also reduces double marginalization. The headline welfare result is that adding the direct channel makes *all* consumers better off and raises social welfare, while hurting intermediaries, and that when forced to pick one channel the upstream firm always selects the socially efficient one (though not always the consumer-optimal one).

## Research question
When and how should an upstream firm with market power sell directly to consumers (e.g., online) versus through independent intermediaries, and what are the consequences of such disintermediation for the firm's profits, intermediaries' profits, consumer surplus, and social welfare? A subsidiary policy question is whether legal bans on direct manufacturer sales (e.g., U.S. car-dealership franchise laws, direct-shipment wine laws) are welfare-improving.

## Method / identification
The paper is a fully analytical equilibrium model solved for its unique rational-expectations equilibrium; there is no estimation. Three classes of risk-neutral actors interact: one upstream monopolist, a continuum of intermediaries with transaction costs $k_I$ uniform on $[\underline{k}_I,1]$, and a continuum of consumers with valuations $v$ uniform on $[0,1]$.

Timing has three stages: (1) the upstream firm sets a stationary linear wholesale price $w$ (linear pricing is justified via Robinson–Patman nondiscrimination and the fact that richer contracts give degenerate results in search models); (2) each intermediary decides entry and sets a stationary ask price $p_I$; (3) each consumer forms a reservation price $r$ and searches sequentially until finding $p_I\le r$.

Consumers face two frictions. Search is time-consuming: gains are discounted by $\beta\in(0,1)$ and each consumer exits the market each period with probability $\lambda\in[0,1]$ (geometric horizon, à la Rust & Hall, 2003), being replaced by a fresh draw to keep the policy stationary. Second, the good fits poorly with probability $\alpha$, in which case the consumer balks and gets zero utility; $\alpha$ indexes the "touch-and-feel" / experience-good character (low for commodities, high for furniture, wine, clothes).

A consumer's value function solves the Bellman equation
$$V(v,p_I)=\max\Big\{0,\ (v-p_I),\ \beta(1-\lambda)\textstyle\int V(v,p_I)\,dF(p_I)\Big\}.$$
The optimal reservation price satisfies the standard Weitzman (1979) recursion, which after integration by parts gives
$$v(r)=r+\frac{\beta(1-\lambda)}{1-\beta(1-\lambda)}\int_0^{r}F(p_I)\,dp_I,$$
strictly increasing in $r$, so higher-value consumers choose higher reservation prices and search less — the key correlation between value and search cost. Each intermediary's optimal price is $p_I^{*}=\tfrac{1}{2}(\bar r+w+k_I)$, yielding an endogenous price-dispersion distribution $F(p_I)$. The direct (online) channel is modeled with its own discount factor $\beta_U$ (online search may be more or less convenient than physical search), an upstream transaction cost $k_U$, and a per-return cost $c$ incurred with probability $\alpha$. The hybrid equilibrium is characterized by a marginal high-value consumer $\bar v^{H}$ indifferent between buying direct and searching, and a marginal low-value consumer $\underline v^{H}$ indifferent between searching and not participating.

## Data
None — this is a pure theory paper. The authors cite descriptive e-commerce statistics (e.g., 68% of consumer-goods manufacturers planning to sell online; manufacturers' web sales at 15% of retail e-commerce, BCG/Forrester 2000) and motivating examples (Tiffany, Amazon jewelry, airline e-tickets, Expedia/Orbitz), but no estimation or experiment.

## Key findings
- **Equilibrium characterization (Propositions 1–3, Lemmas 1–3):** A unique rational-expectations equilibrium exists in each market structure. In the pure intermediated market the optimal wholesale price is $w=\tfrac{1}{2}(1-\underline{k}_I)$, intermediary prices are dispersed, and higher-value consumers search less.
- **Self-selection / price discrimination:** In the hybrid structure the direct online price exceeds the average intermediary price, and high-value (low-search) consumers self-select into the direct channel. Direct sales let the upstream firm price-discriminate and cut double marginalization.
- **Channel-choice thresholds:** Comparing upstream profits across structures yields cutoffs $\underline{k}_U,\bar{k}_U$: the hybrid strategy is optimal when $\underline{k}_U<k_U<\bar{k}_U$; only intermediated sales when $k_U>\bar{k}_U$; only direct sales when $k_U<\underline{k}_U$. Both channels coexist only when the intermediated discount factor is low enough relative to the direct one and upstream costs are not too high.
- **Channel conflict (Propositions 4–7):** Direct sales raise upstream and consumer welfare but lower intermediary profits, so intermediaries may refuse to participate in the hybrid model. If $k_U$ is low enough, the upstream firm's profit gain exceeds the intermediaries' loss, so side payments can yield a Pareto improvement; bans on direct sales then reduce consumer surplus (Prop. 6) and total welfare (Prop. 7).
- **Welfare under forced exclusivity (Proposition 8):** When constrained to a single channel, the upstream firm *always* chooses the socially optimal channel — direct if $k_U$ is low, intermediated if high — but this is not always consumer-optimal: for intermediate-high $k_U$ the firm picks intermediation even though direct sales would give consumers more surplus.

## Contribution
The paper extends the price-setting-intermediary search model of Spulber (1996a) by (i) introducing asymmetry — the intermediary is a price taker to the upstream firm but a price maker to consumers — and (ii) adding a direct online channel with its own search convenience, fit/return risk, and transaction costs. It thereby bridges the search, vertical-integration, and marketing channel-management literatures, delivering sharp welfare predictions about disintermediation and a normative read on direct-sales bans. It also offers testable product-level predictions for which goods migrate to direct online sales: low-immediacy, low-bulk, specialty, and low-$\alpha$ (commodity/standardized/strong-brand) goods.

## Limitations & open questions
- **Single homogeneous good:** the model excludes services intermediaries actually provide — assortment, cross-manufacturer comparison, complementary-good aggregation, user reviews — which the authors flag as important omitted channel value.
- **Manufacturer-only direct channel:** the authors note a "simplest first step" extension would let a single online *intermediary* (not the manufacturer) buy at wholesale and compete with physical stores; they conjecture similar high-value-online sorting but a complicated rational-expectations equilibrium.
- **Uniform wholesale pricing:** if the firm cannot price-discriminate across online and physical intermediaries, the wholesale price could rise and reduce consumer surplus and welfare — left unanalyzed.
- **Free-riding / showrooming:** because the direct price exceeds the average store price, the model avoids the case where consumers inspect in-store then buy online; the authors flag store-as-showroom free riding as an unmodeled risk.
- **Weak empirical base:** the authors note essentially no empirical work on online direct sales at the time (citing only Carlton & Chevalier, 2001 and Bell et al., 2003), leaving their product-level predictions untested.

## Connections
The search-and-intermediation backbone is most directly Spulber (1996a, 1996b, 1999) and Rust & Hall (2003) on middlemen versus market makers; the consumer-search machinery descends from Weitzman (1979), Stahl (1989), Salop & Stiglitz (1977), and Varian (1980), with the value/search-cost correlation echoing the "informed shoppers" of Varian and Stahl. The intermediation-theory lineage includes Rubinstein & Wolinsky (1987), [[@Biglaiser1993|Biglaiser (1993)]], Gehrig (1993), Yavas (1992, 1994, 1996), and Fingleton (1997). On the vertical-contracting and foreclosure side it connects to Katz & Shapiro (1986), Hart & Tirole (1990), O'Brien & Shaffer (1992), and McAfee & Schwartz (1994). The marketing channel-management strand includes [[@McGuire1983|McGuire & Staelin (1983)]], [[@Jeuland1983|Jeuland & Shugan (1983)]], [[@Coughlan1985|Coughlan (1985)]], [[@Moorthy1987|Moorthy (1987)]], [[@Choi1991|Choi (1991)]], Purohit (1997), Trivedi (1998), and Liu & Zhang (2002), the last giving a contrasting result where direct sales can *raise* prices and lower welfare. The microstructure analogy for price-setting intermediaries draws on Glosten & Milgrom (1985); the search/experience-good distinction is [[@Nelson1970|Nelson]] (1970, 1974).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
