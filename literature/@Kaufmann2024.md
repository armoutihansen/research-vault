---
citekey: Kaufmann2024
title: Understanding markets with socially responsible consumers
authors: ["Kaufmann, Marc", "Andre, Peter", "K\\Hoszegi, Botond"]
year: 2024
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/WYPTC2AH"
pdf: /Users/jesper/Zotero/storage/VRGCBIEI/Kaufmann2024.pdf
tags: [literature]
keywords: [socially-responsible-consumption, externalities, competitive-equilibrium, price-taking, environmental-policy, consumer-beliefs]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
Kaufmann, Andre, and Kőszegi build a competitive-equilibrium framework for markets in which consumers care about the externalities (climate, animal welfare, working conditions) their purchases generate. Their central insight is that even a vanishingly small "socially responsible" consumer is *not* a price taker in the relevant sense: cutting one's own demand lowers the price and induces other consumers to buy more, so the individual's net effect on the aggregate externality is *dampened* to a factor $q_c \in (0,1)$ below one-to-one. Dampening erodes the motive to mitigate and produces a new market failure—overconsumption persists even when consumers fully internalize the externality ($k=K$). A 2,000-person survey shows 38% of consumers do perceive dampening but 54% naively expect a one-to-one impact; the paper then shows naive consumers help in single-good markets but can worsen outcomes in multi-good markets with cross-market spillovers.

## Research question
How do markets behave, what is the welfare outcome, and which policy interventions work best, when a non-trivial share of consumers are willing to modify their consumption to reduce the externalities it causes? Specifically: does the standard price-taking assumption survive for such consumers, and do voluntary, decentralized consumer responses substitute for systemic policy?

## Method / identification
Three complementary parts.

(1) **Theory.** A single-good "replicator economy": one focal consumer plus $I$ identical other consumers (demand $D(p)$, $D'<0$) and $I$ identical suppliers (supply $S(p)$, $S'>0$), with $I\to\infty$. A Walrasian auctioneer clears the market at price $p(c)$ solving $c+ID(p(c))=IS(p(c))$, generating externality $g(c)=q(c)=IS(p(c))$. The rational consequentialist consumer maximizes
$$u(c)-p(c)\,c-k\bigl(g(c)-g(0)\bigr),$$
with $u(\cdot)$ thrice-differentiable, strictly concave, and $k>0$ the strength of social concern. A *competitive equilibrium* is a fixed point in which the market clears, each consumer optimizes given the perceived dampening, and that dampening is consistent with aggregate behavior. The planner weights the externality at exogenous marginal social cost $K$, and the paper argues $k\le K$ is natural.

(2) **Survey.** A preregistered survey of 2,000 U.S. consumers (Prolific, October 2023). Eight real-world goods split into four *quantity-dampening* questions (reducing fuel, meat, flights, energy) and four *substitution-dampening* questions (brown→green electricity, new→secondhand clothing, inefficient→efficient housing, conventional→fair-trade coffee). Respondents pick from five categorical impact options and write open-ended explanations; social concern is measured by comparing willingness-to-pay for an action when it does versus does not reduce the aggregate externality, separating consequentialist from deontological/warm-glow motives.

(3) **Extension to naïveté.** The same framework is re-solved replacing rational dampening-aware consumers with "naive" consumers who expect a one-to-one impact, including a two-good model with both product choice and quantity choice.

## Data
Original survey data: 2,000 U.S. respondents from Prolific (Oct 2023), approximating the adult U.S. population on gender, age, income, region (over-representing college-educated/Democratic consumers; results robust to reweighting). Both categorical impact predictions and open-ended qualitative text. No external/administrative datasets.

## Key findings
- **Proposition 1 (Violation of price taking).** As $I\to\infty$, the consumer's price impact $p'(c)\to0$ (she is a price taker for expenditure), but her impact on others' consumption is $q_c \equiv \lim q'(c) = \frac{S'(p^*)}{S'(p^*)-D'(p^*)} \in (0,1)$. Others dampen her reduction by $1-q_c=\frac{-D'(p^*)}{S'(p^*)-D'(p^*)}$, the same object as the producer incidence of a commodity tax. Dampening is large when demand is elastic relative to supply.
- **Proposition 2 (Overconsumption).** There is a unique social optimum $q^{FB}$; for any $k\le K$, every competitive-equilibrium quantity strictly exceeds $q^{FB}$. Even fully internalizing consumers ($k=K$) overconsume—a new market failure driven by a pecuniary externality on others' private utility that even responsible consumers ignore. With non-market (home) production this failure vanishes (Observation 2).
- **Proposition 3 (Multiple equilibria).** When $u'$ is steep over a range, multiple equilibria coexist; welfare strictly decreases in equilibrium quantity, and path dependence makes the worst (highest-consumption) equilibrium plausible.
- **Policy (Propositions 4–6).** Policies that induce *lower* dampening are better. More responsive permit supply dominates ($\pi<1$ beats caps); taxes decreasing in the consumer price beat fixed taxes, which beat increasing taxes (Prop. 5), generalizing Herweg & Schmidt (2022) that a unit tax beats a cap. Under international trade with a less-regulated polluting partner, a cap can beat a tax (Prop. 6) because it dampens the consumer's effect on dirty foreign production less.
- **Two-good model (Proposition 7).** With unit demand there is always a "selfish" equilibrium where clean and dirty products sell at the same price and responsible consumers are indifferent—the clean product gains no market advantage and this may be the only equilibrium. With quantity choice, a cross-market effect emerges: raising clean consumption raises its price and pushes someone to the dirty product, so a good's realized externality can exceed its direct externality.
- **Survey facts.** 38% of consumers perceive dampening (perceived degree 0.19–0.55; most of these expect *zero* effect), but 54% naively expect one-to-one impact and 3% expect a positive multiplier. Social concerns are frequently consequentialist.
- **Proposition 8 (Effects of naïveté).** Naive consumers consume less than rational ones in a single-good economy (raising welfare) but more in multi-good economies with cross-market spillovers; a mix of naive and rational consumers can yield the worst outcomes.

## Contribution
First framework to recognize that socially responsible consumers violate price taking and to embed the resulting *dampening* into competitive-equilibrium behavior in a standard product market. It overturns the Econ-1 intuition that internalizing consumers ($k=K$) deliver the social optimum, supplies a portable equilibrium tool adaptable to offsets, other externalities and other social-concern formulations, derives novel policy rankings, and grounds the model's key behavioral primitives (beliefs about impact, nature of concerns) in original survey evidence.

## Limitations & open questions
- No formal equilibrium-selection criterion among multiple equilibria—only informal path-dependence arguments (Prop. 3).
- Off-equilibrium beliefs about dampening in the two-good naive model are not uniquely pinned down; under a strict belief rule equilibrium may not exist (footnote 29 to Prop. 8).
- Whether beliefs about the *mechanism* (e.g. "too small to matter" vs. understanding offset dynamics) can be shifted by persuasion or policy framing is left for future work (footnote 25).
- The authors flag many unexplored environments: consumer purchase/deletion of offsets and permits, dynamic policy rules, and how different consumer types behave in settings beyond those modeled.
- Survey predictions are largely non-incentivized (controlled-scenario design); robustness checks are relegated to the Online Appendix.

## Connections
The benchmark contrasts with the classical price-taking tradition (Debreu 1959; Arrow & Hahn 1971; Mas-Colell 1980) and with prior treatments of social preferences in markets that implicitly assume price/behavior taking (Sobel 2007; Dufwenberg, Heidhues, Kirchsteiger & Riedel 2011; Hakenes & Schliephake 2021; Pástor, Stambaugh & Taylor 2021; Dewatripont & Tirole). The dampening mechanism extends Heinkel, Kraus & Zechner (2001) to vanishingly small consumers and parallels Norwood & Lusk (2011) and Trammell (2023). The tax-versus-cap analysis builds directly on Herweg & Schmidt (2022). The "replacement logic" / replacement-of-impact behavior connects to Falk, Neuber & Szech (2020) and Ziegler, Romagnoli & Offerman, and the erosion of moral behavior by markets to Falk & Szech (2013) and Bartling, Weber & Yao (2015). The replicator-economy device follows Shubik (1973) and Roberts & Postlewaite (1976). The open-ended survey methodology draws on Andre et al. (2022), Ferrario & Stantcheva (2022), and Stantcheva (2023); measurement of consequentialism relates to Bénabou, Falk & Henkel (2022) and Hart, Thesmar & Zingales (2024).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
