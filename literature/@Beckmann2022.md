---
citekey: Beckmann2022
title: "Empowerment, Task Commitment, and Performance Pay"
authors: ["Beckmann, Michael", "Kräkel, Matthias"]
year: 2022
type: journalArticle
doi: 10.1086/718465
zotero: "zotero://select/library/items/DAQURII5"
pdf: /Users/jesper/Zotero/storage/EL6ZNQKN/20059appendix.pdf
tags: [literature]
keywords: [empowerment, task-commitment, performance-pay, intrinsic-motivation, principal-agent, personnel-economics, moral-hazard]
topics: ["[[motivated-agents-intrinsic-motivation]]"]
related: [Benabou2003, Besley2005, Cassar2018]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero) — From the published summary: Although from the viewpoint of social psychology task commitment is a driving force for intrinsic motivation in the workplace, this topic has been widely ignored in labor and personnel economics. The paper reduces this gap by offering a theoretical analysis of worker empowerment and task commitment, which also helps explain the observed variety of compensation schemes across workers and firms. Using a large-scale linked employer–employee panel data set, the authors present empirical evidence consistent with the predicted patterns of the theoretical model.

## Summary
Beckmann & Kräkel embed "empowerment" (granting a worker autonomy) into a standard principal–agent hidden-action model by assuming that empowerment endogenously produces *task commitment* — an extra utility the worker enjoys only when the task succeeds. Because this commitment-based intrinsic incentive and monetary performance pay are substitutes in the worker's incentive constraint, the model predicts that more committed (empowered) workers receive *less* performance pay, that empowerment is offered to high-skilled workers, and that it is more attractive when labor-market competition raises workers' outside options. A linked German employer–employee panel (LPP × IAB) yields evidence consistent with all three patterns.

## Research question
How does worker empowerment — autonomy over job-related decisions — affect optimal personnel policy (the empowerment decision plus the bonus/salary contract) once empowerment is recognized as a source of *task commitment* and hence intrinsic motivation? When do firms optimally substitute empowerment-driven intrinsic incentives for monetary performance pay, and to which workers and market conditions do they extend empowerment?

## Method / identification
**Theory.** A risk-neutral employer hires a risk-neutral worker who exerts unobservable effort $e$ to produce binary output $y\in\{y_L,y_H\}$, $y_L<y_H$. Success ($y=y_H$) occurs with probability $(1+\eta E)se$, where $s>0$ is skill, $E\in\{0,1\}$ is the empowerment dummy, and $\eta\in(-1,1)$ is the ambiguous productivity effect of empowerment (more effective effort vs. shirking/communication losses). Effort cost is $c(e)=\frac{\kappa}{2}e^2$. The novel ingredient: an empowered worker enjoys extra (non-verifiable) commitment utility $v\ge 0$ upon success, $v=0$ if $E=0$. A contract is a tuple $(E,F,b)$ — empowerment, fixed salary $F$, and success bonus $b$ — with limited liability $F,\,F+b\ge 0$ and worker outside option $s\bar u$.

The worker's incentive constraint gives effort $e=\frac{(b+E\theta)(1+\eta E)s}{\kappa}$ (with $\theta$ the commitment term, here $v$), so $b$ and $v$ enter additively — monetary and commitment incentives are perfect substitutes at the margin. Empowerment is efficient iff
$$v>-\frac{\eta}{1+\eta}\,\Delta y \;\equiv\; \hat v,\qquad \Delta y:=y_H-y_L.$$
The game is solved by backward induction (effort → contract → empowerment).

**Identification (empirical).** The commitment effect of empowerment is estimated with a *bracketing-property* strategy: a fixed-effects (FE) within estimator and a lagged-dependent-variable (LDV) POLS estimator bracket the causal effect $[\hat\alpha_{LDV},\hat\alpha_{FE}]$, combined with a selection-on-observables design (a large covariate set grounded in the "three-legged-stool" organizational-architecture theory plus control-aversion confounders à la Falk–Kosfeld). Robustness checks address attenuation (measurement-error) bias and serial correlation. Empowerment $E_Z$ is a double-standardized z-score of job autonomy (AUT) and work-from-home (WFH); task commitment $v_Z$ is a double-standardized score of the nine-item Utrecht Work Engagement Scale (vigor, dedication, absorption).

## Data
German linked employer–employee panel data: the **Linked Personnel Panel (LPP)** — employee surveys on HR, corporate culture, and management practices — merged with the **IAB Establishment Panel**, representative of the processing industry and service sector. The merged data identify empowerment, task commitment, performance pay, skills, training, and labor-market-competition proxies (poaching activity, regional unemployment rate). One regression block reports n ≈ 766 employees / N ≈ 1,042 observations.

## Key findings
- **Proposition 1 (optimal contract).** There exist cutoffs $\bar u_2(E)>\bar u_1(E)>0$ such that: (i) for low outside options ($\bar u\le\bar u_1$), $F^*=0$ and $b^*=\frac{1}{2}\max\{\Delta y-vE,0\}$ — the worker earns a rent; (ii) for intermediate $\bar u$, $F^*=0$ with $b^*=\max\{2\kappa s\bar u/[(1+\eta E)s]-Ev,\,0\}$; (iii) for high $\bar u$, a positive salary $F^*$ is paid and $b^*=\Delta y$ (efficient effort). The bonus falls in commitment $v$ and can hit zero: **a monotone inverse relationship between task commitment and performance pay.**
- **Proposition 2 (empowerment, skills, competition).** If empowerment is efficient ($v>\hat v$): (i) $\Pi^*(1)>\Pi^*(0)$ — efficient empowerment is always chosen; (ii) $\partial\Delta\Pi^*/\partial s>0$ — empowerment is more profitable for **high-skilled** workers (skill–effort complementarity); (iii) $\partial\Delta\Pi^*/\partial\bar u\ge 0$ — empowerment is more attractive under **stronger labor-market competition** (higher outside options).
- **Hidden-information extension.** With private information about either task commitment or ability, firms optimally use a **menu of empowerment / nonempowerment contracts as a self-selection device**; the comparative-statics patterns for skills and competition remain qualitatively unchanged.
- **Empirical.** A positive commitment effect of empowerment on work engagement is confirmed (point estimate declines from 0.224 to 0.084 after controls but stays highly significant); performance pay decreases with the empowered worker's task commitment; empowerment is more prevalent among high-skilled workers and under intense competition for labor.

## Contribution
The paper imports the management/social-psychology constructs of *empowerment*, *psychological ownership*, and *task commitment* into labor and personnel economics, formalizing them inside a tractable moral-hazard model. It rationalizes the empirically observed heterogeneity of compensation schemes as the optimal substitution of intrinsic (commitment) for monetary incentives, and — unusually for this theoretical literature — pairs the model with a complementary large-scale empirical test on linked employer–employee data.

## Limitations & open questions
The authors flag two explicit limitations. (1) The **psychological microfoundation is not pinned down**: the empowerment→commitment mapping could be driven by psychological ownership, by reciprocity, or by control aversion (Falk & Kosfeld 2006; Schnedler & Vadovic 2011); the empirical design confirms the effect but cannot discriminate among these mechanisms. (2) The empirical results **cannot distinguish hidden action from hidden information** — observed patterns are consistent with both theoretical regimes. Further open hooks: the net productivity effect of empowerment ($\eta$) is assumed ambiguous and not separately identified; negative emotions from failure are assumed away for tractability; and the model abstracts from multi-task/team interactions where empowerment may distort coworker beliefs.

## Connections
The commitment-utility device builds directly on Friebel & Schnedler (2011) and Kräkel (2018), the only prior economic papers modeling empowerment-induced task commitment, but adds skills, competition, and an empirical test. It sits within the behavioral literature on nonmonetary incentives and meaningful work surveyed by [[@Cassar2018|Cassar & Meier (2018)]] — Murdock (2002), Glazer (2004), Francois (2000), [[@Besley2005|Besley & Ghatak (2005)]], Delfgaauw & Dur (2007, 2008), Cassar (2019), and Cassar & Armouti-Hansen (2020) on mission-oriented motivation. The link between empowerment, authority, and intrinsic motivation connects to Bénabou & [[@Benabou2003|Tirole]] (2003, 2006) and to the experimental work on the intrinsic value of decision rights by Fehr, Herz & Wilkening (2013) and Bartling, Fehr & Herz (2014); job-design screening relates to Bartling, Fehr & Schmidt (2012) and Delfgaauw & Dur (2007). The econometric bracketing logic draws on Angrist & Pischke (2009), Keele & Kelly (2006), and Ding & Li (2019).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
