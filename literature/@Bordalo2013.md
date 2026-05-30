---
citekey: Bordalo2013
title: Salience and Consumer Choice
authors: ["Bordalo, Pedro", "Gennaioli, Nicola", "Shleifer, Andrei"]
year: 2013
type: journalArticle
doi: 10.1086/673885
zotero: "zotero://select/library/items/X8SN8PWU"
pdf: /Users/jesper/Zotero/storage/NL4KNN9J/Bordalo2013.pdf
tags: [literature]
keywords: [salience-theory, context-dependent-choice, behavioral-economics, decoy-effect, reference-dependence, willingness-to-pay, attention]
topics: []
related: [Bernheim2009, Eliaz2011a, Hauser1990, Heidhues2008, Huber1982, Kahneman1979, Kamenica2008, Koszegi2006b, Simonson1989, Tversky1993]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We present a theory of context-dependent choice in which a consumer's attention is drawn to salient attributes of goods, such as quality or price. An attribute is salient for a good when it stands out among the good's attributes relative to that attribute's average level in the choice set (or, more broadly, the choice context). Consumers attach disproportionately high weight to salient attributes, and their choices are tilted toward goods with higher quality/price ratios. The model accounts for a variety of disparate evidence, including decoy effects and context-dependent willingness to pay. It also suggests a novel theory of misleading sales.

## Summary

Bordalo, Gennaioli, and Shleifer extend their salience theory of risky choice to riskless consumer choice over goods described by quality $q$ and price $p$. A "salient thinker" overweights the attribute that stands out most relative to a reference good of average attributes, which mechanically tilts choice toward goods with a high quality/price ratio. Two perceptual primitives drive everything: *ordering* (contrast: an attribute is salient when far from its average) and *diminishing sensitivity* (a uniform level increase dampens salience). The interplay of these two forces gives a unified, tractable account of decoy/compromise effects, the Savage car-radio and Kahneman-Tversky jacket-calculator puzzles, context-dependent willingness to pay (Thaler's beer), the Hastings-Shapiro gasoline substitution, and a novel theory of "misleading sales."

## Research question

Can a single, parsimonious psychological mechanism, attention drawn to salient attributes, explain the broad set of context-dependence anomalies in riskless consumer choice (IIA violations, context-dependent WTP, asymmetric reactions to price changes) that standard utility theory and external-reference-point/loss-aversion models cannot jointly accommodate?

## Method / identification

A formal axiomatic decision model (no data). A consumer evaluates $N>1$ goods $C=\{(q_k,p_k)\}$ with undistorted quasi-linear utility $u_k=q_k-p_k$. The reference good is the average $(\bar q,\bar p)$ with $\bar q=\frac{1}{N}\sum_k q_k$, $\bar p=\frac{1}{N}\sum_k p_k$. A salience function $\sigma(\cdot,\cdot)$ is symmetric, continuous, and satisfies (Definition 1): **Ordering** (salience rises with contrast: for $m=\operatorname{sgn}(a_k-\bar a)$ and $\epsilon,\epsilon'\ge0$, $\sigma(a_k+m\epsilon,\bar a-m\epsilon')>\sigma(a_k,\bar a)$) and **Diminishing sensitivity** ($\sigma(a_k+\epsilon,\bar a+\epsilon)<\sigma(a_k,\bar a)$). Assumption 1 strengthens this to **homogeneity of degree zero**: $\sigma(\alpha a_k,\alpha\bar a)=\sigma(a_k,\bar a)$, with the canonical form

$$\sigma(a_k,\bar a)=\frac{\lvert a_k-\bar a\rvert}{a_k+\bar a}.$$

Valuation distorts the relative weights toward the salient attribute while keeping their sum fixed (Definition 2): if quality is salient, $u_k^S=\frac{2}{1+\delta}q_k-\frac{2\delta}{1+\delta}p_k$; if price is salient, the weights swap; with $\delta\in(0,1]$ decreasing in the severity of salient thinking ($\delta\to1$ recovers rationality, $\delta\to0$ collapses onto the single salient attribute). The model is extended (Section IV, Definition 3) so the choice *context* $C_{\mathrm{cont}}=C\cup C^e$ also includes the goods at their rationally expected prices $p_k^e=E[p_k]$, so the reference price becomes $\bar p=\frac{1}{2N}\sum_k(p_k+p_k^e)$. Identification of the latent quality $q$ is achieved via a WTP elicitation: in isolation $C=\{(q,p),(0,0)\}$ salience cancels and $\mathrm{WTP}=q$ (Remark 1).

## Data

None. This is a pure theory paper; it reinterprets thought experiments and prior empirical findings (Thaler's beer, Hastings and Shapiro 2013 gasoline, decoy-effect surveys) but introduces no new dataset. Hastings and Shapiro's separately calibrated salience model is cited as supporting evidence.

## Key findings

- **Proposition 1**: Under homogeneity of degree zero, a good's above-reference quality (or below-reference price) is salient iff $q_k/p_k>\bar q/\bar p$, equating salience ranking with the quality/price-ratio ranking.
- **Proposition 2**: On a rational indifference curve, the salient thinker chooses $k^*=\arg\max_k q_k/p_k$, the highest quality/price ratio (cheapest if $q_1/p_1>1$, most expensive if $q_1/p_1<1$).
- **Proposition 3**: Adding the outside option $(0,0)$ preserves the result when quality is salient; intermediate goods may be chosen but always retain an above-average quality/price ratio.
- **Corollary 1**: Demand for quality is increasing in the overall (expected) price level: a uniform price shift $\Delta$ past a threshold $\Delta^*$ flips choice from the low- to the high-quality good (diminishing sensitivity, the wine example).
- **Proposition 4 (decoys/compromise)**: A decoy with a sufficiently low quality/price ratio makes the high-quality good's quality salient and boosts its demand; crucially the effect is *asymmetric*, no decoy can reverse an initial preference for the high-quality good. Matches Heath and Chatterjee (1995).
- **Proposition 5**: The central comparative static. A uniform marginal price hike to a subset $C_C$ (fraction $\eta$) of the context boosts price salience for the most expensive good iff $\frac{p_C^{\max}-\bar p_C}{\bar p_F}<\frac{1-\eta}{\eta}$. *Expected* uniform hikes ($\eta=1$) lower price salience (diminishing sensitivity dominates, lower price sensitivity); *unexpected* hikes ($\eta=1/2$, expected prices fixed) raise it (ordering dominates, higher price sensitivity). This generates the asymmetric gasoline substitution.
- **Proposition 6 (context-dependent WTP)**: $\mathrm{WTP}(q\mid(q,p^e))$ weakly increases in the expected price $p^e$ over $p^e\le\frac{7}{2\delta}q$ (an anchoring effect explaining Thaler's beer), but collapses below true valuation when $p^e\gg q/\delta$ (price becomes salient).
- **Predictions 1-2 (falsifiable)**: When only price and quality *rankings* are observed, IIA can be deliberately violated by manipulating "irrelevant" goods' prices to make $q_j$ salient (Prediction 1); under uniform price shifts pairwise choice is flat, monotonic, or inverse-U-shaped, with at most two reversals (Prediction 2).
- **Misleading sales (Propositions 7-8)**: Inflating a "regular" price $p_f$ and offering a steep discount makes the sale price act as a decoy, letting a retailer extract up to $q/\delta$ (Prop. 7). Sales asymmetrically boost demand for high-quality (Prop. 8) and *nonstandard* goods only; for standard goods sold by many sellers, induced price variation makes price salient and *reduces* demand.

## Contribution

Provides a tractable, falsifiable, attention-based microfoundation for context-dependent riskless choice that unifies phenomena previously treated piecemeal (mental accounting, transaction utility, reference dependence). Unlike loss-aversion/external-reference-point models (Tversky-Kahneman 1991; [[@Tversky1993|Tversky-Simonson 1993]]; Bodner-Prelec 1994), salience predicts choice of *extreme* options and the empirically documented *asymmetry* of decoy and sales effects; unlike Gabaix (2012) ex-ante rational inattention, attention is allocated *ex post* to whatever stands out; unlike Koszegi-Szeidl (2013), it retains diminishing sensitivity (handling the Savage puzzle). It delivers a genuinely new theory of misleading sales tying inflated reference prices to decoy logic, consistent with regulatory concerns over fictitious "original" prices.

## Limitations & open questions

The authors explicitly flag several hooks:
- The **choice set / consideration set is taken as exogenous**; endogenizing the evoked set (typically 2-5 goods) is named as "an important direction of future work" (cf. [[@Hauser1990|Hauser-Wernerfelt 1990]]; [[@Eliaz2011a|Eliaz-Spiegler 2011]]).
- **Rational expectations for the reference price** is a disciplining assumption that "may need to be revised in some applications" (e.g., airport-sandwich or ballpark-hotdog prices perceived as abnormal).
- **Rank-based salience weighting** can make valuation non-monotonic in attributes (online Appendix C shows continuous weighting removes this), an undesirable feature in some applications.
- **Quality measurement** is delicate (the octane-vs-"regular/premium" gasoline ambiguity); the authors recommend treating quality as a *latent* variable to be estimated jointly even when proxies exist.
- The **separable, two-attribute, price-linear utility** restriction; the multi-attribute extension (Appendix B) and a gain-loss-utility version are sketched but not developed.
- Numerous predictions (Propositions 4-8, Predictions 1-2) are offered as testable but **left to future empirical work**; the authors recommend between-subject designs to avoid contaminating price expectations.

## Connections

Directly builds on the authors' own salience theory of risky choice, Bordalo, Gennaioli, and Shleifer (2012), porting overweighting of salient lottery states to overweighting of salient goods attributes. It situates itself against the reference-dependence and loss-aversion tradition ([[@Kahneman1979|Kahneman and Tversky 1979]]; Tversky and Kahneman 1991; [[@Koszegi2006b|Koszegi and Rabin 2006]], whose expectation-based reference points it adapts but replaces loss aversion with salience) and against information-theoretic accounts of decoys (Wernerfelt 1995; [[@Kamenica2008|Kamenica 2008]]). It is closest in spirit to Koszegi and Szeidl (2013) on ordering/focusing and to relative-thinking models (Azar 2007; Cunningham 2011), differing by combining ordering *with* diminishing sensitivity. Empirically it speaks to Thaler (1985, 1999) on transaction utility and mental accounting, Hastings and Shapiro (2013) on gasoline, Heath and Chatterjee (1995) and [[@Simonson1989|Simonson (1989)]]/[[@Huber1982|Huber-Payne-Puto (1982)]] on decoy/compromise effects, and the standard price-discrimination theory of sales (Varian 1980; Sobel 1984; Lazear 1986; [[@Heidhues2008|Heidhues-Koszegi 2008]]). The neuroeconomic evidence of attention-modulated attribute weighting ([[@Bernheim2009|Hare-Camerer-Rangel 2009]]; Fehr-Rangel 2011) and the "core number system" psychology (Feigenson-Dehaene-Spelke 2004) provide external grounding for the salience-weighting and homogeneity-of-degree-zero assumptions.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
