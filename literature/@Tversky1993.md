---
citekey: Tversky1993
title: Context-Dependent Preferences
authors: ["Tversky, Amos", "Simonson, Itamar"]
year: 1993
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/VYJ7QDW2"
pdf: /Users/jesper/Zotero/storage/JY5IWZR8/Tversky1993.pdf
tags: [literature]
keywords: [context-dependent-choice, value-maximization, attraction-effect, compromise-effect, loss-aversion, independence-of-irrelevant-alternatives, contingent-weighting]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The standard theory of choice-based on value maximization-associates with each option a real value such that, given an offered set, the decision maker chooses the option with the highest value. Despite its simplicity and intuitive appeal, there is a growing body of data that is inconsistent with this theory. In particular, the relative attractiveness of x compared to y often depends on the presence or absence of a third option z, and the "market share" of an option can actually be increased by enlarging the offered set. We review recent empirical findings that are inconsistent with value maximization, and present a context-dependent model that expresses the value of each option as an additive combination of two components: a contingent weighting process that captures the effect of the background context, and a binary comparison process that describes the effect of the local context. The model accounts for observed violations of the standard theory and provides a framework for analyzing context-dependent preferences.

## Summary

Tversky and Simonson review experimental evidence that choice violates value maximization (and hence independence of irrelevant alternatives), then propose the **componential context model**, a value representation in which an option's attractiveness is the sum of (i) a context-free additive value, (ii) a *background* contribution that re-weights attributes according to previously encountered tradeoffs, and (iii) a *local* contribution that sums the option's relative advantages against the other members of the current offered set. The model reproduces background contrast, the attraction/asymmetric-dominance effect, the compromise effect, and polarization with a single mechanism grounded in loss aversion (disadvantages loom larger than advantages).

## Research question

Can a tractable, normatively-motivated value model account for the systematic, replicable ways in which the relative attractiveness of options depends on context—both the *local* context (the current offered set) and the *background* context (options seen previously)—when classical value maximization cannot?

## Method / identification

The paper is theoretical, organized around testable choice-theoretic properties and a structural value model.

**Setup.** $T=\{x,y,z,\dots\}$ is a finite option set; the choice function $C$ maps any offered set $S\subseteq T$ to a nonempty $C(S)\subseteq S$. **Value maximization (VM)** holds if there is $v$ with $x\in C(S)\iff v(x)\ge v(y)$ for all $y\in S$. VM is the formal content of independence of irrelevant alternatives: orderings are choice-set independent, so $x\in C(S)$ and $x\in R\subseteq S$ imply $x\in C(R)$.

**Aggregate-testable consequences.** With $P(x,S)$ the share choosing $x$ from $S$, VM implies **regularity**: $x\in R\subseteq S\Rightarrow P(x,R)\ge P(x,S)$ (market share cannot rise as the set grows). Imposing a monotone, multi-attribute (vector) structure $x=(x_1,\dots,x_n)$ defines a **betweenness relation** $x\mid y\mid z$ (y lies between x and z on every attribute). VM plus a **ranking condition** then yields the **betweenness inequality** $x\mid y\mid z \Rightarrow P(y;x)\ge P_z(y;x)$, where $P_z(y;x)=\frac{P(y;x,z)}{P(y;x,z)+P(x;y,z)}$ is the popularity of y relative to x inferred from $\{x,y,z\}$. The appendix proves this implication.

**The componential context model.** Let $C_B(\cdot)$ be the choice function under background $B$. The general form is
$$C_B(S)=x \iff V_B(x,S)>V_B(y,S)\ \forall y\in S,\qquad V_B(x,S)=v(x)+\beta f_B(x)+\theta g(x,S),\ \beta,\theta\ge 0.$$
Setting $\beta=\theta=0$ recovers VM; the coefficients are expected to be positive when choices are difficult and preferences ill-articulated. Two structural assumptions sharpen it:

- **Additive value / background re-weighting.** Binary preference is additive, $v(x)=\sum_i v_i(x_i)$. Background enters via nonnegative weights $b_i$ summing to one with $f_B(x)=\sum_i b_i x_i v(x_i)$, so $v(x)+\beta f_B(x)=\sum_i \beta_i v_i(x_i)$ with $\beta_i=1+\beta b_i$—a **contingent weighting** model in which the background frontier's tradeoffs rescale attribute weights.
- **Local relative advantage.** The advantage of x over y on attribute i is $A_i(x,y)=v_i(x_i)-v_i(y_i)$ if positive, else $0$; $A(x,y)=\sum_i A_i(x,y)$. The disadvantage $D_i(x,y)=\delta_i\big(A_i(y,x)\big)$ for an increasing **convex** $\delta_i$ with $\delta_i(t)\ge t$ (loss aversion: disadvantages loom larger). The **relative advantage** is
$$R(x,y)=\frac{A(x,y)}{A(x,y)+D(x,y)}.$$
The local term sums these over the set: $g(x,S)=\sum_{y\in S}R(x,y)$ when $|S|>2$, and $0$ otherwise.

Combining gives the **componential context model**
$$V_B(x,S)=\sum_{i=1}^{n}\beta_i v_i(x_i)+\theta\sum_{y\in S}R(x,y),$$
read as a *tournament*: x is scored by its summed relative-advantage matches against each rival in S.

## Data

None original. The paper reviews prior experiments (chiefly Simonson and Tversky 1992; Huber, Payne, and Puto 1982) and reports their share statistics: e.g., tires/coupon gifts for background contrast; a $6-vs-Cross-pen plus a dominated pen lifting the pen's share from 36% to 46%; microwave ovens where a dominated $200 Panasonic raised the cheaper Panasonic's share from 43% to 60% (regularity violation); Minolta cameras where adding an extreme model made the middle option chosen by 57% (betweenness-inequality violation $P_z(y;x)-P(y;x)=0.22$, $t=3.2$); and AM-FM players showing compromise. The appendix notes the ranking condition held in every category tested.

## Key findings

- **Two behavioral hypotheses unify the anomalies.** *Tradeoff contrast*: a tradeoff looks better against backgrounds offering worse tradeoffs. *Extremeness aversion*: a natural extension of loss aversion in which an option's extreme attribute values are penalized because disadvantages outweigh advantages.
- **Background contrast** follows from the re-weighting term: a steeper background price/quality frontier shifts $\beta_i$ and hence the binary preference between equally-valued target options.
- **Attraction / asymmetric dominance** (regularity violation) arises because adding z dominated by x but not y gives $R(x,z)>R(y,z)$, so x gains more local score; asymmetric dominance is the extreme $R(\cdot,z)=1$ case.
- **Compromise effect** follows from the *convexity* of $\delta_i$: with three pairwise-equivalent options, the middle option accumulates more relative advantage than the extremes, $V(y,S)>V(x,S)$ and $V(y,S)>V(z,S)$.
- **Polarization**: if $\delta$ is strictly convex on one attribute but linear on the other, the model yields $V(x,S)>V(y,S)>V(z,S)$—a bias against one extreme only.

## Contribution

Provides a single, parsimonious, additively-structured value function nesting value maximization ($\beta=\theta=0$) that simultaneously explains background contrast, attraction, compromise, and polarization effects. It formalizes the "preferences are constructed, not revealed" view, separates background from local context as independently manipulable channels, and connects choice anomalies to loss aversion in riskless choice and to contingent weighting—giving marketers and decision theorists a framework where market shares can be reshaped by adding or deleting nominally irrelevant alternatives.

## Limitations & open questions

The authors explicitly note: (i) the model is "at best approximate and incomplete"; (ii) it does **not** model choice heuristics and editing operations (eliminating common components, discarding nonessential differences) used to simplify evaluation; (iii) it is "considerably more complicated than the standard theory," raising the paradox that a process meant to simplify choice needs a more complex descriptive model; (iv) additivity is invoked for parsimony, not as essential—non-additive alternatives expressing multiple choice in terms of binary advantages exist (Lakshmi-Ratan et al. 1991; Marley 1991) and are left uncompared; (v) most data are pooled across individuals, so the link from the individual choice function $C$ to aggregate $P$ rests on the ranking condition rather than direct individual-level tests; (vi) the failure of VM is attributed to people lacking a global preference order, an interpretation not separately identified from the model fit.

## Connections

Builds directly on the companion empirical paper Simonson and Tversky (1992, "Choice in Context") and on Huber, Payne, and Puto (1982) on asymmetric dominance / the attraction effect, and Simonson (1989) on reason-based compromise. The relative-advantage term generalizes the loss-aversion machinery of Tversky and Kahneman (1991, "Loss Aversion in Riskless Choice") and prospect theory's convex disadvantage function. The background re-weighting term is an instance of contingent weighting (Tversky, Sattath, and Slovic 1988). $R(x,y)$ is explicitly related to Restle (1961) and Tversky's (1972) elimination-by-aspects set-theoretic binary choice probabilities. Range-frequency theory (Parducci 1965; Birnbaum 1974) is considered and rejected as an alternative account (per Huber and Puto 1983; Wedell 1991). The constructed-preference theme connects to Payne, Bettman, and Johnson (1992). Additive-representation foundations draw on Krantz et al. (1971), Keeney and Raiffa (1976), and Wakker (1989).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
