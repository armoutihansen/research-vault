---
citekey: Heidhues2008
title: Competition and Price Variation When Consumers Are Loss Averse
authors: ["Heidhues, Paul", "Kőszegi, Botond"]
year: 2008
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/UK9LE2SH"
pdf: /Users/jesper/Zotero/storage/3JNJI2G3/Heidhues2008.pdf
tags: [literature]
keywords: [loss-aversion, behavioral-io, reference-dependence, focal-pricing, price-stickiness, salop-competition, koszegi-rabin]
topics: []
related: [Gabaix2006, Koszegi2006b, Tversky1992]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We modify the Salop (1979) model of price competition with differentiated products by assuming that consumers are loss averse relative to a reference point given by their recent expectations about the purchase. Consumers' sensitivity to losses in money increases the price responsiveness of demand—and hence the intensity of competition—at higher relative to lower market prices, reducing or eliminating price variation both within and between products. When firms face common stochastic costs, in any symmetric equilibrium the markup is strictly decreasing in cost. Even when firms face different cost distributions, we identify conditions under which a focal-price equilibrium (where firms always charge the same "focal" price) exists, and conditions under which any equilibrium is focal.

## Summary

Heidhues and Kőszegi embed Kőszegi–Rabin expectations-based loss aversion into a Salop (1979) circular-city model of price competition. Because consumers are more sensitive to paying *above* their expected price than to paying below it, demand is kinked: it is more responsive to price increases than to price decreases. This asymmetry makes high prices unusually competitive, compressing or eliminating price variation. The model explains three empirical regularities at once—sticky prices (prices unresponsive to cost/demand shocks), focal pricing (identical prices across differentiated competitors), and uniform pricing (one price across a retailer's heterogeneous products)—and predicts these tendencies are stronger in more concentrated industries.

## Research question

Why do prices in imperfectly competitive industries vary so little—both over time (sticky prices) and across non-identical products and competitors (focal and uniform pricing)? Existing theories (menu costs, tacit collusion, search costs, kinked-demand stories) explain stickiness but not why prices are *equal* across differentiated products. Can a single mechanism rooted in consumer reference dependence explain all three patterns, and how does it interact with industry concentration?

## Method / identification

A static Salop (1979) circular-city model with $n$ firms (none owning two neighboring products) located equidistant on a circle of circumference normalized so transport/taste cost is parameterized by $t$. A consumer's taste is drawn uniformly on the circle; intrinsic utility is decreasing in distance to the chosen product and additively decreasing in price. The behavioral departure: following Kőszegi and [[@Koszegi2006b|Rabin]] (2006, 2007), a consumer derives *gain-loss utility* from comparing her realized money and product-satisfaction outcomes to a stochastic reference point given by her lagged rational expectations over those outcomes, with losses weighted more heavily than equal gains by a coefficient $\lambda>1$ (the calibration benchmark is $\lambda\approx 3$, i.e. roughly two-to-one loss aversion à la [[@Tversky1992|Tversky–Kahneman 1992]]).

Reference points are determined endogenously through a *personal equilibrium*: expectations must be rational given the behavior they induce. Firms have privately observed stochastic marginal costs and simultaneously set prices to maximize expected profit given rivals' strategies and consumer expectations (a Bayesian–Nash market equilibrium nested with consumers' personal equilibrium). The central analytical object is the *comparison effect*: when a consumer's expected purchase price is $p^*$, paying more than $p^*$ registers as a money loss and paying less merely as a gain, generating a demand kink at $p^*$ that makes demand strictly more elastic upward than downward. The authors characterize when a focal-price equilibrium (all firms always charge a common $p^*$) exists, when *every* equilibrium is focal, and the comparative statics of markups in cost and concentration. Loss aversion is modeled in both the money and the product-satisfaction dimensions (the money-only version simplifies proofs but they keep both for realism and robustness).

## Data

None—this is a theoretical paper. It is calibrationally disciplined: the authors plug in $\lambda\approx 3$ to show focal-price equilibria survive for nontrivial cost variation, and they cite marketing evidence (Erickson–Johansson 1985; Kalwani–Yim 1992; Winer 1986; Hardie–Johnson–Fader 1993) that consumers compare prices to expectation-based reference prices with loss-averse asymmetry.

## Key findings

- **Proposition 1 (existence condition for focal-price equilibrium):** A focal-price equilibrium—where all firms always charge the same $p^*$—exists if and only if any two cost realizations of any two firms lie within a given constant. This permits one firm to be strictly higher-cost than another in every state; the demand kink at $p^*$ makes $p^*$ optimal across a range of costs.
- **Markup strictly decreasing in cost:** Under common stochastic costs, in any symmetric equilibrium the markup is strictly decreasing in cost—so prices respond to cost shocks by less than one-for-one (countercyclical-markup / sticky-price behavior).
- **Proposition 2 (focal price level and multiplicity):** Characterizes the set of feasible focal prices as a closed interval; the equilibrium markup lies in $[t/n,\,2t/n]$, and under $\lambda\approx 3$ focal-price equilibria tolerate cost variation between 50% and 100% of the markup. Loss aversion raises equilibrium prices because it lowers firms' incentive to cut prices while leaving the incentive to raise them unchanged.
- **Concentration result:** Focal-price equilibria are more likely in more concentrated industries—when the value of a marginal consumer is high, the asymmetric demand responsiveness at $p^*$ creates a larger gap in marginal profit between raising and lowering price.
- **Propositions 3 & 4 + Corollary 1 (all equilibria focal):** If firms' cost-support intervals overlap (and a mild bound on $\lambda$ holds, satisfied whenever $\lambda<1+2\sqrt{2}\approx 3.8$), there is no equilibrium with stable-but-different prices (Prop. 3); if each firm's cost density is sufficiently high everywhere on its connected support, each firm sets a deterministic price (Prop. 4). When both hold, *every* interior market equilibrium is focal—a robustness of focal pricing the authors note no prior price-setting model delivers.
- **Stickiness ≠ focality:** Examples show that if cost distributions do *not* overlap, equilibria with different deterministic prices exist—so sticky pricing need not coincide with focal pricing.

## Contribution

First model to derive sticky, focal, *and* uniform pricing from one micro-founded behavioral mechanism (expectations-based loss aversion), and to show these patterns can be the *unique* equilibrium even for asymmetric firms and differentiated products—something menu-cost, collusion, and kinked-demand theories cannot deliver for equality of prices. A foundational contribution to "behavioral industrial organization," applying Kőszegi–Rabin reference-dependent preferences to strategic firm pricing and generating the testable prediction that price rigidity strengthens with concentration.

## Limitations & open questions

- **Static model:** The fully dynamic case (repeated pricing with cost redraws, where past prices shape future reference points) is only discussed heuristically. Whether focal/sticky pricing is the *unique* dynamic outcome depends on how lagged expectations form reference points; the authors flag this as important but beyond scope, noting it "could potentially lead to novel models of advertising and price leadership."
- **Correlated costs:** Propositions 3–4 require *independent* cost shocks; with correlated costs a firm's price change shifts the conditional distribution of rivals' prices and marginal consumers. The authors believe the comparison effect survives but cannot formally analyze it.
- **Ownership structure:** They assume no firm owns two neighboring products; allowing multi-product ownership requires accounting for reduced inter-firm competition.
- **Technical bounds on $\lambda$:** Conditions (5) and Prop. 4 impose restrictions on $\lambda$ to keep firms' profit problems single-peaked; sharper results would need these relaxed.
- **Heterogeneity:** Robust to heterogeneity in loss aversion in principle, but estimation methods would need to account for it.

## Connections

The behavioral core is Kőszegi and [[@Koszegi2006b|Rabin]] (2006, 2007) on expectations-based reference-dependent preferences and risk attitudes; the loss-aversion calibration draws on [[@Tversky1992|Tversky and Kahneman (1992)]] and the endowment-effect evidence of Kahneman, Knetsch, and Thaler (1990, 1991). The market structure is Salop (1979); the menu-cost/kinked-demand tradition it supersedes includes Hall and Hitch (1939), Sweezy (1939), and Maskin and Tirole (1988), while the collusion-based account of price rigidity is Athey, Bagwell, and Sanchirico (2004), with focal-point-as-collusion evidence from Knittel and Stango (2003). The empirical price-stickiness backdrop is Kashyap (1995), Slade (1999), and Chevalier, Kashyap, and Rossi (2003); uniform-pricing puzzles come from McMillan (2004) and Einav and Orbach (2005). Reference-price marketing evidence (Erickson and Johansson 1985; Winer 1986; Kalwani and Yim 1992; Hardie, Johnson, and Fader 1993) motivates the demand side. The paper situates itself in behavioral IO, reviewed by Ellison (2006), alongside obfuscation/add-on models of Ellison (2005) and [[@Gabaix2006|Gabaix and Laibson (2006)]], and the concentration-and-competition question of Stiglitz (1987). It builds on the authors' own companion work, Heidhues and Kőszegi (2007), on focal pricing.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
