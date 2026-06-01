---
citekey: Selten1998
title: Axiomatic characterization of the quadratic scoring rule
authors: ["Selten, Reinhard"]
year: 1998
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/NLYVGQLW"
pdf: /Users/jesper/Zotero/storage/Z59SJEFT/Selten - 1998 - Axiomatic characterization of the quadratic scoring rule.pdf
tags: [literature]
keywords: [proper-scoring-rules, quadratic-scoring-rule, belief-elicitation, predictive-success, axiomatic-characterization, probabilistic-forecasting]
topics: ["[[scoring-rules-elicitability]]"]
related: [Gneiting2007]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> In the evaluation of experiments often the problem arises of how to compare the predictive success of competing probabilistic theories. The quadratic scoring rule can be used for this purpose. Originally, this rule was proposed as an incentive compatible elicitation method for probabilistic expert judgments. It is shown that up to a positive linear transformation, the quadratic scoring rule is characterized by four desirable properties.

## Summary
Selten provides an axiomatic foundation for using the quadratic scoring rule as a measure of *predictive success* when comparing competing probabilistic theories — for example, rival learning theories that each predict, for every choice situation in an experiment, a probability distribution over the available actions. The central insight is methodological: the choice of a criterion for ranking probabilistic theories is not arbitrary but can be put on an axiomatic basis, making debates about goodness-of-fit measures transparent. The paper first surveys the candidate scoring rules (linear, logarithmic, spherical, and a parametric family), shows why several are deficient, and then proves that four plausible axioms single out the quadratic rule uniquely up to positive affine rescaling. Coverage is full; this is a pure theory paper.

## Research question
Which scoring rule should be used to evaluate and compare the predictive success of probabilistic theories over discrete outcomes, and can the choice be justified non-arbitrarily? Specifically: is there a set of minimal, intuitively desirable properties that pins down a unique rule?

## Method / identification
A scoring rule $S=(S_1,S_2,\dots)$ assigns, for each predicted distribution $p=(p_1,\dots,p_n)$ over $n$ actions and each observed action $i$, a score $S_i(p)$. The **quadratic scoring rule** is
$$S_i(p) = 1 - \sum_{j=1}^{n}(\delta_{ij}-p_j)^2 = 2p_i - \sum_{j=1}^{n}p_j^2,$$
i.e. one minus the squared Euclidean distance between $p$ and the unit vector $\delta(i,n)$ representing the realized outcome as a degenerate frequency distribution. Defining the expected score $V(p\mid r)=\sum_i r_i S_i(p)$ and the expected score loss $L(p\mid r)=V(r\mid r)-V(p\mid r)$, the quadratic rule yields $L(p\mid r)=\sum_i (r_i-p_i)^2$, the squared Euclidean distance between truth $r$ and prediction $p$.

The four axioms are: **(1) Symmetry** — scores are invariant to a renumbering (permutation) of actions; **(2) Elongation invariance** — appending an impossible $(n{+}1)$th alternative with predicted probability zero does not change the scores $S_1(p),\dots,S_n(p)$ of the existing alternatives; **(3) Incentive compatibility** — the expected score loss is strictly positive for $p\neq r$, so only the true theory maximizes expected score; **(4) Neutrality** — $L(p\mid q)=L(q\mid p)$, so the penalty for predicting $p$ when $q$ is true equals the penalty for the reverse error.

The proof strategy: a *normed* scoring rule satisfies $S_1(0,1)=-1$ and $S_1(1,0)=+1$. Lemmas 2–5 show any rule satisfying axioms 1, 3, 4 is a positive linear transformation of a normed rule (the logarithmic rule fails here, since $S_1(0,1)=-\infty$). Lemmas 6–7 use symmetry and elongation invariance to fix the scores on unit vectors: $S_i(\delta(j,n))=1$ if $i=j$ and $-1$ otherwise. Lemma 8 then combines these with the neutrality identity to derive the preliminary formula $S_i(p)=2p_i-V(p\mid p)$, solves the self-referential equation to get $V(p\mid p)=\sum_j p_j^2$, and recovers $S_i(p)=2p_i-\sum_j p_j^2$ — exactly the quadratic rule.

## Data
None. This is a pure axiomatic / decision-theoretic paper; there is no empirical dataset. Its object of study is the space of scoring rules over discrete probability distributions, and its illustrations (learning experiments, weather forecasting, lottery choice) are motivational.

## Key findings
The main **Theorem**: there is one and only one normed scoring rule satisfying axioms 1–4, namely the quadratic scoring rule; equivalently, a scoring rule satisfies axioms 1–4 if and only if it is a positive linear transformation $R_i(p)=\alpha S_i(p)+\beta$ ($\alpha>0$) of the quadratic rule. Supporting results: **Lemma 1** verifies the quadratic rule satisfies all four axioms; the chain of **Lemmas 2–8** establishes uniqueness. Along the way the paper documents the deficiencies of competitors: the *linear* rule violates incentive compatibility (the highest expected score goes to a wrong deterministic theory that predicts the modal action with certainty — a point made by Brier, 1950); the *logarithmic* rule, though incentive compatible and tied to maximum likelihood, is over-sensitive to differences among tiny probabilities yet sometimes insensitive to whether the prediction is near or far from truth, and is not affinely normalizable.

## Contribution
The paper supplies the first complete axiomatic characterization of the quadratic scoring rule as a *measure of predictive success* (as opposed to merely an incentive-compatible elicitation device), recasting the choice of goodness-of-fit criterion for probabilistic theories as a justifiable decision rather than a convention. It thereby gives experimental economists a principled basis — symmetry, elongation invariance, incentive compatibility, and neutrality — for adopting the Brier/quadratic score when ranking competing stochastic models of choice and learning.

## Limitations & open questions
The characterization applies only to *fully specified* theories predicting probability distributions over a finite action set. Selten flags several open problems: (i) theories with unknown parameters require estimating those parameters to maximize the quadratic score sum, and fair comparison presupposes equal parameter counts — a model-complexity penalty is not formalized; (ii) "area theories" (Selten, 1991) predict regions of outcomes rather than distributions and need a different success measure trading precision (area smallness) against accuracy (hit rate); (iii) most pointedly, when a theory predicts a *subset of the space of probability distributions* delineated by qualitative properties (e.g. unimodality) rather than a parametric family — as in error-laden expected-utility models à la Hey and Orme (1994) — finding a reasonable measure of predictive success is left as an explicit open problem. The neutrality axiom itself is a substantive normative choice that could be contested for asymmetric-loss settings.

## Connections
The proper-scoring-rules lineage traces to Brier (1950), who introduced the quadratic rule for weather forecasting, and to Good and the logarithmic rule of Toda (1963); the spherical rule is due to Roby (1965). Foundational elicitation and evaluation work includes Winkler (1969), Murphy and Winkler (1970), Matheson and Winkler (1976), Savage's earlier characterization of proper scoring rules, and Stael von Holstein (1970) on the linear rule's defects. Friedman (1983) on effective scoring rules for probabilistic forecasts is acknowledged as a direct influence. The modern synthesis of this literature is [[@Gneiting2007|Gneiting and Raftery (2007)]], "Strictly Proper Scoring Rules, Prediction, and Estimation". Within Selten's own program, this paper complements Selten (1991) on measuring predictive success for area theories, and connects to the broader question of model comparison in discrete-choice and learning-in-games settings, where the quadratic score sum offers an incentive-compatible alternative to log-likelihood for ranking behavioral theories. The error-in-choice framework of Hey and Orme (1994) is cited as the motivating open case.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
