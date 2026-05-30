---
citekey: Zimmerman2010
title: Neighborhood Context and the Gender Gap in Adolescent Violent Crime
authors: ["Zimmerman, Gregory M.", "Messner, Steven F."]
year: 2010
type: journalArticle
doi: 10.1177/0003122410386688
zotero: "zotero://select/library/items/NWWZWP6N"
pdf: /Users/jesper/Zotero/storage/6LAEPREJ/Zimmerman2010.pdf
tags: [literature]
keywords: [gender-gap, violent-crime, neighborhood-disadvantage, peer-effects, multilevel-models, item-response-theory, criminology]
topics: []
related: [Johnson2003, Jones2009]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Research consistently demonstrates that females engage in less criminal behavior than males across the life course, but research on the variability of the gender gap across contexts is sparse. To address this issue, we examine the gender gap in self-reported violent crime among adolescents across neighborhoods. Multilevel models using data from the Project of Human Development in Chicago Neighborhoods (PHDCN) indicate that the gender gap in violent crime decreases as levels of neighborhood disadvantage increase. Furthermore, the narrowing of the gender gap is explained by gender differences in peer influence on violent offending. Neighborhood disadvantage increases exposure to peer violence for both sexes, but peer violence has a stronger impact on violent offending for females than for males; this produces the reduction in the gender gap at higher levels of disadvantage. We also find that the gender difference in the relationship between peer violence and offending is explained, in part, by (1) the tendency for females to have more intimate friendships than do males and (2) the moderating effect of peer intimacy on the relationship between peer violence and self-reported violent behavior.

## Summary
Zimmerman and Messner ask whether the well-established individual-level gender gap in violent offending is constant across local social contexts, and if not, what produces the variation. Using three-level (item-within-person-within-neighborhood) Rasch/HLM models on Chicago longitudinal data, they show the male-female gap in adolescent violent crime *narrows* as neighborhood concentrated disadvantage rises. Their initial control-theory mechanism (disadvantage raises exposure to violent peers more for girls) is rejected: exposure rises equally for both sexes. Instead, the gap closes because violent peers exert a *stronger effect on offending for females than for males*, and this differential is partly explained by girls' more intimate friendships, which amplify peer influence. The result is a person-in-context argument: even a covariate as powerful as gender is conditioned by neighborhood structure.

## Research question
Does the gender gap in adolescent violent offending vary across neighborhoods, and—if it narrows in disadvantaged areas—through what mechanism? The paper advances two formal hypotheses framed as cross-level interactions: (1) the effect of gender on violent offending decreases as neighborhood disadvantage increases; (2) the effect of disadvantage on exposure to violent peers is stronger for females than for males (the proposed explanation for (1)).

## Method / identification
The estimator is a multivariate, multilevel **Rasch / item-response model** embedded in a three-level hierarchical generalized linear model (HGLM), estimated with generalized estimating equations and robust standard errors in HLM 6. Dichotomous violent-crime items are nested within persons nested within neighborhoods. The level-one (item-within-person) model expresses the log-odds $\eta_{tijk}$ of an affirmative response to item $i$ at wave $t$ by person $j$ in neighborhood $k$ as a quadratic function of (age-centered) time plus item severity:
$$\eta_{tijk}=\pi_{0jk}+\pi_{1jk}D_{tjk}+\pi_{2jk}D_{tjk}^{2}+c_{tijk}$$
where $D_{tjk}$ is age centered over waves and $\pi_{0jk}$ is the latent person propensity to violence (assumed normal on a logit metric, weighted for item seriousness/frequency). The level-two (person) model lets propensity vary with individual covariates and a random person effect $m_{jk}$:
$$\pi_{0jk}=\beta_{0k}+\beta_{1k}X_{1k}+\cdots+\beta_{nk}X_{nk}+m_{jk}$$
The level-three (neighborhood) model lets neighborhood mean propensity depend on concentrated disadvantage plus a random neighborhood effect $y_k$, and the key step is letting the **slope of gender vary randomly across neighborhoods** and then explaining that slope with disadvantage:
$$\beta_{\text{GENDER}\,k}=\gamma_{\text{GENDER}0}+\gamma_{\text{GENDER}1}(\text{Disadvantage})_{k}+a_{k}$$
The full model thus contains the cross-level $\text{GENDER}\times\text{Disadvantage}$ interaction. A parallel two-level model regresses the peer-violence scale on gender, disadvantage, and their interaction to test mechanism hypothesis (2). When that fails, the authors add a $\text{GENDER}\times\text{PeerViolence}$ interaction to the offending model, then a $\text{PeerViolence}\times\text{PeerIntimacy}$ interaction. Significance of the cross-level interaction is judged by BIC comparison of models with vs. without it. Identification rests on within-neighborhood variation in the gender slope plus the wealth of repeated item-level observations (~420 observations per neighborhood); covariates are grand-mean centered to ease interpretation and reduce collinearity.

## Data
**Project on Human Development in Chicago Neighborhoods (PHDCN).** The longitudinal cohort study supplies 1,502 adolescents from the age-12 and age-15 cohorts, interviewed across three waves (1994-2002, ~2.5 years apart), spanning the peak offending years (mean ages 13.5, 15.5, 18.1). Subjects are nested in 70 neighborhood clusters (collapsed from 78/80 sampled clusters; average ~21 subjects per cluster). The dependent variable is self-reported participation in up to eight violent acts (e.g., hitting, attacking with a weapon, robbery, arson, gang fighting) per wave, yielding 30,160 item responses; violence is rare (only "hitting someone," 26%, exceeds 30% threshold). Neighborhood **concentrated disadvantage** is a factor-score index from six 1990-census variables (poverty, public assistance, non-intact families, unemployment, median income, % non-White); immigrant concentration and residential instability are controls. Peer violence is a four-item friend-behavior scale ($\alpha=.70$); peer intimacy a three-item friendship-quality scale. Rich individual/family controls (self-control, IQ, victimization, externalizing/internalizing problems, family structure, SES, immigrant generation, race/ethnicity).

## Key findings
- **Gap narrows with disadvantage.** At the mean, males' odds of offending are ~77% higher than females'; the cross-level $\text{Male}\times\text{Disadvantage}$ interaction is negative and significant ($-.178^{*}$, robust to full controls at $-.207^{*}$). At +1 SD of disadvantage the male premium falls to ~45%, reaching nonsignificance at +1.4 SD (≈10% of neighborhoods).
- **Proposed mechanism rejected.** Disadvantage raises exposure to violent peers for *both* sexes ($\text{Disadvantage}=.200^{***}$) but the $\text{Male}\times\text{Disadvantage}$ interaction on peer violence is null ($p=.653$)—exposure rises equally.
- **Actual mechanism: differential peer susceptibility.** Adding $\text{Male}\times\text{PeerViolence}$ ($-.408^{***}$) shows violent peers affect *female* offending more strongly; this interaction absorbs the gender/disadvantage interaction (which becomes nonsignificant, $p=.149$).
- **Victim-retaliation explanation rejected.** Gender does not moderate peer-violence→victimization ($p=.540$) nor victimization→offending ($p=.539$).
- **Intimacy partially explains it.** Girls have more intimate friendships; a significant $\text{PeerViolence}\times\text{PeerIntimacy}$ interaction ($.090^{***}$) shows peer influence is amplified by friendship quality, partly accounting for the female susceptibility—though it does not fully explain it ($\text{Male}\times\text{PeerViolence}$ remains $-.370^{***}$).
- Variance decomposition: ~14.8% of reliable variation lies between items, 73.5% between individuals, 6.6% between neighborhoods, 5.2% between sexes; net of controls <1% remains between neighborhoods.

## Contribution
First explicitly **multilevel** treatment of the gender gap in violent offending, filling the gap between individual-level and large-aggregate (city/country) studies by exploiting localized neighborhood clusters. It demonstrates that gender's effect is *context-conditioned*, and—methodologically—shows how a random gender slope plus cross-level interactions can both detect contextual moderation and adjudicate among competing mechanisms (control theory vs. social learning vs. victim-retaliation). Substantively it relocates the explanation from differential *exposure* to differential *susceptibility* to violent peers, integrating control theory (disadvantage erodes informal social control, raising exposure for both sexes) with social-learning theory (peer effects, stronger for females) rather than treating them as competitors, and reaffirms feminist "gendered lives" arguments that peer influence is not gender-universal.

## Limitations & open questions
Explicit limitations and open problems the authors flag:
- **Neighborhood assignment / measurement error:** neighborhood variables attach to wave-one residence; movers create error. The "residence vs. offense location" problem is unresolved because PHDCN lacks offense locations—knowing where youths offend is important for the mechanism.
- **Generalizability:** the Chicago-bounded sample is likely more criminogenic than the average U.S. neighborhood ("how bad are the bad neighborhoods?").
- **Peer-measure weaknesses:** same-source bias (perceived friend behavior may mirror own), no count of friends, and no gender composition of peer groups—so same-sex vs. mixed-gender peer effects cannot be separated.
- **Discrepancy with prior work:** their finding (peers matter more for females) contradicts Heimer and De Coster (1999, peers matter more for males); reconciling this (measurement? specification?) is "an important task for future research."
- **Mechanism still incomplete:** peer intimacy does not fully account for the gender difference in peer influence. Open questions: how much time each sex spends with violent vs. non-violent peers; how friendship-group gender composition differs; whether mixed-gender vs. same-sex groups influence girls differently; gendered victimization by violent peers and coping (linking to intimate-partner-violence literature).
- The proposed disadvantage → weakened social control → peer exposure → offending causal chain needs to be "documented more directly and theorized more fully."

## Connections
Builds methodologically on Sampson, Raudenbush, and colleagues' PHDCN work and the multivariate multilevel Rasch approach ([[@Johnson2003|Raudenbush, Johnson, and Sampson 2003]]; Sampson, Morenoff, and Raudenbush 2005; Osgood et al. 2002; De Boeck and Wilson 2004). Theoretically it sits between control theory (Hirschi 1969; Shaw and McKay 1942; Sampson and Lauritsen 1994), social-learning/differential-association traditions (Sutherland and Cressey 1974; Akers 1998; Warr 2002; Agnew 1991 on friendship quality), and feminist criminology / pathways frameworks (Daly 1998; Miller 2001, 2008; [[@Jones2009|Jones 2009]]; Miller and Mullins 2006). It directly engages the gender-gap-over-contexts literature (Steffensmeier and Haynie 2000; Heimer, Wittrock, and Unal 2006; Schwartz et al. 2009) and contests Heimer and De Coster (1999) on the direction of gendered peer effects. For an economist working on social preferences and choice modeling, the paper is a clean example of (i) hierarchical IRT as a measurement-cum-behavioral model and (ii) using cross-level interactions to test whether a stable individual trait's behavioral mapping is moderated by environment—relevant to context-dependent preference estimation.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
