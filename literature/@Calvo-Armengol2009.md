---
citekey: Calvo-Armengol2009
title: Peer Effects and Social Networks in Education
authors: ["Calvó-Armengol, Antoni", "Patacchini, Eleonora", "Zenou, Yves"]
year: 2009
type: journalArticle
doi: 10.1111/j.1467-937X.2009.00550.x
zotero: "zotero://select/library/items/YG8HD7JQ"
pdf: /Users/jesper/Zotero/storage/DTW22VBK/Calvo-Armengol2009.pdf
tags: [literature]
keywords: [peer-effects, social-networks, katz-bonacich-centrality, network-games, identification, education-economics, spatial-econometrics]
topics: []
related: []
added: 2026-05-29
generated: 2026-05-29
---

> [!abstract] Abstract
> We develop a model that shows that, at the Nash equilibrium, the outcome of each individual embedded in a network is proportional to his/her Katz-Bonacich centrality measure. This measure takes into account both direct and indirect friends of each individual, but puts less weight to his/her distant friends. We then bring the model to the data using a very detailed dataset of adolescent friendship networks. We show that, after controlling for observable individual characteristics and unobservable network specific factors, a standard deviation increase in the Katz-Bonacich centrality increases the pupil school performance by more than 7% of one standard deviation.

## Summary
The paper supplies a micro-founded bridge between non-cooperative game theory and sociological network centrality. In a peer-effects game with linear-quadratic utilities and local strategic complementarities, the unique interior Nash equilibrium effort of each agent is exactly proportional to that agent's Katz-Bonacich centrality. This turns an otherwise abstract network statistic into the equilibrium outcome of a structural behavioural model, and it converts the empirical estimation into a behaviourally-grounded spatial error model. Taking the model to the Add Health adolescent friendship data (11,964 pupils over 199 networks), the authors estimate the peer-effect intensity and show that a one-standard-deviation rise in Katz-Bonacich centrality raises school performance by roughly 7% of a standard deviation, dominating the explanatory power of degree, closeness and betweenness centralities.

## Research question
Can the heterogeneous strength of peer effects across individuals be derived from, and measured by, each agent's precise position in a friendship network, rather than treated as a single average intra-group externality applied uniformly to an arbitrarily-bounded group? And can such a structural network model be identified and estimated despite Manski's reflection problem and endogenous network formation?

## Method / identification
The model places $n$ agents on an undirected network $g$ with adjacency matrix $G=[g_{ij}]$, $g_{ij}\in\{0,1\}$, $g_{ii}=0$. Each agent $i$ chooses an idiosyncratic effort $y_i^0\ge 0$ and a peer effort $z_i\ge 0$ under the linear-quadratic payoff
$$u_i(y^0,z;g)=\theta_i y_i^0-\tfrac{1}{2}(y_i^0)^2+\mu g_i z_i-\tfrac{1}{2}z_i^2+\phi\sum_{j=1}^{n}g_{ij}z_i z_j,$$
with $\phi>0$, $\mu>0$, and $g_i=\sum_j g_{ij}$ the degree. The cross-derivative $\partial^2 u_i/\partial z_i\partial z_j=\phi g_{ij}\ge 0$ encodes local strategic complementarity between direct friends. The intercept $\theta_i(x)=\sum_m \beta_m x_{im}+\tfrac{1}{g_i}\sum_m\sum_j \gamma_m g_{ij}x_{jm}$ folds in individual characteristics ($\beta$) and contextual effects ($\gamma$, average traits of friends).

The Katz-Bonacich centrality vector is $b(g,\phi)=\sum_{k=0}^{\infty}\phi^{k}G^{k}\cdot(\phi G\mathbf{1})=(I-\phi G)^{-1}\phi G\mathbf{1}$, counting all direct and indirect paths from each node with geometric decay $\phi^{k}$ in path length. The central result, **Proposition 1**, states that if $\phi\omega(g)<1$ (where $\omega(g)$ is the largest eigenvalue / spectral radius of $G$), the equilibrium is unique, interior, and given by $y_i^*(x,g)=\theta_i(x)+\tfrac{\mu}{\phi}b_i(g,\phi)$. The condition bounds network complementarity relative to own-concavity so the complementarity feedback loop does not escalate without bound.

**Theorem 1** (Appendix A) generalises this to arbitrary linear-quadratic games via the additive decomposition of the interaction matrix $\Sigma=-\beta I-\gamma J+\lambda G$, separating own-concavity ($-\beta I$), global substitutability ($-\gamma J$, $J$ the all-ones matrix) and local complementarity ($+\lambda G$). The equilibrium is then a weighted Bonacich centrality $w_u(g,a)=(I-aG)^{-1}u$; existence/uniqueness holds under $\beta>\lambda\omega(G)$ (homogeneous $\alpha$) or a tighter bound involving $n\gamma(\bar\alpha/\underline\alpha-1)$ (heterogeneous $\alpha$). This generalisation to ex-ante heterogeneity is what makes the model estimable.

Estimation uses the empirical counterpart in which the peer-effect efforts load entirely onto the regression residual, yielding a spatial error model (Anselin 1988): $\varepsilon=\mu(I-\phi G)^{-1}G\mathbf{1}+(I-\phi G)^{-1}\nu$, estimated jointly for $(\beta,\gamma,\phi,\mu)$ by maximum likelihood with network fixed effects $\eta_\kappa$ (within-group demeaning) plus school fixed effects. Networks failing $\phi\omega(g)<1$ are discarded (18 of 199), leaving 11,491 pupils over 181 networks.

Identification (**Proposition 2**): given $\phi\omega(g)<1$ and $\mu\ne 0$, peer effects are identified iff $g_i^{[2]}/g_i\ne g_j^{[2]}/g_j$ for at least two agents — i.e. two agents must differ in the average connectivity of their direct friends ($G\mathbf{1}$ and $G^2\mathbf{1}$ linearly independent). The reflection problem is escaped because reference groups are individual-specific and overlapping rather than common, and the friend-of-friend structure (intransitive triads) provides the instrument; regular networks fail identification.

## Data
Add Health in-school friendship nominations (up to five male and five female best friends) merged with in-home educational records, grades 7-12, ~130 US schools, 1994-1995. The school-performance index is a factor-analytic score over math, history/social-studies and science grades (Cronbach $\alpha=0.86$). Final sample: 11,964 pupils over 199 networks (11,491 / 181 after the eigenvalue filter); network sizes range 16-107, mean 60.4. Roughly 14% of nominations are non-reciprocal, used in the directed-network robustness check.

## Key findings
- **Proposition 1 (Nash-Katz-Bonacich linkage):** equilibrium effort is proportional to Katz-Bonacich centrality, $y_i^*=\theta_i+(\mu/\phi)b_i(g,\phi)$, the paper's signature theoretical contribution.
- **Theorem 1:** existence, uniqueness and interiority of equilibrium for the general linear-quadratic game, expressed via weighted Bonacich centrality; covers global substitutabilities and ex-ante heterogeneity.
- **Proposition 2:** sharp necessary-and-sufficient identification condition (heterogeneity in friends' average connectivity).
- **Empirical:** estimated $\mu$ and $\phi$ both positive and highly significant; all 181 network-specific $\hat\phi_\kappa>0$, confirming strategic complementarity. A one-SD rise in Katz-Bonacich centrality yields ~7% of an SD in school performance (cf. ~17% for parental education). Robust to relaxing $\phi\omega(g)<1$ (running all 199 networks), and to directed networks (~5.6%, significant at 1%).
- **Alternative centralities:** degree centrality only weakly significant (10% level, ~2.1% effect); closeness and betweenness insignificant — the structural Katz-Bonacich measure, which depends on both topology and the estimated peer-effect strength $\phi$, outperforms parameter-free geometric indices.
- **Network structure:** the bilateral-influence strength $\hat\phi_\kappa$ rises with network density (up to ~60% of possible links), is non-monotone in asymmetry, and increases with redundancy/clustering above a threshold.

## Contribution
The paper gives the canonical behavioural foundation for using Katz-Bonacich centrality in applied peer-effects work, generalising Ballester, Calvó-Armengol and Zenou (2006) to ex-ante observable heterogeneity so the model can confront micro data. It reframes peer effects as an equilibrium aggregation of overlapping dyadic influences rather than a uniform group externality, and it derives — rather than assumes — a spatial-error econometric specification with an explicit, checkable identification condition that sidesteps the reflection problem through network geometry.

## Limitations & open questions
The authors are explicit about several hooks:
- The analysis is restricted to **linear-quadratic utility**; whether the Katz-Bonacich-Nash linkage survives beyond this functional form is left open and flagged as challenging.
- Peer effects are modelled as a **local aggregate** (sum of friends' efforts). Replacing this with a **local average** would let one study conformism in education — an explicitly proposed extension.
- The **arbitrary separation of idiosyncratic and peer efforts** into two distinct efforts $y_i^0$ and $z_i$ is a strong assumption; the online appendix / companion (Calvó-Armengol, Patacchini and Zenou 2008) develops one-effort alternatives, but these cannot disentangle the impact of network location from idiosyncratic characteristics.
- Peer-oriented effort might be **counter-productive** ("doing homework with friends" reducing output); allowing $y_i^*=y_i^0-z_i$ flips the sign of $\mu$, and indeed ~6% of networks show negative $\hat\mu$.
- Extending the network-location lens to **other outcomes** — labour markets, crime, smoking — is offered as a direction.

## Connections
Directly extends Ballester, Calvó-Armengol and Zenou (2006) "Who's Who in Networks. Wanted: The Key Player" (the source of the Bonacich-equilibrium machinery and optimal network policy). The identification argument builds on and parallels Bramoullé, Djebbari and Fortin (2009) on identification of peer effects through social networks, and confronts Manski (1993)'s reflection problem head-on. Centrality concepts trace to Katz (1953) and Bonacich (1987); the econometrics is the spatial error model of Anselin (1988). It sits within the economics-of-networks programme surveyed by Goyal (2007) and Jackson (2008), and complements the natural-experiment / IV peer-effects literature (Sacerdote 2001; Angrist and Lavy 1999; De Giorgi, Pellizzari and Redaelli 2007) by taking a structural rather than reduced-form route. The supermodular-games literature (Topkis 1979; Vives 2005) is invoked for the multiple-equilibria regime when $\phi\omega(g)<1$ fails.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
