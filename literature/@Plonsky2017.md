---
citekey: Plonsky2017
title: "Psychological Forest: Predicting Human Behavior"
authors: ["Plonsky, Ori", "Erev, Ido", "Hazan, Tamir", "Tennenholtz, Moshe"]
year: 2017
type: journalArticle
doi: 10.1609/aaai.v31i1.10613
zotero: "zotero://select/library/items/JWTLQZSK"
pdf: /Users/jesper/Zotero/storage/YKLSSGD9/Plonsky2017.pdf
tags: [literature]
keywords: [choice-prediction, random-forest, behavioral-features, decisions-under-risk, ambiguity, theory-driven-ml, beast, feature-engineering]
topics: ["[[choice-prediction-risky-choice]]"]
related: [Erev2010, Kahneman1979, Noti2016, Tversky1992]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We introduce a synergetic approach incorporating psychological theories and data science in service of predicting human behavior. Our method harnesses psychological theories to extract rigorous features to a data science algorithm. We demonstrate that this approach can be extremely powerful in a fundamental human choice setting. In particular, a random forest algorithm that makes use of psychological features that we derive, dubbed psychological forest, leads to prediction that significantly outperforms best practices in a choice prediction competition. Our results also suggest that this integrative approach is vital for data science tools to perform reasonably well on the data. Finally, we discuss how social scientists can learn from using this approach and conclude that integrating social and data science practices is a highly fruitful path for future research of human behavior.

## Summary
The paper argues that the long-standing tension between "theory-free" data science and theory-driven social science in predicting human choice is an artifact of *insufficient integration*, not a genuine trade-off. The authors propose deriving rigorous, engineered features directly from psychological theories of risky choice and feeding them into off-the-shelf machine-learning algorithms. Applied to the data of a choice prediction competition (CPC) on decisions under risk and ambiguity, a random forest equipped with 13 theory-derived features ("psychological forest") matches and then beats the purely psychological state-of-the-art benchmark (BEAST and the CPC winner). The integration also yields a back-to-cognition payoff: by selectively dropping feature groups, the method disentangles which of BEAST's six behavioral mechanisms actually drive prediction.

## Research question
Can integrating psychological theory with data-science tools — specifically, by translating theory into engineered features for generic learners — outperform both pure machine learning and pure psychological models at predicting aggregate human choice behavior over time? And can this integration, as a by-product, test the relative importance of the theory's underlying behavioral mechanisms?

## Method / identification
The unit of prediction is the mean aggregate choice rate (across participants) for one gamble in each of 5 temporal *blocks* within each choice problem, a value in $[0,1]$. Each problem is a repeated binary choice between gambles $A$ and $B$ played 25 times, uniquely described by 11 parameters (the distribution of $A$, a parametrized lottery for $B$, plus ambiguity $Amb$, correlation $Corr$, and a $Feedback$ indicator that is 0 in block 1 and 1 thereafter). The task is content-filtering style: predictions for the 60 test problems cannot use realized choices.

Three nested feature sets are compared. **Objective** = the 11 raw parameters plus a block index. **Naïve** = four domain-relevant differences ($dEV$, $dSD$, $dMins$, $dMaxs$). **Psychological** = 13 features hand-engineered from choice psychology, each tied to a behavioral mechanism. Examples: an estimated EV difference under ambiguity incorporating pessimism, $dEV_0 = (Min_B + UEV_B + EV_A)/3 - EV_A$ where $UEV_B$ is the equal-weight EV; a feedback-aware EV estimate $dEV_{FB} = \frac{1}{2}(dEV + dEV_0)$; "probability one gamble is better" features such as $pBetter_0 = P[F_B^{-1}(x_1) \succ F_A^{-1}(x_1)] - P[F_B^{-1}(x_1) \prec F_A^{-1}(x_1)]$ (with correlation-dependent variants after feedback); a uniform-heuristic feature $dUniEV = EV_{UB} - EV_{UA}$; sign-heuristic features ($dSignEV$, $pBetterS_0$, $pBetterS_{FB}$) using sign-transformed outcomes; minimax/pessimism features ($dMins$, $SignMax$, $RatioMin$); and a stochastic-dominance indicator $Dom \in \{-1,0,1\}$.

Learners tested: random forest, neural nets (1–2 hidden layers, 3/6/12 nodes), SVM (radial, polynomial kernels), and kNN ($k=1,3,5$), all off-the-shelf R packages, run with both default and cross-validation-tuned hyperparameters (results qualitatively identical; defaults reported). Performance metric: MSE over the 300 test choice rates. Mechanism importance is identified two ways: (i) leave-one-mechanism-out re-runs of the random forest, and (ii) the random forest's built-in importance tool after first reducing each mechanism to a single representative feature to defuse the correlated-feature bias documented by Strobl et al. (2008).

## Data
CPC 2015 data (Erev, Ert & Plonsky 2015): 446 incentivized participants, 150 choice problems in a common 11-dimensional space, split into 90 train (30 hand-selected, the rest algorithmically randomized) and 60 test problems. Each participant faced 30 problems × 25 decisions (5 blocks). Publicly available at the competition website.

## Key findings
1. **No simple learner predicts well without psychological features.** The best Objective/Naïve learner (random forest on both) reaches MSE $0.0142$, 61% worse than the CPC winner; all non-psychological learners are significantly worse than BEAST and the winner.
2. **Random forest on the 13 psychological features alone already slightly beats BEAST**, the model that inspired those features.
3. **Psychological forest (all three feature sets, random forest) reaches MSE $0.0087$**, a 39% improvement over the best feature-free learner and beating the CPC winner (MSE $0.0088$).
4. **Adding BEAST's full numeric prediction as one more feature gives MSE $0.0070$** — 20% better than the CPC winner and 29% better than BEAST, and the first model to *significantly* beat BEAST on these data.
5. **Random forests dominate the other algorithms** across nearly all feature combinations; the authors conjecture an affinity between decision-tree stochasticity/dichotomous splits and human choice processes.
6. **Mechanism disentangling:** of BEAST's six mechanisms, sensitivity to estimated EV and minimization of immediate regret matter most; dropping dominance actually *improves* prediction, implying special treatment of dominant options is misguided given the other mechanisms. The richer six-mechanism theory thus reduces to a simpler "sensitive to EV and to probability of the better payoff" summary.

## Contribution
Demonstrates a concrete, transferable recipe — theory → engineered features → generic learner — that achieves a new state-of-the-art on a well-benchmarked human-choice-prediction task while remaining interpretable. It reframes the data-science-versus-social-science debate as one of integration quality, and shows the method doubles as a hypothesis-testing tool for disentangling theoretical mechanisms otherwise entangled by a model's auxiliary assumptions.

## Limitations & open questions
- The authors flag that the affinity between random forests and human decision processes is conjectural and "further investigation... is thus due."
- Features are engineered for the gambles domain; the claim that they "seamlessly" transfer across domains is asserted but not demonstrated outside this CPC.
- Results rest on a single dataset (150 problems, aggregate choice rates), leaving external validity to other populations, individual-level prediction, and richer choice domains open.
- Translating theory into features still requires human judgment; the paper does not automate feature derivation.
- Whether the "EV + probability-of-better" reduction holds beyond this paradigm is left open.

## Connections
The work sits squarely in the choice-prediction-competition tradition of [[@Erev2010|Erev et al. (2010)]] and Erev, Ert & Plonsky (2015), whose BEAST baseline supplies the six behavioral mechanisms operationalized here. It is explicitly contrasted with agent-design work that *assumes* psychological models (Azaria et al. 2012; De Melo, Gratch & Carnevale 2014; Prada & Paiva 2009) and credits independent hybrid feature-based work by [[@Noti2016|Noti et al. (2016)]]. The psychological features draw on prospect theory and its descendants ([[@Kahneman1979|Kahneman & Tversky 1979]]; [[@Tversky1992|Tversky & Kahneman 1992]]), the priority heuristic (Brandstätter, Gigerenzer & Hertwig 2006), efficient decision heuristics (Thorngate 1980; Edwards 1954), regret/probability-of-winning ideas (Payne 2005; Erev & Roth 2014), maxmin/ambiguity attitudes (Gilboa & Schmeidler 1989; Wakker 2010; Viscusi 1989), and the reflection effect (Markowitz 1952). The correlated-feature-importance caveat invokes Strobl et al. (2008). The broader theme — structural/theory-informed features improving learned models of economic choice — connects to later structural-versus-ML comparisons in behavioral and experimental economics.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
