---
citekey: Bardey2021
title: Nursing-homes' competition and distributional implications when the market is two-sided
authors: ["Bardey, David", "Siciliani, Luigi"]
year: 2021
type: journalArticle
doi: 10.1111/jems.12415
zotero: "zotero://select/library/items/PV2M9DKS"
pdf: /Users/jesper/Zotero/storage/7P48P8PH/Bardey and Siciliani - 2021 - Nursing-homes' competition and distributional implications when the market is two-sided.pdf
tags: [literature]
keywords: [two-sided-markets, nursing-homes, health-economics, common-network-externality, hotelling-competition, worker-altruism, price-regulation, pay-for-performance]
topics: []
related: [Besley2005]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> We investigate the effect of competition in the nursing-homes sector with a two-sided market approach. Using a Hotelling model, our key findings are that (i) the two-sidedness of the market leads to higher wages for nurses, (ii) this is then passed to residents in the form of higher prices, and (iii) nursing-homes profits are instead unaffected. In contrast, when nurses wages are regulated, the two-sidedness of the market implies a transfer between residents and nursing homes. When residents' price is regulated, it implies a transfer between nurses and nursing homes. These key results are generally robust to institutional settings which employ pay-for-performance schemes, the presence of altruistic motives of nursing homes and the heterogeneity in residents reservation utility.

## Summary
Bardey and Siciliani model competition among nursing homes as a two-sided market in which providers compete simultaneously for residents (consumers) and for altruistic nurses (the workers who endogenously choose quality). Because quality depends on the residents-to-nurses ratio, both sides care about how many agents are affiliated on each side, generating a "common network externality" (CNE). The central result is distributional: the two-sidedness of the market intensifies competition for nurses, raising their wages; these higher wages are passed through to residents as higher prices, while nursing-home profits are left unchanged. The paper traces how this transfer logic changes under wage regulation, price regulation, pay-for-performance (P4P) schemes, an uncovered market, and altruistic providers.

## Research question
What are the distributional consequences of competition among nursing homes across the three key actors (residents, nurses, nursing homes) when the market is two-sided — i.e., when a higher number of nurses raises residents' demand (via better matching and higher quality) and a higher number of residents worsens nurses' working conditions — and how do these consequences differ across institutional regimes (free market, regulated wages, regulated prices, P4P, partial public ownership)?

## Method / identification
A two-stage Hotelling duopoly with two nursing homes $i=\{1,2\}$ at the endpoints of the unit line. Residents (mass 1) and nurses (mass 1) are each uniformly distributed. A resident at distance $y$ from home $i$ has utility $U_i(y)=\theta q_i - p_i - t_r y + \beta\left(v-\frac{1}{4N_i}\right)$, where $q_i$ is quality, $p_i$ price, $\theta$ the marginal benefit of quality, $t_r$ travel disutility, and the $\beta$ term captures the matching benefit of having more nurses $N_i$. A nurse at distance $y$ has utility $V_i(y)=w_i+\alpha q_i-\frac{1}{2}\frac{c}{(k-\gamma)+\gamma N_i/D_i}q_i^2-t_N y$, with altruism $\alpha$, wage $w_i$, and a congestion parameter $\gamma$ making quality more costly when the residents-nurses ratio $D_i/N_i$ is high.

Timing: (1) homes set price $p_i$ and wage $w_i$; (2) residents and nurses choose affiliation; (3) nurses choose quality. By backward induction, optimal quality is $q_i^*=\frac{\alpha}{c}\left(k-\gamma+\gamma\frac{N_i}{D_i}\right)$. Substituting yields interdependent demand $D_i$ and supply $N_i$ functions; the two-sidedness shows up because $dD_1/dw_1>0$ and $dN_1/dp_1>0$. Homes maximize $\pi_i=(p_i-g)D_i-w_iN_i$. The paper signs strategic complementarity of prices and wages and characterizes the symmetric equilibrium, then re-solves under each institutional variant. Two key knobs: $\gamma$ (strength of the CNE / two-sidedness) and $\alpha$ (altruism) — both must be positive for the two-sidedness effect to appear.

## Data
None — this is a purely theoretical model. The paper cites empirical work (Lin 2014; Konetzka et al. 2008; Werner et al. 2012; Grabowski & Gruber 2007; Mommaerts 2018) to motivate assumptions, such as the elasticity of demand and the link between staffing and quality, but estimates nothing itself.

## Key findings
**Proposition 1 (free market):** $p^*=g+t_r+\frac{\gamma\alpha(\alpha+2\theta)}{c}$ and $w^*=\beta+\frac{\gamma\alpha(\alpha+2\theta)}{c}-t_N$, with profit $\pi^*=\frac{1}{2}(t_r+t_N-\beta)$. The extra CNE term $\frac{\gamma\alpha(\alpha+2\theta)}{c}$ raises both price and wage by the same amount, so the entire effect is a transfer from residents to nurses; profits and welfare are unchanged (because the ratio is a degree-zero homogeneous function, per Bardey et al. 2014). Equilibrium quality $q^*=\alpha k/c$ is independent of $\gamma$. Counterintuitively, higher altruism $\alpha$ raises nurses' wages by amplifying competition for nurses.

**Propositions 2-3 (regulated wage $\bar w$):** $\bar p=g+t_r+\frac{\gamma\alpha}{ct_N-\gamma\alpha^2}(\alpha(\beta-\bar w)+2\theta t_N)$. A higher regulated wage *lowers* residents' price (counterintuitive). The two-sidedness now transfers between residents and nursing homes rather than residents and nurses.

**Price regulation:** the two-sidedness affects nurses' wages and a transfer arises between nurses and nursing homes; a higher regulated price raises wages.

**P4P (Section 4):** P4P at the *nursing-home* level leaves quality unchanged but amplifies wage competition, raising prices ($\Delta U<0,\ \Delta V>0,\ \Delta\pi>0,\ \Delta W=0$). P4P paid *to nurses* (fee equal to residents' valuation of quality) does raise quality, makes nurses better off, but still leaves residents worse off and profits unchanged ($\Delta\pi=0,\ \Delta W>0$).

**Uncovered market (Section 5):** with reservation-utility heterogeneity (covered fraction $\lambda$), the core results survive when the uncovered segment is small, but now two-sidedness also reduces demand and raises quality, with ambiguous welfare effects.

**Altruistic providers (Section 6):** with objective $\tilde\pi_i=\pi_i+\delta\tilde U_i$ and price weight $\sigma\in[0,1]$, the CNE transfer is amplified when homes care mainly about quality ($\sigma<1/2$) and dampened when they weight price ($\sigma>1/2$); residents are not necessarily better off.

## Contribution
The paper is the first to model the nursing-home (and analogous health/primary-care platform) sector as a two-sided market with a *common network externality* in which quality is endogenously chosen by altruistic workers rather than by the firm. It micro-founds the CNE framework of Bardey et al. (2012, 2014) by deriving the quality function from the resident-nurse ratio, and it systematically maps how the two-sidedness reshuffles rents across residents, nurses, and providers under a rich menu of regulatory regimes (free market, wage regulation, price regulation, two flavors of P4P, partial public ownership). It draws sharp policy lessons: raising regulated nurse wages can *lower* resident prices, and P4P evaluations should look at prices and profits, not just quality.

## Limitations & open questions
The authors flag several explicit open problems. (1) They assume profit-maximizing homes (relaxed only partially via altruism); future work could study **mixed markets where public providers compete with private providers**. (2) The model is tailored to nursing homes; extending it to **primary care** (gatekeeping, hospital interface, alternative payment arrangements, online platforms like Doctolib that may begin charging patients) is left open. (3) The **education sector** application (schools/universities competing for students and teachers via the pupil-teacher ratio) is sketched but not formalized. (4) Quality is fixed in the symmetric equilibrium in the baseline; richer settings where quality responds endogenously are only partially explored. (5) Asymmetric equilibria are not formally ruled out (the 4×4 stability analysis is deemed too involved). (6) The number of nurses is held fixed in the regulation sections, abstracting from labor-supply responses documented empirically (Hackmann 2019).

## Connections
The model builds directly on the common-network-externality framework of Bardey, Cremer & Marchand (2012, 2014) and the two-sided market foundations of Rochet & Tirole (2003, 2006) and Armstrong (2006). It extends Bardey & Rochet (2010) on PPO/HMO competition for policyholders and providers (and Boilley 2012), and relates to Pezzino & Pignataro (2007) and Gal-Or (1997) on hospital competition where consumers value provider access. The horizontal-differentiation health-competition lineage includes Ma & Burgess (1993), Gravelle (1999), and Brekke, Siciliani & Straume (2012). Gal-Or, Gal-Or & Penmetsa (2019) provide a contrasting two-sided crowdfunding model where quality is a firm investment rather than a worker-chosen CNE. The altruistic/motivated-agent assumption draws on Ellis & McGuire (1986), Chalkley & Malcomson (1998), Heyes (2005), [[@Besley2005|Besley & Ghatak (2005)]], and Francois (2000). Empirical motivation comes from Lin (2014), Konetzka et al. (2008), Werner et al. (2012, 2013), Grabowski & Gruber (2007), and the education evidence of Angrist & Lavy (1999).

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
