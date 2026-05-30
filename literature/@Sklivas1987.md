---
citekey: Sklivas1987
title: The Strategic Choice of Managerial Incentives
authors: ["Sklivas, Steven D."]
year: 1987
type: journalArticle
doi: 10.2307/2555609
zotero: "zotero://select/library/items/LMIF2RJJ"
pdf: /Users/jesper/Zotero/storage/2E6M3Q83/Sklivas1987.pdf
tags: [literature]
keywords: [strategic-delegation, managerial-incentives, oligopoly, cournot-bertrand, industrial-organization, strategic-commitment]
topics: []
related: [Vickers1985]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Do firms with separate owners and managers maximize profits? We address this question for an oligopoly where managers compete in quantities or prices, as in the Cournot or Bertrand models, and owners choose their managers' incentives. We find that there is a strategic aspect in the problem of selecting incentives and that profit-maximizing behavior does not result. In particular, in the oligopoly we study, the behavior of firms competing in quantity (price) more closely resembles perfectly competitive (collusive) behavior than Cournot (Bertrand) behavior.

## Summary
Sklivas shows that when ownership and management are separated, profit-maximizing owners will deliberately write contracts that commit their managers to *not* maximize profits, because doing so manipulates the equilibrium actions of rival firms. In a two-stage duopoly game where owners first publicly announce linear profit-plus-revenue incentive contracts and managers then compete in the second stage, quantity competition leads firms to behave more aggressively than Cournot (output above Cournot, toward the competitive level), while price competition leads firms to behave less aggressively than Bertrand (prices above Bertrand, toward collusion). The result is a classic strategic-commitment mechanism: incentive design becomes a tool of oligopolistic rivalry.

## Research question
Do firms with separated owners and managers maximize profits when they operate in an oligopoly? More precisely, what incentive contracts will profit-maximizing owners choose for their managers when those contracts are publicly observable and affect rivals' equilibrium behavior, and how does the resulting market outcome compare to standard Cournot and Bertrand benchmarks?

## Method / identification
A two-stage, owner-manager game solved by subgame-perfect (Nash-in-both-stages) equilibrium. There are two firms, each with one owner and one manager. In stage one owners simultaneously write and *publicly announce* a contract; in stage two managers simultaneously choose the firm's quantity (or price). Each manager $i$ chooses his action to maximize his incentive measure $g_i$, a linear combination of profit $\Pi_i$ and revenue $R_i$:
$$g_i = \lambda_i \Pi_i(x_1,x_2) + (1-\lambda_i) R_i(x_1,x_2) = R_i(x_1,x_2) - \lambda_i C(x_i),\quad i=1,2.$$
The owner's only choice variable is the weight $\lambda_i$; a lower $\lambda_i$ makes the manager weight cost less and act more aggressively. Owner $i$ chooses $\lambda_i$ to maximize true profit $\Pi_i(x_i^*(\lambda_i,\lambda_j), x_j^*(\lambda_i,\lambda_j))$ anticipating the second-stage Nash equilibrium. The method is to solve backwards: derive managers' best responses and the second-stage Nash quantities/prices as functions of $(\lambda_1,\lambda_2)$, substitute into owners' profit, and solve owners' first-stage Nash. The structure parallels strategic-commitment two-stage games such as Dixit (1980) and Fudenberg & Tirole (1984).

**Quantity competition:** linear demand $P = a - bx$ with $x = x_1 + x_2$, homogeneous product, constant marginal cost normalized to $c=1$, $a>1$. Manager best response $x_i = (a - \lambda_i - b x_j)/2b$; second-stage equilibrium $x_i^* = (a - 2\lambda_i + \lambda_j)/3b$; symmetric equilibrium incentive $\lambda^* = (6-a)/5$.

**Price competition:** symmetric differentiated demand $x_i = a - P_i + \beta P_j$ with $0 < \beta < 1$, constant marginal cost $c$. Manager best response $P_i = (a + \lambda_i c + \beta P_j)/2$; the equilibrium incentive weight satisfies $\lambda^* > 1$.

The Appendix generalizes the quantity model to $n$ firms.

## Data
None - this is a pure theory paper. Section 5 discusses (but does not itself estimate) prior empirical work on executive compensation: Roberts (1959), McGuire, Chiu & Elbring (1962), Williamson (1963), Lewellan & Huntsman (1970), Yarrow (1972), and especially Lackman & Craycraft (1974), whose corrugated-specialties study found Cournot inadequate and revenue-augmented reaction functions more predictive.

## Key findings
- **Proposition 1 (quantity competition):** In equilibrium owners set $\lambda^* < 1$, so managers behave more aggressively than profit maximizers. Outputs exceed the Cournot level but remain below the social optimum: $(a/2b) > x_i^*(\lambda^*,\lambda^*) > x_i^*(1,1)$. Total output $x_1^* + x_2^* = 4(a-1)/5b$ is below the competitive level $a/b$. Because both owners commit to aggression, both earn *lower* profits than in Cournot - a prisoner's-dilemma-like outcome. Profit maximization ($\lambda=1$ for both) is not an equilibrium.
- **Proposition 2 (price competition):** In equilibrium $\lambda^* > 1$, so managers behave *less* aggressively than profit maximizers. Equilibrium prices exceed Bertrand prices: $P^*(\lambda^*,\lambda^*) > P^*(1,1)$. Commitment is now mutually beneficial: both firms earn *higher* profits than Bertrand, approaching collusion (though still below joint-profit-maximizing levels).
- **Mechanism / intuition:** choosing $\lambda_i$ is equivalent to choosing the manager's best-response function, so owners effectively "play a game in best-response functions." Starting from the standard ($\lambda=1$) outcome, a unilateral deviation is profitable, so symmetric profit maximization cannot be an equilibrium. Equilibrium occurs where each owner's isoprofit curve is tangent to the rival manager's best-response function.
- **$n$-firm result (Appendix):** the equilibrium weight $\lambda^*$ increases monotonically with $n$ and approaches 1 as $n \to \infty$ - the strategic distortion vanishes as the market becomes competitive.

## Contribution
Provides one of the foundational "strategic delegation" results in industrial organization: it shows that the separation of ownership and management is not merely an agency-cost friction but a *strategic commitment device*, and that profit-maximizing owners rationally choose non-profit-maximizing incentive contracts. It reconciles long-standing managerial-firm critiques of the profit-maximization hypothesis (Baumol, Marris, Williamson, Galbraith) with optimizing behavior, and supplies a clean comparative result tying the *direction* of distortion to the mode of competition (strategic substitutes vs. complements). It is the canonical companion to Fershtman & Judd and Vickers, who reached similar conclusions independently and contemporaneously.

## Limitations & open questions
- The author explicitly calls for a direct empirical test: "We would like to see a test of the model of oligopolistic behavior proposed here" - existing studies (Lackman & Craycraft, etc.) only approximate it.
- Contracts are restricted to a *linear* profit-revenue combination; the optimal-contract space is not characterized.
- Contracts are assumed *publicly observable and credibly committed* - the results hinge on this; unobservable or renegotiable contracts are not analyzed.
- The model is a symmetric duopoly with linear demand and constant marginal cost; robustness to asymmetry, nonlinear demand, and richer cost structures is only briefly footnoted.
- Owners are assumed to know demand and cost; the paper notes (footnote) that cost uncertainty preserves qualitative results but does not develop it.
- The contracting environment abstracts from the standard moral-hazard / observability frictions of Holmstrom (1979); integrating strategic delegation with genuine hidden action is left open.

## Connections
The paper is a cornerstone of the strategic delegation literature and is explicitly tied to Fershtman & Judd (1985), who derive nearly identical results independently and simultaneously, and to [[@Vickers1985|Vickers (1985)]], who frames delegation as truthful preference revelation. Its two-stage commitment logic builds directly on Dixit (1980) on investment and entry deterrence and on Fudenberg & Tirole (1984) ("fat cat / puppy dog / lean and hungry"), and contrasts deliberately with the single-agent contracting of Holmstrom (1979), where the optimal contract is independent of other contracts. It formalizes the managerial-firm skepticism toward profit maximization of Simon (1957), Cyert & March (1963), Marris (1964), Williamson (1963, 1964), Galbraith (1967), and Baumol (1977). The quantity-versus-price asymmetry connects to the strategic-substitutes/complements distinction later crystallized by Bulow, Geanakoplos & Klemperer and to the Singh & Vives treatment of Cournot versus Bertrand in differentiated duopoly. Empirically it invokes Roberts (1959), McGuire, Chiu & Elbring (1962), Lewellan & Huntsman (1970), Yarrow (1972), and Lackman & Craycraft (1974) on sales-based executive compensation.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
