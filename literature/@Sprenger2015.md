---
citekey: Sprenger2015
title: "An Endowment Effect for Risk: Experimental Tests of Stochastic Reference Points"
authors: ["Sprenger, Charles"]
year: 2015
type: journalArticle
doi: 10.1086/683836
zotero: "zotero://select/library/items/YHEITDA7"
pdf: /Users/jesper/Zotero/storage/9J3UB524/Sprenger2015.pdf
tags: [literature]
keywords: [reference-dependent-preferences, endowment-effect-for-risk, koszegi-rabin, disappointment-aversion, risk-preference-elicitation, loss-aversion, experimental-economics]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Recent models of reference-dependent preferences indicate that expectations may play a prominent role in the presence of behavioral anomalies. A subset of such expectations-based models predicts an "endowment effect for risk": that risk attitudes differ when reference points change from certain to stochastic. In two purposefully simple risk preference experiments, eliminating often-discussed confounds, I demonstrate both between and within subjects such an endowment effect for risk. These results provide needed separation between expectations-based reference-dependent models, allow for evaluation of recent theoretical extensions, and may help to close a long-standing debate in decision science on inconsistency between utility elicitation methodologies.

## Summary
Sprenger runs deliberately stripped-down risk-preference experiments to test a sharp comparative-static prediction that separates the two leading expectations-based reference-dependent models: Köszegi–Rabin (KR) preferences predict an "endowment effect for risk" — risk attitudes shift depending on whether the reference point is certain or stochastic — whereas disappointment aversion (DA) does not. Eliciting risk attitudes two ways from the same gambles (probability equivalents with a certain referent versus certainty equivalents with a gamble referent), he finds near risk neutrality in certainty equivalents but substantial risk aversion in probability equivalents, both between and within subjects. The pattern, plus out-of-sample predictions for "uncertainty equivalent" tasks, supports KR (under a non-equilibrium "first-focus" referent) and rejects DA and KR's equilibrium refinements.

## Research question
Do risk attitudes depend on whether the reference point is certain or stochastic — i.e., is there an "endowment effect for risk"? More precisely: can one design a neutral, confound-free experiment that empirically separates KR expectations-based reference dependence (which predicts such an effect) from disappointment aversion (which does not), thereby adjudicating between competing accounts of how the referent is determined?

## Method / identification
The core is a comparative-static prediction derived under the KR utility for binary lotteries. With consumption utility $m(\cdot)$ taken approximately linear (small stakes, $\eta=1$) and piecewise-linear gain-loss utility governed by loss aversion $\lambda>1$, the KR value of consumption $F$ under stochastic referent $G$ is
$$U(F\mid G)=\int\int u(x\mid r)\,dG(r)\,dF(x),\qquad u(x\mid r)=m(x)+\mu\big(m(x)-m(r)\big).$$
Two cases give the separating prediction. (i) **Probability equivalent** — certain referent $r$, binary consumption gamble paying $x_1\geq r$ with prob $q$ and $x_2\leq r$ otherwise. The indifference probability is
$$q^{*}=\frac{r-x_2-\lambda\cdot(x_2-r)}{(x_1-x_2)+[1\cdot(x_1-r)-\lambda\cdot(x_2-r)]},$$
which exceeds the risk-neutral level $(r-x_2)/(x_1-x_2)$ for $\lambda>1$: the agent looks **risk averse**, with $dq^{*}/d\lambda>0$. (ii) **Certainty equivalent** — binary referent gamble $(r_1,r_2)$, certain consumption $x$ with $r_1\geq x\geq r_2$. Solving $U(c\mid G)=U(G\mid G)$ yields indifference exactly at the expected value $c^{*}=p\,r_1+(1-p)\,r_2$: the agent looks **risk neutral for all $\lambda$**, because evaluating a certainty equivalent inside the referent's support never crosses a loss-averse kink. DA, by contrast, always evaluates against the fixed certainty-equivalent referent and so predicts identical risk attitudes across the two methods; expected utility and cumulative prospect theory (fixed referent) likewise predict equivalence.

Design: a between-subjects, two-condition experiment using Multiple Price Lists (21–22 rows). Condition 1 elicits probability equivalents (option A a fixed certain amount, option B a gamble with rising win probability — inducing a **certain** referent); condition 2 elicits certainty equivalents (option A a fixed gamble, option B a rising certain amount — inducing a **stochastic** referent). The referent is identified via KR's non-equilibrium "first-focus" assumption: the initially presented, fixed decision element becomes the reference point. Deliberately neutral framing, no explicit endowments, no ownership language, and real (non-hypothetical) stakes eliminate Plott–Zeiler-style demand and hypothetical-bias confounds. A third out-of-sample task set — uncertainty equivalents (condition 1.3) and inverted uncertainty equivalents (condition 2.3) — provides a stress test: KR predicts quadratically declining risk premia in $p^2$ for 1.3 but uniform risk neutrality in 2.3, while DA predicts no difference. The KR model is estimated by nonlinear least squares (aggregate and individual $\hat\lambda$) from 1.1/1.2 and used to predict 1.3 out of sample.

## Data
Primary experiment: 136 UCSD undergraduates (70 in condition 1, 66 in condition 2); analysis focuses on the 122 subjects with unique switch points across all 22 tasks (1,474 decisions in condition 1; 1,210 in condition 2). A secondary within-subjects study reuses 76 subjects from Andreoni and Sprenger (2011). Post-experiment surveys collected demographics, six-item numeracy, three-item Cognitive Reflection Test, and self-reported risk attitudes; an omnibus balancing logit does not reject equality across conditions ($\chi^2=14.1$, $p=.12$).

## Key findings
- **Endowment effect for risk confirmed (between subjects).** Median risk premia are near zero in certainty equivalents (conditions 2.1/2.2, virtual risk neutrality) but substantially positive in probability equivalents (conditions 1.1/1.2, risk aversion). By coarse classification, 67% of probability-equivalent decisions are risk averse vs. 38% of certainty-equivalent decisions; subjects are between three and four times more likely to be risk averse under probability equivalents.
- **Within-subjects replication.** The same reversal appears in the Andreoni–Sprenger data where each subject faces both methods, ruling out an experiment-level Preferred Personal Equilibrium (PPE) explanation.
- **Parameter recovery.** Aggregate $\hat\lambda\approx3.4$ and median individual $\hat\lambda\approx3.6$, close to prior KR estimates.
- **Out-of-sample validity.** The estimated KR model reproduces the predicted quadratically declining risk premia in condition 1.3 and near risk neutrality in condition 2.3; individual-level predicted vs. actual expected risk premia correlate $.76$ with a regression slope of $1.06$ (not significantly different from 1). KR (first-focus) outperforms a CRRA expected-utility benchmark out of sample.
- **Model adjudication.** Results are consistent with KR (and, the author notes, third-generation prospect theory) but **reject DA**, and because the findings reject DA they also reject KR's equilibrium refinements (UPE/PPE applied at the choice level, which predict no difference).

## Contribution
Provides the first clean experimental separation of KR from DA via the endowment effect for risk, without relying on manipulating expectations per se and without the confounds (physical endowments, ownership framing, hypothetical choice) that plagued earlier exchange and elicitation studies. It supplies KR parameter estimates near literature values and demonstrates out-of-sample predictive validity at the individual level. It also reframes a long-standing decision-science puzzle — that probability-equivalent elicitation yields more risk aversion than certainty-equivalent elicitation — as a theory-grounded consequence of KR reference dependence rather than an ad hoc "response-mode bias." Applied implications are sketched for stock-market participation, insurance purchase, and the portability of first-order risk aversion.

## Limitations & open questions
- **Referent control is indirect.** Without explicit endowments, the researcher cannot directly observe the referent; the whole interpretation rests on the "first-focus" assumption that the fixed element becomes the reference point. The author flags the inability to actually induce referent changes as the design's key limitation.
- **External validity gap.** The link between experimentally manipulated referents and real-world settings where referents form naturally is "not established"; the finance/insurance applications are offered with explicit caution.
- **First-focus vs. equilibrium.** Data support the non-equilibrium first-focus referent, not KR's rational-expectations equilibria; reconciling first-focus with equilibrium discipline is open.
- **KR vs. PT3 unresolved.** Third-generation prospect theory predicts the same valuation gap; distinguishing them (KR evaluates states as statistically independent, PT3 is state-contingent) is left to future work.
- **Methodological caution.** If fixed price-list elements serve as referents, small framing changes can flip elicited risk/time preferences — raising concerns for the broad practice of preference elicitation, and a hopeful but open agenda for marketers/policymakers using "menus alone."
- Compound-lottery randomization (one task paid) potentially links choices and referents across tasks, complicating the KR analysis.

## Connections
Builds directly on Köszegi and Rabin (2006, 2007) expectations-based reference dependence and contrasts it with disappointment aversion (Bell 1985; Loomes and Sugden 1986; Gul 1991), rooted in Kahneman and Tversky (1979) prospect theory and cumulative prospect theory (Tversky and Kahneman 1992). The uncertainty-equivalent methodology and secondary data come from Andreoni and Sprenger (2011). It engages the endowment-effect confound debate of Plott and Zeiler (2005, 2007) and the hypothetical-bias caution of Holt and Laury (2002), and connects to the field/lab literature testing expectations-based reference dependence (Abeler et al. 2011; Crawford and Meng 2011; Ericson and Fuster 2011; Gill and Prowse 2012; Heffetz and List 2014), much of which cannot separate KR from DA. Schmidt, Starmer, and Sugden (2008) third-generation prospect theory is the closest unrefuted alternative; Song (2012) and Castillo and Eil (2014) report related endowment-effect-for-risk findings. The decision-science elicitation-inconsistency literature (Hershey et al. 1982; Hershey and Schoemaker 1985; McCord and de Neufville 1985, 1986; Schoemaker 1990) is reinterpreted through KR.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
