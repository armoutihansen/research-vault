---
citekey: Shoshan2023
title: "BEAST-Net: Learning novel behavioral insights using a neural network adaptation of a behavioral model"
authors: ["Shoshan, Vered", "Hazan, Tamir", "Plonsky, Ori"]
year: 2023
type: report
doi: ""
zotero: "zotero://select/library/items/B3Q2FGSG"
pdf: /Users/jesper/Zotero/storage/T7KK9396/Shoshan2023.pdf
tags: [literature]
keywords: [behavioral-economics, decision-under-uncertainty, interpretable-ml, beast-model, risky-choice, neural-network-adaptation]
topics: []
related: [Erev2017, Fudenberg2022, Hartford2016, Kahneman1979, Peterson2021, Plonsky2017, Plonsky2019]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> In this study, we introduce BEAST-Net, an interpretable model of human decision making under uncertainty, that fuses the foundational principles of BEAST, a behavioral model grounded in psychological theory, with the capabilities of machine learning techniques. Our strategy involves mathematically formalizing BEAST as a differentiable function and parameterizing it via a neural network. This approach facilitates the learning of model parameters from data and optimizes it through backpropagation. BEAST-Net scales to larger datasets and adapts to new data more efficiently, while preserving the psychological interpretability of the original model. Evaluations of BEAST-Net on the most extensive publicly accessible human choice task datasets demonstrate its superior performance over several baselines, including the original BEAST model. Importantly, BEAST-Net provides interpretable explanations for choice behavior, leading to the extraction of novel psychological insights from the data. This research demonstrates the potential of machine learning techniques to enhance the scalability and adaptability of models rooted in psychological theory, without compromising their interpretability or insight generation capabilities.

## Summary
BEAST-Net is a differentiable, neural-network reimplementation of BEAST (Best Estimate And Sampling Tools), a leading psychological theory of human choice between gambles. The authors rewrite BEAST's simulation-based prediction as a closed-form expectation, replace the non-differentiable choice indicator with a logistic approximation, and expose six interpretable behavioral parameters as the network's learnable weights. Trained by backpropagation, BEAST-Net runs in minutes (vs. over a day for BEAST), beats BEAST and several theory-plus-ML baselines on the largest risky-choice dataset, and — crucially — yields fresh, falsifiable behavioral hypotheses (e.g., people ignore some outcomes in many-outcome gambles) by reading off the fitted parameters.

## Research question
Can the predictive power and scalability of machine learning be combined with the psychological interpretability of theory-based behavioral models, so that one obtains both better predictions of human risky choice *and* new, interpretable behavioral insights — rather than the usual trade-off where ML wins on accuracy but is a black box, while theory models are interpretable but inaccurate and non-scalable?

## Method / identification
The core move is to convert BEAST from a Monte-Carlo simulation into a differentiable function and then realize that function as a small neural network whose weights are the behavioral parameters.

In BEAST, a simulated agent chooses gamble B over A iff $\Delta\text{BEV} + \Delta\text{ST} + e > 0$, where $\Delta\text{BEV} = \text{BEV}_B - \text{BEV}_A$ is the difference in best estimates of expected value, $e$ is mean-zero Gaussian noise, and $\Delta\text{ST} = \text{ST}_B - \text{ST}_A$ is the difference in "sampling tools" terms. Each $\text{ST}_m$ averages $\kappa \sim U(1,3)$ outcomes drawn under one of four sampling tools $T_j$ chosen with probabilities $p_{unb}, p_{unif}, p_{pess}, p_{sign}$: the unbiased distribution, a uniform reweighting, a pessimism transform (worst outcome with certainty), and a sign-only transform.

The simulation prediction is the empirical mean of indicators,
$$\text{Pred}_{\text{BEAST}} = \frac{1}{n}\sum_{i=1}^{n} \mathbf{1}_{\Delta\text{BEV}_i + \Delta\text{ST}_i + e_i > 0}.$$
The authors take three steps to make this differentiable. First, let $n\to\infty$ so the mean converges to the expected decision, $\lim_{n\to\infty}\text{Pred}_{\text{BEAST}} = P[e > -g]$ with $g = \Delta\text{BEV} + \Delta\text{ST}$. Second, approximate the Gaussian CDF by a logistic sigmoid, $P[e > -g] \approx \frac{1}{1 + \exp(-b\cdot g)}$, where $b$ controls curvature (larger $b$ = less noise). Third, drop BEAST's arbitrary auxiliary restrictions ($p_{unif}=p_{pess}=p_{sign}$ and equal weighting of $\Delta\text{BEV}$ and $\Delta\text{ST}$), introducing a free relative weight $w$ on $\Delta\text{BEV}$. Because $\Delta\text{BEV}$ is constant for a task, the expectation depends only on $\Delta\text{ST}$:
$$\text{Pred}_{\text{BEAST-Net}} = \sum_{\Delta\text{ST}} P(\Delta\text{ST})\, d(\Delta\text{ST}), \qquad d(\Delta\text{ST}) = \frac{1}{1 + \exp(-b(w\cdot\Delta\text{BEV} + \Delta\text{ST}))}.$$
The distribution $P(\Delta\text{ST})$ is obtained by the law of total probability over $\kappa$ and the independent tool draws $T_1,\dots,T_\kappa$, giving $P(\Delta\text{ST}) = \sum_{\kappa=1}^{3} P(\kappa)\sum_{T_1}P(T_1)\cdots\sum_{T_\kappa}P(T_\kappa)\,P(\Delta\text{ST}\mid\kappa,T_1,\dots,T_\kappa)$, with $P(\kappa)=\tfrac13$. Since each of $\kappa\in\{1,2,3\}$ positions can take one of four tools, there are $\sum_{i=1}^{3}4^i = 84$ tool-combinations, which are precomputed as 84 vectors of possible $\Delta\text{ST}$ values plus 84 vectors of their conditional probabilities.

The network learns exactly six parameters: $b$, $w$, and the four tool probabilities $p_{unb}, p_{unif}, p_{pess}, p_{sign}$. A preprocessing stage computes $\Delta\text{BEV}$ and the 84 $\Delta\text{ST}$/probability vectors per task; the network computes $d(\Delta\text{ST})$ and $P(\Delta\text{ST})$ from the learned parameters, forms the prediction, and minimizes MSE against observed choice proportions via SGD. The authors also segment tasks and fit a separate parameter set per segment, using either (a) a *manual* segmentation grounded in theory — a stochastic-dominance group ("Dom") plus four groups by number of outcomes ("1vs2", "1vsM", "2vs2", "2vsM") — or (b) a *data-driven* deep-clustering segmentation (autoencoder latent space + KMeans).

## Data
Three datasets. Main: **Choices13k** [[[@Plonsky2019|Bourgin et al. 2019]] — 13,006 two-gamble choice tasks with five trials each; following [[@Peterson2021|Peterson et al. (2021)]] the analysis focuses on the 9,831 feedback tasks. Validation: **MS22** [He, Analytis & Bhatia 2022] — 1,565 tasks compiled from 15 diverse datasets with individual-level responses, very different from BEAST's development data (CPC15). Synthetic: **synthBEAST** — 1,565 tasks generated by BEAST itself to test parameter recovery. Training used ten 80-20 splits (Choices13k) or 10-fold CV (MS22, synthBEAST), reporting test MSE.

## Key findings
BEAST-Net is far faster (minutes vs. >1 day) while improving accuracy. On Choices13k it reaches test MSE 0.0118, beating Original BEAST (0.0211) and the neural Expected-Utility / Prospect-Theory / Cumulative-Prospect-Theory adaptations (0.0204-0.0217). Manually segmented BEAST-Net (0.0111) edges out even the Mixture-of-Theories model (MoT, 0.0113) — and is the best *interpretable* model by a wide margin (MoT is non-interpretable). Theory-guided manual segmentation beat data-driven KMeans segmentation. On synthBEAST it recovers parameter values close to true BEAST values, validating interpretability; on MS22 it nearly halves BEAST's MSE (0.072 to 0.038), though it underperforms some models specialized to that heterogeneous data.

Reading the learned parameters yields four substantive insights: (1) pessimism usage $p_{pess}$ is much lower than in BEAST, consistent with Choices13k participants being unable to actually lose money; (2) in dominance tasks the model learns a large $b$ (low noise), matching BEAST's built-in dominance assumption; (3) $w$ (weight on EV differences) is smaller when an option has more than two outcomes, suggesting EV computation is harder there; (4) in "1vsM" tasks high $b$ prompted a new hypothesis — people *ignore some outcomes* in multi-outcome gambles. Encoding this as outcome "dropout" in original BEAST cut its Choices13k MSE by over 5.3%.

## Contribution
A general recipe for "white-box" neural behavioral modeling: take a psychologically grounded but non-differentiable model, express its population prediction as a differentiable expectation, parameterize it as a network, and fit by backprop — keeping every weight psychologically meaningful. Unlike prior ML-in-choice work that treats ML as a standalone competitor to theory, BEAST-Net *collaborates* with the theory, preserving its logical process and thereby addressing "algorithm aversion" among domain experts. The fitted parameters are not just predictive knobs but generators of testable behavioral hypotheses (demonstrated by the outcome-dropout discovery). The authors note the dropout trick generalizes to any network-adapted behavioral model.

## Limitations & open questions
The authors explicitly flag: (i) reliance on large training data, problematic in behavioral science where datasets are typically small; (ii) on diverse datasets like MS22, BEAST-Net struggles to find universally applicable parameters and its ability to learn distinct sub-group models is limited by data; (iii) predictions are confined to the classical full-information setting (EVs computable), not ambiguity. Open directions they raise: incorporating learned phenomena (e.g., outcome dropout) back into theory; *learning new sampling tools* ("new filters") on gambles; and developing a deeper understanding of why ML-based clustering underperforms theory-guided segmentation for human choice.

## Connections
Directly extends [[@Peterson2021|Peterson et al.]] (2021, *Science*), whose large-scale benchmark on Choices13k found BEAST the strongest theory model and MoT the best overall; BEAST-Net targets MoT-level accuracy with interpretability. It adapts the BEAST model of [[@Erev2017|Erev, Ert & Plonsky et al.]] (2017, *Psychological Review*) and builds on the dataset and synthetic-data methodology of [[@Plonsky2019|Bourgin et al. (2019)]]. It situates against Prospect Theory ([[@Kahneman1979|Kahneman & Tversky 1979]]) and its cumulative variants as the neural baselines it surpasses, and against the "psychological forest" feature-engineering approach of [[@Plonsky2017|Plonsky et al. (2017)]]. Conceptually it advances the explanation-vs-prediction agenda of Hofman et al. (2021, *Nature*) and the model-completeness program of [[@Fudenberg2022|Fudenberg, Kleinberg, Liang & Mullainathan (2022)]]; methodologically it is kin to [[@Hartford2016|Hartford et al. (2016)]], who used inductive bias in networks to model strategic behavior. The deep-clustering component follows Yang et al. (2017).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
