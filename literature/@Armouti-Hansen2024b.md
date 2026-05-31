---
citekey: Armouti-Hansen2024b
title: Managing anticipation and reference-dependent choice
authors: ["Armouti-Hansen, Jesper", "Kops, Christopher"]
year: 2024
type: journalArticle
doi: ""
zotero: "zotero://select/library/items/YUL6KULG"
pdf: /Users/jesper/Zotero/storage/PYSTZ69Y/Armouti-Hansen and Kops - 2024 - Managing anticipation and reference-dependent choi.pdf
tags: [literature]
keywords: [reference-dependent-preferences, anticipatory-utility, loss-aversion, consideration-sets, revealed-preference, decision-theory]
topics: ["[[expectations-based-reference-dependence]]"]
related: [Abeler2011, Akerlof1982, Baillon2020, Baucells2017, Bell1985, Berns2006, Brunnermeier2005, Brunnermeier2007, Caplin2001, Chen2013, Cherepanov2013, Freeman2017, Goeree2001, Gollier2010, Gul1991, Harless1994, Jouini2014, Kahneman1979, Koszegi2006b, Koszegi2007, Lleras2017, Loewenstein1987, Loomes1986, Manzini2007, Masatlioglu2012, Oster2013a, Sarver2018, Schmitz2012, Shalev2000, Sugden1993]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> Extensive field and experimental evidence shows that reference points shape behavior. But, what shapes the reference point? Candidates put forward in the literature range from the status quo, to rational expectations and the narrow focus of dreaming or worrying about a single possible outcome. This paper develops a model that includes all of these candidate sources. It does so, by allowing the reference point to be any convex combination of the outcomes possible under a consumption lottery. We introduce new solution concepts for reference-dependent choices, characterize these solution concepts on the level of choice data and identify the model's parameters.

## Summary
The paper proposes a two-period model of anticipation-based, reference-dependent preferences that modifies Köszegi and [[@Koszegi2006b|Rabin (2006)]]. A decision maker (DM) first chooses an anticipatory lottery $r$ (what to dream or worry about) and then a physical lottery $p$; the chosen $r$ both delivers anticipatory utility and sets the reference point for period-2 gain-loss utility. By letting the reference point be any convex combination of outcomes in the support of the chosen lottery, the model nests status-quo, rational-expectations, and "narrow-focus" (single-outcome dreaming/worrying) reference points as special cases. The authors introduce three equilibrium concepts (MAE, PMAE, CMAE), show they are observationally equivalent to Köszegi-Rabin's PE/PPE/CPE on choice data, and recast PMAE choice as a two-stage consideration-filtering-then-maximization procedure, which they fully characterize and identify from choice data alone.

## Research question
What shapes the reference point? Can a single reference-dependent model accommodate the mixed experimental evidence (expectations-based vs. security-level vs. optimistic/pessimistic reference points) while still being falsifiable from observable choice data, given that expectations and reference points are unobservable in the field?

## Method / identification
A two-period decision problem. In period 1 the DM picks an anticipatory lottery $r\in\Delta$ over outcomes; in period 2 a physical lottery $p\in X$ realizes. Utility is additively separable across the two periods:
$$U(r,p)=\zeta U_1(r)+\delta U_2(r,p)=\zeta\sum_{y\in\mathrm{supp}(r)} r(y)u_1(y)+\delta\sum_{z\in\mathrm{supp}(p)} p(z)\sum_{y\in\mathrm{supp}(r)} r(y)u_2(y,z)$$
The main Köszegi-Rabin-style specialization embeds a gain-loss term $\mu$, with the linear form
$$U(r,p)=\zeta\sum_{y\in\mathrm{supp}(r)} r(y)\cdot y+\delta\sum_{z\in\mathrm{supp}(p)} p(z)\sum_{y\in\mathrm{supp}(r)} r(y)\cdot(z+\mu(z-y)),$$
where $\mu(x)=\eta x$ if $x>0$ and $\mu(x)=\eta\lambda x$ otherwise, $\eta$ weights gain-loss utility and $\lambda>1$ is loss aversion. The rationality restriction is $\mathrm{supp}(r)\subseteq\mathrm{supp}(p)$: the DM can only anticipate outcomes possible under her chosen lottery.

Three solution concepts depending on commitment timing: the **managing anticipations equilibrium (MAE)** (commitment shortly before resolution, reference point fixed); its refinement **preferred MAE (PMAE)** (the DM's most preferred MAE); and the **choice-acclimating MAE (CMAE)** (commitment far in advance, reference point adapts). These parallel Köszegi-Rabin's PE, PPE, and CPE. Existence is guaranteed via a reformulated **limited cycle inequalities** condition (Freeman, 2017) on $U$.

On the domain of observables (only the chosen physical lottery is seen), the authors derive an induced binary relation $\succsim^{*}$ on $X$ and a consideration filter $\Gamma_{\mathrm{MAE}}$, expressing PMAE choice as the two-stage procedure $C(S)=C(\Gamma_{\mathrm{MAE}}(S);\succsim^{*})$. Characterization uses axioms Contraction (property $\alpha$), Expansion (property $\gamma^{*}$), and Weak Congruence; an alternative characterization in the appendix uses Expansion, Weak WARP, and No Reversible Binary Cycles, relating the model to the Rational Shortlist Method of [[@Manzini2007|Manzini and Mariotti (2007)]]. Identification proceeds by constructing revealed-preference relations ($R^{*}$, $P^{*}$ as transitive closures) and a revealed consideration set $\tilde\Gamma$, each shown to capture exactly the revealed object.

## Data
None. This is a pure decision-theory paper; "data" enters only as abstract observable choice correspondences $C:\mathcal{P}(X)\to\mathcal{P}(X)$. Empirical regularities (Allais paradox, Goeree-Holt matching pennies, Huntington's-disease testing avoidance, defensive pessimism) are used illustratively, not estimated.

## Key findings
- **Corollary 3.1** gives exact conditions for MAE = PMAE and PMAE = CMAE in terms of $U$.
- **Proposition 4.1**: on choice data, (C,P)MAE and (C,P)PE are equivalent (same filters $\Gamma_{\mathrm{MAE}}=\Gamma_{\mathrm{PE}}$, same induced preference $\succsim^{*}=\succsim^{**}$), so the two reference-point theories are indistinguishable from choice alone; they differ only in how the reference point forms.
- **Corollary 4.1**: $\Gamma$ equals the MAE-filter iff it satisfies Contraction and Expansion; $C$ equals the two-stage procedure iff it satisfies Expansion and Weak Congruence.
- **Propositions 4.2-4.3 / Corollaries 4.2**: $R^{*}$ identifies revealed weak preference, $P^{*}$ revealed strict preference, and $\tilde\Gamma$ the revealed consideration set.
- **Theorem 4.1**: whenever a PMAE (CMAE) exists, there exists one with a *degenerate* lottery as the reference point - so a single anticipated outcome can always serve as reference point under PMAE/CMAE, unlike PPE/CPE where the chosen lottery itself is the reference point.
- **Corollaries 4.3-4.4**: "more can be less" (welfare) and "more need not imply more" (consideration) - testable failures of rational-choice monotonicity.
- The model rationalizes the Allais paradox (anticipating the best outcome plus loss aversion), Goeree-Holt asymmetric matching-pennies play, information aversion in genetic testing (anticipating being disease-free), and defensive pessimism (strategically anticipating the worst to dampen disappointment).
- **Discussion / Corollary 5.1**: with unrestricted reference-point formation any choice behavior is rationalizable (the theory loses falsifiability); a **naive anticipation equilibrium (NAE)** for non-sophisticated DMs is defined and shown to violate Expansion, distinguishing naive from sophisticated DMs.

## Contribution
Unifies competing accounts of reference-point sources within one tractable model by making the reference point an endogenous convex combination of supported outcomes, reconciling the mixed experimental evidence. Crucially, it delivers a falsifiable, choice-data-only characterization and identification of an expectations-/anticipation-based reference-dependent theory - addressing the standing objection that such theories are untestable because expectations are unobservable. It also bridges reference-dependent preferences and the bounded-rationality literature on consideration sets and two-stage choice procedures (RSM, categorize-then-choose, rationalization, overwhelming choice).

## Limitations & open questions
The authors explicitly flag extensions: (i) move beyond simple objective lotteries to richer/more complex objects; (ii) add periods to separate anticipation before commitment from anticipation after commitment but before resolution; (iii) allow a *second party* to influence the DM's anticipation (marketing exposing consumers to states to raise willingness-to-pay; a transformational leader whose positive visions raise employee effort). A further open tension: under fully unrestricted reference-point formation the model rationalizes everything (Corollary 5.1), so falsifiability hinges on the imposed rationality restriction; and the existence of naive (NAE) DMs raises sophistication-assumption questions.

## Connections
The model directly modifies Köszegi and [[@Koszegi2006b|Rabin (2006)]] and Kőszegi and [[@Koszegi2007|Rabin (2007)]], and the period-1/period-2 anticipation structure builds on Kőszegi (2010). Antecedents in reference dependence and loss aversion include [[@Kahneman1979|Kahneman and Tversky (1979)]], [[@Shalev2000|Shalev (2000)]], Heidhues and Kőszegi (2008), and Masatlioglu and Ok (2005); disappointment- and regret-aversion roots are [[@Bell1985|Bell (1985)]], [[@Loomes1986|Loomes and Sugden (1986)]], [[@Gul1991|Gul (1991)]], and [[@Sugden1993|Sugden (1993)]]. The anticipatory-utility component connects to [[@Akerlof1982|Akerlof and Dickens (1982)]], [[@Loewenstein1987|Loewenstein (1987)]], [[@Caplin2001|Caplin and Leahy (2001)]], and [[@Baucells2017|Baucells and Bellezza (2017)]], and especially to optimal-belief / choice-of-anticipation models by [[@Brunnermeier2005|Brunnermeier and Parker (2005)]], [[@Brunnermeier2007|Brunnermeier et al. (2007)]], [[@Gollier2010|Gollier and Muermann (2010)]], [[@Jouini2014|Jouini et al. (2014)]], [[@Chen2013|Chen (2013)]], and [[@Sarver2018|Sarver (2018)]] - distinguished here by letting each anticipated *state* (not the anticipated payoff) enter gain-loss utility. The equilibrium-existence and choice-procedure machinery draws on [[@Freeman2017|Freeman]] (2017, 2016, 2019); the two-stage filtering links to the Rational Shortlist Method of [[@Manzini2007|Manzini and Mariotti (2007)]], its correspondence extension in Armouti-Hansen and Kops (2018), categorize-then-choose (Manzini and Mariotti, 2012), rationalization ([[@Cherepanov2013|Cherepanov et al., 2013]]), overwhelming choice ([[@Lleras2017|Lleras et al., 2017]]), limited attention ([[@Masatlioglu2012|Masatlioglu et al., 2012]]), and the unifying result of Kops (2022, 2018). Empirical motivation comes from [[@Abeler2011|Abeler et al. (2011)]], [[@Baillon2020|Baillon et al. (2020)]], [[@Oster2013a|Oster et al.]] (2013a, 2013b), [[@Harless1994|Harless and Camerer (1994)]], [[@Goeree2001|Goeree and Holt (2001)]], Norem and Cantor (1986), and neurobiological evidence in [[@Berns2006|Berns et al.]] (2006, 2007) and [[@Schmitz2012|Schmitz and Grillon (2012)]].

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
