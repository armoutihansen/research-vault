---
citekey: Gigerenzer1995
title: "How to improve Bayesian reasoning without instruction: frequency formats."
authors: ["Gigerenzer, Gerd", "Hoffrage, Ulrich"]
year: 1995
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/EPUWYN9W"
pdf: /Users/jesper/Zotero/storage/DPJP5GX9/Gigerenzer and Hoffrage - 1995 - How to improve Bayesian reasoning without instruction frequency formats..pdf
tags: [literature]
keywords: [bayesian-reasoning, frequency-format, natural-sampling, base-rate-neglect, heuristics-and-biases, probability-judgment, risk-communication]
topics: []
related: []
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> Is the mind, by design, predisposed against performing Bayesian inference? Previous research on base rate neglect suggests that the mind lacks the appropriate cognitive algorithms. However, any claim against the existence of an algorithm, Bayesian or otherwise, is impossible to evaluate unless one specifies the information format in which it is designed to operate. The authors show that Bayesian algorithms are computationally simpler in frequency formats than in the probability formats used in previous research. Frequency formats correspond to the sequential way information is acquired in natural sampling, from animal foraging to neural networks. By analyzing several thousand solutions to Bayesian problems, the authors found that when information was presented in frequency formats, statistically naive participants derived up to 50% of all inferences by Bayesian algorithms. Non-Bayesian algorithms included simple versions of Fisherian and Neyman-Pearsonian inference.

## Summary

Gigerenzer and Hoffrage reframe the debate over whether humans are "Bayesian." The heuristics-and-biases tradition (Kahneman & Tversky) concluded from base-rate-neglect experiments that the mind does not reason according to Bayes' theorem at all; the Enlightenment probabilists held the opposite. The authors argue both camps committed the same error: studying *cognitive algorithms* in isolation from the *information format* on which those algorithms operate. Just as a calculator's multiplication routine fails on binary input though it works on Arabic numerals, a Bayesian algorithm in the mind cannot be detected if information is fed in a representation it was not designed for. Their central thesis is that mathematically equivalent representations are not computationally equivalent. The format for which evolved statistical algorithms were designed, they contend, is *frequencies acquired by natural sampling* — sequential event counts, not single-event probabilities or percentages, which are recent cultural inventions. Two experiments confirm that converting the classic disease/eyewitness problems from probability to frequency formats roughly triples or quadruples the proportion of genuinely Bayesian solutions, without any instruction.

## Research question

Does the failure of statistically naive people to reason according to Bayes' theorem reflect a missing cognitive algorithm, or merely a mismatch between the algorithm and the *information format* in which the problem is posed? Equivalently: can Bayesian reasoning be improved purely by changing the external representation of the same information, with no teaching?

## Method / identification

The task throughout is elementary Bayesian inference: infer a single-point estimate of $p(H\mid D)$ for two mutually exclusive, exhaustive hypotheses $H,\neg H$ given one datum $D$ (e.g. the mammography problem). The paper's identification strategy is theoretical-then-experimental.

The authors formally separate two dimensions of representation: **information format** (single-event *probability* vs. *frequency*) and **information menu** (how information is segmented). The standard probability format supplies base rate $p(H)$, hit rate $p(D\mid H)$, false alarm rate $p(D\mid\neg H)$ and requires the textbook Bayes equation

$$p(H\mid D)=\frac{p(H)\,p(D\mid H)}{p(H)\,p(D\mid H)+p(\neg H)\,p(D\mid\neg H)}.$$

The **frequency format** obtained by natural sampling instead supplies absolute counts $d\&h$ and $d\&\neg h$, so the posterior reduces to

$$p(H\mid D)=\frac{d\&h}{d\&h+d\&\neg h},$$

which is Bayes' (1763) original Proposition 5. These are mathematically equivalent but the second requires fewer operations on natural numbers rather than fractions. From this they derive six theoretical results: (1) **computational demands** — frequency formats are computationally simpler; (2) **attentional demands** — only $d\&h$ and $d\&\neg h$ (or $d\&h$ and $d$) need to be tracked; (3) **base rates need not be attended to** — base-rate neglect is *rational* under natural sampling because the base rate is already absorbed into the counts; (4) **posterior distributions computable** — absolute frequencies carry sample-size information; (5) with a probability format the short menu is simpler than the standard menu; (6) with a frequency format both menus require the same computation.

Crossing the two formats with two menus yields standard/short probability and frequency versions. Participants worked through batteries of such problems; the dependent variable was not just the numerical answer but the *cognitive algorithm* inferred from "write-aloud" protocols, notes, and after-the-fact interviews — classified as Bayesian or as one of several non-Bayesian strategies.

## Data

Original experimental data, not theory-only. **Study 1**: 60 paid University of Salzburg students (none familiar with Bayes' theorem), 15 problems crossed over probability/frequency format and standard/short menu, with "write-aloud" protocols. **Study 2**: 15 University of Konstanz students, 24 problems across three menus (standard, hybrid, short) = 72 tasks each over six sessions, with limited write-aloud and interview data; algorithms were identifiable in 67% of 1,080 judgments. Together these constitute the "several thousand solutions" analyzed.

## Key findings

Across the predictions: **(P1)** frequency formats elicit far more Bayesian solutions — the smallest Bayesian share in any frequency menu (46%) exceeded the largest in any probability menu (28%); format effects were about three times larger than menu effects. **(P2)** within probability formats, the short menu yields more Bayesian solutions than the standard menu (16% vs. 28% in Study 1; ~12-point gap replicated in Study 2). **(P3)** within frequency formats the menu effect almost vanishes, consistent with Result 6. **(P4)** *relative* frequencies (relative to fixed marginals, still asking for a single-event probability) do *not* help — they elicited no more Bayesian algorithms than probabilities, confirming it is natural-sampling absolute frequencies, not "frequency" per se, that matters. Three robust non-Bayesian algorithms recurred: **joint occurrence** ($p(H\&D)$, most common, always underestimates the posterior), **Fisherian** (report $p(D\mid H)$ alone, confusing it with $p(H\mid D)$), and **likelihood subtraction** / Neyman–Pearson-style ($p(D\mid H)-p(D\mid\neg H)$), plus a false-alarm-complement shortcut. Individual algorithms were highly **menu-dependent**: in 96% of 360 triples a participant never used the same algorithm across the three menus, showing reasoning is constructed from the representation rather than stable.

## Contribution

Provides a unifying theoretical framework — the format/menu distinction and the six results — that dissolves the Bayesian-vs.-heuristics impasse by relocating the question from internal competence to representation. It supplies an evolutionary/ecological rationale (natural sampling) for why frequencies should be the privileged format and demonstrates a powerful, instruction-free "human engineering" intervention. The paper became foundational for the frequency-format / fast-and-frugal program and for medical risk communication (natural frequencies in diagnostic testing).

## Limitations & open questions

The claim is explicitly about *external* representations; the authors disclaim specific claims about internal representations, leaving open how the format effect is realized cognitively. Even the best frequency conditions left roughly half of inferences non-Bayesian — the residual is uncharacterized. The evolutionary natural-sampling premise is an assumption, not tested. The "Fisherian" and "Neyman–Pearsonian" labels are admittedly loose analogies to misinterpretations rather than to the statisticians' actual methods. Generalization is limited to elementary two-hypothesis, single-datum problems with single-point estimates; multi-datum updating, posterior distributions (Result 4), and non-student populations are left for future work, as is the design of tutoring systems that add visual aids to frequency representations.

## Connections

The paper directly opposes the base-rate-neglect conclusions of Kahneman & Tversky (1972, 1973) and Bar-Hillel (1980), and reinterprets the cab and disease problems of Tversky & Kahneman (1982), Casscells, Schoenberger & Grayboys (1978), and Eddy (1982). The natural-sampling formalism draws on Kleiter (1994) and Brunswik's representative sampling; the evolutionary framing aligns with Cosmides & Tooby and with Gigerenzer's own ecological-rationality program (Gigerenzer & Murray, 1987). The format-dependence of judgment is a representation effect relevant to framing in decision theory and to how choice problems are described in discrete-choice and behavioral experiments, and connects to belief-elicitation in economics. Follow-on work (Sedlmeier & Gigerenzer) shows frequency-format training transfers and persists.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
