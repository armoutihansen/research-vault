---
citekey: McGuire1983
title: An Industry Equilibrium Analysis of Downstream Vertical Integration
authors: ["McGuire, Timothy W.", "Staelin, Richard"]
year: 1983
type: journalArticle
doi: 10.1287/mksc.2.2.161
zotero: "zotero://select/library/items/PUL8Y4UU"
pdf: /Users/jesper/Zotero/storage/49PPJ78A/McGuire1983.pdf
tags: [literature]
keywords: [vertical-integration, channel-structure, product-substitutability, nash-equilibrium, strategic-decentralization, duopoly-pricing]
topics: ["[[distribution-channels-vertical-integration]]"]
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This paper investigates the effect of product substitutability on Nash equilibrium distribution structures in a duopoly where each manufacturer distributes its goods through a single exclusive retailer, which may be either a franchised outlet or a factory store. Static linear demand and cost functions are assumed, and a number of rules about players' expectations of competitors' behavior are examined. It is found that for most specifications product substitutability does influence the equilibrium distribution structure. For low degrees of substitutability, each manufacturer will distribute its product through a company store; for more highly competitive goods, manufacturers will be more likely to use a decentralized distribution system.

## Summary
McGuire & Staelin build a duopoly model in which two manufacturers each sell a differentiated, competing product through a single exclusive retail outlet that may be either a company (factory) store or an independent franchised dealer. Even with no efficiency advantage to using an intermediary, they show that the Nash-equilibrium channel structure depends on a single parameter: the degree of product substitutability. When products are weak substitutes, both manufacturers vertically integrate (company stores); when products are close substitutes, a decentralized franchised structure becomes the equilibrium. Decentralization functions as a strategic commitment device that softens retail price competition. This is the canonical reference establishing that vertical separation can be privately optimal purely for competition-dampening reasons.

## Research question
Why would a manufacturer place an independent intermediary between itself and the consumer, and lose control over retail price, even when it could perform the selling/distribution functions just as efficiently? Concretely: how does the substitutability of competing end products determine whether the equilibrium industry distribution structure is vertical integration (factory stores) or decentralization (franchised dealers)?

## Method / identification
A multi-stage non-cooperative game solved for subgame-perfect Nash equilibria, layered into a higher-level structure-choice game. The industry has two manufacturers; each has one exclusive retail outlet per (identical) market area. Retail demand is linear; after rescaling, the entire system reduces to one parameter $\theta\in[0,1)$, the ratio of the cross-price to own-price rate of demand change (substitutability). Rescaled demand is
$$q_i = 1 - p_i + \theta p_j, \quad j = 3-i,\ i=1,2.$$
Three channel structures arise from the two outlet types: pure decentralized (DD, four players), pure integrated (II, two players), and mixed (DI). Each is solved as a Stackelberg-style sequential game: retailers set retail prices Nash-non-cooperatively conditional on wholesale prices; manufacturers then set wholesale prices conditional on the resulting conditional-equilibrium retail-price functions. The baseline behavioral rules are D1 (decentralized manufacturer conditions on the two retailers' reaction functions and the rival's wholesale price), M1 (mixed structure), and I1 (integrated manufacturers play Bertrand in retail prices). For the pure decentralized case, retailer reaction functions yield $p_i = \frac{1}{2-\theta} + \frac{2+\theta}{(2+\theta)(2-\theta)}w_i + \cdots$; substituting into manufacturer profit and optimizing gives equilibrium wholesale prices and the closed-form profit expressions in Table 1. The top-level game then has each manufacturer choosing "decentralize vs. integrate," with payoffs equal to the conditional-equilibrium profit pairs; Nash equilibria of this $2\times2$ game are computed. Section 6 robustness-checks alternative behavioral rules (D3, M2) generating games G1, G3, G4, G5, plus a colluding/total-channel-profit variant G2.

## Data
None - this is a purely theoretical paper. The authors deliberately decline empirical testing, arguing confrontation with data would be premature given the abstractions made; they only mention illustrative industries (autos, gasoline, soft drinks, fast food, sewing machines, telephone centers) anecdotally.

## Key findings
- A profit breakeven at $\theta = 0.708$: for $\theta < 0.708$ the pure factory-store (II) system is more profitable; above it the pure franchised (DD) system dominates. At $\theta=0$ each manufacturer is a monopolist and integration is twice as profitable; near $\theta\to 1$ decentralization is far more profitable.
- Nash equilibrium of the structure game (G1): for $\theta < 0.931$ the unique equilibrium is pure integration (II), because a firm whose rival is decentralized always prefers to integrate. For $\theta > 0.931$ there are two Nash equilibria, II and DD, with DD payoff-dominant. Thus the pure franchised system is Nash only for very high substitutability.
- Decentralization is a strategic buffer: with close substitutes, manufacturers profit by inserting independent profit-maximizing dealers that soften head-to-head retail competition, even though they surrender control of retail price and gain no efficiency.
- Capturing retail profit via lump-sum franchise fees expands but does not eliminate the integration region: DD is Nash for $\theta > 0.771$ under a total-channel-profit criterion, while II remains Nash for all $\theta$. Total channel profits are actually higher under decentralization for $\theta > 0.432$.
- Contrast with Jeuland & Shugan (1982): their reduced-form (Stackelberg/dominant-firm) demand implicitly assumes a price leader, so vertical integration maximizes joint profit; explicitly modeling both price-setters' interaction overturns this in a duopoly.
- Sales quotas / retail-price ceilings make a franchised dealer behaviorally identical to a company store, so a manufacturer only wants to control its dealer when cross-elasticities are low; channel conflict should be greater where product differentiation is high.
- Robustness (Table 5): across games G1, G3, G4, G5 the qualitative result holds except G4 (which yields pure integration for all $\theta$). The dominant-structure breakpoint is nearly invariant (0.707 to 0.739) to the D1 vs. D3 assumption.
- Welfare: consumers are best off (lowest prices) under company stores, whether manufacturers collude or compete - so observed fierce dealer competition does not imply low consumer prices.

## Contribution
Establishes that the channel structure (degree of vertical integration) is itself an endogenous equilibrium outcome determined by downstream product competition, rather than a fixed institutional given. It is among the first game-theoretic treatments to make distribution structure the dependent variable in an industry-equilibrium model and to identify strategic vertical separation as a device to relax price competition. Methodologically it differs from the bilateral-monopoly tradition by explicitly modeling competitive interaction between two manufacturer-retailer dyads and by parameterizing substitutability through a single, interpretable $\theta$.

## Limitations & open questions
The authors flag these explicitly: (i) symmetric, identical-cost firms - what happens with different cost structures, or costs that depend on the structure (e.g., the common claim that integrated systems are less efficient)? Under what inefficiency ranges do factory stores survive? (ii) Exactly two manufacturers, one exclusive outlet each - implications of relaxing these are unknown, and results do not apply to retailers carrying multiple manufacturers' lines. (iii) Whether a dual distribution system (one manufacturer using both private and company outlets simultaneously) can be Nash; what is the equilibrium number and organization of outlets? (iv) The behavioral expectation rules are not uniquely justified; which formulation fits a given industry is an empirical question. (v) The model abstracts from risk preferences, asymmetric-information reward/incentive structures, financing, profit/equity-sharing, and multi-brand retailers. The authors regard empirical confrontation as premature.

## Connections
Directly extends the bilateral-monopoly channel literature - Hawkins (1950), Douglas (1975), and especially Jeuland & Shugan (1982), whose joint-profit-maximization-via-coordination result it contrasts and qualifies. Builds on the channel-structure paradigm of McGuire & Staelin's own earlier work (1976) and Doraiswamy, McGuire & Staelin (1979), with related non-linear-demand treatments by Hibshoosh (1978) and Coughlan (1982). Engages dealer-number models of Pashigian (1961) and White (1971), the bilateral-monopoly synthesis of Wu (1964), the L-level vertical-system games of Baligh & Richartz (1967), Nash-bargaining transfer-price work of Zusman (1981), and the sociopolitical channel-behavior framework of Stern & Reve (1980). The strategic-decentralization mechanism here is the foundational marketing-science complement to the strategic-delegation literature in industrial organization (e.g., later Bertrand-competition-softening arguments akin to Bonanno & Vickers and Rey & Stiglitz on vertical restraints). The single substitutability parameter and linear differentiated-demand setup connect to Bertrand competition with differentiated products and to the antitrust analysis of vertical integration.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
