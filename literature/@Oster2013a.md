---
citekey: Oster2013a
title: "Optimal expectations and limited medical testing: evidence from Huntington disease"
authors: ["Oster, Emily", "Shoulson, Ira", "Dorsey, E. Ray"]
year: 2013
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/5BD4HH78"
pdf: /Users/jesper/Zotero/storage/CSXZMVR9/Oster2013a.pdf
tags: [literature]
keywords: [optimal-expectations, information-avoidance, anticipatory-utility, motivated-beliefs, genetic-testing, structural-estimation]
topics: []
related: [Brunnermeier2005, Caplin2001]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We use novel data to study the decision to undergo genetic testing by individuals at risk for Huntington disease (HD), a hereditary neurological disorder that reduces healthy life expectancy to about age 50. Although genetic testing is perfectly predictive and carries little financial or time cost, less than 10 percent of at-risk individuals are tested prior to the onset of symptoms. Testing rates are higher for individuals with higher ex ante risk of carrying the genetic expansion for HD. Untested individuals express optimistic beliefs about their probability of having HD and make fertility, savings, labor supply, and other decisions as if they do not have HD, even though individuals with confirmed HD behave quite differently. We show that these facts are qualitatively consistent with a model of optimal expectations (Brunnermeier and Parker, 2005) and can be reconciled quantitatively in this model with reasonable parameter values. This model nests the neoclassical framework and, we argue, provides strong evidence rejecting the assumptions of that framework. Finally, we briefly develop policy implications.

## Summary

Oster, Shoulson, and Dorsey document that fewer than 10% of people at risk for Huntington disease take a cheap, perfectly predictive genetic test, that untested individuals systematically under-perceive their risk and act as if they are healthy even at very high objective risk, and that testing rises with ex ante risk. They argue these joint facts are well explained by an *optimal expectations* model (Brunnermeier and Parker, 2005), in which agents derive anticipatory utility and can choose optimistic beliefs while untested but lose that option once tested. The model fits the data quantitatively with a real testing cost roughly two orders of magnitude below the cost of mismatched action, and they argue the neoclassical (no-anticipation) benchmark is rejected both qualitatively and quantitatively.

## Research question

Why do so few at-risk individuals undergo medical testing when the test is perfectly informative and nearly costless? More specifically: what model of beliefs and behavior can jointly explain (i) low predictive testing rates, (ii) downward-biased subjective risk perceptions, (iii) "healthy-matched" actions even among high-risk untested individuals, (iv) testing that rises with ex ante risk, and (v) frequent *confirmatory* testing once symptoms appear?

## Method / identification

The paper combines a descriptive analysis with a structural optimal-expectations model and a structural estimation. The model has a binary state $s\in\{0,1\}$ (sick / healthy) with prior $p=E(s)$, a binary action $a\in\{0,1\}$, and three periods. At time 0 the agent chooses whether to test at real cost $C$; at time 1 the agent picks an action and experiences anticipatory utility (down-weighted by $\delta\in[0,1]$); at time 2 the state is revealed and consumption utility is paid. The key assumption: if *untested*, the agent may adopt a belief $\pi\in[0,1]$ that differs from $p$, but must act consistently with $\pi$. The untested objective is

$$U(\pi\mid p)=\delta\,E(u(\hat a,s)\mid\pi)+E(u(\hat a,s)\mid p),\qquad \hat a(\pi)=\arg\max_a E[u(a,s)\mid\pi].$$

Payoffs are $u(0,0)=1$, $u(1,1)=0$, $u(1,0)=1-\Phi$, $u(0,1)=-\Omega$, with $\Phi,\Omega<1$ (so the agent values being healthy more than acting correctly). If tested, beliefs are pinned to $p$ but the agent can act optimally ($a=s$), giving $(1+\delta)[p\,u(1,1)+(1-p)\,u(0,0)]$. The estimation imposes $C_i\sim \mathrm{Unif}[0,0.01]$ and $\Phi_i=\Omega_i\sim\mathrm{Unif}[\alpha,\alpha+\beta]$ with a single $\delta$, fitting 10 behavioral moments (group-level action and testing rates by motor-score group) via method-of-moments matching. The neoclassical case is the restriction $\delta=0$, re-estimated with separately free supports for $\Phi_i$ and $\Omega_i$ to equalize degrees of freedom.

## Data

The PHAROS (Prospective Huntington At Risk Observational Study) prospective observational study: 1001 at-risk individuals (one parent/first-degree relative with HD), all untested and symptom-free at enrollment, at ~40 US/Canada sites, interviewed roughly every nine months from 1999 to 2010. Four data elements are used: investigator confidence of carrying the expansion (0-4 scale, with 4 = $\geq99\%$ confidence) plus motor score (0-154); subjective probability (self-reported 0-100); testing status (inferred for ~80% of tested individuals via Oster et al. 2010); and a "Life Experience Survey" capturing choice-relevant events (marriage, pregnancy, divorce, new job, major financial change, church/recreation change, retirement). Supplementary survey evidence: a 300-person Mechanical Turk survey on preferred timing (too-early vs. too-late) of marriage, childbearing, retirement. The sample is ~two-thirds female and highly educated (limiting external validity). Appendix B draws on existing HIV-testing and cancer-screening literature.

## Key findings

- **Descriptive facts.** Predictive testing is ~5-7%; financial cost is only a few hundred dollars; 60% cite "preference for living with uncertainty" as a reason not to test vs. 20% citing financial cost. Among those the investigator rates $\geq99\%$ likely to carry the expansion, mean self-perceived risk is only 52% and 11% report *zero* chance. A regression of self-perception on objective risk yields a slope of ~0.09 (vs. 1 under rationality). Uncertain individuals behave like those *certain they are healthy*, not intermediate, even at $\geq98\%$ objective risk. Confirmatory testing is common (30% in PHAROS; 75% in COHORT among symptomatic untested).
- **Lemma 1.** The untested agent chooses $a=0$ iff $\pi\le \Phi/(\Phi+\Omega)$ (cutoff $=0.5$ under $\Phi=\Omega$).
- **Proposition 1 (belief choice).** The agent always chooses $\pi\le p$ (over-optimism), choosing $\pi=0$ for $p\le p^*$ where $p^*=\frac{\Phi}{\Phi+\Omega}+\frac{\delta\Phi(1-\Omega)}{(\Phi+\Omega)^2}>\frac{\Phi}{\Phi+\Omega}$.
- **Proposition 2 (skewed action).** $a=0$ is chosen for $p\le p^*$; under $\Phi=\Omega$ this yields the "act healthy" choice for some $p>0.5$.
- **Proposition 3 (testing).** With low anticipation ($\delta<\Omega$) the value of testing is positive only above cost thresholds and is maximized at $p^*$; with high anticipation ($\delta\ge\Omega$) testing value is negative for all $p$ — these agents *never* test, so all testing variation comes from low-$\delta$ agents.
- **Estimation.** The fitted $\Phi_i$ distribution is compressed and very close to $\delta$, implying most agents are near-indifferent to testing or never test; the utility loss from a wrong action is ~180 times the real testing cost. Confirmatory testing is rationalized for $\Psi>C$.
- **Neoclassical rejection (Prop. 5, $\delta=0$).** Beliefs are accurate (cannot match bias); skewed actions up to $p=0.9$ require $\Phi\ge 9\Omega$, contradicting MTurk evidence (55%/57%/50% prefer "too late" — no asymmetry); the restricted fit is worse and implies the wrong action when "healthy" is ~10,000 times worse than when "sick," plus testing costs ~6× the wrong-action cost. Cross-country evidence (Canada 7% vs. US 5% despite lower Canadian cost) further undermines cost-driven explanations.
- **Policy counterfactuals.** Cutting testing cost to zero raises testing only to ~10%; reducing $\delta$ or raising the value of correct action moves testing far more.

## Contribution

First, a rich longitudinal dataset documenting four interlocking facts (low testing, biased beliefs, healthy-skewed actions, testing increasing in risk) for a setting with a perfectly predictive, low-cost test. Second, an extension of the Brunnermeier-Parker optimal-expectations framework to endogenous information acquisition, deriving belief, action, and testing predictions and estimating it structurally. Third, a sharper rejection of the neoclassical information-seeking benchmark — going beyond the "low testing despite low cost" puzzle to show the model also cannot accommodate biased beliefs or confirmatory testing without implausible loss asymmetries. Fourth, suggestive external evidence (HIV, cancer screening) and policy levers implying that salience of consequences, not test cost, is the effective margin.

## Limitations & open questions

- The authors flag that the model predicts *all* $a=0$ agents report $\pi=0$, but observed beliefs cluster near $\pi=0.4$ (a 50% focal point); they propose adding a psychic cost of mis-reporting or reinterpreting any $\pi<0.5$ as "thinks healthy" — left unmodeled.
- The key assumption that testing fully shuts down belief manipulation suits perfectly accurate tests (HD, HIV); they explicitly flag *partial* belief restriction under imperfect tests as an interesting extension.
- The PHAROS sample is non-random (willing participants, untested and symptom-free at enrollment, two-thirds female, highly educated), cautioning extrapolation; behavior of the tested may differ from the untested.
- The Life Experience Survey is coarse (binary, no intensity, ambiguous "major financial change"), and behaviors are not all true "choices."
- Welfare is delicate: biased beliefs are *privately optimal*, so forced testing can reduce welfare; the social case for encouraging testing (contagion in HIV, under-saving externalities) needs the externality, not paternalism.
- The optimal-expectations vs. wishful-thinking (Mayraz, 2011) distinction is weakly identified; the data only mildly favors optimal expectations.

## Connections

The core model is an information-acquisition extension of [[@Brunnermeier2005|Brunnermeier and Parker (2005)]]'s optimal expectations. Anticipatory utility traces to [[@Caplin2001|Caplin and Leahy (2001]], 2004) and the broader belief-dependent utility literature. Closely related belief-distortion models include Mayraz (2011) on wishful thinking, Yariv (2005), and Benabou and Tirole (2002) on self-confidence; the principal-agent information-provision variant is Koszegi (2006), while Koszegi (2003) studies information-averse preferences and health and is the paper's closest competing explanation. The low-testing puzzle echoes earlier work by Koszegi (2003), Lerman et al. (1996), and Thornton (2008), and HD-specific evidence in Shoulson and Young (2011) and Oster et al. (2008, 2010). The psychology of avoiding bad news draws on Dawson, Gilovich, and Regan (2002). The under-optimization analogy (slow beneficial action) references Choi et al. (2011) on retirement savings. The work sits in a broader behavioral-economics tradition on motivated beliefs and information avoidance that connects to Benabou and Tirole's self-signaling research and to the experimental information-avoidance literature.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
