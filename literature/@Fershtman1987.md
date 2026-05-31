---
citekey: Fershtman1987
title: Equilibrium Incentives in Oligopoly
authors: ["Fershtman, Chaim", "Judd, Kenneth L."]
year: 1987
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/74NC7KR5"
pdf: /Users/jesper/Zotero/storage/Q2N8K3T7/Fershtman1987.pdf
tags: [literature]
keywords: [strategic-delegation, managerial-incentives, oligopoly, cournot-competition, bertrand-competition, principal-agent, industrial-organization]
topics: ["[[strategic-delegation-firm-objectives]]"]
related: [Sklivas1987, Vickers1985]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We examine the incentives that owners of competing firms give their managers. We show that, in equilibrium, each manager will be paid in excess of his decision's marginal profit in a Cournot-quantity game, but paid less than the marginal profit in a price game. In the Cournot case, deviations from profit maximization are reduced by ex ante cost uncertainty and increased by correlation in the firms' costs.

## Summary
Profit-maximizing owners of competing firms will, in equilibrium, deliberately give their managers incentives that depart from profit maximization, because doing so manipulates the behavior of rival managers. The direction of distortion depends on the mode of competition: under Cournot (quantity) competition owners reward sales beyond marginal profit, making managers aggressive and expanding output (raising efficiency, lowering rents); under Bertrand (price) competition with differentiated goods owners penalize sales, making managers price softly and pushing prices toward monopoly. This is the foundational "strategic delegation" result.

## Research question
When the profit accruing to a principal–agent (owner–manager) pair depends on the decisions of other rational agents, should an owner who cares only about profits still instruct his manager to maximize profits? More concretely: in an oligopoly where competing managers observe one another's incentive contracts, what equilibrium incentive contracts do owners choose, and how do these depend on the mode of competition, cost uncertainty, cost correlation, and the number of firms?

## Method / identification
A two-stage subgame-perfect Nash equilibrium ("incentive equilibrium"). In stage one, owners simultaneously choose, for risk-neutral managers, a linear incentive that has the manager maximize a weighted combination of profit and sales,
$$O_i = \alpha_i \pi_i + (1-\alpha_i) S_i,$$
where $\pi_i$ and $S_i$ are firm $i$'s profit and sales; $\alpha_i$ is unrestricted (negative values allowed). In stage two, after demand/cost uncertainty is realized and made common knowledge, managers play the oligopoly game knowing all contracts. The game is solved by backward induction. Crucially, ex ante uncertainty about demand/cost parameters is assumed: it gives the manager a genuine role as an observer and rules out the deterministic alternative in which quantity-forcing contracts would just reproduce the Cournot/Bertrand outcome.

The Cournot model uses linear demand $p = a - bQ$ with constant unit costs $c_i$. Since $\alpha_i$ enters the manager's objective only through perceived marginal cost $\alpha_i c_i$, choosing $\alpha_i$ amounts to shifting firm $i$'s reaction function — each owner thereby acts as a Stackelberg leader vis-à-vis the rival's manager. The price model uses differentiated linear demand $q_i = A - b p_i + a p_{3-i}$ with $b > a$ (own-price effect dominates), where price reaction curves slope up.

## Data
None — this is a pure theory paper. No empirical estimation; results are analytical theorems on a parametric duopoly/oligopoly model.

## Key findings
- **Theorem 1 (Cournot, known costs):** Both owners set $\alpha_i < 1$ (sales incentives), and may even penalize profits if costs are low. The equilibrium weight is $\alpha_i = 1 - (a + 2c_j - 3c_i)/(5c_i)$, with equilibrium price $p = (a + 2(c_1+c_2))/5$ — below the Cournot price.
- **Corollary 1:** Relative to ordinary Cournot, the incentive equilibrium yields greater output, lower rents, lower prices, and a *more efficient* allocation — efficiency improves both because price is nearer marginal cost and because the low-cost firm's output share rises.
- **Theorem 2 (uncertain demand intercept $a$):** Analogous results hold; the case of uncertain slope $b$ is trivial since $b$ does not enter the owners' choice of $\alpha$.
- **Theorem 3 (uncertain, identically distributed costs):** With variance $\sigma^2$, coefficient of variation $v=\sigma/\mu$, and correlation $r$, the equilibrium weight is $\alpha = \frac{6(v^2+1)}{(4+r)v^2+5}$. Distortion from profit maximization *falls* as cost variance $v$ rises (it is harder to pick the right $\alpha$ when costs are noisy) and *rises* as cost correlation $r$ rises (commonly experienced shocks make distortion more valuable).
- **Theorem 4 (many firms):** As $n \to \infty$, $\alpha_i \to 1$ — managers become profit maximizers. Strategic delegation vanishes under competition, matching perfect-competition intuition; hence the market-structure–to–incentives relationship is non-monotonic (monopoly and perfect competition both yield profit maximization, only oligopoly distorts).
- **Theorem 5 (Bertrand, differentiated goods):** $\alpha_i > 1$ — managers are *overcompensated* for profit at the margin (equivalently taxed on sales), so they price *softly*. Equilibrium price exceeds the profit-maximizing (standard Bertrand) price, moving toward the monopoly price; here the distortion is mutually advantageous, so the focal-point objection that undermines the deterministic Cournot case does not apply.

## Contribution
Establishes the canonical "strategic delegation" / "managerial incentives as commitment device" result: separation of ownership and control is not merely an agency cost but a *strategic instrument*. An owner distorts internal incentives to exploit the rival's reaction, achieving a Stackelberg-leader advantage that profit-maximizing contracts cannot. The sign of the distortion is pinned to whether strategic variables are substitutes (quantities, downward-sloping reactions) or complements (prices, upward-sloping reactions). It links the theory of the firm's objective to market structure and to the strategic-trade-policy literature (Brander–Spencer), generalizing those insights by adding parameter uncertainty.

## Limitations & open questions
- Restriction to **linear contracts** (profit/sales mix) is imposed for tractability; unrestricted contracts may admit no equilibrium (Myerson 1982). The authors flag this as the major weakness.
- **No genuine moral hazard / asymmetric information** motivating contracts in the first place — addressed in their companion paper (Fershtman and Judd, 1987 working paper).
- **Two-stage (single-shot) game** with stage-two common knowledge of contracts; true repeated play would generate many new possibilities but raises intractable inference and multiple-equilibria problems.
- Managers play **Nash noncooperative**; a bargaining (cooperative) theory of manager behavior is suggested as an alternative that would still leave room for strategic incentive design.
- Linear demand and the assumption that owners observe only profits/sales (not their rival's) are simplifying; further research should generalize.
- Multiple-equilibria / focal-point issues arise when forcing contracts coexist with linear ones in the deterministic Cournot case.

## Connections
Builds directly on the principal–agent tradition of Ross (1973), Mirrlees (1976), Holmström (1977), and Harris & Raviv (1979), and on the separation-of-ownership-and-control literature (Jensen & Meckling 1976; Williamson 1964; Simon 1964; Baumol's 1958 sales-maximization hypothesis). It extends the strategic-trade-policy work of Brander & Spencer (1983, 1985) and the capital-structure-as-commitment work of Brander & Lewis (1986) and Maksimovic (1986) by treating managerial incentives as the commitment device and adding parameter uncertainty. The linear-contract optimality assumption is justified by appeal to Holmström & Milgrom (1987). The companion paper Fershtman & Judd (1987, "Strategic Incentive Manipulation in Rivalrous Agency") embeds the result in a moral-hazard structure. The paper is the twin of [[@Sklivas1987|Sklivas (1987)]] and [[@Vickers1985|Vickers (1985)]], with which it jointly founds the strategic-delegation literature later surveyed and extended in work on competition with delegation.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
