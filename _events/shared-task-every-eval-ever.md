---
layout: event
title: "Shared Task: Every Eval Ever"
subtitle: Building a Unifying, Standardized Database of LLM Evaluations
status: active
order: 2
category: Infrastructure
event_date: 2026-05-01
location: 🌐 Online
host: EvalEval
description: |
  Help us build the first unifying, open database of LLM evaluation results! Convert evaluation data from leaderboards, papers, or your own runs into a shared format — and join as co-author on the resulting paper.
---
As the cost of genAI model evaluation is rapidly increasing, researchers, non-profits, small companies, and civil society orgs need to rely on existing evaluation data on the web. Evaluation data refers to Large Language Model evaluations on popular benchmarks or domain-specific tasks, which are commonly saved under Hugging Face leaderboards or reported in research papers. However, with numerous evaluation frameworks emerging across research and industry, evaluation data is scattered across different platforms, stored in inconsistent formats, and lacks standardization that would enable meaningful comparison and meta-analysis.

The [Every Eval Ever](https://github.com/evaleval/every_eval_ever) Shared Task aims to address this fragmentation by establishing a unified metadata schema for LLM evaluations to populate a comprehensive, standardized database of evaluation results. Qualifying contributors will be invited to join the paper write-up as co-authors.

## 🎯 Task

Participants will contribute to building a comprehensive database of LLM evaluations by converting existing evaluation data into our standardized schema. The task is divided into two tracks:

### 🏁 Track 1: Public Eval Data Parsing

**Objective 1:** Parse and convert evaluation data from existing public leaderboards (e.g., Chatbot Arena, Open LLM Leaderboard, AlpacaEval, MT-Bench, etc.) into our standardized metadata schema.

**Objective 2:** Extract evaluation results from academic papers and technical reports, converting them into our standardized schema. This includes results from tables, figures, and text descriptions in published research.

**Deliverables:**
1. Python scripts that programmatically extract data from leaderboard APIs or web interfaces, or Python scripts for automated or (semi-)automated extraction from papers
2. Converted datasets in our schema format (JSON)
3. Documentation of data extraction methodology and any issues encountered (txt)

### 🔒 Track 2: Proprietary Evaluation Data

**Objective:** Convert proprietary evaluation datasets (from companies, research labs, or private benchmarks) into our schema and contribute them to the shared database. This track welcomes both public release of new data and private contributions under appropriate data use agreements.

**Deliverables:**
1. Converted datasets in standardized schema format (JSON)
2. Python conversion scripts (if data structure can be shared according to your org policies)
3. Documentation of data extraction methodology and any issues encountered (txt)

## 👥 Participation Guidelines

**Who can participate:** Anyone! Academic researchers, industry practitioners, independent developers.

**Submission Requirements:**
- ✓ All submissions should include conversion scripts (Python preferred)
- ✓ Converted data must validate against our schema
- ✓ Documentation explaining the conversion process
- ✓ Participants may use any publicly available leaderboard or paper (link attribution), if not already in database
- ✓ Proprietary data submissions must include appropriate permissions
- ✓ Optional: use the data you parsed for a research question and submit a workshop paper for [EvalEval at ACL](/events/2026-acl-workshop/)

## 📅 Important Dates

- **Schema and example data release:** February 17, 2026
- **Shared Task period begins:** February 17, 2026
- **Submission deadline:** May 1, 2026
- **Results announcement:** June 1, 2026
- **Workshop/presentation:** [ACL San Diego, July 7, 2026](/events/2026-acl-workshop/)

## 🔍 Schema at a Glance

For the full story, see our blog post: [Every Eval Ever: Toward a Common Language for AI Eval Reporting](/infrastructure/2026/02/15/everyevalever-launch/).

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

The three components that make [Every Eval Ever](https://github.com/evaleval/every_eval_ever) work:

📋 A [metadata schema](https://github.com/evaleval/every_eval_ever/blob/main/eval.schema.json) that defines the information needed for meaningful comparison of evaluation results

🔧 [Validation](https://github.com/evaleval/every_eval_ever/blob/main/utils/validate_data.py) that checks data against the schema before it enters the repository

🔌 [Converters](https://github.com/evaleval/every_eval_ever/tree/main/eval_converters) for popular evaluation tools like [Inspect AI](https://inspect.aisi.org.uk/), [HELM](https://github.com/stanford-crfm/helm), and [lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness), so you can transform your existing evaluation logs into the standard format.

### 📋 The Schema

One thing we realized early on: evaluation harnesses are amazing — we love them all — but they were each built for their own purposes, and we cannot simply aggregate their scores. Take MMLU: the lm-eval-harness, HELM, and the original Berkeley implementation all evaluate the same dataset, but with different prompt formatting, different answer extraction methods, and different ordering of few-shot examples. The result? [LLaMA 65B scored 0.637 on HELM but 0.488 on the EleutherAI harness](https://huggingface.co/blog/open-llm-leaderboard-mmlu) — both called "MMLU score," same dataset, big gap.

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

The schema also records the exact model details — name, developer, and how it was accessed. Was it called through the developer's own API (like OpenAI or Anthropic), through a third-party provider (like OpenRouter or Together AI), or run locally with an inference engine like vLLM? The same model, accessed through different providers or run with different engine configurations, [can produce different outputs](https://arxiv.org/pdf/2312.03886) — and therefore different scores.

Next, generation settings. We all know how much they matter — changing temperature or the number of samples alone can shift scores by several points. Yet they're routinely absent from leaderboards and incomplete even in papers. So we want to capture this information — and where it's missing, record that gap explicitly, so anyone interpreting the results knows what context they do and don't have:

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

And then there's the score itself. A model scoring 0.31 on [HumanEval](https://arxiv.org/abs/2107.03374) (pass@1) means higher is better. But 0.31 on [RealToxicityPrompts](https://github.com/allenai/real-toxicity-prompts) means lower is better. [Every Eval Ever](https://github.com/evaleval/every_eval_ever) standardizes to enable better eval result interpretation:

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

### 🔧 Validation & Converters

Better eval infrastructure should be easy and frictionless for practitioners. That's why [Every Eval Ever](https://github.com/evaleval/every_eval_ever) provides:

**Converters:** If you're already running evaluations with existing eval tools, you shouldn't have to manually parse your results. Our converters transform evaluation logs into the Every Eval Ever format automatically. Converters for [HELM](https://github.com/evaleval/every_eval_ever/tree/main/eval_converters/helm), [lm-eval](https://github.com/evaleval/every_eval_ever/tree/main/eval_converters/lm_eval), and [Inspect AI](https://github.com/evaleval/every_eval_ever/tree/main/eval_converters/inspect) are already available, with more on the way.

**Validation:** Validation runs automatically on every submission via Hugging Face Jobs — before any result file is merged, it's checked against the schema to catch missing fields and structural issues early, not months later when someone tries to use the data.

## 🧑‍🔬 Core Organizers

- [Jan Batzner](mailto:jan.batzner@tum.de), Weizenbaum Institute, MCML, TU Munich
- Leshem Choshen, MIT, IBM Research, MIT-IBM Watson AI Lab
- Sree Harsha Nelaturu, Zuse Institute Berlin
- Usman Gohar, Iowa State University
- Damian Stachura, Evidence Prime
- Andrew Tran, Independent
- Avijit Ghosh, Hugging Face

## 🔗 Resources
- 📂 **Schema:** [Documentation and examples on GitHub](https://github.com/evaleval/every_eval_ever)
- ✓ **Validation:** [Script to validate your data against the schema](https://github.com/evaleval/every_eval_ever/blob/main/scripts/validate_data.py)
- 🚀 **Submit:** [Drag & drop or PR on our Hugging Face Datastore](https://huggingface.co/datasets/evaleval/EEE_datastore)
- 💬 **Slack:** [Reach out to join our discussion forum](mailto:jan.batzner@tum.de)
- 🤝 **Partner project:** [IBM Auto-BenchmarkCard](https://huggingface.co/datasets/ibm-research/Auto-BenchmarkCard), capturing benchmark metadata complementary to our evaluation schema, with a joint effort to bridge both databases ahead

## ❓ FAQ

**Q: Do I need to submit data for both tracks?**
A: No, you can participate in any single track or combination of tracks that interests you.

**Q: Can I submit data from multiple leaderboards/papers?**
A: Yes! We encourage comprehensive contributions covering multiple sources.

**Q: What if I find errors or inconsistencies in source data?**
A: Document these in your submission. Our goal is transparency about data quality.

**Q: Will my conversion scripts be made public?**
A: Yes, to enable reproducibility and allow others to update the data as leaderboards evolve.
