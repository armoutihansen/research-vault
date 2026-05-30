---
citekey: vanWezel2007
title: Improved customer choice predictions using ensemble methods
authors: ["van Wezel, Michiel", "Potharst, Rob"]
year: 2007
type: journalArticle
doi: 10.1016/j.ejor.2006.05.029
zotero: "zotero://select/library/items/RG3HJ8UA"
pdf: /Users/jesper/Zotero/storage/F3AWDZN8/vanWezel2007.pdf
tags: [literature]
keywords: [ensemble-learning, brand-choice, bias-variance-decomposition, decision-trees, boosting, bagging, choice-modeling]
topics: []
related: [Heskes1998]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> In this paper various ensemble learning methods from machine learning and statistics are considered and applied to the customer choice modeling problem. The application of ensemble learning usually improves the prediction quality of flexible models like decision trees and thus leads to improved predictions. We give experimental results for two real-life marketing datasets using decision trees, ensemble versions of decision trees and the logistic regression model, which is a standard approach for this problem. The ensemble models are found to improve upon individual decision trees and outperform logistic regression.

## Summary
Van Wezel & Potharst recast brand-choice modeling as a multi-class classification problem and show that ensemble learning (Bagging, LogitBoost, MultiBoost) applied to CART decision trees beats both a single tree and the standard logistic-regression benchmark on two real marketing datasets. They then explain *why* using James's (2003) general-loss bias/variance decomposition: trees are low-bias/high-variance, logistic regression is high-bias/low-variance, and ensembles cut the variance term while leaving bias essentially untouched. This is, by their account, the first application of the bias/variance decomposition to a brand-choice problem.

## Research question
Can ensemble (committee) learning methods from machine learning improve out-of-sample prediction of customer brand choice over the standard logistic-regression approach, and can the bias/variance decomposition of prediction error explain when and why such improvements occur?

## Method / identification
A choice model is treated as a classifier mapping a feature vector $x$ (customer, product and situation attributes) to one of $K$ disjoint brands. Class-membership probabilities $f_k(x\mid\theta)=p_k(x)=P(C_k\mid x)$ are scored under two losses: zero–one loss $\sum_n I(\text{predicted},\text{actual})$ and cross-entropy (negative multinomial log-likelihood) $E(T\mid\theta)=-\sum_n\sum_k z_{nk}\log f_k(x_n\mid\theta)$.

Two base learners are used. Logistic regression with the softmax form $f_k(x\mid\theta)=\exp(w_k^\top x)/\sum_{k'}\exp(w_{k'}^\top x)$ gives linear decision boundaries $(w_a-w_b)^\top x=0$. CART builds a recursive binary partition $f_k(x\mid\theta)=\sum_i p_{ik}\,\chi_{R_i}(x)$ over rectangular regions.

Three ensembles are built on top: (i) **Bagging** — average $f_{T_t}$ trained on bootstrap resamples $T_1,T_2,\dots$ of equal size (voting under zero–one loss, plain averaging under cross-entropy); (ii) **LogitBoost** (Friedman et al.), which boosts on the logit scale $G_k(x)=\sum_m g_{mk}(x)$ with inverse-link $p_k(x)=e^{G_k(x)}/\sum_k e^{G_k(x)}$, using regression trees as base models and giving calibrated multi-class probabilities; (iii) **MultiBoost** (Webb), combining wagging (random weights) with LogitBoost, splitting $M$ base models into $\lceil\sqrt{M}\rceil$ wagged sub-ensembles.

The explanatory framework is James's bias/variance decomposition for general loss. With average model $f^A(x)=\arg\min_\mu E_T[L(f_T(x),\mu)]$ and optimal model $f^*(x)=\arg\min_\mu E_y[L(y,\mu)\mid x]$, the systematic effect (bias) is $SE(f)=E_{y,x}[L(y,f^A(x))-L(y,f^*(x))]$ and the variance effect is $VE(f)=E_{y,x,T}[L(y,f_T(x))-L(y,f^A(x))]$, yielding the additive split $PE(f)=\text{irreducible}+SE(f)+VE(f)$. For convex loss (cross-entropy) Jensen's inequality makes $VE\geq 0$, so aggregation cannot hurt; for non-convex zero–one loss $VE$ can be negative.

## Data
Two product categories from the ERIM scanner-panel database (A.C. Nielsen, two Midwestern U.S. cities): ketchup (3 brands, 32 oz) and peanut butter (6 brands, 18 oz). Features ($3+5K$ inputs): day of week, plus per-brand loyalty, reference price, price, display and ad indicators, plus household income and size; target is chosen brand. Loyalty is exponentially smoothed past purchases $l_t^{hk}=\alpha l_{t-1}^{hk}+(1-\alpha)y_{t-1}^{hk}$ with $\alpha=0.15$; reference price is analogously smoothed. Only households with $\geq 10$ purchases are kept; first four purchases initialize the smoothed variables. Evaluation uses twofold cross-validation, 25 runs per fold.

## Key findings
- On **ketchup**, MultiBoost CART is best (21.60% error), then Boost CART (21.77%), bagged CART (23.79%); logistic regression scores 25.02%, so the standard model is ~16% worse than MultiBoost.
- On **peanut butter**, bagged CART is best (43.88%) versus single CART 51.86% — an ~18% reduction; MultiBoost (44.23%) is close; logistic regression (45.85%) is only ~4.5% worse here.
- Wilcoxon signed-rank tests (Bonferroni-corrected) confirm ensembling significantly improves CART on both datasets, but **never** improves logistic regression — because a linear combination of linear models is still linear.
- Bias/variance decomposition (Table 4, intrinsic noise set to zero) shows the mechanism: for peanut-butter zero–one loss the CART variance effect falls from 8.62 (single) to 1.57 (bagged) while the systematic effect stays ~42–43; logistic regression has high bias (~45) and tiny variance (~0.4–0.6), explaining why ensembling does nothing for it.
- Ensembles help precisely on instances where the individual CART models disagree (illustrated in Table 3). A noted side effect: MultiBoost can increase confusion between two variants of the same manufacturer's brand even as overall accuracy rises.
- Appendix A derives the decomposition for both losses; under cross-entropy the average model is just the per-class average of base-model probabilities, under zero–one loss it corresponds to majority voting (Bayes error rate is the irreducible term).

## Contribution
First application of the general-loss bias/variance decomposition to a brand-choice problem, extending prior ensemble-in-marketing work (Hu's stacking; Lemmens & Croux's churn trees) to a genuinely multi-class (non-binary) choice setting and to LogitBoost/MultiBoost. The paper also frames the decomposition as a diagnostic tool: a parametric choice model (e.g. multinomial logit) showing high bias relative to a flexible learner signals that the theory-derived model misrepresents the true choice process.

## Limitations & open questions
- Improvements are "noticeable but not overwhelming," attributed to high intrinsic noise in the ERIM data; the authors conjecture larger 30–50% gains on cleaner data.
- Intrinsic noise is assumed zero, inflating the systematic-effect estimates; estimating it (e.g. via neighboring inputs, as in James) is left open.
- Only twofold CV (computational cost); richer resampling untested.
- Interpretability tools (relative-importance and partial-dependence plots) for ensembles were not produced due to software limits.
- Explicit further-research hook: determine **which regions of feature space / which marketing-variable values produce high inter-model variance**, since $SE$ and $VE$ can be localized to subsets of the feature space.
- SVMs and neural networks as base learners were excluded for scope/compute and remain candidates.

## Connections
Methodologically rooted in Breiman (1996) on Bagging and Bagging predictors, Freund & Schapire (1996, 1997) on Boosting/AdaBoost, and Friedman, Hastie & Tibshirani (2000) on LogitBoost (additive logistic regression); MultiBoost follows Webb (2000) and the bias/variance theory follows Breiman (1996, 1998), James (2003), [[@Heskes1998|Heskes (1998)]] and Domingos (2000), with Geman, Bienenstock & Doursat (1992) for the classical squared-error case. Within marketing it extends Hu & Tsoukalas (2003) on stacked generalization and Lemmens & Croux (2006) on bagging/boosting trees for churn from binary to multi-class choice. The choice-modeling baseline connects to McFadden (1973) conditional logit and the IIA critique, the Guadagni & Little (1983) loyalty-smoothing brand-choice model, reference-price work by Kalyanaram & Winer (1995), and the flexible neural brand-choice model of Hruschka et al. (2002). Tools and background draw on Breiman et al. (1984) CART and Hastie, Tibshirani & Friedman (2001).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
