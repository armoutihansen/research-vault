---
citekey: Trautmann2015
title: "Belief elicitation: A horse race among truth serums"
authors: ["Trautmann, Stefan T.", "van de Kuilen, Gijs"]
year: 2015
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/T6X4YRMW"
pdf: /Users/jesper/Zotero/storage/LHCSHJEP/Trautmann and van de Kuilen - 2015 - Belief elicitation A horse race among truth serums.pdf
tags: [literature]
keywords: [belief-elicitation, proper-scoring-rules, truth-serums, incentive-compatibility, risk-aversion, ultimatum-game, experimental-economics]
topics: ["[[experimental-belief-elicitation]]"]
related: [Armantier2013, Bellemare2008, Fehr1999, Gneiting2007, Hossain2013, Offerman2009]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> We pit non-incentivised introspection against five revealed-preference mechanisms ('truth serums') in the elicitation of beliefs in a simple two-player game. We measure the additivity, the predictive power for own behaviour and the accuracy of each method. Beliefs from incentivised methods are better predictors of participants' own behaviour compared to introspection. However, introspection performs equally well as the truth serums in terms of accuracy and additivity. We also find that correction for risk aversion improves the additivity of scoring rule belief reports.

## Summary
The paper runs a controlled "horse race" comparing six methods for eliciting subjective beliefs in an ultimatum game: non-incentivised introspection plus five incentive-compatible mechanisms (truth serums) of increasing complexity. Coverage is full (20-page article extracted cleanly). The central question is empirical and pragmatic: do more theoretically robust (and more costly) elicitation methods actually deliver higher-quality belief data than cheap introspection, and does the extra machinery of risk-corrected methods pay off? The answer is largely negative. Across three quality criteria, the authors find no across-the-board advantage of complex methods. Introspection matches the truth serums on accuracy and additivity but loses on one dimension: predicting the respondent's own choices. The work is a methodological benchmark for the experimental belief-elicitation literature.

## Research question
Two linked questions: (i) Do truth serums provide higher-quality belief data than simple non-incentivised introspection? (ii) Among truth serums, do more complex (more theoretically robust) methods elicit better data than simpler ones? "Quality" is decomposed into internal validity (additivity of complementary probabilities; consistency of beliefs with own behaviour) and external validity (accuracy versus objective frequencies). The authors are deliberately agnostic about theoretical incentive compatibility, judging methods by empirical data quality, since applied researchers rarely know whether the underlying assumptions (risk neutrality, expected-utility maximisation) hold.

## Method / identification
Beliefs are elicited about uncertain events in a strategy-method ultimatum game (€20 pie, six allocations). Let $E$ be an uncertain event and $xEy$ a prospect paying $x$ if $E$ obtains and $y$ otherwise. Under expected utility the prospect is valued $B(E)U(x)+B(E^c)U(y)$ with $B(E^c)=1-B(E)$. Six methods:

- **Introspection**: directly state the probability $0$–$100$; flat €5 fee.
- **Outcome matching**: elicit the certainty equivalent $CE$ of $xE0$ via a 21-row choice list. Under expected-value maximisation $CE=B(E)x+(1-B(E))y$, so $B(E)=(CE-y)/(x-y)$.
- **Probability matching**: find $p$ with $xp y\sim xE y$. Since $w[B(E)]=w(p)\Rightarrow B(E)=p$, this is valid under EU, rank-dependent utility and prospect theory (most robust).
- **Quadratic scoring rule (QSR)**: offer the prospect $[a-b(1-r^2)]E(a-br^2)$ with $a,b>0$; the agent picks $r\in[0,1]$. The first-order condition $2bB(E)(1-r)=2br[1-B(E)]$ gives the optimum $r=B(E)$ for an expected-value maximiser. A single choice suffices ($a=b=€20$).
- **Outcome matching (corrected)**: under utility $U$, $B(E)=[U(CE)-U(y)]/[U(x)-U(y)]$; concave $U$ biases the raw estimate downward, so beliefs are corrected using a separately elicited CRRA power utility $U(x)=x^{\theta}$.
- **QSR (corrected)**: the Offerman, Sonnemans, van de [[@Offerman2009|Kuilen & Wakker (2009)]] refinement; elicit $r$ for known probabilities, fit a correction function $p=dr+cr^2$ per subject, then map the uncertain-event report via $B(E)=d^{*}r_E+c^{*}(r_E)^2$.

Design: 206 subjects, between-subject 4-treatment design (introspection, outcome matching, probability matching, scoring rule; the two corrected methods are derived within the matched treatments using stage-3 risk-attitude data). One stage and one decision are randomly selected for payment to block hedging and wealth effects. Internal validity is tested by whether beliefs in complementary events sum to 100% (additivity) and whether beliefs predict own play; accuracy is measured against the observed choice/acceptance frequencies (the experimenter knows the true frequencies). A separate control experiment ($N=162$) tests whether framing the QSR in terms of probabilities and stating that truthful reporting is optimal affects additivity.

## Data
Original lab data. 206 Tilburg undergraduates in the main experiment (102 proposers, 102 responders after exclusions), z-Tree, all randomisations by physical dice; plus 162 fresh undergraduates in the control experiment. Replication dataset and programs are archived with the article. Risk attitudes: 70.62% risk averse; mean (median) CRRA $\theta=0.978$ ($0.931$), significantly below the risk-neutral benchmark of $1$.

## Key findings
1. **No general benefit of complexity.** Few differences among the five truth serums on any criterion, and incentivised methods do not clearly beat introspection.
2. **Accuracy: a tie.** All methods beat random prediction, but introspection is as accurate as every truth serum. Beliefs are systematically distorted toward uniformity (conservatism, à la Edwards 1954): too optimistic about rarely-accepted offers, too pessimistic about likely-accepted ones — and crucially this conservatism appears for introspection too, so it is partly a property of belief formation, not elicitation.
3. **Additivity: a tie, with structure.** Non-additivity is strong for all five truth serums and worse for six events than for two (consistent with Tversky & Koehler's 1994 support theory); introspection sometimes outperforms incentive-compatible methods. The control experiment shows that probability framing and optimality claims do not improve additivity.
4. **Predicting own behaviour: truth serums win.** Truth serums beat random prediction for proposers' own choices across social-utility specifications, whereas introspection does not — the one dimension favouring incentivised methods. Predictive power is modest throughout, and objective probabilities clearly outperform subjective beliefs.
5. **Risk corrections work directionally but weakly.** The QSR correction significantly reduces the uniformity bias; the outcome-matching correction significantly raises the downward-biased reports. Both move in the predicted direction (significant at 5% by Wilcoxon tests) but the quantitative impact on accuracy is modest, plausibly because the correction functions are measured noisily.

## Contribution
The first systematic head-to-head comparison spanning a large set of belief-elicitation methods on both internal and external validity, and the first to include explicit risk corrections for outcome matching and the scoring rule within the comparison. Earlier work compared at most two methods and only on accuracy with mixed results (Huck & Weizsäcker 2002; Hollard et al. 2010; [[@Hossain2013|Hossain & Okui 2013]]). The practical takeaway: introspection is a defensible choice when accuracy and additivity matter, but incentive-compatible mechanisms add value when the goal is to predict an agent's own behaviour.

## Limitations & open questions
- Conservatism toward uniform beliefs is shared by introspection, so it is unclear how much is elicitation bias versus a genuine feature of subjective probability formation — disentangling these is open.
- Risk corrections underperform their theoretical promise, attributed to noisy estimation of the correction function; whether repeated/refined measurement recovers the benefit (at higher cost) is untested.
- The poor predictive performance of introspection may be specific to social-interaction tasks with moral/fairness motives; in individual decision tasks (health, finance) introspective beliefs may predict better — the moderating role of task domain is unresolved.
- Unmodelled social preferences (e.g. ~10% of responders reject the most generous offers) mean the belief-to-choice link is fit through a possibly misspecified social-utility function; richer preference models could change the prediction comparison.
- Corrections ignore ambiguity attitude; ambiguity-robust elicitation is left open.
- External validity beyond a student pool and a single game is untested.

## Connections
The formal apparatus builds on proper scoring rules introduced by Brier (1950) and de Finetti (1962), with the QSR popularised by McKelvey & Page (1986) and Nyarko & Schotter (2002); the broader theory of proper scoring rules is synthesised by [[@Gneiting2007|Gneiting & Raftery (2007)]]. The risk-correction of the QSR is the method of Offerman, Sonnemans, van de [[@Offerman2009|Kuilen & Wakker (2009)]], generalised by Kothiyal, Spinu & Wakker (2011); outcome-matching corrections follow Heinemann, Nagel & Ockenfels (2009), and the lottery-ticket route to inducing risk neutrality is Allen (1987) and [[@Hossain2013|Hossain & Okui (2013)]]. The hedging concern motivating random payment is from Blanco, Engelmann, Koch & Normann (2010) and [[@Armantier2013|Armantier & Treich (2013)]]. The substantive belief-and-play literature it speaks to includes Nyarko & Schotter (2002), Costa-Gomes & Weizsäcker (2008), Bellemare, Kröger & van [[@Bellemare2008|Soest (2008)]], Rey-Biel (2009) and Blanco, Engelmann & Normann (2011); the additivity/support-theory framing is Tversky & Koehler (1994), and conservatism is Edwards (1954). The ultimatum-game and social-preference backdrop ties to [[@Fehr1999|Fehr & Schmidt]] (1999, 2003). z-Tree is Fischbacher (2007).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
