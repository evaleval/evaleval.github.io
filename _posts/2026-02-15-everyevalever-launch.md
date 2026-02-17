---
layout: post
title: "Every Eval Ever: Toward a Common Language for AI Eval Reporting"
date: 2026-02-15
published: true
exclude_from_collection: true
category: Infrastructure
image: "/assets/img/blogs/EEEstacked_launch-post.webp"
image_contain: true
authors:
  - name: "Jan Batzner*"
  - name: "Leshem Choshen*"
  - name: "Avijit Ghosh*"
  - name: "Sree Harsha Nelaturu*"
  - name: "Anastassia Kornilova*"
  - name: "Damian Stachura*"
  - name: "Yifan Mai"
  - name: "Asaf Yehudai"
  - name: "Anka Reuel"
  - name: "Irene Solaiman"
  - name: "Stella Biderman"
tags:
  - "infrastructure"
  - "eval metadata"
  - "reproducibility"
description: "The multistakeholder coalition EvalEval launches Every Eval Ever, a shared format and central eval repository. We're working to resolve AI evaluation fragmentation, improving formatting, settings, and ways to compare and build on each other's work."
---
As AI models advance, we encounter more and more evaluation results and benchmarks—yet evaluation itself rarely takes center stage. It plays an important role across the entire development cycle, from design decisions and [research to marketing and maintenance](https://dl.acm.org/doi/full/10.1145/3708359.3712152). This rapid progression forces evaluation solutions and eval infrastructure to keep up, often pushing them to adapt to settings [they were not originally designed for](https://arxiv.org/abs/2405.14782). For example, the popular evaluation tool [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness) was initially designed for base model evaluation, but it now supports instruction-tuned and reasoning models that didn’t even exist when it was created.

This rapid progression and wide range of evals led to fragmentation. Lacking standards, each framework reports different attributes in different formats, preventing the community from reliably comparing, replicating, determining which component fails, separating signal from noise, reusing others’ (often costly) evaluations, and performing large-scale analysis. This lack of reusability makes it difficult to build on the momentum of previous efforts. As model training has moved past the point where we retrain models from scratch or rewrite their training code, we must ask: why are we still rerunning every evaluation from scratch?

As part of a **cross-institutional, cross-sector initiative, the [EvalEval Coalition](https://evalevalai.com),** we are announcing [Every Eval Ever](https://evalevalai.com/projects/every-eval-ever/) to improve the state of evaluation building and comparison: 

(1) **Defining a shared schema** so results from different frameworks can be compared, and 

(2) Providing a **crowdsourced eval database**<sup><a href="#fn:1">1</a></sup> so researchers don't have to start from scratch every time.

Today, we're launching [Every Eval Ever](https://github.com/evaleval/every_eval_ever),<sup><a href="#fn:2">2</a></sup> built upon valuable feedback from AI Eval Ecosystem actors including researchers and practitioners at the U.S. Center for AI Standards and Innovation (CAISI), EleutherAI, Hugging Face, Noma Security, Trustible, Inspect AI, Meridian, AVERI, Collective Intelligence Project, Stanford HELM, Weizenbaum, Evidence Prime, MIT, TUM, and IBM Research.

## The Hidden Problem
The infrastructure is fragmented, and the results scattered.
How does Model A compare to Model B on a given benchmark? One lab reports a five-shot score from its own harness. Another uses zero-shot through a different framework. A third pulls numbers from a leaderboard that does not disclose generation parameters. 
This fragmentation has concrete costs. Large-scale analysis of evaluation trends or improving evaluation methodologies requires weeks of data wrangling before any research can begin. If they are possible at all, without (re)running full leaderboards at extreme costs. Comparison is unreliable when evaluations use different settings but carry the same benchmark name. Reproducibility is elusive when the details are lacking and inconsistent. 
It is time for a change. We have seen this before in other parts of the ML pipeline. The community stopped retraining models from scratch or rewriting training code for each project long ago. Evaluations are next.

## Why Us, Why Now
We just know the pain. The [EvalEval Coalition](https://evalevalai.com/about/) is a community of researchers working to fix how AI evaluations are built, run, documented, shared, and compared. We worked on a myriad of projects where collecting evaluations restricts what can be done or takes most of the project’s efforts. Need examples?  See [1](https://arxiv.org/abs/2602.03344), [2](https://arxiv.org/abs/2503.01622), [3](https://proceedings.neurips.cc/paper_files/paper/2024/hash/28236482f64a72eec43706b6f3a6c511-Abstract-Conference.html), [4](https://arxiv.org/abs/2412.06540), [5](https://arxiv.org/abs/2410.11840), [6](https://aclanthology.org/2024.acl-long.456/), [7](https://arxiv.org/abs/2407.13696), [8](https://par.nsf.gov/servlets/purl/10547932), [9](https://aclanthology.org/2024.naacl-long.139/), [10](https://aclanthology.org/2025.acl-long.34/) among others.

The urgency of standardized AI evaluation has reached a critical tipping point, driven by the shift toward evaluations as a primary mechanism of governance. With the EU AI Act and the U.S. Executive Order now mandating rigorous risk assessments, standardized data is no longer a luxury but a prerequisite for meaningful sociotechnical safety standards. 
This need is further intensified by the exploding complexity of modern AI, where frameworks like Inspect AI and HELM must navigate multi-turn agentic behaviors and human preferences that defy simple scoring. 

Ultimately, failing to adopt reusable formats imposes a technical debt on the community, forcing researchers to waste resources rerunning redundant evaluations rather than advancing the scientific frontier. Oh, and of course, even what is shared is often just a single score per dataset, obscuring many questions.

## What We're Building
The [Every Eval Ever](https://github.com/evaleval/every_eval_ever) is a schema to describe evaluation results and a community collection of those results. It is by the community and for the community, made simple to contribute to, evaluation or code. Enough high-level, let’s get into the details.

The repository is organized by benchmark, model, and evaluation run. Each result file captures not just scores but the context you need to interpret and reuse them: 
- who ran the evaluation, 
- what model, 
- with what settings, 
- what these scores actually mean, 
- and instance-level scores, if you have them.

```
data/
└── {benchmark}/
    └── {developer_name}/
        └── {model_name}/
            ├── {uuid}.json
            └── {uuid}.jsonl
```

The three components that make [Every Eval Ever](https://github.com/evaleval/every_eval_ever) work 💙

📋 A [metadata schema](https://github.com/evaleval/every_eval_ever/blob/main/eval.schema.json) that defines the information needed for meaningful comparison of evaluation results

🔧 [Validation](https://github.com/evaleval/every_eval_ever/blob/main/utils/validate_data.py) that checks data against the schema before it enters the repository 

🔌 [Converters](https://github.com/evaleval/every_eval_ever/tree/main/eval_converters) for popular evaluation tools like [Inspect AI](https://inspect.aisi.org.uk/), [HELM](https://github.com/stanford-crfm/helm), and [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness), so you can transform your existing evaluation logs into the standard format.

## 📋 The Schema
One thing we realized early on: evaluation harnesses are amazing — we love them all — but they were each built for their own purposes, and we cannot simply aggregate their scores. Take MMLU: the lm-eval-harness, HELM, and the original Berkeley implementation all evaluate the same dataset, but with different prompt formatting, different answer extraction methods, and different ordering of few-shot examples. The result? [LLaMA 65B scored 0.637 on HELM but 0.488 on the EleutherAI harness](https://huggingface.co/blog/open-llm-leaderboard-mmlu) — both called "MMLU score," same dataset, big gap. 

And then, think about all the evaluation data that doesn't come from a harness at all: hand-built benchmarks, leaderboard scrapes, results pulled from research papers and blog posts. We wanted one format that could capture whether harness-run or hand-built alike, truly every evaluation ever.
Here's how the schema looks in practice, using [LiveCodeBench Pro](https://github.com/GavinZhengOI/LiveCodeBench-Pro) as an example from our repo.

First, we capture where the evaluation came from and who ran it:

```json
{
  "source_metadata": {
    "source_name": "LiveCodeBench Pro",
    "source_type": "evaluation_platform",
    "source_organization_name": "LiveCodeBench",
    "evaluator_relationship": "third_party"
  }
}
```

The schema also records the exact model details — name, developer, and how it was accessed. Was it called through the developer's own API (like OpenAI or Anthropic), through a third-party provider (like OpenRouter or Together AI), or run locally with an inference engine like vLLM? This isn't just because we love eval metadata. The same model, accessed through different providers or run with different engine configurations, [can produce different outputs](https://arxiv.org/pdf/2312.03886) — and therefore different scores.

Next, generation settings. We all know how much they matter — changing temperature or the number of samples alone can shift scores by several points. Yet they're routinely absent from leaderboards and incomplete even in papers. When a model's score is reported without this context, we're left guessing whether differences reflect actual model capability or just different settings. So we want to capture this information — and where it's missing, record that gap explicitly, so anyone interpreting the results knows what context they do and don't have:

```json
{
  "generation_config": {
    "generation_args": {
      "temperature": 0.2,
      "top_p": 0.95,
      "max_tokens": 2048
    },
    "additional_details": {
      "n_samples": 10,
      "stop_sequences": ["\n```"]
    }
  }
}
```

And then there's the score itself. Let’s take a model on the coding benchmark [HumanEval](https://arxiv.org/abs/2107.03374): scoring 0.31 on the first try (called pass@1) represents a fraction of coding problems it solved — higher would be better. On the contrary, if the same model scores again 0.31 but on [RealToxicityPrompts](https://github.com/allenai/real-toxicity-prompts), lower scores would be better. [Every Eval Ever](https://github.com/evaleval/every_eval_ever) standardizes to enable better eval result interpretation:

```json
{
  "evaluation_results": [
    {
      "evaluation_name": "code_generation",
      "metric_config": {
        "evaluation_description": "pass@1 on code generation tasks",
        "lower_is_better": false,
        "score_type": "continuous",
        "min_score": 0,
        "max_score": 1
      },
      "score_details": {
        "score": 0.31
      }
    }
  ]
}
```

## 🔧 Validation & Converters
Better eval infrastructure should be easy and frictionless for practitioners. That's why we're proud that [Every Eval Ever](https://github.com/evaleval/every_eval_ever) provides:

**Converters:** If you're already running evaluations with existing eval tools, you shouldn't have to manually parse your results. Our converters transform evaluation logs into the Every Eval Ever format automatically. Converters for [HELM](https://github.com/evaleval/every_eval_ever/tree/main/eval_converters/helm), [lm-eval](https://github.com/evaleval/every_eval_ever/tree/main/eval_converters/lm_eval), and [Inspect AI](https://github.com/evaleval/every_eval_ever/tree/main/eval_converters/inspect) are already available, with more on the way. One step, and your eval data fits in.[^3]

**Validation:** Validation runs automatically on every submission via Hugging Face Jobs — before any result file is merged, it's checked against the schema to catch missing fields and structural issues early, not months later when someone tries to use the data. 

## 🧩 Design Decisions
What counts as a unique evaluation for you? This can get quite a thorny question! Imagine two [GSM8K](https://huggingface.co/datasets/openai/gsm8k) runs might differ in prompt template, chat template, vLLM version, GPU kernels, or dataset version — each affecting scores. Within our own coalition, members used GSM8K for purposes as different as measuring mathematical reasoning and benchmarking speculative decoding.

We considered defining a canonical parameter set to fingerprint unique runs. In practice, the space of score-affecting variables is too large for any fixed set. Our solution: each run gets its own file, identified by a UUID, with as much metadata as possible captured alongside it. Deduplication and grouping happen at the analysis layer, not the schema layer. This keeps data lossless while letting consumers apply their own equivalence criteria.

On purpose we allowed reporting whatever one has. For many, this is an aggregation score with some metadata; for others, it is per-example data and a lot of hyperparameters. Why should you care?
Hardly any evaluation research is done on the aggregation scores. You want to check whether there are biases, errors, redundant questions, questions that measure the wrong thing, aggregate datasets differently, and analyse errors. All of those questions require at least the model outputs or scores per example, not per dataset. 

## What’s Next
[Every Eval Ever](https://github.com/evaleval/every_eval_ever) grew out of a need we kept running into in our own research. When [EvalEval researchers mapped how social impact evaluations are reported across the field](https://arxiv.org/abs/2511.05613), examining 186 first-party reports and 183 third-party sources, the lack of a common format turned what should have been a straightforward analysis into weeks of manual data wrangling. That work made the case for why something like Every Eval Ever needed to exist: even though a lot of evaluation data is available open source, it is in incompatible formats, with no shared infrastructure to aggregate or compare it. 

This schema enables research. Beyond just good documentation hygiene, [researchers already used the repository in a multi-author EvalEval effort to analyze benchmark saturation across 60 benchmarks](https://evalevalai.com/projects/bench-sat/), finding that nearly half had lost their ability to differentiate top-performing models. Centralized, standardized evaluation data opens up more: seeing where the ecosystem is thin, which capabilities are over-measured, and which risks are neglected. With instance-level data, researchers can move beyond leaderboard averages to study item difficulty, robustness, and temporal drift. Every Eval Ever enables meta-evaluation: testing evaluation methods themselves to distinguish real progress from artifacts of setup and reporting.
We need your help. We're launching a [Shared Task](https://evalevalai.com/events/shared-task-every-eval-ever/) for practitioners alongside this post — two tracks for contributing public and proprietary eval data to the repository, with co-authorship for qualifying contributors and a [workshop at ACL 2026 in San Diego](https://evalevalai.com/events/2026-acl-workshop/). 

*Submissions open now, deadline May 1, 2026.*

## Get involved
- Try the schema 📋 : [HuggingFace Datastore](https://huggingface.co/datasets/evaleval/EEE_datastore)[^1], [Interactive Visualization](https://evalevalai.com/projects/every-eval-ever/)[^2], and [GitHub](https://github.com/evaleval/every_eval_ever)

- Join the Shared Task 🏁 : [Call for Participation](https://evalevalai.com/events/shared-task-every-eval-ever/)

- Join the community 💬 : [Reach out to be added](mailto:jan.batzner@tum.de)

[^1]: EvalEval (2026). [Hugging Face Every Eval Ever Datastore](https://huggingface.co/datasets/evaleval/EEE_datastore). The crowdsourced database of standardized evaluation results. Top Contributor: Sree Harsha Nelaturu.
[^2]: EvalEval (2026). [Interactive Visualization of the Every Eval Ever Schema](https://evalevalai.com/projects/every-eval-ever/). Top Contributor: Avijit Ghosh.
[^3]: EvalEval (2026). [Every Eval Ever Converters](https://github.com/evaleval/every_eval_ever/tree/main/eval_converters). Converters for popular evaluation frameworks to the Every Eval Ever format. Top Contributor: Damian Stachura.

```bibtex
@misc{evaleval2026everyevalever,
  title   = {Every Eval Ever: Toward a Common Language for AI Eval Reporting},
  author  = {Jan Batzner and Leshem Choshen and Avijit Ghosh and Sree Harsha Nelaturu and Anastassia Kornilova and Damian Stachura and Yifan Mai and Asaf Yehudai and Anka Reuel and Irene Solaiman and Stella Biderman},
  year    = {2026},
  month   = {February},
  url     = {https://evalevalai.com/infrastructure/2026/02/15/everyevalever-launch/},
  note    = {Blog Post, EvalEval Coalition}
}
```

### Acknowledgement and Feedback
We acknowledge feedback by, but not limited to, JJ Allaire (Inspect, Meridian Labs), Ryan Steed (US CAISI), Zeerak Talat
(University of Edinburgh), Gal Moyal (Noma Security), Sean McGregor (AVERI), Joal Stein
(WeVal/CiP), Elizabeth M. Daly (IBM Research), Aris Hofmann (IBM Research), Inge Vejsbjerg (IBM Research), Dhaval Salwala (IBM Research), Srishti Yadav (University of Copenhagen), Andrew Tran (Independent), Sanchit Ahuja (Northeastern),  Marek Šuppa (Slido), Stefan Schmid (Weizenbaum, TUB), Gjergji Kasneci (TUM, MCML).





