---
citekey: Arieli2011
title: Tracking Decision Makers under Uncertainty
authors: ["Arieli, Amos", "Ben-Ami, Yaniv", "Rubinstein, Ariel"]
year: 2011
type: journalArticle
doi: 10.1257/mic.3.4.68
zotero: "zotero://select/library/items/H44INZSA"
pdf: /Users/jesper/Zotero/storage/PM4WDVP9/Arieli2011.pdf
tags: [literature]
keywords: [process-tracing, eye-tracking, decision-under-uncertainty, bounded-rationality, similarity-based-choice, expected-utility, heuristics]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Eye tracking is used to investigate the procedures that participants employ in choosing between two lotteries. Eye movement patterns in problems where the deliberation process is clearly identified are used to substantiate an interpretation of the results. The data provide little support for the hypothesis that decision makers rely exclusively upon an expected utility type of calculation. Instead eye patterns indicate that decision makers often compare prizes and probabilities separately. This is particularly true when the multiplication of sums and probabilities is laborious to compute. (JEL D81, D87)

## Summary
A short, process-tracing experiment that uses eye tracking to ask *how*, not just *what*, people choose when picking between two simple lotteries. By exploiting the screen layout (prizes stacked above probabilities for the two alternatives), the authors read off whether subjects integrate each lottery holistically (vertical gaze) or compare prizes and probabilities feature-by-feature (horizontal gaze). The data give little support for pure expected-utility-style integration: subjects mix procedures, and they lean heavily on separate component comparison precisely when computing an expectation $p\cdot x$ would be arithmetically laborious. The paper is a methodological/empirical contribution to the bounded-rationality program associated with Rubinstein's "similarity"-based choice models.

## Research question
When choosing between two monetary lotteries, do decision makers reason **holistically** — collapsing each lottery into a single number (certainty equivalent, expectation, or a general $g(p)v(x)$) and comparing those — or **componentwise** — comparing the prizes against each other and the probabilities against each other, possibly using similarity judgments? And does the choice of procedure depend on how computationally hard the holistic calculation is?

## Method / identification
The core identification idea is a clean mapping from *gaze geometry* to *choice procedure*. Each problem shows lottery $L$ (parameters $a,b$) and lottery $R$ (parameters $c,d$) on one screen, with prizes on the top row and probabilities on the bottom row. The authors formalize two candidate procedure classes:

- **Holistic (H-) procedures**: a function $u$ exists such that lottery 1 is chosen iff $u(x_1,p_1) > u(x_2,p_2)$ — e.g. comparing expectations or certainty equivalents, or any $g(p_i)v(x_i)$ rule. Evaluating a lottery requires looking *within* an alternative, i.e. **vertical** eye movement (prize-to-probability of the same lottery).
- **Component (C-) procedures**: functions $f,g,h$ exist such that lottery 1 is chosen iff $h(f(x_1,x_2),\,g(p_1,p_2)) > 0$ — compare prizes to prizes, probabilities to probabilities, invoking similarity (à la Rubinstein 1988; Tversky–Sattath–Slovic 1988). This requires looking *across* alternatives, i.e. **horizontal** eye movement.

Measurement: a high-speed infrared eye tracker (SMI iView, 240 Hz, one sample / 4.2 ms) records point of gaze. The screen is split into four quadrants; transitions are classified into six movement types (left-vertical, right-vertical, top-horizontal, bottom-horizontal, descending-diagonal, ascending-diagonal). For each problem the proportion of *time* spent in each movement type is computed per participant and averaged into a vector $a$ whose six components sum to 100%. Formally, with presentation time $0$, click time $T$, and transition times $t_2,\dots,t_n$, the interval $[0,T]$ is partitioned at midpoints $[0,(t_1+t_2)/2],\,[(t_1+t_2)/2,(t_2+t_3)/2],\dots$ and each sub-interval's duration is credited to the movement type occurring at its transition; dividing by total movement time yields $a(i)$, then averaged to $a$. A parallel vector $\beta$ counts *number of transitions* rather than time; it gives nearly identical results, guarding against the confound that hard-to-read parameters lengthen dwell time. Blinks (lost-eye periods) and dwells under 100 ms are dropped; problems where omissions exceed 20% of response time are excluded.

Crucially, the authors **anchor the interpretation with "transparent" calibration problems** where the procedure is known a priori: difference-comparison tasks D1, D2 ("which difference $a-b$ vs $c-d$ is larger") and time-preference tasks T1–T3 (comparing dated dollar amounts), where a present-value-like integration is implausible so behavior *should* be horizontal/C-type. They then ask where the lottery problems' gaze vectors fall relative to these benchmarks. Diagonal layouts (U5–U8) are used as a robustness check.

## Data
Process-tracing experiment. 47 participants (24 male, 23 female; mean age 27), all students in non-economics fields in Rehovot, Israel, with normal/corrected vision; informed consent under the Declaration of Helsinki. Each faced a sequence of virtual binary choice problems with **no time limit** (median response time about 6–8 seconds). Subjects received only a \$12 show-up fee and were **not** paid by choice, justified by Camerer–Hogarth (1999) that incentives rarely shift choices; in any case the focus is the *procedure*, not choice distributions. Because incomplete-data answers were dropped, the analyzed subset varies by question (e.g. $N\approx35\text{–}41$ for U1–U4). A companion dataset is published with the AEJ article.

## Key findings
1. **Difficulty drives componentwise processing.** Comparing easy-expectation problems (U1–U2) with hard-expectation problems (U3–U4, e.g. \$637 at $p=0.649$ vs \$549 at $p=0.732$): horizontal movement is only 45–47% in the easy pair but rises to 59–61% in the hard pair. When the $p\cdot x$ multiplication is laborious, subjects switch toward C-procedures.
2. **Calibration tasks behave as predicted.** In difference problems (D1) and time-preference problems (T1–T3), roughly two-thirds (and up to ~82%) of movements are horizontal — confirming componentwise comparison where holistic integration is implausible, validating the gaze-to-procedure mapping.
3. **Lottery choice is a hybrid.** The lottery problems' $a$-vectors sit *between* the clearly-holistic and clearly-componentwise benchmarks: vertical share is well below a difference task like D1 yet above a time-preference task like T3. So even "easy" lottery choices are not pure EU integration — they blend H- and C-procedures.
4. **Some individual consistency, but procedure does not predict choice.** Ranking subjects by $V/(V+H)$, Spearman rank correlations are significant (5% level) in 4 of 6 question pairs (e.g. $\rho(\text{U3},\text{U4})=0.42$), indicating a stable individual tendency. However, eye-movement tendency is **not** correlated with which lottery was actually chosen.
5. **Layout robustness.** With a diagonal layout (U5–U8), diagonal movements dominate, consistent with the same componentwise reading.

## Contribution
Provides direct, low-cost, naturalistic process evidence that the expected-utility "integrate then compare" story is at best incomplete as a *description of deliberation*. By tying an explicit formal taxonomy (H- vs C-procedures) to a measurable physical signal and calibrating it against transparent tasks, the paper supplies empirical traction for similarity- and comparison-based choice models (Rubinstein 1988) that need not derive from maximizing a well-defined preference relation. Methodologically it advances the eye-tracking process-tracing tradition (Russo–Rosen 1975; Russo–Dosher 1983) and complements MouseLab studies, while arguing eye tracking captures more natural, unconscious search than mouse-based information acquisition.

## Limitations & open questions
- The authors are explicit that they "go no further than examining experimental data to find evidence for the use of C-procedures" — they do **not** estimate or test a structural $h(f(x_1,x_2),g(p_1,p_2))$ model; specifying and identifying such a model is left open.
- Discernment from raw gaze movies failed in all but a few cases, forcing the aggregate $a$-vector measure; finer trial-level procedure inference remains unsolved.
- No monetary incentives; although defended, incentive-sensitivity of *procedure* (as opposed to choice) is untested.
- Procedure does not predict the actual choice, leaving open how componentwise gaze translates into a decision rule and what the unmodeled determinants of choice are.
- Small, homogeneous student sample on a narrow problem set; external validity and the boundary conditions of the difficulty effect are open.
- "The proof is in the pudding": whether this evidence should actually change how decision-making under uncertainty is modeled is posed as an open program rather than settled.

## Connections
The theoretical anchor is Ariel Rubinstein (1988), "Similarity and Decision-Making under Risk," which proposes similarity-based comparison as a resolution to the Allais paradox — the C-procedures here are its behavioral correlate. The componentwise/contingent-weighting idea draws on Tversky, Sattath, and Slovic (1988). Methodologically the paper sits squarely in process-tracing: the early eye-fixation work of Russo and Rosen (1975) and Russo and Dosher (1983) (feature-by-feature comparison), and the MouseLab paradigm of Payne, Bettman, and Johnson (1993), with Johnson, Schulte-Mecklenbeck, and Willemsen (2008) on gambling choice and Lohse–Johnson (1996) on tracing-method comparison; the no-incentive choice is licensed by Camerer and Hogarth (1999). Contemporary neuroeconomic process studies include Wang, Spezio, and Camerer (2010) on deception in sender–receiver games and Reutskaja et al. (2011) on consumer search under time pressure. The work is a touchstone for bounded-rationality and attention-based models of risky choice (e.g. later attentional-drift-diffusion and salience theories).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
