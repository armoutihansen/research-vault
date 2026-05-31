---
citekey: Caplin2019
title: "Rational Inattention, Optimal Consideration Sets, and Stochastic Choice"
authors: ["Caplin, Andrew", "Dean, Mark", "Leahy, John"]
year: 2019
type: journalArticle
doi: 10.1093/restud/rdy037
zotero: "zotero://select/library/items/MLXL5AJ5"
pdf: /Users/jesper/Zotero/storage/BZ5T4SRZ/Caplin2019.pdf
tags: [literature]
keywords: [rational-inattention, consideration-sets, stochastic-choice, shannon-mutual-information, limited-attention, discrete-choice]
topics: ["[[limited-attention-consideration-sets]]"]
related: [Brady2016, Gabaix2006, Hauser1990, Manzini2014, Masatlioglu2012, Roberts1991]
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We unite two basic approaches to modelling limited attention in choice by showing that the rational inattention model implies the formation of consideration sets—only a subset of the available alternatives will be considered for choice. We provide necessary and sufficient conditions for rationally inattentive behaviour which allow the identification of consideration sets. In simple settings, chosen options are those that are best on a stand-alone basis. In richer settings, the consideration set can only be identified holistically. In addition to payoffs, prior beliefs impact consideration sets. Linear inequalities identify all priors consistent with each possible consideration set.

## Summary
Caplin, Dean, and Leahy show that the Shannon rational-inattention (RI) model endogenously produces *consideration sets*: in discrete-choice problems, typically only a strict subset of available options is ever chosen, and the rest receive no attention. The paper's technical engine is a set of *necessary and sufficient* first-order conditions for the Shannon model (strengthening the merely necessary conditions of Matějka and McKay), which pin down not just choice probabilities among chosen options but *which* options are chosen. Applying these conditions to three consumer problems, the authors characterise when an option enters the consideration set, link consideration to prior beliefs and attention costs, and show that the same parameters that generate consideration sets also generate stochastic choice "mistakes" within them. Read in full (34 pages); coverage is full including all proofs in the main text.

## Research question
Two literatures model limited attention separately: (i) *consideration-set* models (chiefly from marketing and revealed-preference theory), in which a decision maker screens down to a subset of options before choosing, and (ii) *rational inattention*, in which choice is stochastic because information is costly. Can these be unified? Specifically: does optimal information acquisition under a Shannon mutual-information cost endogenously generate consideration sets, and if so, which options are considered, how do prior beliefs and attention costs determine the set, and how can the consideration set be identified from choice data?

## Method / identification
The setting is the discrete-choice Shannon model of Sims (2003) as reformulated by Matějka–McKay (MM): finitely many states $\omega\in\Omega$ with prior $\mu$, a finite action set $A\subseteq\mathcal{A}$, utilities $u(a,\omega)$. By MM Corollary 1 the decision maker chooses a state-dependent stochastic choice rule $P(a\mid\omega)$ to maximise expected utility minus $\lambda$ times the mutual information between states and actions, where $\lambda>0$ is the marginal cost of attention. Writing $z(a,\omega)\equiv\exp(u(a,\omega)/\lambda)$, MM's necessary condition is
$$P(a\mid\omega)=\frac{P(a)\,z(a,\omega)}{\sum_{b\in A}P(b)\,z(b,\omega)}.$$
The paper's central contribution (**Proposition 1**) adds the missing piece: $P$ is optimal *if and only if*, for every $a\in A$,
$$\sum_{\omega\in\Omega}\frac{z(a,\omega)\,\mu(\omega)}{\sum_{b\in A}P(b)\,z(b,\omega)}\le 1,$$
with *equality* whenever $a$ is in the consideration set $B(P)=\{a\in A\mid P(a)>0\}$. The proof rewrites the objective in terms of unconditional probabilities $P(a)$ only, shows it is concave with linear constraints, and applies Kuhn–Tucker (the Lagrange multiplier on the adding-up constraint equals $\lambda$). A dual, posterior-based restatement (**Proposition 2**) gives the *Invariant Likelihood Ratio* (ILR) conditions: for chosen $a,b$, $\frac{\gamma^a(\omega)}{z(a,\omega)}=\frac{\gamma^b(\omega)}{z(b,\omega)}$, and for unchosen $c$, $\sum_\omega \frac{\gamma^a(\omega)}{z(a,\omega)}z(c,\omega)\le 1$. The ILR equality says posterior likelihood ratios depend only on normalised relative payoffs, not priors—an expression of the "Invariance Under Compression" property that characterises the Shannon cost among information-cost functions (Caplin et al. 2017). A geometric reading via the net-utility function $N(\gamma^a)=\sum_\omega[\gamma^a(\omega)u(a,\omega)-\lambda\gamma^a(\omega)\ln\gamma^a(\omega)]$ shows an action is considered iff its net utility touches the supporting hyperplane (convex hull) above the prior. Uniqueness of the optimum (hence of $B(P)$) holds under affine/linear independence of the normalised payoff vectors (Remark 1).

## Data
None—this is a pure decision-theory paper. Results are illustrated with numerical worked examples (Examples 1–4) rather than empirical data. The authors note the techniques may inform empirical demand-system and marketing analysis, but no estimation is performed.

## Key findings
- **Proposition 1 / Proposition 2 (ILR):** necessary *and* sufficient conditions for the Shannon optimum, identifying the consideration set, not just within-set choice. This fills a gap: many policies satisfy MM's necessary conditions yet are suboptimal (illustrated by **Corollary 1**, which enumerates all subsets admitting an MM solution in Consumer Problem 1).
- **Theorem 1 (find-the-good-alternative):** with one high-quality and many low-quality options, the optimum is a *threshold* rule on prior probabilities: only options whose prior of being good exceeds an endogenous cutoff are considered. Closed-form $P(a_i)$ and posteriors are given; strikingly, every chosen option has the *same* posterior probability of being high-quality conditional on choice, regardless of its prior. Lower $\lambda$ enlarges the consideration set and reduces mistakes.
- **Theorem 2 (independent valuations):** with independently distributed values, a cutoff again applies, but the ranking statistic is the expected *normalised* utility $Ez(a_i,\omega)=\sum_{\omega_i}\exp(\omega_i/\lambda)\mu_i(\omega_i)$—a convex transform reflecting the option value of information. **Example 2** and **Lemma 1** show the consideration set varies *non-monotonically* in $\lambda$: a safe option is used at very high costs (to stay uninformed), dropped at intermediate costs, and used again at very low costs (when it is genuinely best). **Figure 4** maps consideration sets jointly in $(\lambda,\rho)$ risk-aversion space.
- **Consumer Problem 3 (correlated valuations):** no simple cutoff exists—a *hedging motive* arises even for risk-neutral agents, so the set depends on all available options. A simple **"market entry" test** (plug the candidate into the Proposition 1 inequality holding incumbents' $P(b)$ fixed) decides whether a new option is considered; a covariance-decomposition shows hedging value comes from paying off in states where other options pay little. **Example 3** exhibits an option with the highest expected normalised utility that is nonetheless excluded because a rival hedges better.
- **Theorem 3 (priors partition):** the ILR conditions generate a system of *linear inequalities* whose convexification partitions the prior simplex $\Delta(\Omega)$ into regions $S_B$, each the set of priors for which $B$ is the consideration set. $B$ is the consideration set iff $\mu$ lies in the interior of the convex hull of the ILR-implied posteriors $\hat\gamma_b$. The naive condition $f(\mu;a,b)\ge 1$ is neither necessary nor sufficient—what matters is the posteriors that average to the prior, not the prior's location.

## Contribution
The paper unifies consideration-set theory and rational inattention, showing consideration sets *emerge from optimisation* rather than being imposed as primitives (as in [[@Masatlioglu2012|Masatlioglu–Nakajima–Ozbay 2012]] or [[@Manzini2014|Manzini–Mariotti 2014]]). It delivers a single parsimonious model of both endogenous consideration-set formation *and* stochastic mistakes within the set, the latter being absent or ad hoc (logit) in prior consideration-set models. Methodologically, Proposition 1 / the ILR conditions are a general-purpose tool for *solving* any Shannon RI problem—useful well beyond this paper, since generically not all actions are taken at the optimum. The market-entry test and the linear-inequality characterisation of priors are directly usable in applied demand and IO settings.

## Limitations & open questions
- Results are derived for a *finite* state space; the authors contrast with Jung et al. (2015), whose dimensionality results require analytic/integrable payoffs and "have no bite when the state space is finite"—extension/integration across the finite and continuous cases is left open.
- The closed-form characterisations are Shannon-specific: the ILR / Invariance-Under-Compression property *fails* for other cost functions (e.g. Tsallis entropy), so consideration-set predictions under more general (posterior-separable or neighbourhood-based) attention costs are an open problem.
- Closed-form solutions exist only for the stylised "find the good alternative" case; the independent and correlated problems are solved only via the conditions and examples, and richer correlation structures remain analytically hard.
- The paper inherits known intractability of alternative sequential-search/satisficing models ([[@Gabaix2006|Gabaix et al. 2006]]) as motivation but does not bridge to them; reconciling sequential information acquisition with the static RI consideration set is unaddressed.
- The model abstracts from *why* attention is limited (lack of awareness vs. cognitive cost); it fits the cost interpretation, leaving awareness-based consideration outside scope.
- Empirical identification and testing of the predicted priors-partition and market-entry test on real choice data is suggested but not carried out.

## Connections
The paper builds directly on Matějka and McKay (2015), supplying the sufficiency half of their characterisation (cf. also Stevens 2014), and on the rational-inattention program of Sims (2003). The geometric/net-utility apparatus and the Invariance-Under-Compression axiom come from Caplin and Dean (2013) and Caplin, Dean, and Leahy (2017). On the consideration-set side it engages the revealed-preference models of [[@Masatlioglu2012|Masatlioglu, Nakajima, and Ozbay (2012)]] and Demuynck and Seel (2017), the stochastic-consideration model of [[@Manzini2014|Manzini and Mariotti (2014)]] and [[@Brady2016|Brady–Rehbeck (2016)]], the satisficing/search tradition of Simon (1955), Caplin, Dean, and Martin (2011), and [[@Gabaix2006|Gabaix et al. (2006)]], and the marketing literature ([[@Hauser1990|Hauser and Wernerfelt 1990]]; [[@Roberts1991|Roberts and Lattin 1991]]). It connects to dimensionality results of Jung, Kim, Matějka, and Sims (2015) and to applied RI work on pricing, investment, and global games. It sits squarely within the literature on stochastic choice and is a natural companion to empirical demand-estimation approaches to consideration (Goeree 2008; Abaluck and Adams 2017).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
