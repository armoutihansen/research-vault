---
citekey: Muszaidi2022
title: Deep Learning Approach for Football Match Classification of English Premier League (EPL) Based on Full-Time Results
authors: ["Muszaidi, Muhaimin", "Mustapha, Aida Binti", "Ismail, Shuhaida", "Razali, Nazim", "Mustapha, Aida Binti", "Shamsuddin, Suhadir", "Zuhaib Haider Rizvi, Syed", "Asman, Saliza Binti", "Jamaian, Siti Suhana"]
year: 2022
type: conferencePaper
doi: 10.1007/978-981-16-8903-1_30
zotero: "zotero://select/library/items/WM7GW32A"
pdf: /Users/jesper/Zotero/storage/53HZJCFP/Muszaidi et al. - 2022 - Deep Learning Approach for Football Match Classifi.pdf
tags: [literature]
keywords: [football-prediction, deep-learning, multilayer-perceptron, match-classification, hyperparameter-tuning, sports-analytics]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The trend of modeling the football match classification has become increasingly popular in the last few years, thus many classification models have been proposed with the point of evaluating the attributes that lead a football team to win, draw or lose a certain match. There are two types of approaches has been considered for classification of football matches results, which include the statistical approaches and deep learning approaches. This paper proposes a Multilayer Perceptron (MLP) and Dense Neural Network (DNN) to evaluate the performance of the classification football matches results in the terms of home win (H), away win (A), and draw (D) for games under the English Premier League (EPL). The experiment revealed that MLP produced better classification accuracy rate of 78.42% as compared to 67.63% by the standard DNN. Nonetheless, the performance of DNN can be further improved by means of hyperparameter tuning, whereby DNN achieved the highest accuracy of 70.53% when modeled in a three-dense layers with the size of 16 nodes and trained with 200 epochs.

## Summary
A short applied-ML conference paper that benchmarks two artificial-neural-network classifiers — a Multilayer Perceptron (MLP) and a Dense Neural Network (DNN) — on the three-class problem of predicting English Premier League full-time results (home win H, away win A, draw D) from in-match statistics. Using one season of EPL data and the WEKA / WekaDeeplearning4j toolkit, the authors find the shallower MLP (78.42% accuracy) outperforms the standard DNN (67.63%), but DNN accuracy can be pushed up to ~70.5% via hyperparameter tuning over depth, layer width, and epochs.

## Research question
Which of two ANN-family classifiers — MLP versus a fully-connected DNN — better classifies EPL match outcomes into {H, A, D} from match-level statistics, and how does DNN performance respond to hyperparameter tuning (number of dense layers, nodes per layer, number of epochs)?

## Method / identification
The task is a supervised multi-class classification problem with a three-valued target, the Full Time Result (FTR) $\in \{\text{H}, \text{A}, \text{D}\}$. Two function-based classifiers from WEKA are compared:

- **MLP**: WEKA's backpropagation-trained multilayer perceptron, with default learning rate $0.3$, momentum $0.2$, $100$ epochs, and a single hidden layer auto-sized to WEKA's `'a'` setting (attributes plus classes averaged).
- **DNN**: the `DenseLayer` architecture from the WekaDeeplearning4j package (Deeplearning4j backend), where every neuron in a layer is fully connected to the previous layer. The output layer is fixed at three nodes for {H, A, D}.

A hyperparameter sweep is run on the DNN only: hidden-layer depth from one to three dense layers, layer width following a geometric progression ($8$ vs $16$ nodes), and epoch counts of $100$ vs $200$ — i.e. configurations such as $8$, $8\times 8$, $8\times 8\times 8$, $16$, $16\times 16$, $16\times 16\times 16$. Evaluation uses 10-fold cross-validation. Performance metrics are derived from the confusion matrix counts (TP, TN, FP, FN):

$$\text{Accuracy} = \frac{TP + TN}{FP + TP + TN + FN}$$

$$\text{Precision} = \frac{TP}{TP + FP}, \qquad \text{Recall} = \frac{TP}{TP + FN}$$

$$\text{F-measure} = \frac{TP}{TP + \frac{1}{2}(FP + FN)}$$

(The paper's stated formula for F-measure follows WEKA's confusion-matrix convention rather than the textbook harmonic-mean expression.)

## Data
Public match data from football-data.co.uk, restricted to the EPL. The selected subset is the 2018–2019 season: $380$ rows (matches) with $62$ attributes. Predictive features include home/away shots (HS/AS), shots on target (HST/AST), fouls (HF/AF), corners (HC/AC), and yellow/red cards (HY/AY/HR/AR); the label is the nominal FTR. The dataset is small (a single 380-match season), which constrains generalizability.

## Key findings
- **MLP beats the standard DNN**: MLP attains $78.42\%$ accuracy (precision $0.780$, recall $0.784$, F-measure $0.782$) versus DNN's $67.63\%$ (precision/recall/F-measure all $\approx 0.676$).
- **Tuning helps the DNN but does not close the gap**: the best DNN configuration reaches $70.79\%$ (a two-layer $16\times 16$ network at $200$ epochs) or $70.53\%$ for the three-layer $16\times 16\times 16$ at $200$ epochs — both still well below MLP.
- **Monotone-ish gains from capacity**: accuracy tends to rise with more layers, more nodes, or more epochs; e.g. an $8$-dense layer at $200$ epochs and a $16$-dense layer at $100$ epochs both reach $\approx 70.26\%$, illustrating a width-vs-epochs trade-off.
- **Diminishing returns / overfitting caution**: the authors note that added depth and epochs sharply increase computation, large epoch counts are unwarranted on small data, and training should stop when validation error rises (overfitting onset).

## Contribution
Provides a direct empirical comparison of MLP versus a fully-connected DNN for EPL three-class outcome classification, plus a documented DNN hyperparameter sweep over depth, width, and epochs, all reproducibly within the open-source WEKA / WekaDeeplearning4j workbench. The authors frame the results as a baseline for future deep-learning work on football outcome classification.

## Limitations & open questions
- **Single small dataset**: only the 2018–2019 EPL season (380 matches) is used; the authors flag data availability and quality as a primary challenge and suggest examining other public databases or web scraping.
- **No held-out future-match test of betting-market value**: the paper notes that "hardly any" statistical models consistently beat betting markets, but does not itself benchmark against odds.
- **Computational cost vs accuracy trade-off** is raised but not formally characterized.
- **Overfitting control**: early stopping is recommended in prose but not implemented as a tuned criterion.
- **Scope of tuning**: only the DNN is swept; learning rate, momentum, regularization, and feature selection are left at defaults — open avenues for improvement.

## Connections
The applied football-prediction lineage cited includes Purucker (1996) on neural-network quarterbacking for the NFL, Kahn (2003) on NFL game prediction with engineered features, Chinwe Peace / Igiri (2014) on logistic-regression-weighted ANN for the EPL reaching 85% accuracy, and Rahman (2020) on a deep-learning football-prediction framework. Statistical and odds-based forecasting is represented by Hvattum & Arntzen (2010) on ELO-rating match prediction and Goddard & Asimakopoulos (2004) on fixed-odds betting efficiency. Alternative ML methods surveyed include Rotshtein, Posner & Rakityanskaya (2005) on genetic/neural-tuned fuzzy models, Guan & Wang (2021) on neural-network optimization, Esme & Kiran (2018) on k-nearest-neighbors from bookmaker odds, and Bayesian-network approaches by Constantinou, Fenton & Neil (2012) and Razali, Mustapha et al. (2017) — the latter by an overlapping author team. The tooling rests on Lang et al. (2019) WekaDeeplearning4j and Nielsen (2021) for the ANN-vs-DNN exposition.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
