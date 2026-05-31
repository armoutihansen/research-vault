---
citekey: Matthey2008
title: "Yesterday's Expectation of Tomorrow Determines What You Do Today: The Role of Reference-Dependent Utility from Expectations"
authors: ["Matthey, Astrid"]
year: 2008
type: journalArticle
doi: 10.2139/ssrn.920997
zotero: "zotero://select/library/items/7ILGUHTV"
pdf: /Users/jesper/Zotero/storage/6NR5YMSY/Matthey2008.pdf
tags: [literature]
keywords: [reference-dependent-utility, expectations, anticipatory-utility, loss-aversion, personal-equilibrium, habituation]
topics: ["[[anticipatory-utility-motivated-beliefs]]"]
related: [Benartzi1995, Brunnermeier2005, Caplin2001, Kahneman1979, Koszegi2006a, Koszegi2006b, Loewenstein1987]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The paper introduces the concept of adjustment utility, that is, reference-dependent utility from expectations. It offers an explanation for observed preferences that cannot be explained with existing models, and yields new predictions for individual decision making. The model gives a simple explanation for, e.g., why people are reluctant to change their plans even when these turn out to be unexpectedly costly; people's aversion towards positive but false information, which cannot be explained with previous models; and the increasing acceptance of risks when people get used to them.

## Summary

Matthey introduces *adjustment utility*: reference-dependent utility derived not from realized outcomes but from *expectations* of future outcomes. The pleasure or pain of anticipating a future state depends on a *reference expectation* one held earlier, so preferences become path-dependent in expectations. Survey evidence motivates the construct, a formal model embeds it alongside expected, prospect-theoretic and anticipatory utility, and the framework rationalizes three otherwise puzzling phenomena: reluctance to abandon costly plans, habituation to risk, and aversion to positive-but-false information.

## Research question

Do *past expectations* influence the utility an individual currently derives from her *present* expectations of the future, even when current and expected outcomes are identical across situations? Existing utility concepts (expected utility, prospect theory, anticipatory utility) predict no difference in such cases; the paper asks whether a fourth, reference-dependent-on-expectations component is needed, and what it predicts for decision making.

## Method / identification

The paper combines two classroom surveys with a formal model. The model places adjustment utility in a 2x2 taxonomy of utility components: absolute vs. relative (reference-dependent), crossed with utility from *realized outcomes* vs. utility from *expectations*. The three existing cells are vNM expected utility $u^{o}(x)$, prospect-theory relative utility $v^{o}(x\mid r)$, and Caplin-Leahy anticipatory utility $u^{a}(p^{c})$; the new cell is adjustment utility $v^{a}(p^{c}\mid p^{r})$.

An individual in period $t$ chooses an action inducing a probability distribution $p^{c}\in P$ over outcomes $X$ realized at $T>t$. Adjustment utility is defined axiomatically by a function $v^{a}:P\times P\to\mathbb{R}$ satisfying: A1 $v^{a}(p^{c}\mid p^{c})=0$ (no gain/loss against one's own reference); A2 monotonicity in the anticipated distribution, $v^{a}(p^{y}\mid p^{r})\ge v^{a}(p^{z}\mid p^{r})$ whenever $p^{y}\succeq p^{z}$; A3 *negative* dependence on the reference, $v^{a}(p^{c}\mid p^{r})\ge v^{a}(p^{c}\mid p^{r'})$ for all $p^{r'}\succeq p^{r}$ (a worse reference makes any given anticipation feel better). Overall utility of action $y$ aggregates all four components over the periods until realization:

$$U(y)=\sum_{l=t}^{T-1}\bigl[u^{a}_{l}(p^{y})+v^{a}_{l}(p^{y}\mid p^{r}_{l})\bigr]+u^{o}(x)+v^{o}(x\mid r).$$

The reference expectation $p^{r}_{i,t}=p^{r}_{i,t}(p_{i,s};p_{-i,s};\beta)_{s<t}$ is built from the individual's own past expectations $p_{i,s}$ and her past expectations of relevant others $p_{-i,s}$, mentally discounted by $\beta\in[0,1]$ so that distant expectations matter less; it rises with better expected own and others' states. The author then ports [[@Koszegi2006a|Koszegi-Rabin (2006)]] personal equilibrium to expectations, contrasting an *outcome personal equilibrium* (OPE, outcomes only) with an *expectation personal equilibrium* (EPE) that internalizes anticipatory and adjustment utility, and analyzes repeated choice and a priced consumption decision. Proofs are in the appendix.

## Data

Two hypothetical classroom surveys at TU Berlin, 2006. Survey 1 ("own", $n=47$) varied the path of expectations about one's own wage (a falsely promised then retracted raise vs. no news); Survey 2 ("others", $n=78$) varied expectations about colleagues' wages. Utility was elicited at the moment expectations had re-converged across conditions, isolating the path effect. Responses are hypothetical, not incentivized, by design (incentivizing would reveal the later expectation change and destroy the manipulation). Empirical support beyond surveys is anecdotal: German HIV-infection and condom-use statistics, 1997-2004 (appendix A).

## Key findings

Surveys: a large majority judged the individual *happier when never given false good news* — about 94% in Survey 1 and 78% in Survey 2 chose the no-prior-elevated-expectation situation; the uniform-noise null is rejected at $p=0.000$ (binomial test). This identifies path dependence in expectations and shows the reference expectation rises with both past own and past others' expectations.

Model results. *Corollary 1* gives an explicit condition under which the EPE action differs from the preferred OPE action, formalizing why one may stick to a costly plan (e.g., keep working toward a prestigious job, or buy increasingly pricey shoes) to avoid the felt loss of downgrading a pleasant expectation. *Proposition 1*: for a loss-averse individual who first chooses action $y$ in $t$, the net utility from $y$ is higher in $t+1$ than in $t$ — habituation, because $p^{y}$ enters the reference expectation and, with $v^{a}$ steeper for losses than gains, repeated exposure raises the relative payoff of the action (rationalizing rising risk acceptance, e.g., declining condom use). *Proposition 2*: in a priced consumption problem with a cheaper risky action $y$ ($p^{y}\prec 0$), once $y$ is chosen at $t$, $EU_{t+1}(y)-EU_{t+1}(z)>EU_{t}(y)-EU_{t}(z)$ — the trade-off tilts toward the risky option as its expectation is absorbed into the reference. Value-of-information analysis: positive false information later corrected can yield *negative* net utility, $\Delta U<0$ when terms III+IV (post-correction disappointment) dominate I+II (initial elation), more likely the more loss-averse the agent; negative false information always reduces utility, matching existing models.

## Contribution

It is the first formal treatment of reference dependence applied to utility *from expectations* (distinct from prospect theory's reference dependence over *realized* outcomes), completing the 2x2 taxonomy of utility components. It supplies survey evidence for the construct, an axiomatic definition, a reference-formation rule with own/social inputs and mental discounting, and an EPE solution concept yielding falsifiable predictions on plan persistence, habituation, and aversion to false good news. It also derives firm-pricing implications (penetration pricing of risky goods like GM food to erode reference expectations, then raising prices) and regulatory implications of habituation-driven rising risk acceptance.

## Limitations & open questions

The author is explicit: (1) survey evidence is hypothetical, not incentivized, so the construct needs stronger experimental substantiation; (2) empirical support is so far only anecdotal (HIV/condom data), and the model's predictions await tests on micro consumption data — GM-product introductions are proposed as a natural test of the penetration-pricing prediction. A deeper theoretical open problem (Section 6): the reference expectation is *exogenous* in general and cannot be fully endogenized, because gradual, continuous reference adjustment ($\Delta\to 0$) means the reference is always partly pinned by prior, exogenous expectations except when fully adjusted with no news arriving; even leaving initial unawareness fixes it exogenously at zero. Open questions include when the individual vs. social component dominates, the speed of reference adjustment, and the role and interaction of other candidate anchors such as aspiration levels.

## Connections

The taxonomy builds directly on von Neumann & Morgenstern (1944), [[@Kahneman1979|Kahneman & Tversky (1979)]] prospect theory, and [[@Caplin2001|Caplin & Leahy (2001)]] anticipatory utility. The closest relative is [[@Koszegi2006b|Koszegi & Rabin (2006)]], whose expectations-based reference points and personal-equilibrium concept are adapted here into EPE, and who independently study optimal consumption plans under adjustment-like utility; Sugden (2003) similarly uses stochastic expectation-based reference points over realized outcomes. The work draws on [[@Loewenstein1987|Loewenstein (1987)]] on anticipation/anxiety and [[@Brunnermeier2005|Brunnermeier & Parker (2005)]] and Koszegi (2005) on belief-based utility, and on Kimball & Willis (2006) for an informal treatment of utility from expectation changes. Reference-state evidence for realized outcomes is cited from Kahneman, Knetsch & Thaler (1990/1991) on the endowment effect and [[@Benartzi1995|Benartzi & Thaler (1995)]] on the equity premium puzzle, with habit-formation parallels in Campbell & Cochrane (1999), Abel (1990) and Constantinides (1990). Plan persistence is contrasted with time-inconsistency models (Laibson, 1997), and the empirical reference-adjustment speed assumption rests on the author's companion work Matthey & Dwenger (2007) and earlier Matthey (2005, 2006).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
