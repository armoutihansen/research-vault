---
citekey: Cerulli-Harms2019
title: "Randomizing Endowments: An Experimental Study of Rational Expectations and Reference-Dependent Preferences"
authors: ["Cerulli-Harms, Annette", "Goette, Lorenz", "Sprenger, Charles"]
year: 2019
type: journalArticle
doi: 10.1257/mic.20170271
zotero: "zotero://select/library/items/2HQ787G3"
pdf: /Users/jesper/Zotero/storage/J27GW88Z/Cerulli-Harms2019.pdf
tags: [literature]
keywords: [expectations-based-reference-dependence, koszegi-rabin, endowment-effect, personal-equilibrium, loss-aversion, experimental-economics, willingness-to-pay-accept]
topics: []
related: [Abeler2011, Allen2017, Bell1985, Dellavigna2017, Gneezy2017, Gul1991, Koszegi2006b, Loomes1986, Sprenger2015, Tversky1990]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We test expectations-based reference dependence in market experiments with probabilistic forced exchange. Kőszegi and [[@Koszegi2006b|Rabin (2006)]] predict that when the probability of forced exchange increases, individuals cannot expect to stick with the status quo, and should grow more willing to exchange. This mechanism may eliminate and even reverse the "endowment effect" (Knetsch and Sinden 1984; Kahneman, Knetsch, and Thaler 1990). In a series of experiments with overall 930 subjects, we show some tentative support for the notion that attitudes toward exchange are influenced by the probability of forced exchange. However, the results are sensitive to small changes in experimental design. (JEL C92, D12, D84, D91)

## Summary
The paper builds a clean experimental test of Kőszegi-Rabin (KR) expectations-based reference dependence applied to the classic endowment effect. The innovation is *probabilistic forced exchange*: with known probability $p$, sellers' mugs are confiscated for cash (and buyers' cash for a mug) at an arbitrary price, regardless of stated valuations. Because the status quo can no longer be expected with certainty, the expectations-based reference point must shift as $p$ rises, predicting that buyers' willingness-to-pay ($WTP$) should rise and sellers' willingness-to-accept ($WTA$) should fall — an asymmetric comparative static that can shrink, eliminate, or even reverse the endowment effect. Across three experiments (930 subjects) the support is mixed: a clear null in experiment 1, strong confirmation in experiment 2, and a null again in experiment 3. The headline message is that KR predictions are fragile to minor, off-model details of experimental design.

## Research question
Do attitudes toward exchange respond to the probability of forced exchange in the direction predicted by the KR personal-equilibrium model? Specifically, does increasing $p$ raise buyers' $WTP$ and lower sellers' $WTA$ (the asymmetric comparative static), and can probabilistic forced exchange attenuate or reverse the endowment effect? The authors also ask whether the model's sharper *point* predictions (no endowment effect at $p=0.5$, reversal for $p>0.5$) hold.

## Method / identification
The theoretical backbone is the KR reference-dependent utility $U(F\mid G)=\int\int u(c\mid r)\,dF(c)\,dG(r)$, evaluating a consumption lottery $F$ against a reference lottery $G$. Over mugs $m\in\{0,M\}$ and money $y$, with $c=(m,y)$ and $r=(r_m,r_y)$, utility is separable with a piecewise-linear gain-loss kernel:
$$u(c\mid r)=m+y+\mu(m-r_m)+\mu(y-r_y),\qquad \mu(z)=\begin{cases}\eta z & z\ge 0\\ \eta\lambda z & z<0\end{cases}$$
where $\eta$ scales deviations from the reference point and $\lambda>1$ is loss aversion. Consistency is imposed via **Personal Equilibrium (PE)**: a choice $F\in\mathcal{D}$ is a PE if $U(F\mid F)\ge U(F'\mid F)\ \forall F'\in\mathcal{D}$ — the reference and consumption distributions coincide (rational expectations).

Under forced exchange probability $p$, a seller wishing not to sell holds the stochastic reference $G=p\cdot(0,x)+(1-p)\cdot(M,0)$. Solving the PE inequality yields the highest price at which she can support *not* selling,
$$\bar S(p)=\frac{1+p(1-\lambda)\eta+\eta\lambda}{1-p(1-\lambda)\eta+\eta}\,M,$$
which is strictly decreasing in $p$ for $\eta>0,\lambda>1$. Symmetrically, the lowest price at which a buyer can support *not* buying is
$$\underline B(p)=\frac{1-p(1-\lambda)\eta+\eta}{1+p(1-\lambda)\eta+\eta\lambda}\,M,$$
strictly increasing in $p$. The lower-bound selling price $\underline S(p)=\frac{1+\eta}{1+\eta\lambda}M$ and upper-bound buying price $\bar B(p)=\frac{1+\eta\lambda}{1+\eta}M$ are constant in $p$. Mapping $\bar S(p)\equiv WTA(p)$ and $\underline B(p)\equiv WTP(p)$ gives the testable **Comparative Static Asymmetry**: $WTP(p)$ increases and $WTA(p)$ decreases in $p$. The PE-endowment-effect region (where $\bar S(p)>\underline B(p)$) shrinks with $p$ and vanishes for $p>0.5$ (since $\bar S(0.5)=\underline B(0.5)$), with reversals for $p>0.5$ and the symmetry $\bar S(p)=\underline B(1-p)$. The authors also derive that the qualitative comparative statics survive the **Preferred Personal Equilibrium (PPE)** and **Choice-Acclimating Personal Equilibrium (CPE)** refinements, even though the endowment effect itself does not survive PPE/CPE. A mathematical appendix generalizes the $\mu$-function and analyzes price-list elicitation.

Empirically, identification rests on a **difference-in-differences** across forced-exchange probabilities: the change in $WTA$ minus the change in $WTP$ as $p$ rises should be negative under KR. Subjects are randomized to buyer/seller roles and to $p\in\{0,0.25,0.5,0.75,0.99\}$, with all markets run simultaneously to rule out endogenous valuation shifts. The design deliberately differs from probabilistic *permission*-to-exchange paradigms (Ericson-Fuster 2011; Camerer et al. 2016; Heffetz-List 2014); the authors show that not responding to permission probability is fully PE-consistent, whereas forced exchange acts precisely on the would-be non-traders who generate the endowment effect.

## Data
Three lab/classroom experiments at the University of Lausanne, 930 subjects total. **Experiment 1** (N=465; 236 buyers, 229 sellers): KKT-1990 market-price design, endowments given *first*, then forced-exchange explained, $p\in\{0,0.25,0.5,0.75\}$. **Experiment 2** (N=228 first-year law students): identical except forced exchange explained *before* endowments are shown, $p\in\{0.25,0.5,0.75\}$. **Experiment 3** (N=237, ORSEE pool): forced exchange first, but *random* price determination (CHF 0.50–10) replacing market pricing, $p\in\{0.25,0.5,0.75,0.99\}$. Mugs vs. CHF 10 ($\approx$ US$10). A 41-subject comprehension study confirmed ~85% fully understood the protocol.

## Key findings
- **Robust baseline endowment effect**: at $p=0$ in experiment 1, $WTA-WTP=$ CHF 2.51 (SE 0.44), highly significant ($t=5.71$). An endowment effect persists in *every* condition of all three experiments, including $p>0.5$, contradicting the KR point prediction of no/reverse endowment effect.
- **Experiment 1 — null**: $WTA$ and $WTP$ barely move with $p$; the diff-in-diff is CHF 0.49 (0.61), indistinguishable from zero ($t=0.80$). The asymmetric comparative static is rejected.
- **Experiment 2 — supportive**: with the mechanism presented first, $WTA$ falls CHF 0.58 and $WTP$ rises CHF 1.40 ($t=2.94$) as $p$ goes 0.25→0.75. The diff-in-diff is CHF $-1.98$ (0.66), significant ($t=2.99$), shrinking the endowment effect by ~72% ($-1.98/2.74$). Both sides move in the predicted directions simultaneously — the strongest evidence for KR.
- **Experiment 3 — null/fragile**: buyers' $WTP$ rises CHF 1.11 ($t=1.73,p=0.09$) as $p$ goes 0.25→0.99, but sellers' $WTA$ *also* rises CHF 1.01 (wrong sign), so the diff-in-diff is CHF $-0.10$ ($t=0.11$). Both sides jump sharply at $p=0.99$, suggesting a common design artifact rather than the KR mechanism. Ignoring $p=0.99$, valuations are flat in $p$.
- **Overall scorecard**: of six comparative statics (buyers and sellers $\times$ three experiments), three are directionally consistent with KR, two significant; the full asymmetric pattern appears only in experiment 2.

## Contribution
Provides the first experimental test of KR personal equilibrium via *forced* (not permitted) exchange — a manipulation that, unlike prior permission-probability designs, bites precisely on the agents who would otherwise generate an endowment effect, and yields crisp, asymmetric comparative-static predictions plus sharp point predictions ($p=0.5$ knife-edge, reversal above). It formally derives the PE cutoff functions, locates the disappearance of the PE endowment effect at $p=0.5$, and shows the comparative statics survive PPE/CPE refinements. Substantively, it documents that KR predictions are real but fragile — confirmed under one presentation order and pricing rule, absent under others — sharpening an emerging literature on the instability of expectations-based reference points.

## Limitations & open questions
- **Design fragility is itself the central, unresolved finding**: results flip between null and supportive based on (a) the order in which endowments vs. the forced-exchange mechanism are presented, and (b) market vs. random price determination. The paper cannot pin down *which* off-model feature drives the difference.
- **Point predictions broadly fail**: an endowment effect persists at all $p$, including $p>0.5$ where KR predicts reversal — implying additional forces or reference points (e.g., a standard status quo referent) operate alongside expectations.
- **Equilibrium-selection confound**: a lack of sensitivity to $p$ is consistent with the selected PE already being pro-exchange, or with selection itself shifting with $p$; the design cannot separate these from a genuine null.
- **Open agenda (explicit)**: "Critical future steps will deliver understanding on when and why specific formulations of reference points are likely to be adopted by decision makers" — i.e., a theory of *which* referent (expectations-based, status-quo, gift) applies in a given environment, to restore KR's disciplining power without ad hoc freedom.
- The $p=0.99$ spike in experiment 3 hints at an extreme-probability artifact not fully diagnosed.

## Connections
The paper is a direct empirical confrontation of **Kőszegi and [[@Koszegi2006b|Rabin]] (2006, 2007, 2009)** expectations-based reference dependence, contrasting PE with the PPE/CPE refinements (CPE links to disappointment aversion à la **[[@Bell1985|Bell 1985]]; [[@Loomes1986|Loomes-Sugden 1986]]; [[@Gul1991|Gul 1991]]**). It situates against the endowment-effect canon (**Knetsch-Sinden 1984; Knetsch 1989; [[@Tversky1990|Kahneman-Knetsch-Thaler 1990]]**) and the methodological critiques of **Plott-Zeiler (2005, 2007)** on gifts and mistaken market power. Most closely, it joins permission-to-exchange tests — **Ericson-Fuster (2011)**, **Camerer et al. (2016)**, and **Heffetz-List (2014)** — which the authors argue test a logically distinct (and PE-compatible-with-no-response) manipulation, and which themselves reach conflicting conclusions. The fragility theme parallels labor-supply tests of KR (**[[@Abeler2011|Abeler et al. 2011]]; [[@Gneezy2017|Gneezy et al. 2017]]**) and the "first-focus" referent evidence of **[[@Sprenger2015|Sprenger (2015)]]**. The proposed remedy — non-expectations-based or status-quo reference points — connects to **[[@Allen2017|Allen et al. (2017)]]**, **[[@Dellavigna2017|DellaVigna et al. (2017)]]**, and **Rees-Jones (2018)**. Applications motivating the model span macro (**Pagel 2016, 2017**), IO (**Heidhues-Kőszegi 2008, 2014**), and contract theory (**de Meza-Webb 2007; Herweg-Müller-Weinschenk 2010**).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
