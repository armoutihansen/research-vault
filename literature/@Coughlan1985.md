---
citekey: Coughlan1985
title: "Competition and Cooperation in Marketing Channel Choice: Theory and Application"
authors: ["Coughlan, Anne T."]
year: 1985
type: journalArticle
doi: 10.1287/mksc.4.2.110
zotero: "zotero://select/library/items/DZPES792"
pdf: /Users/jesper/Zotero/storage/UGA82NB3/Coughlan1985.pdf
tags: [literature]
keywords: [vertical-integration, distribution-channels, strategic-delegation, price-competition, product-differentiation, duopoly, game-theory]
topics: ["[[distribution-channels-vertical-integration]]"]
related: [Jeuland1983, McGuire1983]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper discusses the problem of choosing a vertical marketing channel in a product-differentiated duopolistic market. Firms choose product price and the form of the marketing channel to maximize profits. It is shown that integration of the marketing function results in greater price competition and lower prices than does the use of independent marketing middlemen. The profitability of reducing price competition by using such middlemen is investigated. Two hypotheses—that integration is negatively associated with the products' substitutability and that symmetric channel structures are stable—are tested in a preliminary way and supported with survey data from the international semiconductor industry.

## Summary

Coughlan builds a game-theoretic model of vertical channel choice in a product-differentiated price-setting duopoly and shows that delegating distribution to exclusive, pricing-autonomous middlemen is a strategic device that softens price competition between rival manufacturers. Because separating manufacturing from marketing blunts a firm's ability to react to a competitor's price moves, non-integration can raise channel profits toward the collusive level — and does so more, the closer substitutes the products are. The paper generalizes McGuire & Staelin's specific linear-demand result to a broad class of demand functions and supplies preliminary empirical support from the international semiconductor industry: low-substitutability products are sold through integrated channels, and pure (non-mixed) channel structures are stable.

## Research question

When can a manufacturer earn higher profits by selling through an independent marketing middleman rather than integrating distribution forward — even absent any marketing economies of scale/scope or middleman "value added" — and how does this depend on the degree of product substitutability between competing duopolists?

## Method / identification

A two-good symmetric duopoly with prices as strategic variables and zero manufacturing/marketing costs. Demand for product $i$ takes the general form

$$q_i = f(p_i; \gamma) + d\gamma p_j, \quad i = 1,2,\ j = 3-i,$$

with $f'(p_i;\gamma) < 0$, $|f'| > d\gamma$, $d\gamma > 0$; demand may be convex, linear, or concave in own price but is linear in the rival's price. Nine assumptions (A1–A9) impose symmetry, negative own-price and positive constant cross-price effects, own-price dominance ($|f'| > d\gamma$), decreasing price marginal revenue, and zero costs. The substitutability parameter $\gamma \ge 0$ governs the strength of cross-price competition.

Four channel structures are solved as games: (1) **collusive** — both integrate and jointly maximize $\Pi_c = \sum_i p_i[f(p_i;\gamma)+d\gamma p_j]$ (benchmark); (2) **Nash integrated** — both integrate, compete in prices à la Nash; (3) **private** — both use exclusive middlemen who set final price $p_i$ while manufacturers set wholesale price $w_i$, with manufacturers acting as Stackelberg leaders over middlemen (middleman maximizes $(p_i - w_i)[f(p_i;\gamma)+d\gamma p_j]$, manufacturer maximizes over a derived demand); (4) **mixed** — one integrates, one does not, yielding asymmetric equilibria. Equilibria are characterized by symmetric first-order conditions; the relative slopes of reaction functions (integrated reaction functions have half the slope of collusive ones) drive the price-competition results.

The empirical model is a binary **logit** regression of an integration dummy $\text{INT}$ on a substitutability proxy $\text{LOWSUB}$ and a market-structure control $\text{INTMKT}$ (whether all incumbents are integrated at entry), with model chi-square tests and predicted-probability comparisons.

## Data

Survey/interview data from a National Science Foundation study (Flaherty & Teece 1982) on international technology transfer in the semiconductor industry: 14 component, equipment, and materials technologies, with foreign-market entry observations (Europe, Japan, Southeast Asia, Rest of World) over 1954–1979. An observation is a (technology, firm, foreign market) triple coded as direct selling (integrate) vs. selling through an independent distributor/representative. Samples range from 62 observations / 26 firms down to 25 observations / 18 firms as successive restrictions (no prior market experience, pure incumbent channel, channel preservation) are imposed.

## Key findings

- **Proposition 1(a–c):** A given own-price change moves quantity demanded least in the private case, more in the mixed case, and most in the integrated case (under stated convexity conditions, e.g. $f' + (p_i-w_i)f'' < 0$). Separation of manufacturing and marketing thus mechanically restricts a manufacturer's ability to initiate or respond to price competition.
- **Proposition 2(a):** Collusive (joint-profit-maximizing) prices always exceed Nash-integrated prices, except at $\gamma = 0$ where they coincide. **Proposition 2(b):** Private-case prices always exceed Nash-integrated prices.
- Defining $L \equiv 2d\gamma p + wf'$, private-case channel profits exceed Nash-integrated profits iff $L > 0$. Since $\partial L/\partial\gamma > 0$ under reasonable conditions (e.g. $2d > |\partial f'/\partial\gamma|$, satisfied by the McGuire/Staelin linear example), the profitability of using middlemen **rises with substitutability** $\gamma$; for $\gamma = 0$ or $d = 0$ middlemen never help.
- Combining with McGuire & Staelin's mixed-case analysis: the mixed structure is generally not a Nash equilibrium; pure structures are stable; and over an intermediate range of $\gamma$ a **prisoner's dilemma** arises (both prefer the private channel, but each has a unilateral incentive to integrate, collapsing to Nash integration).
- **Empirics:** $\text{LOWSUB}$ enters positively (less-substitutable products → integration), significant in the cleaner specifications; $\text{INTMKT}$ strongly predicts entrant channel choice, and pure structures are largely preserved — consistent with the model and the McGuire/Staelin gaming view.

## Contribution

Generalizes the competition-softening role of independent distribution from McGuire & Staelin's specific linear-demand duopoly to a broad family of demand functions (convex/linear/concave in own price), isolating substitutability as the key driver of channel choice. It reframes "using a middleman" as a strategic commitment device that relaxes price competition — independent of conventional efficiency rationales — and pairs the theory with one of the first attempts to confront such channel-choice predictions with field data.

## Limitations & open questions

- The substitutability proxy $\text{LOWSUB}$ (component/material vs. equipment) is admittedly crude and binary; the underlying demand functions and $\gamma$ are not estimated, so results cannot adjudicate which demand form is "correct."
- Multicollinearity between $\text{LOWSUB}$ and $\text{INTMKT}$ weakens identification in some specifications.
- The model assumes a duopoly, symmetric firms, zero/identical costs, and abstracts from marketing economies of scale/scope and dynamic learning — applicability is restricted to small-numbers industries where these are minor (the author names automobiles, home computers, industrial equipment).
- The mixed case cannot be ranked on profitability in the general model because equilibrium prices are asymmetric; only the specific McGuire/Staelin example permits that analysis.
- Coughlan flags FTC Line of Business data as a future avenue for properly estimating demand and testing the hypotheses more powerfully.

## Connections

Directly builds on and generalizes [[@McGuire1983|McGuire & Staelin]] (1983a, b; 1982), whose linear-demand duopoly first showed that non-integration can dominate integration. It engages [[@Jeuland1983|Jeuland & Shugan (1983)]] on channel coordination — reinterpreting an "integrated" firm as any manufacturer–marketer pair that has achieved Jeuland/Shugan coordination — and contrasts with their single-manufacturer/single-retailer setting where coordination always dominates. Earlier channel literature (Artle & Berglund 1959; Baligh & Richartz 1967) studied within-channel vertical interactions rather than inter-manufacturer competition; Etgar (1978) and Etgar & Zusman (1982) model competing distributors and forward integration as service differentiation, while Zusman & Etgar (1981) study cooperation-enhancing contracts. The strategic-delegation logic — delegating pricing to soften competition — anticipates the industrial-organization literature on strategic delegation and vertical separation as a commitment device (e.g. later work by Bonanno & Vickers and the broader Vickers strategic-delegation tradition). The empirical data derive from Flaherty & Teece (1982).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
