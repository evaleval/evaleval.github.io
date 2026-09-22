---
layout: post
title: "How UK AISI and EvalEval Are Making Benchmark Results Reproducible"
date: 2026-09-22
published: true
category: Infrastructure
image: "/assets/img/blogs/evaleval-aisi-banner.webp"
authors:
  - name: "Avijit Ghosh"
  - name: "Jenny Chim"
  - name: "Deep Joshi"
  - name: "Srishti Yadav"
  - name: "Wm. Matthew Kennedy"
  - name: "Irene Solaiman"
  - name: "Jessica McFadyen"
  - name: "Lynn Tan"
  - name: "Cozmin Ududec"
author_groups:
  - affiliation: "EvalEval Coalition"
    authors:
      - name: "Avijit Ghosh"
      - name: "Jenny Chim"
      - name: "Deep Joshi"
      - name: "Srishti Yadav"
      - name: "Wm. Matthew Kennedy"
      - name: "Irene Solaiman"
  - affiliation: "UK AI Security Institute"
    authors:
      - name: "Jessica McFadyen"
      - name: "Lynn Tan"
      - name: "Cozmin Ududec"
tags:
  - "infrastructure"
  - "evaluation reporting"
  - "reproducibility"
  - "eval metadata"
description: "UK AISI is sharing verified evaluation results through EvalEval's open reporting infrastructure, making benchmark findings easier to reproduce, interpret, and compare."
---

<div class="aisi-collab-post" markdown="1">

<style>
.aisi-collab-post .evaluation-figure {
  margin: 2.5rem 0;
}

.aisi-collab-post .evaluation-figure iframe {
  display: block;
  width: 100%;
  border: 1px solid var(--border);
  border-radius: 4px;
  background: var(--bg-subtle);
}

/* These embeds are cross-origin, so they cannot report their height, and their
   shell stretches to fill whatever height it is given. Each height below is the
   embed's measured content height at the narrowest column width its tier
   produces, so the figures are sized to their content rather than padded out.
   The step at 1279px is the sidebar: it sits beside the text from 1024px up,
   which squeezes the column to its narrowest at exactly that breakpoint. */
.aisi-collab-post .evaluation-figure--trajectories iframe { height: 615px; }
.aisi-collab-post .evaluation-figure--distribution iframe { height: 470px; }

@media (max-width: 1343px) {
  .aisi-collab-post .evaluation-figure--trajectories iframe { height: 655px; }
}

@media (max-width: 1279px) {
  .aisi-collab-post .evaluation-figure--trajectories iframe { height: 685px; }
  .aisi-collab-post .evaluation-figure--distribution iframe { height: 500px; }
}

@media (max-width: 1023px) {
  .aisi-collab-post .evaluation-figure--trajectories iframe { height: 670px; }
}

@media (max-width: 767px) {
  .aisi-collab-post .evaluation-figure--trajectories iframe { height: 770px; }
}

@media (max-width: 663px) {
  .aisi-collab-post .evaluation-figure--trajectories iframe { height: 810px; }
}

@media (max-width: 563px) {
  .aisi-collab-post .evaluation-figure--trajectories iframe { height: 885px; }
  .aisi-collab-post .evaluation-figure--distribution iframe { height: 580px; }
}

@media (max-width: 463px) {
  .aisi-collab-post .evaluation-figure--trajectories iframe { height: 980px; }
  .aisi-collab-post .evaluation-figure--distribution iframe { height: 612px; }
}

@media (max-width: 383px) {
  .aisi-collab-post .evaluation-figure--trajectories iframe { height: 1125px; }
  .aisi-collab-post .evaluation-figure--distribution iframe { height: 680px; }
}

.aisi-collab-post .evaluation-figure figcaption {
  margin-top: 0.8rem;
  color: var(--fg-muted);
  font-size: 0.9rem;
  line-height: 1.6;
}
</style>

The [EvalEval Coalition](https://evalevalai.com/) is thrilled to share that the [UK AI Security Institute (AISI)](https://www.aisi.gov.uk/) is using EvalEval's infrastructure to openly share evaluation results, supporting more reproducible and verifiable evaluation science.

AISI and EvalEval have previously collaborated on research that began at a [joint workshop alongside NeurIPS 2025]({{ site.baseurl }}/events/workshop-2025/), and feedback from the Institute has helped shape the [Every Eval Ever (EEE) schema]({{ site.baseurl }}/projects/every-eval-ever/). This next phase of the collaboration puts that shared infrastructure into practice.

## Why reproducible evaluation reporting matters

As AI deployment accelerates, evaluations are becoming increasingly important sources of evidence about model and system performance. Yet results are reported across many formats, platforms, and outlets, often without enough information to reproduce them. Running the evaluations again may itself be prohibitively expensive.

EvalEval's mission is to improve this ecosystem through a shared reporting schema, [Every Eval Ever]({{ site.baseurl }}/projects/every-eval-ever/), and an open platform, [Evaluation Cards](https://evalcards.evalevalai.com/), that brings evaluation results and the information needed to interpret them into a common structure.

This builds naturally on AISI's work to make evaluation more efficient through [OptStop](https://arxiv.org/abs/2608.14425), more statistically rigorous through [HiBayES](https://www.aisi.gov.uk/blog/hibayes-improving-llm-evaluation-with-hierarchical-bayesian-modelling), and more standardised in areas including transcript analysis and capability elicitation. Together, AISI and EvalEval are working to diagnose gaps in evaluation reporting and build shared infrastructure to close them.

## What AISI is sharing

Transcript-level transparency matters not only for reproducibility, but also for analysis and diagnosis. In this new phase of the collaboration, AISI is making publicly reported evaluation methods and findings available through Evaluation Cards where appropriate. The release includes verified results, context, and configuration information for the five benchmarks in the paper's main experiment:

- HealthBench
- FrontierMath
- Humanity's Last Exam
- SWE-Bench Pro
- Terminal-Bench 2.0

These results cover six frontier models: Claude Opus 4, Claude Opus 4.5, Claude Opus 4.6, GPT-5, GPT-5.2, and GPT-5.4. The release also includes results from two related cyber evaluations—Cyber CTFs and The Last Ones—which use a different, partially overlapping set of models. The data accompany AISI's paper, [*How Inference Compute Shapes Frontier LLM Evaluation*](https://arxiv.org/abs/2606.17930), which studies how benchmark performance depends on inference-time compute and evaluation protocol.

<figure class="evaluation-figure evaluation-figure--trajectories">
  <iframe
    scrolling="no"
    src="https://evaleval-general-eval-card.hf.space/embed/eval/trajectories/aisi-inference-scaling/hle?panel=tokens"
    title="Humanity's Last Exam cumulative success rate by tokens used">
  </iframe>
  <figcaption><strong>Figure 1.</strong> Performance on Humanity’s Last Exam changes with evaluation protocol and inference compute. Each curve shows the cumulative share of attempted tasks solved within a given token count, using the earliest observed success per task. When models received correctness feedback from an oracle after each attempt, they continued to solve additional tasks as token use increased.</figcaption>
</figure>

When results are openly released with setup information, researchers and practitioners can examine individual studies more closely and compare findings across the wider ecosystem. Where other reports lack these details, releases like AISI's provide verified reference points for interpreting evaluations in context—for example, by helping researchers understand how setup choices may influence reported performance. As more evaluators adopt EEE, open comparisons like these can support broader and more reliable meta-research.

<figure class="evaluation-figure evaluation-figure--distribution">
  <iframe
    scrolling="no"
    src="https://evaleval-general-eval-card.hf.space/embed/eval/distribution/aisi-inference-scaling/terminal-bench-2?view=context"
    title="AISI Terminal-Bench 2.0 results in the context of other reported evaluations">
  </iframe>
  <figcaption><strong>Figure 2.</strong> AISI's Terminal-Bench 2.0 results alongside other reported evaluations for the same models, under different evaluation setups.</figcaption>
</figure>

We are excited about this adoption and look forward to further standardising and sharing evaluations with AISI and other AI evaluation organisations.

## Contribute to the shared mission

- **Model developers:** [Report verified evaluation results](https://evalcards.evalevalai.com/help/get-verified).
- **Evaluation developers:** Report benchmarks and run data using the [Every Eval Ever schema](https://github.com/evaleval/every_eval_ever).
- **Evaluation, governance, and policy researchers:** [Explore Evaluation Cards](https://evalcards.evalevalai.com/) by benchmark or model, or use it to examine the state of evaluation reporting as a whole.

## About the EvalEval Coalition

The EvalEval Coalition is a research community developing scientifically grounded research and robust deployment infrastructure for the evaluation ecosystem. Its goal is to improve evaluation science, address the lack of consensus around documenting evaluation applicability and utility, and broaden coverage of the impacts that matter for scientific research and policy analysis.

The coalition's flagship projects include [Every Eval Ever]({{ site.baseurl }}/projects/every-eval-ever/), a shared schema and repository for evaluation results, and [Evaluation Cards]({{ site.baseurl }}/projects/eval-cards/), which combines benchmark metadata, evaluation-run data, and model metadata into interpretable records. Together, they make it easier to understand when apparently similar scores were produced under meaningfully different conditions.

## About the UK AI Security Institute

The [UK AI Security Institute](https://www.aisi.gov.uk/) is a research organisation within the UK government's Department for Science, Innovation and Technology. Its mission is to equip governments with a scientific understanding of the risks posed by advanced AI. AISI conducts research and builds infrastructure to understand advanced AI capabilities and impacts, develop and test mitigations, and inform policy.

## Further reading

- [*How Inference Compute Shapes Frontier LLM Evaluation*](https://arxiv.org/abs/2606.17930)
- [HiBayES: Improving LLM evaluation with hierarchical Bayesian modelling](https://www.aisi.gov.uk/blog/hibayes-improving-llm-evaluation-with-hierarchical-bayesian-modelling)
- [HiBayES paper](https://arxiv.org/abs/2505.05602)
- [OptStop paper](https://arxiv.org/abs/2608.14425)
- [Every Eval Ever]({{ site.baseurl }}/projects/every-eval-ever/)
- [Evaluation Cards](https://evalcards.evalevalai.com/)

</div>
