---
citekey: Abeler2011
title: Reference Points and Effort Provision
authors: ["Abeler, Johannes", "Falk, Armin", "Goette, Lorenz", "Huffman, David"]
year: 2011
type: journalArticle
doi: 10.1257/aer.101.2.470
zotero: "zotero://select/library/items/6FDMNFZS"
pdf: /Users/jesper/Zotero/storage/GLRKN3UE/Abeler2011.pdf
tags: [literature]
keywords: [reference-dependent-preferences, expectations-based-reference-point, loss-aversion, real-effort-experiment, labor-supply, koszegi-rabin]
topics: []
related: [Bell1985, Farber2005, Gul1991, Kahneman1979, Koszegi2006b, Koszegi2007, Loomes1986, Shalev2000, Tversky1990]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> A key open question for theories of reference-dependent preferences is: what determines the reference point? One candidate is expectations: what people expect could affect how they feel about what actually occurs. In a real-effort experiment, we manipulate the rational expectations of subjects and check whether this manipulation influences their effort provision. We find that effort provision is significantly different between treatments in the way predicted by models of expectation-based, reference-dependent preferences: if expectations are high, subjects work longer and earn more money than if expectations are low. (JEL D12, D84, J22)

## Summary
A tightly controlled lab experiment testing whether *expectations* serve as the reference point in reference-dependent preference models. Subjects do a tedious real-effort task (counting zeros) and choose when to stop; their pay is, with probability $\tfrac12$, their accumulated piece-rate earnings $we$ and, with probability $\tfrac12$, a known fixed payment $f$. The sole treatment manipulation is the size of $f$ (3 euros in LO, 7 euros in HI). Raising $f$ raises rational earnings expectations and, under expectation-based loss aversion, raises effort and pulls stopping decisions toward $f$. Both predictions are confirmed; control treatments rule out salience and reciprocity, and an independent loss-aversion measure shows more loss-averse subjects stop closer to $f$.

## Research question
What determines the reference point in reference-dependent preferences? Specifically: do *rational expectations* about outcomes act as the reference point, and can exogenously shifting expectations change real-effort provision in the direction predicted by expectation-based models (e.g. Kőszegi-Rabin)? The paper sidesteps the field-data problem that expectations and reference points are unobserved/latent by making expectations known and exogenously variable.

## Method / identification
A between-subjects real-effort laboratory experiment (z-Tree, ORSEE; University of Bonn students, non-economists, 60 per treatment). Stage 1: 4 minutes counting zeros at a sure 10c piece rate (familiarization plus a productivity proxy). Stage 2 (main): subjects count for up to 60 minutes and decide when to stop; piece rate doubled to 20c. Before working they draw one of two sealed envelopes; one yields accumulated piece-rate earnings, the other the fixed payment $f$. Uncertainty is resolved only after they stop, so the rational expectation at the stopping moment is a $50/50$ mix of $we$ and $f$. Subjects arrive one at a time, $\geq 20$ minutes apart, work alone in identical rooms — removing peer effects.

The paper formally contrasts three model classes for choice of correctly solved tables $e$, with piece rate $w>0$ and effort cost $c(e)$, $\partial c/\partial e>0$:

- **Canonical separable utility** $U(x,e)=u(x)-c(e)$ gives $U=\tfrac12 u(f)+\tfrac12 u(we)-c(e)$ and FOC $u'(we^{*})=\tfrac{2}{w}c'(e^{*})$. Optimal $e^{*}$ is *independent of $f$* — true for any curvature of $u(\cdot)$ and any cost shape, conditional on separability. Predicts no treatment difference.
- **Status-quo reference dependence**: the status quo is identical across treatments, so varying $f$ does not change effort incentives. Predicts no treatment difference.
- **Expectation-based reference dependence** (Kőszegi-[[@Koszegi2007|Rabin 2007]], choice-acclimating personal equilibrium; [[@Bell1985|Bell 1985]], [[@Loomes1986|Loomes-Sugden 1986]], [[@Gul1991|Gul 1991]] give similar predictions). Consumption utility is linear; gain-loss utility is $\mu(s)=\eta s$ for $s\geq 0$ and $\mu(s)=\eta\lambda s$ for $s<0$, with $\eta\geq 0$, $\lambda>1$ (losses loom larger). Effort cost is borne in both states so it does not enter gain-loss utility. For $we<f$:
$$U=\tfrac12\!\left(\tfrac{we+f}{2}\right)-c(e)+\eta\!\left[\tfrac12\!\left(\tfrac12(we-we)+\tfrac12\lambda(we-f)\right)+\tfrac12\!\left(\tfrac12(f-we)+\tfrac12(f-f)\right)\right]$$
yielding $c'(e^{*})=\tfrac{w}{2}+\tfrac{w}{4}\eta(\lambda-1)$; for $we\geq f$, $c'(e^{*})=\tfrac{w}{2}-\tfrac{w}{4}\eta(\lambda-1)$. The marginal return to effort is higher than the canonical $\tfrac{w}{2}$ below $f$ and lower above $f$, with a discrete drop at $we=f$. This generates **Hypothesis 1** (average effort higher in HI than LO) and **Hypothesis 2** (clustering of stopping exactly at $f$, more so the more loss-averse the population). Estimation is by OLS and Tobit (censored 0-60 min) for effort levels, multinomial logit for the propensity to stop at 3 vs 7 vs elsewhere, plus non-parametric Mann-Whitney U and Kolmogorov-Smirnov tests.

An independent, incentivized loss-aversion measure: after stopping, subjects make six choices between 0 and a $50/50$ lottery winning 6 euros or $Y\in\{-2,\dots,-7\}$. Small stakes mean rejections of positive-EV lotteries cannot be standard risk aversion (Rabin 2000); the count of rejected lotteries proxies $\eta$/$\lambda$. Distance $\lvert we-f\rvert$ is regressed on this proxy.

## Data
Original experimental data: 60 subjects in each of LO and HI, plus 60 each in three control treatments (NOSAL, SAL, R), total 300; ~12,000 correctly counted tables (only 59 thrice-failed). Average earnings 8.70 euros plus a 5-euro show-up fee; sessions ~1 hour.

## Key findings
- **Result 1 (Hyp. 1 confirmed):** Subjects stop at 7.37 euros on average in LO vs 9.22 euros in HI — a 1.85-euro difference (~25% of LO effort), nearly half the 4-euro manipulation; significant in OLS with/without controls (U-test $p=0.015$, KS $p=0.005$). Time worked: 31.7 min (LO) vs +6.4 min (HI).
- **Result 2 (Hyp. 2 confirmed):** Pronounced spikes exactly at $f$. In LO, 15.0% stop at 3 euros (only 3.3% at 7); in HI, 16.7% stop at 7 euros (only 1.7% at 3). The modal choice in both treatments is to stop exactly at $f$ (multinomial logit significant).
- **Results 3-4 (salience ruled out):** NOSAL (cards "5 euros plus acquired earnings" / "8 euros" — number 3 never shown, but stopping at 3 still avoids loss) gives 13.3% stopping at 3, indistinguishable from LO's 15.0%, and no extra mass at the salient 5 or 8. SAL (cards "Acquired earnings" / "Acquired earnings plus 3 euros", piece rate halved — 3 equally salient but stopping there no longer avoids a loss) gives only 3.3% at 3 and significantly *more* total effort than LO, as predicted.
- **Result 5 (reciprocity ruled out):** R treatment adds a 4-euro lump sum "for the work," raising total pay above HI. Effort is not different from LO (if anything lower); HI-vs-R difference highly significant ($p<0.001$). Pooling LO+NOSAL+R against HI keeps the treatment effect at $p\leq 0.003$.
- **Result 6 (direct loss-aversion link):** More loss-averse subjects (more rejected lotteries) stop significantly closer to $f$; the loss-aversion coefficient on $\lvert we-f\rvert$ is significantly negative across all specifications (~$-0.49$, $p<0.05$). This correlation is a *unique* prediction of the expectation-based model and is absent (point estimate near zero) in SAL, where stopping at $f$ does not avoid losses.

## Contribution
Provides clean, exogenous experimental evidence that *expectations* form the reference point, directly disciplining where reference points come from rather than fitting them case-by-case (which the authors warn turns reference dependence into an unfalsifiable free parameter). It extends prior empirical work that fixed the reference point at the status quo or lagged status quo. It complements Crawford-Meng's (2008) structural field study of NYC taxi drivers with a design where rational expectations are known and varied while other reference points are held constant, and it helps reconcile conflicting field findings on transitory wage changes: under expectation-based reference points, anticipated wage changes do not distort effort, while unexpectedly low wages can raise effort — contrary to standard intertemporal substitution.

## Limitations & open questions
- The authors explicitly note they cannot distinguish *which* specification of the expectation-based reference point is empirically correct: the **mean** of expected outcomes (Bell 1985; Loomes-Sugden 1986; [[@Gul1991|Gul 1991)]] vs the **whole distribution** of expected outcomes (Kőszegi-[[@Koszegi2006b|Rabin 2006]], 2007). Both predict clustering at a single $f$.
- They propose a concrete extension as future work: make payoffs a lottery over *two* distinct fixed payments plus accumulated earnings. Mean-based models then predict a stopping spike at the *mean* of the two fixed payments but not at either; distribution-based (Kőszegi-Rabin) models predict spikes at the *two* fixed payments but not the mean — a clean discriminating test.
- Rational expectations are assumed, not measured ("We don't know the actual expectations of subjects"); the design argues the simple, salient lottery makes deviations unlikely but cannot verify it.
- External validity: a single artificial task, small stakes, student sample, one-shot; generalization to field labor supply is argued, not demonstrated.

## Connections
Squarely within the Kőszegi-[[@Koszegi2006b|Rabin (2006]], 2007) program on expectation-based reference-dependent preferences, with the choice-acclimating personal equilibrium as the operative solution concept; precursors [[@Bell1985|Bell (1985)]], [[@Loomes1986|Loomes-Sugden (1986)]], [[@Gul1991|Gul (1991)]], and [[@Shalev2000|Shalev (2000)]] supply the disappointment-aversion lineage, all grounded in [[@Kahneman1979|Kahneman-Tversky (1979)]] loss aversion. It contrasts with status-quo reference-point work ([[@Tversky1990|Kahneman-Knetsch-Thaler 1990]] endowment effect; Odean 1998; Genesove-Mayer 2001). The labor-supply application engages Camerer-Babcock-Loewenstein-Thaler (1997), Fehr-Götte (2007), [[@Farber2005|Farber (2005]], 2008), Crawford-Meng (2008), and Doran (2009) on daily income targeting. The incentivized loss-aversion measure follows Fehr-Götte (2007) and Gächter-Herrmann-Johnson (2007) and invokes Rabin's (2000) calibration critique to separate loss aversion from risk aversion. The goal-setting discussion links to Locke-Latham (1990, 2002), Heath-Larrick-Wu (1999), and Koch-Nafziger (2008).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
