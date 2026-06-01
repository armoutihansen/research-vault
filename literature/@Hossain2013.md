---
citekey: Hossain2013
title: The binarized scoring rule
authors: ["Hossain, Tanjim", "Okui, Ryo"]
year: 2013
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/W7X9KC3S"
pdf: /Users/jesper/Zotero/storage/5DKBUWUX/Hossain and Okui - 2013 - The binarized scoring rule.pdf
tags: [literature]
keywords: [proper-scoring-rules, belief-elicitation, incentive-compatibility, risk-preferences, mechanism-design, experimental-economics, non-expected-utility]
topics: []
related: [Gneiting2007, Karni2009, Offerman2009, Quiggin1982, Savage1971]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> _No abstract in source metadata; see Summary below._

## Summary

Hossain and Okui introduce the **Binarized Scoring Rule (BSR)**, a general-purpose mechanism for eliciting an agent's beliefs about a feature of a random variable that is incentive compatible *irrespective of the agent's risk preference*. The central trick is to convert a standard proper scoring rule into a binary lottery: instead of paying the agent an amount that decreases in her realized loss, the mechanism awards a preferred prize $A$ with a probability that decreases in the realized loss, and a less-preferred prize $B$ otherwise. Because the agent now faces only a choice among binary lotteries over the *same two* prizes, her objective collapses to maximizing the probability of winning $A$ — which, by construction, is achieved by reporting the belief that minimizes expected loss. Risk attitudes therefore drop out. The paper develops the theory in a general setting (Theorems 1–2), then validates it against the standard quadratic scoring rule (QSR) in two laboratory experiments. The paper is primarily a methods/mechanism-design contribution with a confirmatory experimental component (coverage: full).

## Research question

Standard proper scoring rules (e.g. the quadratic/Brier rule, de Finetti promissory notes, Savage's methods) elicit truthful beliefs only under risk-neutrality. Under risk-aversion the curvature of the agent's utility over money confounds the report: a risk-averse agent optimally shades her probability report toward $0.5$, biasing the elicited belief. The question: can one construct an elicitation mechanism that recovers the loss-minimizing report *without* assuming risk-neutrality, expected-utility maximization, or knowledge of the agent's utility function or wealth — and that works for arbitrary features (probabilities, means, quantiles), not just probabilities?

## Method / identification

This is a theory paper with a supporting experiment. Let $X$ be a random variable (scalar, vector, or even an infinite-dimensional process) and let the agent report $\theta\in\Theta$ as a prediction of some characteristic of $X$. A scalar loss function $\ell(X,\theta)\ge 0$ scores the report. **Assumption 1**: the loss is non-negative and $\arg\min_{\theta}E_X[\ell(X,\theta)]$ is well defined. The mechanism's timeline: (1) the agent reports $\theta$; (2) $X$ is realized; (3) the principal independently draws $K\sim U[0,\bar K]$; (4) the agent receives preferred prize $A$ if $\ell(X,\theta)<K$ and prize $B$ otherwise, with $A\succ B$.

The probability of winning is $P(\theta)=E_K E_X[\mathbf{1}\{\ell(X,\theta)<K\}]$. When the loss is bounded by $\bar K$, this is *negatively affine* in expected loss: $P(\theta)=1-E_X[\ell(X,\theta)]/\bar K$. The key behavioral assumption is weak: the agent's preference functional $V$ over the binary lotteries $L(p)=[A,p;B,1-p]$ need only be monotone in $p$ (a weak stochastic-dominance condition in the sense of Machina & Schmeidler (1992)). No expected-utility structure is imposed.

**Theorem 1** (main result): under Assumption 1, monotone $V$, and a bounded loss ($\ell(X,\theta)<\bar K$ for all $\theta,X$),
$$\arg\max_{\theta\in\Theta} V(L(P(\theta))) = \arg\min_{\theta\in\Theta} E_X[\ell(X,\theta)].$$
Maximizing the agent's (possibly non-expected) utility is thus equivalent to minimizing expected loss — the object the principal wants to elicit. This covers rank-dependent EU (Quiggin) and Machina's generalized-EU preferences, requiring only probabilistic sophistication and that preference under the BSR depends only on the win probability.

**Theorem 2** handles the *unbounded* case of eliciting the **mean** with quadratic loss $\ell(X,\theta)=(X-\theta)^2$. For a density $f$ with finite second moment and a light-tail condition ($|a|^{2+\delta} f(a)\to 0$), as $\bar K\to\infty$ the maximizer converges to $E_X[X]$; and if $f$ is symmetric about the mean, reporting the mean is exactly optimal even for finite $\bar K$ (proved via the first-order condition and Leibniz's rule, with a second-order check). The framework extends to multinomial probabilities, medians ($|x-md|$ loss), and $\alpha$-quantiles via the pinball loss, paralleling the family in [[@Gneiting2007|Gneiting & Raftery (2007)]].

The experimental design compares BSR against QSR within-subject across periods; the performance metric is the **negative squared deviation (NSD)** between report and the objective (true) value. Inference uses heteroskedasticity- and autocorrelation-robust standard errors, with subjects treated as independent and observations correlated over periods.

## Data

Original laboratory data from two experiments programmed in z-Tree (Fischbacher 2007). The **P-experiment** (probability elicitation: probability that a ball drawn from an urn is a specified color) ran at Hokkaido University, Japan (July 2010); after dropping 30 outlier observations failing a "betweenness" criterion, it yields a panel of 276 observations from 151 subjects. The **M-experiment** (mean elicitation from noisy signals about a random variable's realized value) ran at Hong Kong University of Science and Technology (June 2009), 2436 observations. All subjects were undergraduates. Objective probabilities/means are known by design, providing a ground-truth benchmark.

## Key findings

- **Theorem 1**: the BSR is incentive compatible for the full class of stochastic-dominance-monotone preferences — including major non-expected-utility theories — needing no assumption on utility curvature or initial wealth.
- **Theorem 2**: the BSR validly elicits the mean even under an unbounded quadratic loss, exact for symmetric distributions and asymptotically exact otherwise.
- **P-experiment**: subjects report probabilities significantly closer to the truth under the BSR than the QSR. The gap is driven by *risk-averse* subjects and is larger for *extreme* true probabilities (far from $0.5$); the BSR–QSR interaction with distance-from-$0.5$ is positive. For risk-neutral subjects the two rules do not differ, exactly as theory predicts.
- **M-experiment**: behavior does not differ significantly across the two schemes — consistent with the paper's theory and with Bhattacharya & Pfleiderer (1985), since the mean-elicitation problem is less sensitive to risk attitudes when payoff mean/variance are equalized by design.
- The results *contradict* Selten et al. (1999), who found binary-lottery payoffs perform worse than money prizes; the authors reconcile this via the "background risk" hypothesis, noting their design equalizes payoff variance across schemes.

## Contribution

A single, parsimonious mechanism that makes belief elicitation robust to unknown risk preferences and to departures from expected utility, while remaining simple (one layer of randomization). It generalizes any proper scoring rule and extends to means, medians, and quantiles — broader than the contemporaneous, independently-derived probabilistic QSR of Schlag & van der Weele (2009), and simpler than the lottery mechanisms of [[@Karni2009|Karni (2009)]] and Qu (2012), which need extra randomization and resist extension beyond probabilities. The BSR has become a workhorse for incentive-compatible belief elicitation and for paying experimental subjects when risk-neutrality cannot be assumed.

## Limitations & open questions

- **Probabilistic sophistication is still required**: the mechanism fails for agents whose preferences violate monotonicity in winning probability or who are not probabilistically sophisticated; characterizing behavior for such agents is left open.
- **Single-task validity**: incentive compatibility is established for one report; eliciting a *sequence* of beliefs or running multiple BSR tasks together (portfolio/hedging across decisions, cf. Azrieli, Chambers & Healy 2012) is flagged but not solved here.
- **Residual reporting noise**: even under the BSR, reports scatter around the truth — the "capriciousness" the authors note suggests an unmodeled stochastic-choice layer.
- **Parameter choice of $\bar K$ and prizes $A,B$**: the practical sensitivity of elicited beliefs to the support of $K$ and the prize spread (especially in the unbounded mean case) is not systematically explored.
- The cleaner, more demanding test would isolate non-EU agents; the experiments confirm direction but the effect sizes are modest (low adjusted $R^2$).

## Connections

The mechanism modifies the classic proper scoring rules of Brier (1950), [[@Savage1971|Savage (1971)]], and de Finetti (1974), and inherits the loss-function taxonomy (mean, median, quantile) catalogued by [[@Gneiting2007|Gneiting & Raftery (2007)]]. It is closest to, and independent of, Schlag & van der Weele (2009), and is an alternative to the binary-lottery elicitation of [[@Karni2009|Karni (2009)]], its extension by Qu (2012), and the empirical comparisons by Hao & Houser (2012) and Hollard, Massoni & Vergnaud (2010). It speaks to the risk-correction approach of Offerman, Sonnemans, van de [[@Offerman2009|Kuilen & Wakker (2009)]] and the joint risk-and-belief estimation of Andersen et al. (2010), and rebuts Selten, Sadrieh & Abbink (1999). The weak-preference foundation draws on Machina (1982), [[@Quiggin1982|Quiggin (1982)]], and Machina & Schmeidler (1992); the logic links to the Becker–DeGroot–Marschak (1964) probabilistic-reward idea. The BSR is directly relevant to incentivizing experiments on social preferences and choice modeling where subject risk attitudes would otherwise confound elicited beliefs.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
