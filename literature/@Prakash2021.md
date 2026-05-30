---
citekey: Prakash2021
title: "Programming with TensorFlow: Solution for Edge Computing Applications"
authors: ["Prakash, Kolla Bhanu", "Kanagachidambaresan, G. R."]
year: 2021
type: book
doi: 10.1007/978-3-030-57077-4
zotero: "zotero://select/library/items/555K8EYA"
pdf: /Users/jesper/Zotero/storage/3LZEI7S5/Prakash and Kanagachidambaresan - 2021 - Programming with TensorFlow Solution for Edge Com.pdf
tags: [literature]
keywords: [tensorflow, deep-learning, edge-computing, neural-networks, machine-learning, single-board-computers]
topics: []
related: [Goodfellow2016]
added: 2026-05-30
generated: 2026-05-30
---

> [!abstract] Abstract
> (no abstract in Zotero)

## Summary
This is a short, practitioner-oriented edited book (Springer/EAI Innovations in Communication and Computing, ~187 pages) that teaches TensorFlow as a hands-on tool for building and deploying machine-learning and deep-learning models, with an emphasis on getting trained models onto resource-constrained single-board computers for edge-computing applications. Rather than presenting new research results, the volume walks through the TensorFlow programming stack chapter by chapter, from the dataflow-graph computational model and installation, through regression and the major neural-network architectures (feedforward, CNN, RNN), to applied case studies (a chatbot, pattern recognition, sentiment/text analysis) and a closing chapter on programming TensorFlow for single-board computers. (Coverage note: 190-page edited handbook read in targeted fashion — front matter/TOC, the introductory TensorFlow chapter, and representative technical/application sections — rather than ingested in full.)

## Research question
The book is a pedagogical handbook, not a hypothesis-driven study, so it has no single research question. Its organizing problem is practical: how can a developer use the TensorFlow package to assemble, train, and evaluate standard ML/DL models, and then move those models onto edge hardware (single-board computers such as Raspberry Pi) so that inference runs locally rather than in the cloud? Each chapter answers a narrower "how do I do X in TensorFlow" question (how to do regression, build a CNN, build an RNN, deploy on an edge device, etc.).

## Method / identification
There is no formal model, estimator, or experimental identification strategy — this is a programming tutorial. The methodological backbone is the exposition of TensorFlow's computational abstraction: a *dataflow graph* whose nodes are mathematical operations and whose edges carry multidimensional arrays (tensors). The introductory chapter motivates this with worked graph examples such as computing $x\cdot y + 2$ and $b + W\cdot x$ as op-graphs, then shows how parameters, training, and testing of deep-learning models are assembled on top of these primitives. Subsequent chapters proceed by code-driven walkthroughs: setting up TensorFlow across operating systems (Ubuntu, macOS, Windows, Raspbian) via `pip`; tensor data types and loading; visualization; linear/logistic regression; the architecture and training loop of feedforward neural networks, convolutional neural networks, and recurrent neural networks; and a comparison/bridge chapter on PyTorch. Method here means recipes and API usage patterns rather than statistical or theoretical derivation.

## Data
None as primary research data. The book uses illustrative/benchmark datasets supplied by standard providers (mentioned in the front matter as "data set providers") to demonstrate model training in its worked examples — e.g., toy regression data, image data for the CNN chapter, and text/tweet data for the sentiment-analysis application. These are pedagogical examples, not an empirical corpus analyzed to support claims.

## Key findings
There are no theorems or empirical results in the scientific sense. The book's substantive "deliverables" are demonstrated capabilities: (1) TensorFlow's dataflow-graph model makes it straightforward to express and differentiate ML computations; (2) the same API stack scales from simple regression to deep CNN and RNN architectures; (3) trained TensorFlow models can be deployed onto single-board computers, enabling on-device edge inference; and (4) applied pipelines — a chatbot, pattern-recognition tasks, and text/sentiment analysis (using helpers such as TextBlob over cleaned tweet text) — can be assembled end-to-end with the covered tooling. The PyTorch chapter functions as a comparative finding, situating TensorFlow against the main alternative framework.

## Contribution
The contribution is pedagogical and integrative rather than original research: it packages, in one short volume, the full path from TensorFlow fundamentals to edge deployment, aimed at researchers, advanced students, and practitioners. Its distinctive angle within the crowded TensorFlow-tutorial space is the explicit edge-computing framing — closing the loop by targeting single-board computers — which most introductory TensorFlow texts treat only in passing.

## Limitations & open questions
The book does not state formal open problems. Implicit limitations, useful as caveats rather than project hooks: (i) it is tied to a 2021 snapshot of TensorFlow APIs and single-board hardware, so code and installation guidance date quickly; (ii) breadth comes at the cost of depth — each architecture (CNN, RNN, etc.) gets only a brief treatment; (iii) it does not engage rigorously with edge-specific concerns such as model quantization, latency/energy trade-offs, or accuracy degradation after deployment, which are the genuinely open research questions the edge framing raises; and (iv) being a multi-author edited volume, coverage and notation are uneven across chapters.

## Connections
The book sits in the TensorFlow / deep-learning practitioner-literature tradition rather than the formal economics or choice-modeling literature, so it connects only loosely to the vault's core. Its closest neighbor here is its own PyTorch chapter, which mirrors framework comparisons common in applied ML texts. Conceptually it builds on the original TensorFlow system design described by Abadi et al. (2016) and the broader deep-learning synthesis of [[@Goodfellow2016|Goodfellow, Bengio & Courville (2016)]] and LeCun, Bengio & Hinton (2015); the edge-deployment theme connects to the edge/fog-computing computing literature surveyed by Shi et al. (2016). For a research economist, the relevance is instrumental — TensorFlow as estimation/optimization tooling for structural and machine-learning models — rather than substantive.

%% ─── below is yours; regeneration never touches it ─── %%
## My notes
