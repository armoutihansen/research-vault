---
citekey: Schlag2021
title: "Simple belief elicitation: An experimental evaluation"
authors: ["Schlag, Karl", "Tremewan, James"]
year: 2021
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/HUMJLYM7"
pdf: /Users/jesper/Zotero/storage/M8596GNY/Schlag and Tremewan - 2021 - Simple belief elicitation An experimental evaluation.pdf
tags: [literature]
keywords: [belief-elicitation, frequency-format, proper-scoring-rules, risk-aversion, partial-identification, cognitive-ability, laboratory-experiment]
topics: ["[[experimental-belief-elicitation]]"]
related: [Gigerenzer1995, Gneiting2007, Karni2009, Offerman2009]
added: 2026-06-01
generated: 2026-06-01
---

> [!abstract] Abstract
> We present a method for eliciting beliefs about probabilities when multiple realisations of an outcome are available, the "frequency" method. The method is applicable for any reasonable utility function. Unlike existing techniques that account for deviations from risk-neutrality, this method is highly transparent to subjects and easy to implement. Rather than identifying point beliefs these methods identify bounds on beliefs, thus trading off precision for generality and simplicity. An experimental comparison of this method and a popular alternative, the Karni method, shows that subjects indeed find the frequency method easier to understand. Significantly, we show that confusion due to the complexity of the Karni method leads to less cognitively able subjects erroneously stating a belief of 50%, a bias not present in the frequency method.

## Summary
Schlag and Tremewan propose and experimentally evaluate the "frequency" method of belief elicitation: instead of asking subjects for a numerical probability, the experimenter exploits the many independent realisations of a random variable that are naturally available in the lab (e.g. the 19 other partners in a one-shot game) and asks the subject to *guess the realised frequency* of each outcome, paying a fixed prize if and only if the guess is exactly correct. The central claims are (i) the method is incentive-compatible for *any* monotone utility — it is robust to risk attitudes; (ii) it does not recover a point belief but a tight *interval* of consistent beliefs, and that interval is provably the most precise any single-report rule can achieve; and (iii) because reports are framed as natural frequencies rather than single-event probabilities, subjects understand it better, answer faster, and avoid the focal "50%" response that plagues the leading risk-robust alternative, the [[@Karni2009|Karni (2009)]] mechanism. A companion quantile-elicitation method built on the same multiple-realisation logic is also tested but found to perform poorly.

## Research question
Can beliefs about event probabilities be elicited in a way that is simultaneously (a) incentive-compatible without assuming risk-neutrality, (b) fast and cheap to run, and (c) genuinely simple for subjects to understand — and does such simplicity actually improve data quality relative to a theoretically clean but cognitively demanding mechanism?

## Method / identification
Let $Y$ be a random variable with $k$ outcomes $s_1,\dots,s_k$ and let $p_i$ be the subject's subjective probability of $s_i$. The experimenter draws $n$ independent realisations of $Y$. The subject submits a report $b=(b_1,\dots,b_k)$ of non-negative integers summing to $n$ and wins a fixed prize $R$ iff $b_i$ equals the number of times $s_i$ actually occurs for every $i$. From the subject's standpoint the prize is won with probability given by the multinomial likelihood
$$f(b)=\frac{n!}{b_1!\cdots b_k!}\prod_{i=1}^{k} p_i^{b_i}.$$
Because the payoff is the *fixed* prize times the probability of an exact match, expected utility is maximised iff $f(b)$ is maximised — for *any* utility with $u(\text{prize})>u(\text{no prize})$. This is what makes the rule robust to risk attitudes: no scoring curve, no probability of intermediate payoffs.

**Proposition 1** characterises the maximiser: $b$ maximises $f$ over the feasible set iff $\frac{b_i}{b_j+1}\le \frac{p_i}{p_j}\le \frac{b_i+1}{b_j}$ for all $j\ne i$ (with $b_j=0$ when $p_j=0$). This pins each report to a region of the belief simplex; equivalently $\frac{b_i}{n+k-1}\le p_i\le \frac{b_i+1}{n+1}$. For binary events ($k=2$) the implied interval has width $1/(n+1)$ — e.g. $5\%$ when $n=19$. Beliefs satisfying the inequalities strictly have a *unique* best report; only beliefs on a boundary admit ties.

**Proposition 2** establishes optimality: define the minimal precision of a rule as the negative of the largest distance between two beliefs mapped to the same report. For $k=2$ any alternative single-report rule has strictly lower minimal precision than the frequency method — i.e. no rule taking the same input can resolve beliefs more tightly while remaining valid for arbitrary utility. The proof (Appendix A) compares $f(b)$ to one-unit reallocations of mass between coordinates. The estimand is therefore an interval (partial identification of the latent belief), trading precision for distributional generality.

## Data
Laboratory experiment ($N=168$; 84 subjects per treatment), recruited via ORSEE, programmed in jtree, run between-subjects with the **frequency** method versus the **[[@Karni2009|Karni (2009)]]** mechanism as benchmark. Three parts: a Stag Hunt game (beliefs about others choosing the risky/cooperative action B), an Urn task (objectively known posterior, $9{:}1$ urns, allowing an accuracy check), and a two-person public-goods game used to test the quantile method (MPCR $0.65$ and $0.9$). Comprehension was measured by four 7-point Likert questions plus response time; cognitive ability by the Cognitive Reflection Test (CRT). Sessions lasted ~30 min; average earnings €12.50.

## Key findings
1. **No loss of belief content but big gain in comprehension.** Mann–Whitney tests show no treatment difference in the *distribution* of elicited beliefs in either the Stag Hunt ($p=0.923$) or Urn ($p=0.559$) tasks, and the interval format loses negligible precision (88–92% of Karni responses are multiples of $0.05$). Yet self-reported understanding is higher for the frequency method (6.7 vs 5.7; $p<0.01$), and it is far faster (31 s vs 79 s; $p<0.01$). No difference in best-response rates (0.76 vs 0.83) or average distance from the empirical proportion.
2. **The 50% bias.** In the Karni treatment 27% of subjects state exactly $0.5$ in the Stag Hunt (vs 5% choosing the corresponding "10 balls" in the frequency treatment; $p<0.01$). This focal $0.5$ is *negatively correlated with CRT score* (probit $p=0.047$): confused, low-ability subjects default to the middle value — a bias absent under the frequency method. The pattern recurs in the Urn task.
3. **Quantile method fails.** The analogous multiple-realisation method for medians/quartiles produced incoherent reports — 8% (24%) of subjects gave an upper (lower) quartile inconsistent with their own median — so the authors do not recommend it as implemented.

## Contribution
Gives the first rigorous theoretical characterisation (Propositions 1–2) of a "frequency-guessing" elicitation that had been used informally and misunderstood in prior work (Wilcox & Feltovich 2000; Costa-Gomes & Weizsäcker 2008; Hurley & Shogren 2005). It supplies a risk-robust, assumption-light, fast belief-elicitation tool, and — methodologically — demonstrates that clean theoretical incentive-compatibility (Karni) does not guarantee clean data: cognitive load induces a systematic focal-point bias correlated with ability. It reframes elicitation design around the cognitive-psychology insight that natural frequencies are processed more easily than single-event probabilities ([[@Gigerenzer1995|Gigerenzer & Hoffrage 1995]]).

## Limitations & open questions
- The method delivers only *interval* (partial) identification; for $k>2$ the bounds are coarser and the optimal-precision result (Prop. 2) is proven only for binary events — extending optimality to $k>2$ is open.
- Requires $n$ genuine independent realisations; not applicable to one-off events without such structure.
- The Urn-task accuracy check is confounded by non-Bayesian updating, so "distance from truth" cannot cleanly rank the methods.
- The companion **quantile elicitation** method is not yet usable; *which* simple, risk-robust quantile/distribution mechanism to adopt remains open (cf. Qu 2012's extension of Karni).
- Whether the focal-$0.5$ bias generalises to other complex mechanisms, and whether graphical aids or alternative Karni implementations remove it, is left for future work.

## Connections
The paper sits squarely in the incentive-compatible belief-elicitation literature: it benchmarks against the risk-robust mechanism of [[@Karni2009|Karni (2009)]] (as implemented by Dal Bó, Foster & Putterman 2017) and contrasts with non-robust proper scoring rules surveyed by [[@Gneiting2007|Gneiting & Raftery (2007)]] and the calibration approach of Offerman, Sonnemans, van de [[@Offerman2009|Kuilen & Wakker (2009)]]; broader surveys include Schotter & Trevino (2014) and Schlag, Tremewan & van der Weele (2015). The cognitive-format argument draws on [[@Gigerenzer1995|Gigerenzer & Hoffrage (1995)]], Cosmides & Tooby (1996), Kahneman & Tversky (1983), and Manski's (2004) observation that subjects round to multiples of five. The ability–accuracy link complements Burfurd & Wilkening (2020). Its motivating use case — separating social preferences from beliefs in games such as the Stag Hunt and public-goods game — connects to elicited-belief studies of conditional cooperation (e.g. Blanco, Engelmann, Koch & Normann 2010).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
