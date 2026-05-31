---
citekey: Schmitz2012
title: Assessing fear and anxiety in humans using the threat of predictable and unpredictable aversive events (the NPU-threat test)
authors: ["Schmitz, Anja", "Grillon, Christian"]
year: 2012
type: journalArticle
doi: 10.1038/nprot.2012.001
zotero: "zotero://select/library/items/SCZL95NE"
pdf: /Users/jesper/Zotero/storage/3ZCQ5NLR/Schmitz2012.pdf
tags: [literature]
keywords: [startle-reflex, fear-vs-anxiety, unpredictable-threat, psychophysiology, emg, translational-research, anxiety-disorders]
topics: ["[[anticipatory-utility-motivated-beliefs]]"]
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> The threat of predictable and unpredictable aversive events was developed to assess short-duration (fear) and long-duration (anxiety) aversive states in humans. A typical experiment consists of three conditions: a safe condition (neutral (N)), during which participants are safe from aversive stimuli, and two threat conditions—one in which aversive events are administered predictably (P) (i.e., signaled by a threat cue), and one in which aversive stimuli are administered unpredictably (U). During the so-called NPU-threat test, ongoing change in aversive states is measured with the startle reflex. The NPU-threat test has been validated in pharmacological and clinical studies and can be implemented in children and adults. Similar procedures have been applied in animal models, making the NPU-threat test an ideal tool for translational research. The procedure is relatively short (35 min), simple to implement and generates consistent results with large effect sizes.

## Summary
This is a Nature Protocols step-by-step methods paper (full text, 6 pages) describing the NPU-threat test: a laboratory paradigm for eliciting and measuring fear versus anxiety in humans. Subjects pass through three blocked conditions — Neutral/safe (N), Predictable threat (P, shock signaled by a cue), and Unpredictable threat (U, shock at any time) — while the eyeblink startle reflex is recorded via orbicularis-oculi EMG. Cue-locked startle potentiation in P operationalizes phasic *fear*; sustained inter-cue startle potentiation in U operationalizes *anxiety*. The protocol's appeal is its translational fidelity (parallel rodent paradigms), short duration (~35 min recording), and large, replicable effect sizes that have been validated against anxiolytic drugs and clinical anxiety populations.

## Research question
How can fear and anxiety — conceptually overlapping but theoretically distinct aversive states — be operationally separated and reliably measured in a controlled human laboratory setting? The authors operationalize the distinction along two dimensions established in preclinical work: response duration (phasic versus sustained) and threat type (predictable versus unpredictable). The protocol's purpose is to provide a standardized, replicable instrument that dissociates a short-duration fear response from a long-duration anxiety state.

## Method / identification
The paradigm is the formal object here (there is no statistical estimator or causal-identification design — it is a protocol). The design is a 3-condition within-subject block manipulation crossed with cue presence:

- **N (neutral):** no shocks delivered; subjects are safe throughout.
- **P (predictable):** shocks delivered only during an 8 s colored geometric cue (e.g., red square), 0.5 s before cue offset; never in its absence.
- **U (unpredictable):** shocks delivered at any time, randomized and explicitly *not* time-locked to the cue, so the cue carries no predictive information.

Conditions are presented in counterbalanced orders (P N U N U N P or U N P N P N U), each condition lasting ~120 s with three 8 s cue presentations. The aversive stimulus is a 100 ms electric shock (1–5 mA), individually calibrated via a four-shock "workup" to a target subjective rating of 4 ("quite unpleasant") on a 1–5 scale; milder stimuli (air blast, scream) substitute for children. Crucially, the contingencies are *instructed* (verbally explained with visual aids and on-screen labels) rather than learned by Pavlovian conditioning, separating expression of fear/anxiety from learning/memory confounds.

The dependent measure is the **startle eyeblink reflex**, elicited by 103 dB, 40 ms white-noise probes (instantaneous rise time) delivered once per cue and once per inter-cue interval (minimum 20 s apart), preceded by a habituation phase (nine probes, then four more) to absorb the steep early habituation. Two recording blocks separated by a 5 min break yield 12 shocks total. EMG of the left orbicularis oculi is rectified, smoothed, and scored as blink magnitude in a 150 ms post-probe window; contaminated trials (excessive baseline noise, movement artifacts, blinks earlier than 21 ms latency) are rejected. Raw magnitudes are converted to within-subject $t$-scores (or baseline startle is entered as a covariate) to control for individual differences in startle reactivity.

The two key derived quantities are difference scores:
$$\text{fear-potentiated startle} = S_{\text{cue},P} - S_{\text{no cue},P}$$
$$\text{anxiety-potentiated startle} = S_{\text{no cue},U} - S_{\text{no cue},N}$$
where $S$ denotes mean startle magnitude in the indicated condition. These difference scores are the operational definitions of fear and anxiety, respectively.

## Data
None — this is a protocol/methods paper, not an empirical study with a dataset. It reports *anticipated* results (an illustrative Figure 4 of mean EMG magnitudes) drawn from the authors' prior validation studies rather than new data. Human subjects must be literate with normal/corrected vision and hearing; informed consent and IRB approval are required.

## Key findings
There are no theorems; the "results" are the expected, validated empirical regularities the protocol reliably produces:

- **Fear-potentiated startle:** in the P condition, startle is larger during the cue than in its absence ($S_{\text{cue},P} > S_{\text{no cue},P}$).
- **Anxiety-potentiated startle:** in the U condition, inter-cue startle exceeds neutral inter-cue startle ($S_{\text{no cue},U} > S_{\text{no cue},N}$).
- **Graded context anxiogenicity:** inter-cue startle in P is intermediate between N and U — a predictable context is more anxiogenic than a safe one but less than an unpredictable one, mirroring rodent findings.
- **Pharmacological dissociation:** anxiolytics (benzodiazepines, SSRIs) selectively reduce *anxiety*-potentiated startle at doses leaving *fear*-potentiated startle intact; conversely, hydrocortisone and nicotine withdrawal selectively increase anxiety.
- **Clinical specificity:** panic disorder and PTSD patients show selectively elevated anxiety-, not fear-, potentiated startle; sex/age differences also appear in the anxiety component.

These map onto the neural double dissociation motivating the design: central amygdala (CeA) lesions abolish phasic cued fear, while bed-nucleus-of-the-stria-terminalis (BNST) lesions abolish sustained anxiety.

## Contribution
The paper provides a standardized, well-documented, and translationally valid laboratory instrument that operationally separates fear from anxiety using a single cross-species measure (startle). Its contributions are practical and infrastructural: short administration time (~35 min), simplicity, large effect sizes, demonstrated sensitivity to anxiolytic pharmacology, demonstrated clinical discriminative validity (panic, PTSD), and successful adaptation to children/adolescents. By aligning the human procedure with rodent paradigms, it enables bidirectional translational research on the neurobiology of anxiety disorders and the screening of candidate anxiolytics.

## Limitations & open questions
The authors flag several boundary conditions and future directions (project-idea hooks):

- **Unvalidated variants:** alternative predictability manipulations (countdown-to-shock; probabilistic 100/60/20% short cues; manipulating shock-*intensity* predictability) yield interesting information but have *not* been validated in anxious subjects or against anxiolytics.
- **Instructed vs. conditioned threat:** the instructed-threat version deliberately excludes learning; a Pavlovian-conditioning version exists for studying associative fear/anxiety learning, but the two answer different questions and are not interchangeable.
- **No conditioned inhibition by design:** because shocks are withheld during the U cue and subjects see too few shocks, the cue does not become a learned safety signal — a deliberate but assumption-laden design choice.
- **Open applications:** screening candidate anxiolytics, discriminating among mood/anxiety disorders, identifying risk factors, developmental studies (including puberty), and neuroimaging (e.g., magnetoencephalography) to elucidate underlying mechanisms.
- **Data quality dependencies:** results hinge on careful artifact rejection, adequate startle habituation, individualized shock calibration, and balanced condition ordering; deviations threaten the large-effect-size claim.

## Connections
The protocol synthesizes the authors' own program of NPU studies (Grillon et al. 2004, 2006, 2008, 2009; Schmitz et al. 2011 for youth) and is grounded in Davis, Walker, Miles & Grillon's (2010) account of phasic versus sustained fear and the extended-amygdala (CeA vs. BNST) dissociation (Walker, Toufexis & Davis 2003). It draws on psychometric/structural models of internalizing disorders (Barlow 2000; Brown, Chorpita & Barlow 1998; Krueger 1999) that separate a "fear" factor (phobias, panic) from an "anxious-misery" factor (GAD, PTSD, depression). Methodologically it relies on standardized startle-measurement guidelines (Blumenthal et al. 2003) and psychophysiological-laboratory references (Curtin, Lozano & Allen 2007). Related independent adaptations include Nelson & Shankman (2011) on intolerance of uncertainty and Moberg & Curtin (2009) / Hefner & Curtin (2012) on alcohol's selective anxiolysis. Note: this is a clinical/neuroscience methods paper and sits outside the economics literature of this vault; its relevance is as a measurement paradigm for affective states under predictable versus unpredictable threat.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
