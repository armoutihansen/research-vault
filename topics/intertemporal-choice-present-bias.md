---
slug: intertemporal-choice-present-bias
title: "Intertemporal Choice & Present Bias"
type: topic
scope: "Time discounting beyond exponential DU: present bias, self-control, commitment, and the timing of payments."
area: "[[decision-under-risk-time]]"
tags: [topic]
created: 2026-05-31
generated: 2026-05-31
---

## Scope

This topic covers intertemporal choice that departs from exponential discounted utility, organized around present bias: the quasi-hyperbolic $(\beta,\delta)$ form $U^t=\sum_{\tau\ge t}D(\tau-t)u_\tau$ with $D(x)=\beta\delta^x$ for $x>0$, $\beta<1$. It spans the axiomatic foundations of time-inconsistency, the sophistication/naivete distinction, the demand for commitment devices, and how present bias rewrites contracting, effort provision, and the timing of payments. The boundary is sharp on two sides: pure reference-dependence over risk lives in [[expectations-based-reference-dependence]], and belief-savoring motives live in [[anticipatory-utility-motivated-beliefs]] — here utility is dated but standard, and the deviation is in *how* the future is weighed.

## Sub-themes

- **Foundations of time-inconsistency.** [[@Gul2005|Gul & Pesendorfer (2005)]] axiomatize Strotz consistent planning and the Phelps–Pollak $\beta$–$\delta$ subclass from a period-0 menu preference; [[@ODonoghue2015|O'Donoghue & Rabin (2015)]] codify the field's modeling discipline (utility-not-money, "about now," calibration, welfare). Together they fix what the workhorse model *is* and what it can be identified from.
- **Field/lab identification of present bias.** [[@Kaur2015|Kaur, Kremer & Mullainathan (2015)]] identify $\beta$ from real effort via dominated-contract take-up and a randomized pay-cycle; [[@Werthschulte2023|Werthschulte (2023)]] isolates payment timing (pay-as-you-go vs. pay-later) in a real-effort billing lab, calibrating $\beta\approx0.89$.
- **Commitment and contracting under present bias.** [[@Kaur2015|Kaur et al. (2015)]] recast agency theory (firm and worker jointly value future-effort-eliciting contracts); [[@Fahn2019|Fahn & Hakenes (2019)]] and its [[@Fahn2018|Fahn & Hakenes (2018)]] online appendix show endogenous teamwork as a relational-contract commitment device, where self-control problems become the glue of cooperation.

## Cross-paper tensions

**Is commitment evidence *of* present bias, or merely consistent with it?** This is the sharpest axis. [[@Kaur2015|Kaur et al. (2015)]] treat voluntary take-up of weakly dominated contracts as a clean revealed signature of sophisticated present bias — a time-consistent worker never strictly prefers them. But [[@ODonoghue2015|O'Donoghue & Rabin (2015)]] explicitly flag (their open Q4) that belief-based-utility motives, mispredicted future behavior, and negative-cost commitments can manufacture apparent commitment without sophistication. [[@Gul2005|Gul & Pesendorfer (2005)]] sharpen this into an impossibility: their Theorem 6 shows any Strotz consistent-planning preference is *observationally identical* on finite data to a Gul–Pesendorfer self-control (temptation) preference. So the very commitment demand Kaur reads as $\beta<1$ is, by Gul–Pesendorfer, equally a temptation-disutility story — and crucially the two carry *opposite* welfare verdicts (multiple-selves vs. a single time-consistent self who would vote for the tempting-good tax).

**What identifies $\beta$ — and does the elicitation device matter?** [[@ODonoghue2015|O'Donoghue & Rabin (2015)]] insist present bias operates on utility, not money, so cash smaller-sooner/larger-later tasks are uninformative. [[@Kaur2015|Kaur et al. (2015)]] confirm this empirically and damagingly: their lab cash-discounting and preference-reversal measures do *not* predict the workers' behavioral effort effects. [[@Werthschulte2023|Werthschulte (2023)]] sidesteps the problem by refusing to estimate $\beta$ from ex-ante-vs-actual choices at all (confounded by mispredicted task difficulty and learning), calibrating it only — leaving direct choice-identification unsettled even within the effort paradigm both papers share.

**Does present bias help or hurt performance?** The applied papers treat $\beta<1$ as a friction to be disciplined (commitment devices, billing redesign). [[@Fahn2019|Fahn & Hakenes (2019)]] invert this: because a present-biased agent's solo outside option $e^I=\beta\delta V/c$ is bad, breakup is more painful, so *more* present bias (lower $\beta$) loosens the relational-contract IC constraint — there exists an interior $\beta^{\max}\in(0,1)$ maximizing cooperation, and present-biased agents can beat time-consistent ones. This sits uneasily with the Kaur/Werthschulte framing of present bias as pure welfare loss, and with the long-run-utility criterion of [[@ODonoghue2015|O'Donoghue & Rabin (2015)]].

**Sophisticated, naive, or a mix?** [[@Kaur2015|Kaur et al. (2015)]] and [[@Fahn2019|Fahn & Hakenes (2019)]] assume sophistication (their core predictions — dominated-contract take-up, breakup credibility — require it). [[@Fahn2018|Fahn & Hakenes (2018)]] show fully naive agents perceive breakup as costless and sustain *zero* team effort. [[@Gul2005|Gul & Pesendorfer (2005)]] make sophistication an observable knife-edge: IRA is its unique testable implication, naifs satisfy P and NC but violate it. Yet none of the empirical members separately identifies the share of naifs, which Kaur concedes would attenuate their key within-worker correlation.

## Open questions

- **Disentangling present bias from its confounds.** O'Donoghue & Rabin's Q3 — habit formation, projection bias, anticipatory utility, news utility — plus Gul–Pesendorfer's temptation observational-equivalence: no member offers a finite-data test that cleanly separates these. What richer evidence (if any) could?
- **What identifies time-inconsistent agents ex ante?** Cash-discounting fails ([[@Kaur2015|Kaur et al. 2015]]); choice-based effort elicitation is confounded ([[@Werthschulte2023|Werthschulte 2023]]). Is there a portable, predictive individual-level measure?
- **Temporal aggregation.** O'Donoghue & Rabin's Q2: monthly/quarterly data net together daily decisions, distorting $\beta$. None of the structural members models the aggregation explicitly.
- **Sorting, naivete, and heterogeneity in teams.** Fahn–Hakenes leave open equilibrium team composition with asymmetric $(\beta_1,\beta_2)$, partial naivete, imperfect monitoring, and a principal who assigns agents.
- **Welfare under observational equivalence.** Gul–Pesendorfer's reinterpretation and O'Donoghue–Rabin's long-run-utility criterion give *different* welfare numbers from the same choices; Werthschulte already finds calibrated utility is ambiguous (pay-later higher absent externality).

## Candidate ideas

- **A discriminating test of commitment: present bias vs. temptation.** Design a real-effort field/lab experiment exploiting where [[@Gul2005|Gul & Pesendorfer (2005)]] equivalence breaks (out-of-finite-sample menu variation) to separate $\beta$–$\delta$ from self-control preferences using [[@Kaur2015|Kaur et al. (2015)]]'s dominated-contract device.
- **A portable ex-ante present-bias measure for the workplace.** Build and validate an effort-based elicitation that predicts the behavioral effects [[@Kaur2015|Kaur et al. (2015)]] found cash-discounting cannot, addressing their unresolved identification gap.
- **Repeated billing and the dynamics of present focus.** Extend [[@Werthschulte2023|Werthschulte (2023)]] to a multi-period pay-as-you-go vs. pay-later design to test whether the timing gap widens or decays via learning/inattention — her flagged open question.
- **Structural estimation of the teamwork commitment model.** Take [[@Fahn2019|Fahn & Hakenes (2019)]] to data: do real teams with present-biased members sustain higher effort, and is there an empirical $\beta^{\max}$? Distinguish the relational-contract mechanism from peer pressure/reciprocity, which they flag as untested.
- **Optimal contracting for self-control-prone workers under naive/sophisticated mixing.** Combine [[@Fahn2018|Fahn & Hakenes (2018)]]'s naivete results with [[@Kaur2015|Kaur et al. (2015)]]'s agency reframing to derive welfare-improving (not merely diagnostic) contracts when the naif share is unidentified.
- **Reconciling welfare criteria.** Quantify how much the long-run-utility criterion of [[@ODonoghue2015|O'Donoghue & Rabin (2015)]] and the time-consistent reinterpretation of [[@Gul2005|Gul & Pesendorfer (2005)]] diverge on [[@Werthschulte2023|Werthschulte (2023)]]'s billing data.

## Members
```dataview
LIST
FROM "literature"
WHERE contains(topics, this.file.link)
SORT file.name ASC
```

## Bordering work
<!-- citation-derived: cited by members, not a member here. Regenerated each run. -->
- [[@Berns2007]] — cited by 1 member
- [[@Gabaix2006]] — cited by 1 member
- [[@Holmstrom1982]] — cited by 1 member
- [[@Koszegi2009]] — cited by 1 member
- [[@Loewenstein1987]] — cited by 1 member
- [[@Sprenger2015]] — cited by 1 member

## Promoted from this topic
```dataview
LIST
FROM "projects"
WHERE contains(topics, this.file.link)
```

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
