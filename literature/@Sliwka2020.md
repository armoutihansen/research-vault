---
citekey: Sliwka2020
title: "Bonus Plans, Subjective Performance Evaluations, and Career Concerns"
authors: ["Zimmermann, Klaus F.", "Sliwka, Dirk"]
year: 2020
type: bookSection
doi: 10.1007/978-3-319-57365-6_119-1
zotero: "zotero://select/library/items/BLMWKUSB"
pdf: /Users/jesper/Zotero/storage/JR8LKGFP/Sliwka2020.pdf
tags: [literature]
keywords: [principal-agent-model, incentives, social-preferences, career-concerns, subjective-performance-evaluation, crowding-out, behavioral-contract-theory]
topics: ["[[social-preferences-contract-theory]]"]
related: [Aggarwal1999, Akerlof1982, Ariely2009, Benabou2006, Bolton2000, Carpenter2016, Dufwenberg2004, Ellingsen2008, Falk2006, Fehr1993, Fehr1999, Gibbons1992, Gneezy2000, Grund2010, Kahneman1979, Kampkotter2018, Koszegi2006b, Kube2013, Lazear2000, Levine1998, Loomes1986, Prendergast1996, Rabin1993, Sliwka2007, Sliwka2017]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero) — Publisher abstract: This article gives a selective review on the (behavioral) economics of incentives in organizations. It starts with the analysis of a simple principal agent model. This model is then step-by-step extended in several domains to incorporate specific behavioral mechanisms that affect how people respond to incentives. Evidence from lab and field experiments as well as firm-level field studies with observational data are discussed. Topics covered are the moral hazard problem and the role of intrinsic motivation, the trade-off between risk and incentives, fairness and reciprocity, career and image concerns, detrimental effects of bonuses, and subjective performance evaluations.

## Summary
A selective handbook survey of the behavioral economics of incentives in organizations. The pedagogical device is a single linear-quadratic principal–agent model that is re-solved under successive behavioral perturbations — intrinsic/mission motivation, inequity aversion, reciprocity with reference-point adaptation, career and image concerns, signaling-based crowding-out, and biased subjective evaluation — to show which qualitative predictions of the classic moral-hazard model survive and which break. Each theoretical block is paired with lab, field-experiment, and firm-level observational evidence. (A ~26-page book chapter; read in full.)

## Research question
How do behavioral motives — social preferences, social norms, intrinsic/mission motivation, and reputational/image concerns — alter the standard moral-hazard prescriptions for incentive design in firms, and what does the empirical evidence say about each channel?

## Method / identification
The backbone is the Holmström–Milgrom linear-quadratic agency model. A risk-averse agent (CARA coefficient $r$) chooses hidden effort $e$ at cost $C(e)=\frac{c}{2}e^2$ and earns intrinsic/private benefit $ve$. A verifiable signal $s=e+a+\varepsilon$ with $\varepsilon\sim N(0,\sigma_e^2)$ drives a linear wage $w=\alpha+\beta s$. The certainty-equivalent objective is
$$\max_e\ \alpha+\beta(e+a)+ve-\frac{c}{2}e^2-\frac{1}{2}r\beta^2\sigma_e^2$$
giving optimal effort $e^\ast(\beta,v)=\frac{\beta+v}{c}$ and, after substituting the binding participation constraint, the classic optimal bonus
$$\beta^\ast=\frac{\theta}{1+r\sigma_e^2 c}.$$
The same scaffold is then re-specified: (i) inequity aversion adds a term $\frac{\gamma}{2}(\alpha-(\theta e-\alpha))^2$, making the fixed wage $\alpha$ an incentive instrument; (ii) reciprocity uses a loss-averse "emotional state" $h(\alpha,\alpha_r)$ around a reference wage $\alpha_r$ with loss weight $\lambda\ge1$; (iii) career concerns add reputational utility $\eta\cdot E[a\mid s]$, solved via normal updating $E[a\mid s]=\frac{\sigma_e^2 m_a+\sigma_a^2(s-e^\ast)}{\sigma_a^2+\sigma_e^2}$; (iv) the Bénabou–Tirole image model makes effort a signaling game over jointly normal task taste $v$ and money taste $\mu$; (v) [[@Sliwka2007|Sliwka (2007)]] turns the contract choice into a principal-to-agent signal of a descriptive social norm; (vi) subjective evaluation builds on Prendergast–Topel / Kampkötter–Sliwka with a supervisor utility weighting accuracy $\lambda_A$, equity $\lambda_E$, and favoritism $\lambda_S$. No new estimation — a survey of others' identification strategies (quasi-experiments, RCTs, panel fixed effects).

## Data
None of the author's own — this is a survey. It reviews secondary evidence: [[@Lazear2000|Lazear (2000)]] Safelite quasi-experiment, field experiments (Shearer 2004; Bandiera et al. 2007; Friebel et al. 2017; Manthei et al. 2018; [[@Kube2013|Kube et al. 2013]]; Gneezy–List 2006; Alfitian et al. 2020; Manthei–Sliwka 2019), lab experiments (Cadsby et al. 2007; Dohmen–Falk 2011; [[@Carpenter2016|Carpenter–Gong 2016]]; Cassar 2019; Irlenbusch–Sliwka 2006; Koch et al. 2009; [[@Ariely2009|Ariely et al. 2009]]; Danilov–Sliwka 2017; Berger et al. 2013; Sebald–Walzl 2014), and observational personnel data ([[@Gibbons1992|Gibbons–Murphy 1992]]; [[@Aggarwal1999|Aggarwal–Samwick 1999]]; [[@Grund2010|Grund–Sliwka 2010]]; Kampkötter–[[@Kampkotter2018|Sliwka 2018]]; Bol 2011; Frederiksen et al. 2020; Ockenfels et al. 2014).

## Key findings
- **Incentives + risk trade-off:** $\beta^\ast>0$ even for intrinsically motivated agents; optimal bonus falls in $r$ and $\sigma_e^2$. Empirically, Lazear's 44% productivity gain splits roughly half incentive / half selection.
- **Selection:** under fixed wages workers sort on motivation $v$; under performance pay the participation constraint becomes increasing in ability $a$ (and decreasing in $r$), so bonuses also recruit more able, less risk-averse workers.
- **Fairness:** with inequity aversion the fixed wage $\alpha$ motivates effort ($e=\frac{v+2\gamma\theta\alpha}{c+\gamma\theta^2}$), but the effect attenuates once prior wealth differences enter.
- **Reciprocity:** wage cuts below $\alpha_r$ depress effort more than equal raises lift it ($\lambda$ large relative to $\omega$, consistent with [[@Kube2013|Kube et al. 2013]]); reference-point adaptation makes positive reciprocity transient (Gneezy–List 2006; [[@Sliwka2017|Sliwka–Werner 2017]]).
- **Career concerns:** add a third motive $e^\ast=\frac{1}{c}\big(\beta+v+\eta\frac{\sigma_a^2}{\sigma_a^2+\sigma_e^2}\big)$; stronger image motivation $\eta$ *lowers* the optimal bonus (direct substitution plus a human-capital-insurance effect), whereas intrinsic $v$ does not, because $v$ is value-creating while image is not. Dynamic versions add the ratchet effect (Meyer–Vickers 1997).
- **Crowding-out:** in Bénabou–[[@Benabou2006|Tirole (2006)]], $\beta$ raises monetary effort but reduces the signal value of effort about task taste, so low-powered incentives can backfire — matched by [[@Ariely2009|Ariely et al. (2009)]] public/private results. [[@Sliwka2007|Sliwka (2007)]]: offering performance pay can signal a weak social norm, demotivating norm-compliers (Danilov–Sliwka 2017; Alfitian et al. 2020).
- **Subjective evaluation:** the supervisor optimum generates leniency bias ($E[r]=E[s]+\frac{\lambda_S\beta}{\lambda_A+\lambda_E}>E[s]$) and centrality/compression bias ($V[r]<V[s]$), the latter arising from equity concerns *and* pure signal noise. Compression dilutes incentives ($e$ in Eq. 13 shrinks); dispersion correlates with higher subsequent performance, but compression can aid cooperation under bonus pools, and leniency interacts with reciprocity in ambiguous ways.

## Contribution
Provides a unified, didactic re-derivation showing that one tractable agency model can host the major behavioral phenomena, clarifying *why* image motivation and intrinsic motivation have opposite implications for optimal bonus design, and organizing two decades of lab/field/firm evidence around these extensions. Serves as an integrative reference connecting moral hazard, social preferences, career concerns, and subjective-evaluation literatures.

## Limitations & open questions
The author explicitly flags: (i) most field experiments use temporary workers in manual jobs — there is little causal evidence on incentives for white-collar workers and middle managers, partly because objective outcome measures are unavailable; (ii) economists have been reluctant to accept subjective survey outcomes (e.g., job engagement), which would open a richer, more representative set of questions; (iii) combining field experiments with algorithmic/textual-data methods could open new ways to study incentive-design practices. Being a "selective" survey, it is non-exhaustive by design. Several models are deliberately simplified (single-agent supervisor reference points, binary contract choices, linear conditional expectations).

## Connections
Builds directly on the moral-hazard scaffold of Holmström & Milgrom (1991) and the classic incentives survey of Prendergast (1999). Social-preference channels draw on [[@Fehr1999|Fehr & Schmidt (1999)]] and [[@Bolton2000|Bolton & Ockenfels (2000)]] for inequity aversion, and on the gift-exchange tradition of [[@Fehr1993|Fehr et al. (1993)]] and [[@Akerlof1982|Akerlof (1982)]]. Reciprocity formalizations cited include [[@Rabin1993|Rabin (1993)]], [[@Dufwenberg2004|Dufwenberg & Kirchsteiger (2004)]], [[@Falk2006|Falk & Fischbacher (2006)]], [[@Levine1998|Levine (1998)]], [[@Ellingsen2008|Ellingsen & Johannesson (2008)]], and Cox et al. (2007), with reference-dependence rooted in [[@Kahneman1979|Kahneman & Tversky (1979)]], [[@Loomes1986|Loomes & Sugden (1986)]], and Kőszegi & [[@Koszegi2006b|Rabin (2006)]]; the author's own [[@Sliwka2017|Sliwka & Werner (2017)]] supplies the reciprocity-with-adaptation model. Career concerns trace to Holmström (1982, 2017) and [[@Gibbons1992|Gibbons & Murphy (1992)]], with dynamics from Meyer & Vickers (1997). Crowding-out rests on Bénabou & [[@Benabou2006|Tirole (2006)]], [[@Sliwka2007|Sliwka (2007)]], and [[@Gneezy2000|Gneezy & Rustichini]] (2000a,b), echoing Deci (1971). Subjective-evaluation modeling follows [[@Prendergast1996|Prendergast & Topel (1996)]] and Kampkötter & [[@Kampkotter2018|Sliwka (2018)]], with reciprocity-to-ratings from Sebald & Walzl (2014) and Ockenfels et al. (2014). Companion handbook chapters by Charness et al. (2020) and Villeval (2020) cover social preferences and feedback, respectively.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
