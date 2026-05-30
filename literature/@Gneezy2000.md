---
citekey: Gneezy2000
title: A Fine Is a Price
authors: ["Gneezy, Uri", "Rustichini, Aldo"]
year: 2000
type: journalArticle
doi: 10.1086/468061
zotero: "zotero://select/library/items/3JAD3RVI"
pdf: /Users/jesper/Zotero/storage/86ARY8C2/Gneezy2000.pdf
tags: [literature]
keywords: [incentives, crowding-out, deterrence, incomplete-contracts, social-norms, field-experiment, fines]
topics: []
related: []
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> The deterrence hypothesis predicts that the introduction of a penalty that leaves everything else unchanged will reduce the occurrence of the behavior subject to the fine. We present the result of a field study in a group of day‐care centers that contradicts this prediction. Parents used to arrive late to collect their children, forcing a teacher to stay after closing time. We introduced a monetary fine for late‐coming parents. As a result, the number of late‐coming parents increased significantly. After the fine was removed no reduction occurred. We argue that penalties are usually introduced into an incomplete contract, social or private. They may change the information that agents have, and therefore the effect on behavior may be opposite of that expected. If this is true, the deterrence hypothesis loses its predictive strength, since the clause "everything else is left unchanged" might be hard to satisfy.

## Summary
A randomized field experiment in ten Israeli private day-care centers shows that introducing a small monetary fine for late pickup *increased* late arrivals rather than deterring them, and removing the fine did not undo the increase. The headline interpretation—"a fine is a price"—is that the fine supplied information (or reframed a non-market favor as a purchasable service), changing the parents' perception of an incomplete contract. The result is a foundational demonstration that monetary incentives can crowd out the behavior they target, with hysteresis.

## Research question
Does introducing a penalty (a fine) that leaves "everything else unchanged" reduce the fined behavior, as the deterrence hypothesis from law-and-economics and behavioral psychology predicts? More pointedly: when a contract is incomplete, can adding a price-like sanction change agents' beliefs about the strategic environment so much that the behavioral response reverses sign?

## Method / identification
A controlled field experiment with a difference-in-differences / staged design over roughly 20 weeks (actually 21, with a one-week holiday break) in Haifa, January–June 1998. Of the centers, six were randomly assigned to a fine treatment and four served as a never-fined control. The timeline has four phases: baseline observation (weeks 1–4, no fine), fine introduced in treatment centers (week 5), fine maintained (weeks 5–16), and fine removed with no explanation (weeks 17–20). The fine was NIS 10 per child for arriving more than 10 minutes late (after 16:10), announced by bulletin-board posting, paid monthly to the owner (not the teacher).

Statistical identification (Appendix B) uses ANOVA on the arcsine–square-root transform of the daily percentage of late parents, with day-care center treated as a random effect nested within group, and week nested within five 4-week blocks. Tests include: baseline equivalence of treatment vs. control (weeks 1–4); a within-control time-trend test to rule out spurious drift; block contrasts to localize when the level shifts; and Duncan's multiple range test to control the family-wise error rate.

The paper also develops the theory on three levels. (1) A differential-information / incomplete-contract argument: pre-fine, parents face a partially specified contract and abstain from "too many" delays for fear of an unspecified worse consequence; the fine reveals that the worst case is merely a fine. (2) A simple formal game: an owner of unknown type—severe ($S$, can "kick out" the child, action $K$) or mild ($M$, can only levy fine $f$), each with probability $1/2$—plays an infinitely repeated sequential game against parents who choose a delay; the per-parent payoff is delay value $v$ minus fee, with $v>f$. The proposed sequential equilibrium (Kreps–Wilson) has parents choosing a threshold delay $d^{*}$ that keeps both owner types indifferent between acting and inaction; charging $f$ off-path reveals the owner is type $M$, after which parents, knowing the worst outcome is $f<v$, switch to maximal delay forever—even if $f$ is later withdrawn. (3) A social-norm account requiring three norms, culminating in "A fine is a price" and "Once a commodity, always a commodity," to explain the persistence after removal.

## Data
Observational counts of late-arriving parents per week for each of the 10 centers over 20 weeks (Table 1), with center enrollment (28–37 children) and four-period averages (Table 2). Raw within-cell weekly counts are reported; no individual-level covariates. A companion lab experiment ("Pay Enough, or Don't Pay at All") on flat-fee vs. small-piece-rate IQ-test performance is summarized as corroborating evidence.

## Key findings
- **Fact 1.** Introducing the fine produced a *significant increase* in the number of late-coming parents in the treatment group (block 1 vs. block 2: $F(1,75)=15.52$, $p=.0002$). The late-arrival rate roughly doubled, rising steadily over 3–4 weeks before stabilizing.
- **Fact 2.** Removing the fine did *not* reduce lateness relative to the fine period; the treatment group stayed elevated above control (hysteresis / no reversal). Block 3 vs. block 4 and block 4 vs. block 5 contrasts are insignificant ($p=.15$, $p=.47$).
- **Fact 3.** No significant baseline difference between treatment and control in weeks 1–4 ($F(1,8)=.65$, $p=.44$) and no significant within-control time trend ($F(19,57)=1.04$, $p=.44$), ruling out a pure time effect.
- The formal game yields exactly three matching predictions: low initial delay; increased delay once a fine is charged off-path (revealing type $M$); and no behavioral change when the fine is later removed.

## Contribution
This is the canonical empirical demonstration of *motivation crowding-out* via monetary sanctions in a real contractual setting, paired with a game-theoretic and a social-norm rationalization. It shows the deterrence hypothesis's ceteris-paribus clause is often unattainable because the sanction itself changes information and the perceived "game." The paper anchors the behavioral-economics literature on incentives backfiring and on the expressive/informational content of prices and laws.

## Limitations & open questions
- The authors explicitly cannot adjudicate between the two interpretations (differential-information game vs. social norms) given the data—an open identification problem.
- They concede the social-norm account is methodologically uncomfortable: three separate norms are invoked to explain three facts, and the real test would be *independent verification* that these norms are active.
- Magnitude dependence is acknowledged: a "large enough" fine would deter; the result is about small, non-linear, certain fines. They flag comparing the U.S. system (large proportional fees announced up front, few delays) against their non-linear scheme as "an interesting research project."
- External validity: the misbehavior and sanction are very mild and detection is certain; whether the reversal extends to severe "crimes" (e.g., tax-evasion enforcement announcements, which they raise as a parallel) is left open.
- Removal-period inertia is hard for the norm story alone, prompting the ad hoc "once a commodity, always a commodity" norm.

## Connections
Builds against the law-and-economics deterrence tradition (Becker 1968; Stigler 1970; Ehrlich 1973, 1975) and the behavioral-psychology punishment literature (Estes 1944; Bandura). The incomplete-contract framing connects to contract theory; the equilibrium uses Kreps–Wilson sequential equilibrium. The social-norm apparatus draws on Coleman's *Foundations of Social Theory*, Ullmann-Margalit, and Sunstein/Lessig on social meaning and expressive law. The companion result (Gneezy & Rustichini, "Pay Enough, or Don't Pay at All") ties this to the broader crowding-out program (cf. Frey, Titmuss on blood donation, Bénabou–Tirole on incentives and reputation). It is a touchstone for behavioral mechanism design and for work on how prices and sanctions carry information and shape norms.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
