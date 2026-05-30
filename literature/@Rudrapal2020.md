---
citekey: Rudrapal2020
title: A Deep Learning Approach to Predict Football Match Result
authors: ["Rudrapal, Dwijen", "Boro, Sasank", "Srivastava, Jatin", "Singh, Shyamu", "Behera, Himansu Sekhar", "Nayak, Janmenjoy", "Naik, Bighnaraj", "Pelusi, Danilo"]
year: 2020
type: conferencePaper
doi: 10.1007/978-981-13-8676-3_9
zotero: "zotero://select/library/items/6QTMZ8HN"
pdf: /Users/jesper/Zotero/storage/DXVW3CGD/Rudrapal et al. - 2020 - A Deep Learning Approach to Predict Football Match.pdf
tags: [literature]
keywords: [football-prediction, multi-layer-perceptron, sports-analytics, feature-engineering, match-result-classification, supervised-learning]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Predicting a match result is a very challenging task and has its own features. Automatic prediction of a football match result is extensively studied in last two decades and provided the probabilities of outcomes of a scheduled match. In this paper we proposed a deep neural network based model to automatically predict result of a football match. The model is trained on selective features and evaluated through experiment results. We compared our proposed approach with the performance of feature-based classical machine learning algorithms. We also reported the challenges and situations where proposed system could not predict the outcome of a match.

## Summary

This short conference paper (Springer, *Computational Intelligence in Data Mining*) proposes a Multi-Layer Perceptron (MLP) to predict the outcome of English Premier League (EPL) football matches from engineered team-, player-, and head-to-head features. Framed as a supervised classification problem over win/loss/draw, the model is trained on data spanning the 2000–01 through 2015–16 seasons and benchmarked against SVM, Gaussian Naive Bayes, and Random Forest. The MLP attains the best accuracy (73.57%) among the compared classifiers. The paper's main substantive contribution is its feature engineering: a 40-feature set partitioned across home/away splits, plus an explicit error analysis cataloguing where the model fails.

## Research question

Can a deep neural network (specifically an MLP), trained on a carefully engineered set of team, player, and head-to-head features, predict the result of a football match more accurately than classical feature-based machine-learning classifiers? Which features are most influential in determining a match outcome?

## Method / identification

The task is cast as a multi-class classification problem: each match is labelled with one of {win, loss, draw}. The proposed classifier is a Multi-Layer Perceptron with 10 hidden units (described as "10 hidden states"), trained by back-propagation. The authors justify the MLP choice by noting that prior work (Kahn 2003; Purucker 1996) found MLPs competitive on similar sports-prediction tasks.

The feature construction is the methodological core. From a literature survey the authors draw 40 features grouped into three classes — Team (9 per side), Player (7 per side), and Head-to-Head (4 per side) — each computed separately for the home and away team, yielding the 20+20 = 40 total. Team features include attack/midfield/defence points, an aggregate Team Rating, and EPL-history features (EPL Times, Streak, Performance, and their average EPL Point) plus league Standings Point. Player features aggregate FIFA-style ratings: overall Player Rating, Player Potential, Market Value, Goal Keeper Point, and pooled Defence/Mid-Field/Striking points built from many sub-parameters (e.g. 19 striking parameters). Head-to-Head features capture average points earned (3/1/0 for win/draw/loss), recent Form Points over the last 5 home and 5 away matches, average Goal Difference, and the home-minus-away Form Points Difference.

Evaluation uses a 70/30 holdout split. The authors report accuracy, sensitivity, specificity, precision/recall, and F1-score, and compare the MLP against SVM, Gaussian Naive Bayes, and Random Forest baselines.

## Data

EPL match data covering seasons 2000–01 to 2015–16. The reported dataset statistics: 15 seasons, 42 match-related entries (table values are 15 / 42 / 462 / 11,400 for season / match / team / player counts), 462 teams, and 11,400 players; the text also states the dataset "includes information of 11,400 matches." Data were scraped from public sources: football-data.co.uk, fifaindex.com, skysports.com, and Kaggle. The 2010–11 season is cited as illustrating the inherent randomness of outcomes (wins/losses/draws at 35.5% / 35.5% / 29%).

## Key findings

- The MLP achieves an accuracy of 73.57% on the held-out test set, with sensitivity 71.45%, specificity 73.57%, and F1-score 71.02% (table values are reported somewhat inconsistently across Tables 3 and 4).
- In the comparison (Table 4), the MLP's F1-score / accuracy (71.45% / 73.57%) outperforms SVM (50.07% / 58.77%), Gaussian Naive Bayes (64.26% / 65.84%), and Random Forest (66.07% / 72.92%). Random Forest is the closest competitor.
- Because sensitivity and specificity are close, the authors argue the model is reasonably balanced rather than biased toward one class.
- Modelling home and away features separately is claimed to be effective, reflecting venue, crowd-support, and familiarity advantages for the home team.

## Contribution

Two stated contributions: (1) an MLP-based prediction model benchmarked against classical ML classifiers on EPL data; and (2) a newly assembled 40-feature set, derived from detailed analysis of feature performance and from head-to-head match history, with a home/away split. The paper sits in the applied sports-analytics / result-forecasting literature rather than offering a methodological advance in deep learning per se.

## Limitations & open questions

The authors give an explicit error analysis listing failure modes and extensions:

1. Only the starting 11 players' features are used; substitutes (and lineup changes between matches) can be decisive. Including all squad players and substitutes is proposed.
2. Hidden, hard-to-quantify factors — crowd support, referee unfairness, the inherently unpredictable nature of the game — are omitted; their inclusion would improve the model.
3. The features are "dynamic" and change only slowly across seasons, so performance is mostly dependent on recent past matches.
4. Future work: incorporate a team's reserve-player strength and coach rating to make the model more robust.

Beyond the authors' own list, the paper does not report confidence intervals, cross-validation, class-imbalance handling for draws, or hyperparameter tuning details, limiting the strength of the accuracy comparison.

## Connections

The paper situates itself in a long sports-forecasting lineage. It cites Stefani (1977) on least-squares football/basketball prediction; Purucker (1996) and Kahn (2003) on neural-network NFL prediction; McCabe & Trevathan (2008) on multi-layer perceptrons across four sports; and Min et al. (2008) on a compound rules-plus-Bayesian-network framework. On the statistical side it references Koopman & Lit (2015), who use a dynamic bivariate Poisson model for EPL results, and Constantinou, Fenton & Neil (2012) on the PI-football Bayesian network. It also draws on student/applied work by Ulmer & Fernandez (2013) and Yezus (2014), Tax & Joustra (2015) on the Dutch competition, Prasetio et al. (2016) on logistic-regression result prediction, and Bunker & Thabtah (2017) on a general machine-learning framework for sport result prediction. The classical-ML baselines connect to standard SVM, Naive Bayes, and Random Forest classifiers.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
