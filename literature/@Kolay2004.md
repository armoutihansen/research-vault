---
citekey: Kolay2004
title: "<span style=\"font-variant:small-caps;\">All‐Units Discounts in Retail Contracts</span>"
authors: ["Kolay, Sreya", "Shaffer, Greg", "Ordover, Janusz A."]
year: 2004
type: journalArticle
doi: 10.1111/j.1430-9134.2004.00018.x
zotero: "zotero://select/library/items/9VET8C2S"
pdf: /Users/jesper/Zotero/storage/FQUXQPXQ/Kolay2004.pdf
tags: [literature]
keywords: [all-units-discounts, vertical-contracts, double-marginalization, second-degree-price-discrimination, nonlinear-pricing, screening, two-part-tariffs]
topics: ["[[distribution-channels-vertical-integration]]"]
related: [Moorthy1987, Spengler1950, Tirole1988]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> All-units discounts in retail contracts refer to discounts that lower a retailer's wholesale price on every unit purchased when the retailer's purchases equal or exceed some quantity threshold. These discounts pose a challenge to economic theory because it is difficult to understand why a manufacturer ever would charge less for a larger order if its intentions were benign. In this paper, we show that all-units discounts may profitably arise absent any exclusionary motive. All-units discounts eliminate double marginalization in a complete information setting, and they extract more profit than would a menu of two-part tariffs in the standard incomplete information setting with two types of buyers. All-units discounts may improve or may reduce welfare (relative to menus of two-part tariffs) depending on demand parameters.

## Summary
A single manufacturer sells to a single retailer who resells to final consumers. The paper rationalizes *all-units discounts* (AUDs) — schedules where reaching a target quantity $\bar q$ retroactively lowers the price on *every* unit, so the total outlay jumps *down* at $\bar q$ — without invoking any exclusionary motive. Under complete information AUDs eliminate double marginalization just as two-part tariffs do. Under incomplete information (private retailer demand) the optimal *menu* of AUDs strictly out-earns the optimal *menu* of two-part tariffs because the discontinuous outlay schedule is a better screening device. Welfare versus two-part tariffs is ambiguous and depends on the shape of demand across states.

## Research question
Can the use of all-units discounts in vertical (manufacturer–retailer) contracts be explained as profit-maximizing behavior absent any motive to exclude rivals, and what are their welfare consequences relative to two-part tariffs and incremental-units discounts?

## Method / identification
Pure theory. A vertical model: upstream manufacturer with constant marginal cost $c$ sells to a downstream monopoly retailer facing consumer inverse demand $p(q)$. Manufacturer profit $\pi^m = T(q) - cq$, retailer profit $\pi^r = p(q)q - T(q)$, joint (integrated) profit $\pi^{int} = p(q)q - cq$. An AUD contract has the form

$$T(q) = \begin{cases} wq & \text{if } q < \bar q,\\ \lambda w q & \text{if } q \geq \bar q,\end{cases}$$

with $w \ge 0$ and $\lambda \in (0,1)$; $w$ is the list price and $1-\lambda$ the percentage discount. The defining feature is that AUDs do *not* separate average from marginal payment, unlike two-part tariffs $T(q)=cq+F$ or incremental-units discounts.

Two information regimes are analyzed:
- **Complete information**: demand known to both at contracting. The authors construct AUD contracts $T(q)=p(0)q$ for $q<q^*(c)$ and $\lambda p(0)q$ for $q\ge q^*(c)$, with $\lambda\in[\tfrac{c}{p(0)},\tfrac{p(q^*(c))}{p(0)}]$, that induce the integrated quantity $q^*(c)$.
- **Incomplete information**: two demand states, low $L$ (prob. $\alpha$) and high $H$ (prob. $1-\alpha$), with $p_H(\cdot)\ge p_L(\cdot)$. Revenues $R_i(q)=p_i(q)q$ satisfy concavity $\partial^2 R_i/\partial q^2<0$ and single-crossing $\partial R_H/\partial q > \partial R_L/\partial q$. The retailer privately learns the state after contracting; the manufacturer designs a screening menu solving a standard self-selection program — maximize expected profit subject to a participation constraint for the low type and an incentive-compatibility constraint for the high type. This is formally equivalent to second-degree price discrimination across retailers of different demand. The optimal AUD menu $(w_i,\lambda_i,\bar q_i)$ is characterized via two lemmas (both constraints bind; the manufacturer sets $\lambda_L w_L = p_L(\bar q_L)$ and induces purchases exactly at the thresholds).

## Data
None — this is a theoretical paper. Illustrative parametric examples use linear inverse demands $p_i(q)=a-\theta_i q$ (common vertical intercept) and a common-horizontal-intercept variant to sign welfare.

## Key findings
- **Proposition 1**: The AUD contracts in the complete-information construction eliminate double marginalization; the target $q^*(c)$ caps the retail price at $p(q^*(c))$, and $\lambda$ divides surplus. Relative to linear pricing these contracts are Pareto-improving (higher firm profits, lower consumer prices).
- **Proposition 2**: When demand is unknown, the manufacturer earns strictly higher profit with a menu of AUDs than with the optimal menu of two-part tariffs: $\pi^{AU} = \pi^{2PT} + (1-\alpha)\varepsilon$ for arbitrarily small $\varepsilon>0$. The discontinuous outlay schedule lets the manufacturer raise prices on all quantities above $q_L^*(w_L^*)$ while still inducing the high type to buy $q_H^*(c)$, shrinking the high type's informational rent. Incremental-units discounts, by contrast, are shown to be *equivalent* to menus of two-part tariffs.
- **Lemmas 1–2 and Propositions 3–4**: At the optimum both the participation and incentive constraints bind; the high-demand retailer buys the integrated quantity $q_H^*(c)$ (no distortion at the top, Proposition 3), while the low-demand retailer's quantity is distorted downward (Proposition 4), with two subcases depending on whether the high type would be constrained by $\bar q_L$.
- **Proposition 5 (welfare, linear demand, $\alpha=1$ limit)**: Consumer welfare can be higher or lower under AUDs than under two-part tariffs. With common vertical intercept (uncertainty over consumers' willingness to pay), flatter high-state demand $\Rightarrow$ lower prices and higher welfare under AUDs. With common horizontal intercept (uncertainty over market size), AUDs raise prices and reduce welfare. The sign turns on whether the high-state marginal-revenue slope exceeds the low-state slope.

## Contribution
Provides the first formal efficiency rationale for all-units discounts, countering the prevailing view (in legal/policy and some economics writing) that they are either irrational or necessarily anticompetitive. It shows AUDs serve two benign roles — eliminating double marginalization under complete information, and acting as a superior screening device under asymmetric information — and that their welfare effects are genuinely ambiguous, making per se condemnation in antitrust unwarranted. The framework maps directly onto second-degree price discrimination across heterogeneous retailers under Robinson-Patman-style constraints.

## Limitations & open questions
- The model assumes a single manufacturer and single retailer, deliberately ruling out rival exclusion; whether AUDs are anticompetitive *with* competing upstream or downstream firms is left open (and is the dimension policymakers actually worry about).
- Only two demand states are analyzed in full; the authors argue results extend to any finite number of states (as long as menu options $\ge$ states) but note that the *relative* effectiveness of AUDs in reducing informational rent may shrink as states proliferate.
- With a *continuum* of types and a monotone hazard rate, the optimal menu of AUDs yields the *same* outcome as the optimal menu of two-part tariffs (citing Maskin & Riley 1984) — so the strict advantage hinges on discreteness of types.
- Implementation and complexity costs of richer menus are acknowledged but not modeled.

## Connections
The double-marginalization problem traces to [[@Spengler1950|Spengler (1950)]]; two-part tariffs as a remedy appear in [[@Moorthy1987|Moorthy (1987)]], [[@Tirole1988|Tirole (1988)]], and Katz (1989). The screening / self-selection apparatus draws on the second-degree price-discrimination literature: Spence (1977, 1980), Willig (1978), Roberts (1979), Goldman, Leland & Sibley (1984), and especially Maskin & Riley (1984), whose continuum-of-two-part-tariffs result delimits when AUDs add value. Ordover & Panzar (1982) is cited for the possibility of top-type distortions when demands are interrelated, and Salant (1989) for conditions under which serving both types is optimal. The policy framing engages Tom, Balto & Averitt (2000) on antitrust treatment of these discounts. The broader nonlinear-pricing and quantity-discount tradition (e.g., the work on incremental-units versus all-units schedules) situates the contribution.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
