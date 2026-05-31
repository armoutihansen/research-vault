---
citekey: Fudenberg2020b
title: Machine learning for evaluating and improving theories
authors: ["Fudenberg, Drew", "Liang, Annie"]
year: 2020
type: journalArticle
doi: 10.1145/3440959.3440962
zotero: "zotero://select/library/items/VZ5RHT66"
pdf: /Users/jesper/Zotero/storage/2P4FIMAU/Fudenberg2020a.pdf
tags: [literature]
keywords: [machine-learning, economic-theory, model-completeness, model-restrictiveness, prospect-theory, cognitive-hierarchy, experimental-design]
topics: ["[[ml-evaluating-economic-theories]]"]
related: [Fudenberg2019a, Fudenberg2020]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We summarize our recent work that uses machine learning techniques as a complement to theoretical modeling, rather than a substitute for it. The key concepts are those of the completeness and restrictiveness of a model. A theory's completeness is how much it improves predictions over a naive baseline, relative to how much improvement is possible. When a theory is relatively incomplete, machine learning algorithms can help reveal regularities that the theory doesn't capture, and thus lead to the construction of theories that make more accurate predictions. Restrictiveness measures a theory's ability to match arbitrary hypothetical data: A very unrestrictive theory will be complete on almost any data, so the fact that it is complete on the actual data is not very instructive. We algorithmically quantify restrictiveness by measuring how well the theory approximates randomly generated behaviors. Finally, we propose "algorithmic experimental design" as a method to help select which experiments to run.

## Summary
This SIGecom Exchanges survey synthesizes Fudenberg and Liang's research program on using machine learning as a *complement* to economic theory rather than a substitute. Two diagnostic measures organize the agenda: **completeness** (how much of the achievable predictive improvement a theory captures, benchmarked against a nonparametric black box) and **restrictiveness** (how strongly a theory's functional form rules out arbitrary behaviors). A theory that is both highly complete and highly restrictive is genuinely capturing real regularities; high completeness with low restrictiveness merely reflects flexibility. The authors then propose **algorithmic experimental design**: using ML to select test cases where a theory is likely to fail, generating data that reveals new regularities. Worked examples are risk preferences (Cumulative Prospect Theory) and initial play in matrix games (Poisson Cognitive Hierarchy).

## Research question
How can black-box machine learning, which predicts well but offers little interpretive insight, be harnessed to *evaluate* and *improve* interpretable economic theories? Specifically: (i) How do we measure whether a theory's predictive shortfall leaves room for improvement? (ii) How do we tell whether a theory's good fit reflects real structure or mere flexibility? (iii) How should an experimenter choose which new instances to collect?

## Method / identification
The formal setup: an observable feature vector $x \in X$ and outcome $y \in Y$, with data pairs $z_i = (x_i, y_i)$. A *predictive mapping* is any $f: X \to Y$; a parametric model is a family $F_\Theta = \{f_\theta\}_{\theta \in \Theta}$ with $\Theta$ finite-dimensional, closed and compact. Predictions are scored by a loss $\ell: Y \times Y \to \mathbb{R}$ (MSE $(y'-y)^2$ or misclassification $\mathbf{1}(y' \ne y)$). Expected prediction error is $E_P(f) = E_P[\ell(f(x), y)]$, and a model's error is $E_P(f_\Theta^\ast)$ at the error-minimizing rule $f_\Theta^\ast = \arg\min_{f \in F_\Theta} E_P(f)$.

Three benchmarks anchor the analysis: a naive rule $f_n$ (expected value for lotteries; uniform play for games), the best in-class rule $f_\Theta^\ast$, and the ideal/irreducible rule $f^\ast(x) = \arg\min_{y' \in Y} E_P[\ell(y', y) \mid x]$ (the conditional mean under MSE), estimated by a nonparametric black box. **Completeness** is the fraction of achievable error reduction attained:
$$\frac{E_P(f_n) - E_P(f_\Theta^\ast)}{E_P(f_n) - E_P(f^\ast)}.$$

**Restrictiveness** is operationalized by sampling random *permissible* mappings $f$ from a set $F_M$ (e.g., all monotone certainty-equivalent maps) under an analyst-chosen prior $\mu$, then measuring how well $F_\Theta$ approximates them. With distance $d(f, f') = E_{P_X}[\ell(f(x), f'(x))]$ and $d(F_\Theta, f) = \inf_{f' \in F_\Theta} d(f', f)$, restrictiveness is
$$r := E_\mu\!\left[\frac{d(F_\Theta, f)}{d(f_n, f)}\right] \in [0,1],$$
where $r = 1$ means the model barely beats naive on random maps (very restrictive) and $r = 0$ means it spans all of $F_M$ (unrestrictive). **Algorithmic experimental design** trains an ML predictor of the theory's predicted action frequency, then selects instances with low predicted frequency, generating adversarial test cases for new data collection.

## Data
Two reused datasets. (1) **Risk preferences**: Bruhin, Fehr-Duda and Epper (2010) certainty equivalents for 25 binary lotteries $(z, \underline{z}, p)$; model is 3-parameter CPT $f_\theta = w(p)v(z) + (1-w(p))v(\underline{z})$ with $w(p) = \delta p^\gamma / (\delta p^\gamma + (1-p)^\gamma)$ and $v(z) = z^\alpha$. (2) **Initial play**: Wright and Leyton-Brown (2014) compilation of play in 86 unique $3\times 3$ normal-form games; model is the 1-parameter Poisson Cognitive Hierarchy Model. New data were elicited on Mechanical Turk for the algorithmically-designed games.

## Key findings
- CPT is **nearly complete** (91% of feasible error reduction; absolute error 64.92 vs naive 98.32, irreducible 61.64). PCHM reaches **76%** completeness, with the 0-parameter Level-1 model the best PCHM variant.
- Inspecting the 14 of 86 games where a bagged decision tree predicted correctly but Level-1/PCHM did not revealed players favoring an "almost level-1" action with lower payoff variance. Adding one risk-aversion parameter via $f(u) = u^\alpha$ yields the **level-1($\alpha$)** model, which weakly *beats* the decision-tree ensemble — ML guided discovery of an interpretable, portable model extension.
- Restrictiveness sharply distinguishes the two complete models: CPT has $r = 0.25$ (approximates random maps four times better than naive), whereas level-1($\alpha$) has $r = 0.91$ (highly restrictive). Since level-1($\alpha$) is restrictive *and* complete, its fit reflects genuine structure rather than flexibility.
- Algorithmic experimental design successfully generated $3\times 3$ games with low level-1($\alpha$) play frequency on MTurk; a hybrid decision-tree-over-models approach outperformed its constituent models.

## Contribution
Reframes ML in economics as a diagnostic complement to theory. Provides two model-evaluation primitives — completeness and restrictiveness — that jointly identify whether a theory is missing regularities or merely overfitting flexibility, plus a constructive loop (algorithmic experimental design) for generating informative new data. Demonstrates a workflow whereby black-box predictions point researchers toward interpretable theory improvements.

## Limitations & open questions
- Both measures depend on the analyst's chosen marginal $P_X$ (the domain of test cases), which is a researcher choice variable, not a primitive; results are domain-relative.
- Restrictiveness depends on the chosen permissible set $F_M$ and prior $\mu$ over mappings (uniform is only "one natural option"); no canonical prior is given.
- The empirical content of the 3-parameter CPT functional form and of the PCHM is *unknown* — representation theorems exist for general CPT but not for these restricted forms.
- Estimation details (how $\theta$, irreducible error, and the black-box benchmark are estimated from finite samples) are deferred to the companion papers; finite-sample bias in the irreducible-error benchmark is not addressed here.
- Whether the completeness/restrictiveness framework extends beyond low-dimensional, finite-feature experimental domains to richer field data is open.

## Connections
This survey condenses three working/published papers: [[@Fudenberg2019a|Fudenberg, Kleinberg, Liang and Mullainathan (2019)]] on completeness; [[@Fudenberg2020|Fudenberg, Gao and Liang (2020)]] on restrictiveness; and [[@Fudenberg2019a|Fudenberg and Liang]] (2019, AER) on predicting and understanding initial play. The risk-preference application builds on Bruhin, Fehr-Duda and Epper (2010) and the CPT functional forms of Goldstein and Einhorn (1987) and Lattimore, Baker and Witte (1992). The games application rests on the cognitive-hierarchy tradition of Stahl and Wilson (1994, 1995), Nagel (1995), and Camerer, Ho and Chong (2004), using the dataset of Wright and Leyton-Brown (2014). Algorithmic experimental design is explicitly framed as kin to adversarial machine learning (Huang et al. 2011) and generative adversarial networks (Goodfellow et al. 2014), repurposed for data design rather than prediction refinement.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
