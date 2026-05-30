---
citekey: Berns2006
title: Neurobiological Substrates of Dread
authors: ["Berns, Gregory S.", "Chappelow, Jonathan", "Cekic, Milos", "Zink, Caroline F.", "Pagnoni, Giuseppe", "Martin-Skurski, Megan E."]
year: 2006
type: journalArticle
doi: 10.1126/science.1123721
zotero: "zotero://select/library/items/EVN7WW4K"
pdf: /Users/jesper/Zotero/storage/XUH5I2LG/Berns2006.pdf
tags: [literature]
keywords: [dread, intertemporal-choice, neuroeconomics, anticipation-utility, pain-matrix, fmri, experienced-utility, discounting]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> Given the choice of waiting for an adverse outcome or getting it over with quickly, many people choose the latter. Theoretical models of decision-making have assumed that this occurs because there is a cost to waiting—i.e., dread. Using functional magnetic resonance imaging, we measured the neural responses to waiting for a cutaneous electric shock. Some individuals dreaded the outcome so much that, when given a choice, they preferred to receive more voltage rather than wait. Even when no decision was required, these extreme dreaders were distinguishable from those who dreaded mildly by the rate of increase of neural activity in the posterior elements of the cortical pain matrix. This suggests that dread derives, in part, from the attention devoted to the expected physical response and not simply from fear or anxiety. Although these differences were observed during a passive waiting procedure, they correlated with individual behavior in a subsequent choice paradigm, providing evidence for a neurobiological link between the experienced disutility of dread and subsequent decisions about unpleasant outcomes.

## Summary
Standard discounted-utility theory predicts people should always want to delay unpleasant outcomes, yet many prefer to "get it over with" — even paying for the privilege. Berns and colleagues operationalize this as the *utility of dread* and use fMRI during anticipation of a painful foot shock to find its neural correlates. Fitting a modified Loewenstein anticipation model to the BOLD time courses, they show that the disutility of waiting is encoded by an early, sustained rise in activity in the *posterior* (somatosensory/attentive) elements of the cortical pain matrix — SI, SII, posterior insula, and caudal ACC — rather than the anterior "emotional" regions. The slope of this anticipatory rise, measured during purely passive waiting, predicts whether an individual will later behave as an "extreme dreader" in a real choice task, biologically linking experienced (hedonic) utility to decision utility.

## Research question
Why do people frequently expedite unpleasant outcomes rather than delay them, contrary to discounted-utility theory? Specifically: which brain regions display a temporal activity profile consistent with a *utility-of-anticipation* (dread) model while waiting for an aversive event, and does this passive neural signature differentiate individuals by their willingness to wait when an actual intertemporal choice is offered?

## Method / identification
The design has two phases run inside the scanner on $n=32$ participants. **Phase 1 (passive delay conditioning):** 96 trials, each opening with a cue specifying a shock voltage (10, 30, 60, or 90% of individual maximum tolerable voltage) and a delay (1, 3, 9, or 27 s) — all 16 combinations. Shocks (cutaneous, 10–15 ms, dorsum of left foot) were delivered on a 100% reinforcement schedule during a 50 ms inter-volume pause to avoid imaging artifacts. After each trial a visual analog scale (VAS) captured the subjective experience of the whole trial including the wait. **Phase 2 (real forced choice):** participants chose between voltage–delay pairs (e.g. "90% in 3 s" vs "60% in 27 s") with real consequences; choosing the shorter delay could not shorten the experiment (saved time was added to the inter-trial interval), so timing preferences reflect dread, not impatience.

From Phase-2 choices an ordinal preference ranking over voltage–delay combinations was constructed, and the **marginal rate of substitution (MRS)** of voltage for delay — how much voltage one would trade for a second of waiting — served as the behavioral dread metric. A clustering procedure split the cohort into *extreme dreaders* ($n=9$, willing to accept higher voltage to avoid waiting) and *mild dreaders* ($n=23$, who shorten delays but won't pay in voltage).

The neural identification rests on a modified version of Loewenstein's anticipation-utility model. The present value at time $t$ of a delayed shock delivered at time $T$ combines discounted consumption and a separately entering dread term:
$$U(V,t) = U(V)\,\big[\,a(T-t) + e^{-r(T-t)}\,\big]$$
where $U(V)$ is the (dis)utility of the shock as a function of voltage $V$, $r$ is the discount rate, and $a$ is the **dread factor**. The dread component is the forward-looking integral from $t$ to $T$ (i.e. proportional to $-at$), which is maximal at cue onset and declines linearly to zero at shock delivery; the consumption component grows exponentially toward the outcome. A significantly positive $a$ implies an *early* rise in the time course. Each term was convolved with a hemodynamic response function and fit to region-of-interest (ROI) BOLD time series for pain-matrix subregions (SI, SII, anterior/posterior insula, rostral/middle/caudal ACC, amygdala), with $a$ compared against zero and between groups. A separate voltage-weighted contrast on the *instantaneous* shock response tested whether waiting changed the disutility of the outcome itself.

## Data
First-hand experimental fMRI and behavioral data from 32 human participants; BOLD time series across pain-matrix ROIs, VAS ratings, and revealed preferences from the real-stakes choice task. No external/observational dataset.

## Key findings
- **Dread is behaviorally real and common:** when voltages were equal, participants chose the shorter delay 78.9% of the time on average; 27 of 32 did so more than half the time. A subset (extreme dreaders) accepted higher voltage purely to avoid waiting.
- **Passive ratings match choice-based categories:** extreme dreaders rated long-wait trials as significantly *more unpleasant* than short-wait trials (group × delay interaction); mild dreaders did not — validating the categorization outside the decision context.
- **The outcome's disutility does not change with waiting:** the instantaneous shock response scaled with voltage in all ROIs but was essentially unaffected by preceding delay (with a marginal exception in right SII) and did not differ between groups. Hence preference for expediting must arise *during waiting*, not from sensitization of the outcome.
- **Dread localizes to posterior pain-matrix elements:** significantly positive dread factors $a$, larger in extreme than mild dreaders, appeared in right SI, right SII, right posterior insula, and the caudal ACC — seen as an early, sustained anticipatory rise. The anterior "emotional" regions (anterior insula, rostral ACC) did not show this profile. The right amygdala had a positive dread factor in both groups but did *not* distinguish them.
- **Interpretation:** dread has a substantial *attentive* component (attention to the expected physical response), not merely fear/anxiety. The dread model fit the data better than a simple discounting model, indicating the dread term is necessary.
- **Experiential-to-decision-utility link:** because the differentiating signals were recorded passively (no choice offered), and yet predicted later choice behavior, the study provides what the authors call the first direct biological link between experienced (hedonic) utility and decision utility.

## Contribution
The paper supplies a neurobiological substrate for the *utility of dread*, a long-assumed but rarely measured construct in intertemporal-choice economics, and validates a specific functional-form prediction (the declining forward-integral dread term) against brain data. Methodologically, it offers a principled way to adjudicate between competing anticipation models by fitting their predicted time courses to fMRI. Conceptually, it relocates dread from a purely emotional phenomenon toward an attentional one and bridges Kahneman-style experienced utility with revealed-preference decision utility.

## Limitations & open questions
- The authors note it is unclear **how malleable** these waiting preferences are; the experiment observed preference *construction* for an unfamiliar stimulus (foot shock) but cannot say how plastic intrinsic preferences are in general.
- They flag **health/policy implications** as open: whether the dread mechanism can be leveraged for better pain management and public health (e.g. how patients confront known-unpleasant medical procedures).
- The model deliberately assumes **constant instantaneous dread intensity** for tractability; richer (non-constant) dread dynamics are left untested.
- The dread/consumption term separation could not be fully resolved on the **1-s and 3-s trials** (cue and shock responses overlap), so those beta estimates are not strictly comparable to the longer delays.
- Generalization beyond the **pain domain** (the cortical pain matrix) and beyond a single aversive modality is raised as a target for the same modeling approach.

## Connections
The economic backbone is Loewenstein's anticipation model (Loewenstein 1987) and the Caplin–Leahy (2001) formalization of anxiety/anticipatory feelings, set against Samuelson's (1937) discounted utility. The experienced-vs-decision-utility framing draws on Kahneman, Wakker & Sarin (1997) and Camerer, Loewenstein & Prelec (2005). It contrasts with McClure, Laibson, Loewenstein & Cohen (2004) on the neural basis of intertemporal choice — crucially, Berns et al. obtain their signals *passively* rather than during choice. The "pain matrix" mapping builds on Ploghaus et al. (1999, 2003) and Koyama et al. (2005) on pain anticipation, Craig (2003) and Vogt (2005) on insular and cingulate organization, and Phelps (2006) on the amygdala in aversive conditioning. The contrast with trial-based learning — Rescorla–Wagner and temporal-difference (Sutton) models — highlights that those theories predict learning from prediction error but say little about the *shape* of anticipation leading up to an outcome, which the dread integral specifies.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
