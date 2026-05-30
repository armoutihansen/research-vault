---
citekey: Milgrom1981
title: "Good News and Bad News: Representation Theorems and Applications"
authors: ["Milgrom, Paul R."]
year: 1981
type: journalArticle
doi: 10.2307/3003562
zotero: "zotero://select/library/items/PFV7HQIZ"
pdf: /Users/jesper/Zotero/storage/GKXB45TB/Milgrom1981.pdf
tags: [literature]
keywords: [monotone-likelihood-ratio, information-economics, first-order-stochastic-dominance, principal-agent, disclosure-games, winners-curse]
topics: []
related: [Akerlof1970]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> This is an article about modeling methods in information economics. A notion of "favorableness" of news is introduced, characterized, and applied to four simple models. In the equilibria of these models, (1) the arrival of good news about a firm's prospects always causes its share price to rise, (2) more favorable evidence about an agent's effort leads the principal to pay a larger bonus, (3) buyers expect that any product information withheld by a salesman is unfavorable to his product, and (4) bidders figure that low bids by their competitors signal a low value for the object being sold.

## Summary

Milgrom builds a portable modeling device for "good news": an ordering of signals by how *favorable* they are about an unknown parameter, defined via first-order stochastic dominance of posteriors and characterized by the **monotone likelihood ratio property (MLRP)**. He proves a handful of representation theorems that reduce any "comparable" information system to a single real-valued, MLRP-ordered statistic, then deploys the tool across four canonical settings — securities pricing, principal–agent moral hazard, persuasion/disclosure games, and sealed-bid auctions — recovering monotone-comparative-statics results that had previously been hard to obtain because no clean notion of "more favorable information" existed.

## Research question

Much of information economics rests implicitly on monotonicity (more able types signal more, riskier types buy more insurance), yet rational-expectations asset pricing and moral-hazard theory lacked any formal definition of what it means for one signal realization to be *better news* than another. The question: can "favorableness" of evidence be given a primitive, prior-independent definition, characterized in terms of likelihoods, and used to generate monotone-comparative-statics across diverse models?

## Method / identification

Pure decision/game theory. Let $\theta \in \Theta \subseteq \mathbb{R}$ be an unknown parameter and $x \in X \subseteq \mathbb{R}^m$ an observed signal with conditional density $f(x \mid \theta)$. Signal $x$ is **more favorable than** $y$ if, for *every* nondegenerate prior $G$ on $\theta$, the posterior $G(\cdot \mid x)$ strictly first-order stochastically dominates $G(\cdot \mid y)$ — i.e. every decisionmaker with increasing utility prefers the posterior gamble induced by $x$. The analysis works through Bayes' rule on posterior odds,
$$\frac{g(\bar\theta\mid x)}{g(\underline\theta\mid x)}=\frac{g(\bar\theta)\,f(x\mid\bar\theta)}{g(\underline\theta)\,f(x\mid\underline\theta)},$$
to convert the dominance requirement into a likelihood condition. The applications layer specific economic structure on top: a representative-investor first-order condition for asset pricing, Holmström's (1979) optimal sharing-rule characterization for moral hazard, sequential equilibrium (Kreps–Wilson) for the persuasion game, and an order-statistic argument for the auction.

## Data

None — this is a theoretical paper. Examples (oil-tract mineral-rights auctions run by the U.S. Department of the Interior; sales encounters; security markets) are illustrative, not empirical.

## Key findings

- **Proposition 1 (characterization):** $x$ is more favorable than $y$ iff for every $\bar\theta > \underline\theta$, $f(x\mid\bar\theta)f(y\mid\underline\theta) - f(x\mid\underline\theta)f(y\mid\bar\theta) \ge 0$ — a likelihood-ratio inequality.
- **Proposition 2 (MLRP):** The family $\{f(\cdot\mid\theta)\}$ has the strict MLRP iff $x > y$ implies $x$ is more favorable than $y$. Normal (mean $\theta$), exponential, Poisson, uniform on $[0,\theta]$, and noncentral chi-square families all qualify.
- **Proposition 3 (representation):** If any two signals in a general space $X$ are comparable, there is a sufficient statistic $H(x)=\int h(\theta)\,dG(\theta\mid x)$ whose densities have the strict MLRP — any comparable information system reduces to a one-dimensional MLRP variable.
- **Proposition 4 (intervals):** Under strict MLRP, the event $\{x\in[a,b]\}$ is more favorable than $\{x\in[c,d]\}$ whenever $a\ge c$, $b\ge d$ (one strict).
- **Securities:** With identical concave investors, equilibrium price equals $E[\theta\mid x]$ under a utility-tilted measure; more favorable news raises price, good news $p(x) > p$, bad news lowers it.
- **Moral hazard (Prop. 5):** Holmström's optimal sharing rule $s(\pi)$ is increasing iff $f_\theta(\pi\mid\theta^*)/f(\pi\mid\theta^*)$ is increasing — i.e. iff output has the MLRP in effort. Nonmonotone fee schedules arise *only* when higher profits are evidence of *lower* effort; under MLRP the incentive contract is steeper than any first-best risk-sharing rule and crosses it once from below.
- **Persuasion (Prop. 6):** At every sequential equilibrium of the sales-encounter game (verifiable but concealable evidence), the salesman uses *full disclosure*; the buyer is extremely skeptical, conjecturing that any withheld information is the least favorable consistent with the report (this is essentially Grossman's 1980 unraveling result). **Proposition 7:** with a $k < N$ assimilation constraint, equilibrium has the salesman report the $k$ most favorable observations.
- **Auctions:** Winning is *bad news* — $E[\theta\mid x_1] \ge E[\theta\mid x_1, B_2(x_2)\le b,\dots]$ — formalizing the **winner's curse**; moreover, winning with a *low* bid is especially bad news, while higher winning bids alleviate the curse.

## Contribution

Provides the now-standard formal vocabulary linking first-order stochastic dominance of posteriors to MLRP, and shows it is the right primitive for "good news." This single device unifies disclosure/unraveling, optimal contracting monotonicity, rational-expectations asset pricing, and the winner's curse, and the representation theorems justify the common practice of modeling information by a scalar MLRP signal. The paper is a methodological cornerstone for information economics, mechanism design, and the affiliation machinery later developed in Milgrom–Weber auction theory.

## Limitations & open questions

- The persuasion result assumes the buyer can verify not just reported facts but also meta-statements like "I have reported everything I know" — i.e. concealment is detectable. Milgrom flags as a *promising but unexplored* direction letting the number of pieces of evidence $N$ be a random variable whose realization is unverifiable, so the seller can plausibly claim ignorance.
- Generalizing the disclosure game to **costly communication** or to **bounded transmit/receive/processing capacity** (only the simple $k$-observation constraint is solved here).
- Existence in the persuasion game requires the least-favorable conjecture's minimizer to exist (e.g. continuous $f$ with compact support); general existence is not resolved.
- The favorableness order is incomplete on non-comparable signals; the theory speaks only to comparable information systems.

## Connections

Builds directly on Holmström (1979) "Moral Hazard and Observability" (and the diminishing-returns correction by Grossman–Hart 1980), supplying the MLRP justification for monotone contracts. The persuasion/unraveling result parallels Grossman (1980) on warranties and disclosure, foundational for the verifiable-disclosure literature. The favorableness/MLRP apparatus feeds into Milgrom–Weber (1980) "A Theory of Auctions and Competitive Bidding" and the affiliation concept, and connects to the winner's-curse analyses of R. Wilson (1977) and Milgrom (1979, 1981). The signaling/adverse-selection backdrop is Spence (1973), [[@Akerlof1970|Akerlof (1970]], 1976), Rothschild–Stiglitz (1976), and C. Wilson (1977); the asset-pricing application links to Cox–Ross (1976) and Harrison–Kreps (1979). Sequential equilibrium is taken from Kreps–Wilson (1980).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
