---
citekey: Karni2009
title: A mechanism for eliciting probabilities
authors: ["Karni, Edi"]
year: 2009
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/UV7U6ABA"
pdf: /Users/jesper/Zotero/storage/2VS5P4QS/Karni - 2009 - A mechanism for eliciting probabilities.pdf
tags: [literature]
keywords: [belief-elicitation, subjective-probability, proper-scoring-rules, mechanism-design, incentive-compatibility, probabilistic-sophistication]
topics: ["[[experimental-belief-elicitation]]"]
related: [Gneiting2007, Savage1971]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> This paper describes a direct revelation mechanism for eliciting agents' subjective probabilities. The game induced by the mechanism has a dominant strategy equilibrium in which the players reveal their subjective probabilities.

## Summary
Karni proposes a simple direct revelation mechanism for eliciting an agent's subjective probability of an event $E$ that, unlike the proper scoring rule and promissory-note methods, decouples the *accuracy* of the elicited estimate from the *strength of incentives* used to obtain it. The agent reports his subjective probability $\mu\in[0,1]$ of $E$. A random number $r$ is drawn uniformly on $[0,1]$. If $\mu\ge r$ the agent receives a fixed bet $\beta:=x_E y$ (pays $x$ if $E$ obtains, $y$ otherwise, $x>y$); if $\mu<r$ he receives the lottery $(r,x,y)$ paying $x$ with probability $r$. Truthful reporting $\mu=\pi(E)$ is the *unique dominant strategy*. The central insight: because the report is rewarded by comparing a bet on $E$ against an objective lottery, only probabilistic sophistication and a dominance condition are required — risk attitude washes out, so the payoff difference $x-y$ can be made arbitrarily large to motivate costly information acquisition without biasing the elicited probability. This four-page Econometrica note is foundational for the experimental and decision-theory literature on belief elicitation.

## Research question
How can one elicit an agent's subjective probability of an event in which the agent has no stake, *accurately* and *incentive-compatibly*, while allowing the experimenter to set the monetary incentives at any desired level? Existing methods force a trade-off: proper scoring rules and de Finetti's promissory notes confound the elicited probability with the agent's marginal utility (risk attitude) unless incentives are vanishingly small; the lotteries method of Kadane & Winkler (1988) is not incentive compatible at all.

## Method / identification
This is a decision-theory / mechanism-design paper; the "identification" is a dominant-strategy argument. Let $S$ be a state space, events being subsets of $S$. A bet on $E$ is a simple act $x_E y$ paying $x$ if $E$ obtains and $y\ (<x)$ otherwise. A simple lottery $(p,x,y)=[x,p;y,(1-p)]$ pays $x$ with probability $p$. Let $\succeq$ be a preference relation on the union $D$ of acts and lotteries. Two assumptions are imposed: (i) **probabilistic sophistication** (Machina & Schmeidler, 1995) — acts are ranked solely by their implied outcome distributions, with implicit probability measure $\pi$; (ii) **dominance** — $(p,x,y)\succeq(p',x,y)$ for all $x>y$ iff $p\ge p'$.

The mechanism: draw $r\sim U[0,1]$; agent reports $\mu$; award $\beta=x_E y$ if $\mu\ge r$, else award $(r,x,y)$.

Truth-telling dominates by case analysis. Suppose the agent over-reports, $\mu>\pi(E)$. If $r\le\pi(E)$ or $r\ge\mu$ the payoff is identical to truthful reporting. The only consequential region is $r\in(\pi(E),\mu)$: reporting $\mu$ yields $\beta$, whereas reporting $\pi(E)$ would yield $(r,x,y)$; since $r>\pi(E)$, probabilistic sophistication and dominance give $(r,x,y)\succ\beta$, so over-reporting is strictly worse. The symmetric argument rules out under-reporting. Hence $\mu=\pi(E)$ is the unique dominant strategy. Karni notes an equivalent **auction representation**: a continuous increasing-bid (clock) auction between the agent and a dummy bidder who stays in until the price reaches $r$; the agent's dominant strategy is to remain until the bid equals $\pi(E)$ — a Becker–DeGroot–Marschak-style construction. The mechanism extends to many agents (run separately, or substitute the highest report for $r$, cf. Karni (2008)) and to finitely many events.

To contrast with scoring rules, Karni formalizes the scoring-rule problem with random wealth $\tilde w$ (distributed independently of $E$, consistent with the no-stake requirement) and shows the first-order condition
$$\frac{\mu^*(r)}{1-\mu^*(r)}=\frac{K(r)\,\pi(E)}{1-\pi(E)},$$
where $K(r)$ is a ratio of expected marginal utilities conditional on $E$ and $E^c$. Thus $\mu^*(r)=\pi(E)$ iff $K(r)=1$, which holds only under risk neutrality; otherwise the scoring rule confounds probabilities and marginal utilities.

## Data
None. This is a pure theory note with no empirical data, experiment, or simulation; the analysis is entirely analytical.

## Key findings
- **Main result (truthful dominant strategy):** under probabilistic sophistication and dominance, the proposed mechanism has truth-telling $\mu=\pi(E)$ as the *unique* dominant strategy, for *any* payoff difference $x-y$.
- **Separation of incentives and accuracy:** because the report is rewarded by comparing a bet on $E$ to an objective lottery, the elicited probability is invariant to the agent's risk attitude. The experimenter may scale $x-y$ up to induce costly effort in forming an accurate assessment, with no resulting bias.
- **Diagnosis of scoring-rule bias:** for a risk-averse agent with $\pi(E)\ne 1/2$, the scoring-rule estimate $\mu^*(r)$ is biased toward $1/2$, and the bias *increases* in the incentive scale $r$; risk-inclined agents are biased toward $0$ or $1$. Obtaining an unbiased scoring-rule estimate requires $r\to 0$, which destroys the incentive to deliberate. de Finetti's promissory-note method shares this defect.
- **Auction equivalence:** the elicitation problem maps onto a clock auction against a random-cutoff dummy bidder, an alternative practical implementation.

## Contribution
Karni delivers a clean construction: a probability-elicitation mechanism that is simultaneously incentive compatible (dominant-strategy), accurate (risk-attitude-free under probabilistic sophistication), and free to use arbitrarily strong incentives. It relaxes the demands on preferences from subjective expected utility to the weaker probabilistic sophistication, and reframes belief elicitation as a direct revelation / BDM-style auction problem. It is widely cited as a theoretical foundation for incentive-compatible belief elicitation in experimental economics.

## Limitations & open questions
- **No-stake assumption is essential.** Accuracy depends critically on the agent having no stake in $E$. With a stake, payoff evaluations become event-dependent and probabilistic sophistication fails; Karni points to Jaffray & Karni (1999) and Karni (1999) for state-dependent extensions, leaving open how to combine those with the present mechanism.
- **Probabilistic sophistication and dominance are maintained hypotheses**, not tested. Agents exhibiting ambiguity aversion or non-probabilistically-sophisticated preferences (Ellsberg-type) are outside the result; whether a robust analogue exists under maxmin/Choquet preferences is open.
- **Effort/deliberation is informal.** The claim that a large $x-y$ "induces effort" toward an accurate assessment is asserted, not modeled; a formal cost-of-information / rational-inattention treatment of when and how much the agent deliberates is left open.
- **Behavioral robustness untested.** Whether real subjects play the dominant strategy (cf. known violations of BDM and reduction-of-compound-lottery axioms) is an empirical question the note does not address.
- **Continuous-report implementability** in the lab (eliciting $\mu\in[0,1]$ and the clock-auction variant) and the many-agent endogenous-$r$ design (Karni, 2008) invite further mechanism-design analysis.

## Connections
This note sits at the intersection of proper scoring rules and incentive-compatible elicitation. It directly contrasts with the proper scoring rule method of [[@Savage1971|Savage (1971)]] and [[@Gneiting2007|Gneiting & Raftery (2007)]], and with the promissory-note method of de Finetti (1974), arguing both confound beliefs with marginal utility away from risk neutrality. It builds on the lotteries method of Kadane & Winkler (1988), which it generalizes into an incentive-compatible form. The required preference structure is probabilistic sophistication in the sense of Machina & Schmeidler (1995). The implementation is closely related to the Becker–DeGroot–Marschak mechanism for eliciting valuations. The handling of stakes and state-dependence connects to Jaffray & Karni (1999) and Karni (1999), and the many-agent extension to Karni (2008). It is a natural reference for experimental belief-elicitation designs and links to the broader literature on subjective expected utility and decision under uncertainty.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
