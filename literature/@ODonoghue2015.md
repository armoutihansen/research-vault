---
citekey: ODonoghue2015
title: "Present Bias: Lessons Learned and To Be Learned"
authors: ["O'Donoghue, Ted", "Rabin, Matthew"]
year: 2015
type: journalArticle
doi: 10.1257/aer.p20151085
zotero: "zotero://select/library/items/CBWGIR42"
pdf: /Users/jesper/Zotero/storage/EJBK2HG5/ODonoghue2015.pdf
tags: [literature]
keywords: [present-bias, quasi-hyperbolic-discounting, time-inconsistency, sophistication-naivete, behavioral-welfare, intertemporal-choice]
topics: ["[[intertemporal-choice-present-bias]]"]
related: [Koszegi2009, Loewenstein1987]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> While present bias is an old idea, it only took hold in economics following David Laibson's (1994) dissertation. Over the past 20 years, research has led to a much better theoretical understanding of present bias, when and how to apply it, and which ancillary assumptions are appropriate in different contexts. Empirical analyses have demonstrated how present bias can improve our understanding of behavior in various economic field contexts. Nonetheless, there is still much to learn. In this paper, we give our assessment of some lessons learned, and to be learned.

## Summary
This AEA Papers & Proceedings essay by O'Donoghue and Rabin takes stock of two decades of research on present bias (the $\beta,\delta$ quasi-hyperbolic discounting model). It is not an empirical or theoretical contribution but a synthesizing reflection: the authors lay out six "lessons learned" that they regard as settled among insiders but worth restating, and four "lessons to be learned" framed as open questions that should guide future work. The recurring theme is methodological discipline: present bias operates on the timing of utility (not money), it is fundamentally about "now," and it should be deployed carefully alongside (not as a substitute for) other behavioral and standard-economic factors.

## Research question
What has the economics literature learned about how to model and apply present bias since Laibson (1994), and what important conceptual and empirical questions remain open? The piece is organized around correctly specifying, identifying, and welfare-evaluating present-biased preferences, and around not over-attributing behavior to present bias.

## Method / identification
The paper is a conceptual/expository review, not a model or estimation exercise. Its analytical backbone is the standard quasi-hyperbolic ($\beta,\delta$) discounting model. Intertemporal preferences from the perspective of period $t$ are represented by
$$U^t = \sum_{\tau=t}^{\infty} D(\tau-t)\,u_\tau,$$
where $u_\tau$ is instantaneous utility in period $\tau$ and the discount function takes the form
$$D(x) = \begin{cases} 1 & \text{if } x = 0,\\ \beta\,\delta^{x} & \text{if } x > 0,\end{cases}$$
with $\beta = 1$ recovering exponential discounting and $\beta \in (0,1)$ encoding present bias. The authors stress the ancillary assumption about beliefs: agents may be sophisticated (aware preferences will change), naive (unaware), or partially naive (in between). On identification, they articulate a recipe: estimating $\beta$ and $\delta$ requires data on multiple choice types — some involving immediate-vs-future tradeoffs (informative about $\beta$) and others involving future-vs-further-future tradeoffs (informative about $\delta$).

## Data
None — this is a synthesis essay with no original dataset. It draws on illustrative findings from prior structural and field studies (e.g., Angeletos et al. 2001 on consumption-saving; DellaVigna & Paserman 2005 on job search; Augenblick, Niederle & Sprenger 2013 on real-effort tasks).

## Key findings
The six lessons learned:
1. **Present bias operates on utility, not money or purchases.** Absent liquidity constraints and uncertainty, choices between dated monetary payments are driven by wealth maximization, so money-only time-preference experiments are uninformative; recent designs use real (effort) flows instead.
2. **Present bias is about "now."** The $\beta,\delta$ form concentrates the deviation from time consistency on the immediate period. Attaching a front-end delay to all payoffs removes present bias from behavior; null results under front-end delay actually support $\beta,\delta$ over the hyperbolic $D(x)=1/(1+kx)$ form.
3. **Any noticeable short-term discounting is evidence of present bias.** A calibration-style argument (analogous to Rabin's risk-aversion calibration): exponential discounting cannot generate noticeable short-horizon impatience without implying absurdly severe long-horizon discounting.
4. **Naivete is a legitimate, rigorously modelable assumption and does not always imply "crazy" behavior** — sometimes naive predictions coincide with sophisticated ones, sometimes they predict damaging-but-realistic behavior (procrastination over diets, quitting smoking, referee reports).
5. **There is a natural intuition for identifying $\beta$ and $\delta$** — combine choices heavily driven by present bias with those driven by long-run discounting (the savings/job-search examples).
6. **Welfare analysis is doable.** The authors advocate the "long-run utility" criterion (evaluating $U$ as if $\beta = 1$), which often coincides with the Pareto-across-selves criterion; they conjecture long-run utility will become the standard.

The four open questions (lessons to be learned) are summarized below.

## Contribution
Consolidates the field's accumulated wisdom into a compact, citable reference that disciplines applied use of present bias. It clarifies common pitfalls (money-flow experiments, front-end-delay confounds, over-attribution) and explicitly stakes out the long-run-utility welfare criterion. It also reframes the research frontier as four targeted questions, serving as an agenda-setting piece.

## Limitations & open questions
The authors' four explicit "lessons to be learned" are direct project hooks:
- **Q1 — How can we improve the predictions of present bias?** Enrichments such as heterogeneity in $\beta$ across individuals and context-dependence of present bias (e.g., dual-process models) are promising, but the authors worry researchers over-focus on the details of present bias while neglecting utility functions, timing of decisions, and constraints/transactions costs. They are skeptical that heterogeneity in tastes is mostly heterogeneity in present bias (cigarette example).
- **Q2 — How important is temporal aggregation?** Data arrive at frequencies (monthly/quarterly) that net together many underlying daily decisions; estimating a model whose period equals the data frequency can badly distort present-bias estimates. The right approach models how underlying decisions aggregate.
- **Q3 — How to assess present bias against other phenomena?** Four confounding intertemporal mechanisms — habit formation, projection bias, anticipatory utility, and intertemporal "news" utility — can mimic or be mistaken for present bias; better tools are needed to tease them apart.
- **Q4 — How to assess whether commitments are due to present bias?** Commitment is the signature prediction of sophisticated present bias, but belief-based-utility motives, mispredicted future behavior (naive snack-package purchasing), and negative-cost commitments can all generate apparent commitment without sophistication.

A general limitation the authors concede: the $\beta,\delta$ model is "not correct," and there is little direct evidence comparing functional forms (psychologists compare only hyperbolic vs. exponential).

## Connections
Builds directly on the authors' own foundational work: O'Donoghue & Rabin (1999a) "Doing It Now or Later," O'Donoghue & Rabin (1999b) on procrastination in retirement saving, O'Donoghue & Rabin (2001) "Choice and Procrastination," and O'Donoghue & Rabin on optimal sin taxes. The model's lineage runs through Laibson (1994, 1997 "Golden Eggs and Hyperbolic Discounting"), Phelps & Pollak (1968), Pollak (1968) "Consistent Planning," and Strotz (1956) on time-inconsistency and the sophistication/naivete distinction; Akerlof (1991) on procrastination and obedience first took naivete seriously. The identification examples come from Angeletos, Laibson, Repetto, Tobacman & Weinberg (2001) and DellaVigna & Paserman (2005); the money-vs-effort point from Augenblick, Niederle & Sprenger (2013). The confounding phenomena cite [[@Loewenstein1987|Loewenstein (1987)]] on anticipatory utility, Loewenstein, O'Donoghue & Rabin (2003) on projection bias, and [[@Koszegi2009|Koszegi & Rabin (2009)]] on reference-dependent/news utility. Wertenbroch (1998) provides the package-rationing commitment evidence. The methodological move parallels Camerer (2000) on prospect theory "in the wild" and Rabin's calibration critique of expected utility.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
