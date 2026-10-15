---
layout: post
title: "Apertus 1.5 sets the bar for open, reproducible evaluation reporting"
date: 2026-10-15
published: true
category: Infrastructure
image: "/assets/img/blogs/evaleval-apertus-banner.webp"
authors:
  - name: "The EvalEval Coalition"
tags:
  - "infrastructure"
  - "evaluation reporting"
  - "reproducibility"
  - "model releases"
description: "Apertus 1.5 is the first model release to submit all of its evaluation results to Evaluation Cards and Hugging Face Community Evals, with enough detail for anyone to reproduce them."
---

<div class="apertus-collab-post" markdown="1">

<style>
.apertus-collab-post .evaluation-figure {
  margin: 2.5rem 0;
}

.apertus-collab-post .evaluation-figure iframe {
  display: block;
  width: 100%;
  border: 1px solid var(--border);
  border-radius: 4px;
  background: var(--bg-subtle);
}

/* Cross-origin embeds cannot report their height, so each is sized to its
   measured content height at the column widths below. */
.apertus-collab-post .evaluation-figure--global-mmlu iframe { height: 560px; }
.apertus-collab-post .evaluation-figure--ifeval iframe { height: 620px; }

@media (max-width: 767px) {
  .apertus-collab-post .evaluation-figure--global-mmlu iframe { height: 580px; }
  .apertus-collab-post .evaluation-figure--ifeval iframe { height: 640px; }
}

@media (max-width: 463px) {
  .apertus-collab-post .evaluation-figure--global-mmlu iframe { height: 600px; }
  .apertus-collab-post .evaluation-figure--ifeval iframe { height: 720px; }
}

.apertus-collab-post .evaluation-figure figcaption {
  margin-top: 0.8rem;
  color: var(--fg-muted);
  font-size: 0.9rem;
  line-height: 1.6;
}
</style>

Congratulations to the Swiss AI Initiative on [Apertus 1.5](https://huggingface.co/collections/swiss-ai/apertus-v15)! It is one of the most open model releases to date, with weights and training data both public. Their [release notes](https://huggingface.co/blog/swiss-ai/apertus-v15-release-notes) and [technical report](https://arxiv.org/abs/2610.15542) document the work in full.

Apertus is the first model developer to submit all of its evaluation results to [Evaluation Cards](https://evalcards.evalevalai.com) and [Hugging Face Community Evals](https://huggingface.co/blog/eee-community-evals), with enough detail for anyone to reproduce them. We have been waiting for a model developer to do this, so we're really happy to see it happen.

## What we did together

Apertus reported every evaluation for both final models in the [Every Eval Ever (EEE)]({{ site.baseurl }}/projects/every-eval-ever/) schema: 48 benchmarks for [Apertus 1.5 8B](https://huggingface.co/swiss-ai/Apertus-v1.5-8B) and 47 for [Apertus 1.5 70B](https://huggingface.co/swiss-ai/Apertus-v1.5-70B). Each record says who ran the evaluation and how, down to the generation settings. Because the text evals ran on their [public fork of lm-evaluation-harness](https://github.com/swiss-ai/lm-evaluation-harness), which EEE already has a converter for, you can rerun them yourself and see if you get the same numbers.

Those records now feed the Evaluation Cards for the [8B](https://evaleval-general-eval-card.hf.space/embed/model/reported-metrics/swiss-ai/Apertus-v1.5-8B) and [70B](https://evaleval-general-eval-card.hf.space/embed/model/reported-metrics/swiss-ai/Apertus-v1.5-70B) models, where each benchmark gets its own plot comparing Apertus with every other model reported on it. Here are two, for multilingual knowledge and instruction following, since those are the two areas the Apertus team singles out in their release notes.

<figure class="evaluation-figure evaluation-figure--global-mmlu">
  <iframe src="https://evaleval-general-eval-card.hf.space/embed/eval/histogram/swissai-apertus-evals/global-mmlu?model=swiss-ai%2FApertus-v1.5-8B" loading="lazy" title="Global MMLU results for Apertus 1.5 8B on Evaluation Cards"></iframe>
  <figcaption>Global MMLU: Apertus 1.5 8B alongside other models reported on Evaluation Cards.</figcaption>
</figure>

<figure class="evaluation-figure evaluation-figure--ifeval">
  <iframe src="https://evaleval-general-eval-card.hf.space/embed/eval/histogram/swissai-apertus-evals/ifeval?model=swiss-ai%2FApertus-v1.5-8B" loading="lazy" title="IFEval results for Apertus 1.5 8B on Evaluation Cards"></iframe>
  <figcaption>IFEval: Apertus 1.5 8B alongside other models reported on Evaluation Cards.</figcaption>
</figure>

## Why this matters

A benchmark score on its own tells you surprisingly little. Without the setup behind it, you can't fairly compare it with another model's score, and you certainly can't check it. Regulators are starting to ask for this detail too. When we [mapped Evaluation Cards against AI governance requirements]({{ site.baseurl }}/infrastructure/2026/09/28/mapping-evaluation-cards-to-ai-governance-requirements/), the EEE schema covered 56 of the 60 evaluation-reporting elements in Article 55 of the EU AI Act and the GPAI Code of Practice.

The [UK AI Security Institute]({{ site.baseurl }}/infrastructure/2026/09/22/uk-aisi-evaleval-reproducible-benchmark-results/) already publishes its evaluations this way. Until now, though, no model developer had done it for their own release.

## An open invitation to model developers

We'd love every model release to look like this. If you build models and want to report your evals the same way, here's how to start:

- Write your results in the [EEE schema](https://github.com/evaleval/every_eval_ever). If you already use lm-evaluation-harness, the converter handles most of it.
- Cross-post them to your Hugging Face model pages through [Community Evals](https://huggingface.co/blog/eee-community-evals). Your [Eval Card](https://evalcards.evalevalai.com) picks them up from there.

If you want a hand with your first submission, reach out through [evalevalai.com](https://evalevalai.com). As for Apertus, we're working with the team to make this the default for every release. Thank you to everyone at the Swiss AI Initiative for going first.

<div class="citation-block">
<span class="citation-label">BibTeX Citation</span>
<pre><code>{% raw %}@misc{evaleval2026apertus,
  author       = {{EvalEval Coalition}},
  title        = {{Apertus} 1.5 Sets the Bar for Open, Reproducible Evaluation Reporting},
  year         = {2026},
  month        = oct,
  howpublished = {EvalEval Coalition Blog},
  url          = {https://evalevalai.com/infrastructure/2026/10/15/apertus-open-reproducible-evals/}
}{% endraw %}</code></pre>
</div>

</div>
