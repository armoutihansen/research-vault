---
citekey: Gottlieb2021
title: Lapse-Based Insurance
authors: ["Gottlieb, Daniel", "Smetters, Kent"]
year: 2021
type: journalArticle
doi: 10.1257/aer.20160868
zotero: "zotero://select/library/items/AELA8UET"
pdf: /Users/jesper/Zotero/storage/QQS67BHH/gottlieb-smetters-2021-lapse-based-insurance.pdf
tags: [literature]
keywords: [life-insurance, lapse-supported-pricing, behavioral-contract-theory, narrow-framing, forgetfulness, liquidity-shocks, competitive-screening]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Most individual life insurance policies lapse, with lapsers cross-subsidizing non-lapsers. We show that policies and lapse patterns predicted by standard rational expectations models are the opposite of those observed empirically. We propose two behavioral models consistent with the evidence: (i) consumers forget to pay premiums and (ii) consumers understate future liquidity needs. We conduct two surveys with a large insurer. New buyers believe that their own lapse probabilities are small compared to the insurer's actual experience. For recent lapsers, forgetfulness accounts for 37.8 percent of lapses while unexpected liquidity accounts for 15.4 percent. (JEL D91, G22, G52)

## Summary
Most individual life insurance policies are surrendered ("lapse") before paying a death benefit, and insurers price this in: lapsers cross-subsidize non-lapsers ("lapse-supported pricing"). Gottlieb and Smetters show that a rational-expectations benchmark predicts the *opposite* of what the data show, then build two behavioral competitive-market models (consumers who forget to pay premiums; consumers who underweight future liquidity shocks) that endogenously generate front-loaded, lapse-based policies with above-market policy loans. Two surveys with a large US insurer ("LLI") provide the direct evidence: new buyers massively underestimate their own lapse risk, and recoded lapser responses attribute 37.8% of lapses to forgetfulness and 15.4% to liquidity shocks.

## Research question
Why do most individual life insurance policies lapse, why do insurers appear to price *for* lapsing (front loads, expensive policy loans, lapsers subsidizing stayers) when the conventional rational view says front loads should be set to *prevent* lapses, and what behavioral mechanism can jointly explain both the demand-side lapse patterns and the supply-side contract structure?

## Method / identification
Two ingredients: (1) competitive contracting models and (2) survey field evidence.

The theory is a three-period competitive insurance market with $N\ge 2$ profit-maximizing firms, a continuum of households (one decision-maker plus an heir), no exogenous restriction on the contract space, one-sided commitment (consumers may drop their policy), and no discounting (net interest normalized to 0). A contract is a vector of state-contingent payments $T_j \equiv (t_{1,j}, t^{R}_{2,j}, t^{R,A}_{3,j}, t^{R,D}_{3,j}, t^{F,A}_{3,j}, t^{F,D}_{3,j})$, indexed by remembering ($R$) versus forgetting ($F$) the period-2 premium and by being alive ($A$) versus dead ($D$) in period 3. Because assets are illiquid, payments map one-to-one to state-contingent consumption $C_j$. Utility is $u_A(c)$ when alive and $u_D(c)$ (bequest) when dead, both strictly increasing, strictly concave, twice differentiable, satisfying Inada conditions. Death probability is $\alpha$.

Model 1 (forgetting): in period 2 a consumer forgets to pay with probability $l\in(0,1)$; the focus is on *naïve* consumers who do not anticipate forgetting (a sophisticated benchmark is in the appendix). Firms observe non-payment but not whether it was strategic.

Model 2 (liquidity): consumers face a background loss $L$ but underweight it when buying (narrow framing or optimistic beliefs). Lapsing and policy loans arise endogenously; a key feature is that lack of commitment (renegotiation-proofness) imposes a *pure state constraint*, making the optimal control problem nonstandard. The authors solve it and offer the technique as portable to other mechanism-design problems with both incentive and renegotiation-proofness constraints (Theorem 1, proved in online Appendix A).

The empirical identification is two surveys fielded with LLI (an A++-rated US insurer): a new-buyers survey (term buyers Oct 2013–Nov 2017, still paying; ~13% response, 1,689 respondents) eliciting ex ante beliefs, and a recent-lapsers survey (lapsed Jan 2012–Nov 2017; ~4.9% response, 157 respondents) eliciting ex post reasons. Stylized facts are corroborated with LIMRA data, HRS regressions (following Fang and Kung), and Compulife (2013) quotes priced against Society of Actuaries (2008) mortality tables to compute actuarial profit-by-policy-year.

## Data
LLI administrative + survey data (matched demographics, policy type/size); LIMRA (2011, 2012) industry lapse statistics; HRS waves (health-shock vs lapse correlations); Compulife (2013) quotation system for 56 California 20-year $500k term policies; 2,854 LLI term policies that lapsed 2012–2017; Society of Actuaries (2008) mortality tables; actuary trade presentations and bankruptcy-proceeding disclosures as anecdotal evidence on lapse-supported pricing.

## Key findings
Stylized facts: 29% of permanent policyholders lapse within 3 years, 57% within 10; ~88% of universal-life policies never pay a benefit. Lapses are *not* positively correlated with health shocks (against reclassification risk), are more frequent for smaller policies and younger buyers, and rise in recessions—pointing to liquidity. Compulife pricing shows insurers profit on lapsers and lose on stayers; only ~4.2% of lapsed LLI policies lapsed at a loss.

Survey: 94.2% of new buyers either did not anticipate lapsing (80.4%) or had not thought about it (12.0%), versus an insurer-implied ~60% lifetime lapse rate. Beliefs about future income losses were uncorrelated with own-lapse beliefs—consistent with narrow framing, not optimism. Recoded lapser reasons: forgetfulness 37.8%, income/cost shocks 15.4%.

Theory. **Proposition 1**: the lapser-to-stayer cross-subsidy $t_1\equiv I_1-c_1\ge 0$ is weakly positive, strictly positive when $(1-l)\,u'(I_1)<u'(I_2)$; with high enough income and forgetting probability the equilibrium is a long-term policy that endogenously lapses on a missed payment, profiting on forgetters and losing on payers. The sophisticated benchmark instead yields either no lapses or profits on rememberers and losses on forgetters, and firms would *choose* to send payment reminders—counterfactual. **Proposition 2** (liquidity, behavioral): policyholders never lapse absent a shock; with a shock they lapse, get perfect conditional smoothing, and pricing is lapse-supported with $\pi^{S}=W>0$ and $\pi^{NS}=-\frac{l}{1-l}W<0$; if the lapse condition fails they instead take above-market policy loans ($\pi^{S}>0>\pi^{NS}$). **Proposition 3** (closed form, $L\sim U[0,\bar L]$, $u(c)=\ln c$): loans are capped at $\tau$, offered at above-market rates so future consumption falls by more than the loss ($c_A'(L)=c_D'(L)<-1$ for $L<\tau$), and losses above $\tau$ trigger lapse. **Theorem 1**: with a loss continuum, consumers lapse iff $L>\tau$, large losses lapse into full re-insurance, small losses borrow, $c_1(L)-L$ is nondecreasing, profits are nondecreasing in $L$, and the insurer earns $W$ per lapser while losing $W/(1-F(\tau))$ on average per stayer. **Proposition 4** (rational expectations): the *opposite* pattern—small losses lapse, large losses borrow; the policy sets a borrowing *floor* not a cap, loans are *subsidized*, and consumers over-consume in period 1—predictions inconsistent with the data.

## Contribution
Provides a unified demand-and-supply explanation of lapse-based insurance, showing the rational benchmark is sign-reversed relative to observed contracts and lapse behavior, and supplying both two behavioral equilibrium models and direct survey identification of the mechanisms. Methodologically, it solves a competitive-screening problem with one-sided commitment where renegotiation-proofness introduces a pure state constraint, offering a reusable optimal-control technique. It is among the behavioral-IO / behavioral contract theory literature on firms exploiting consumer biases.

## Limitations & open questions
The lapser-survey sample is small (157 respondents, ~7.8% margin of error) with a 47.1% "Other" bucket that required subjective recoding. Together the two mechanisms explain only "a small majority" of lapses, leaving the remainder unexplained. Beliefs are elicited from recent buyers, not at the moment of purchase (asking ex ante might itself change the decision). The models assume fully illiquid outside assets and abstract from adverse selection by assuming homogeneous losses; relaxing these is open. Welfare and policy implications (e.g., mandatory payment reminders, since firms facing naïve consumers will not voluntarily remind) and disentangling narrow framing from biased beliefs as the liquidity-underweighting microfoundation remain open.

## Connections
The rational reclassification-risk benchmark is Hendel and Lizzeri (2003), extended by Daily, Hendel, and Lizzeri (2008) and Fang and Kung (2010, 2012); calibrated life-cycle simulations are Hambel et al. (2017) and Krebs, Kuhn, and Wright (2015). The narrow-framing mechanism draws on Barberis, Huang, and Thaler (2006), Read, Loewenstein, and Rabin (1999), and Rabin and Weizsäcker (2009); related insurance-mistakes work includes Abaluck and Gruber (2011), Handel and Kolstad (2015), Bhargava, Loewenstein, and Sydnor (2015), and Baicker, Mullainathan, and Schwartzstein (2015). Imperfect memory / forgetting connects to Bénabou and Tirole (2016), Ericson (2011), and Karlan et al. (2016); biased beliefs/overconfidence to Spinnewijn (2015), Grubb (2009), and Malmendier and Tate (2005). The present-bias alternative is dispatched via Gottlieb and Zhang (2021), DellaVigna and Malmendier (2004), and Heidhues and Kőszegi (2010). Surveys of the behavioral-IO frame are Ellison (2005), Kőszegi (2014), and Grubb (2015), with firm-exploits-bias models by Eliaz and Spiegler (2006, 2008, 2011) and Bordalo, Gennaioli, and Shleifer (2016).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
