---
layout: post
title: "Introducing Evaluation Cards: A Live Interpretive Layer for Understanding the AI Evaluations Ecosystem"
date: 2026-06-09
published: true
exclude_from_collection: true
category: Infrastructure
image: "/assets/img/blogs/evalcards_launch_banner.webp"
image_contain: true
authors:
  - name: "Wm. Matthew Kennedy"
  - name: "Anka Reuel"
  - name: "Jenny Chim"
  - name: "Andrew Tran"
  - name: "Yanan Long"
  - name: "Shrishti Yadav"
  - name: "Kabir Manghnani"
  - name: "Leshem Chosen"
  - name: "David Manheim"
  - name: "Jennifer Mickel"
  - name: "Jessica Ji"
  - name: "Irene Solaiman"
  - name: "Avijit Ghosh"
tags:
  - "infrastructure"
  - "eval metadata"
  - "reproducibility"
  - "evaluation reporting"
description: "The EvalEval Coalition launches Evaluation Cards, an open-source live interpretive layer over the AI evaluations reporting ecosystem—surfacing reproducibility, completeness, provenance, and comparability across 100,000+ reported results."
---

Today, [the EvalEval Coalition](https://evalevalai.com/) is beta launching Evaluation Cards, an open-source project for stakeholders across the evaluation ecosystem to improve reproducibility, completeness, provenance, and comparability across AI evaluations. Evaluation Cards includes:

- An interface to explore the largest and most comprehensive corpus yet assembled, with 101,955 reported evaluation results for 638 benchmarks run by 31 organizations on 5,816 models (as of 9 June 2026) based on our [EvalEval sister project, Every Eval Ever (EEE)](https://evalevalai.com/projects/every-eval-ever/)and [IBM AutoBenchmark Cards](https://research.ibm.com/publications/auto-benchmarkcard-automated-synthesis-of-benchmark-documentation).
- A front end that shows four novel signals about the state of evaluations as a whole: reproducibility, completeness, provenance, and comparability.
- An open platform that developers, evaluators, researchers, and anyone else in the evaluations community can use to centralize evaluation reporting.

**EvalCards is in beta. Fixing evaluation reporting is a community effort that will benefit everyone but, as large as it is, the EvalEval Coalition won't be able to do it alone. Help us by contributing and spreading the word!**

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin: 1.5rem 0;" markdown="0">
  <a href="https://arxiv.org/abs/2606.09809"><kbd>Read the full paper here</kbd></a>
  <a href="https://evalcards.evalevalai.com/"><kbd>Check out Evaluation Cards here</kbd></a>
  <a href="#adopt-use-and-contribute-to-evaluation-cards"><kbd>Adopt, use, get validated, contribute</kbd></a>
</div>



## Addressing fragmentation in the evaluation documentation landscape

AI evaluations are crucial for assessing and improving AI model performance across an increasingly wide variety of domains. Consequently, evaluations communities produce results at tremendous scale. However, these results are reported in different places and in different ways. Some use leaderboards, others model cards, still others blog posts, conference papers, posters, or articles. Although this flexibility can benefit certain stakeholders in different situations, it contributes to an increasingly serious problem: because so few evaluations are reported with enough information to properly interpret their findings, there is no way to compare results across sources, identify what a report leaves out, or trace a major claim back to the evidence it rests on. 

Until today.

The EvalEval Coalition is excited to introduce the beta version of Evaluation Cards, a live interpretive layer over the public reporting ecosystem. For the first time, we have a tool that can reveal the state of reporting across the whole evaluation ecosystem, surfacing glaring gaps that have, until recently, remained undetected.

For example, three different organizations report GPT-5's scores in MATH-500, but those range from 84.7% to 98.9% depending on configuration (which is not fully reported).

Evaluation Cards not only surfaces these discrepancies (which are accessible through existing reporting artifacts, albeit inefficiently), but also provides more granular detail about why these discrepancies exist (which is rarely obvious without detailed examination of each evaluation’s configuration, including specifics such as temperature or max tokens). This is Evaluation Cards’ main purpose: to provide a tool to answer deeper questions about the meaning of evaluation results.

## A card for every evaluation

Evaluation Cards builds on years of hard work by others concerned with reporting practices and improving the state of evaluations. As a reporting artifact, Evaluation Cards is inspired by Datasheets[^1], Model Cards[^2], Benchmark Cards[^3], Audit Cards[^4], System Cards[^5], and BetterBench[^6], each of which specify what should be documented.

However, prior efforts largely stopped at prescription, leaving implementation for another day and important gaps to be filled. Each of those efforts covers only a narrow slice of the evaluation lifecycle, most artifacts are produced for one specific kind of audience, and most reporting proposals remain just that–proposals. 


The [Every Eval Ever (EEE) Schema](https://github.com/evaleval/every_eval_ever) moved the field forward by actually implementing a schema for structured evaluation reporting.

Evaluation Cards goes the rest of the way: composing the raw data that the ecosystem produces at scale into one canonical evaluation record:

**Run data:** Who ran the eval? On what model? With what generation settings? The source of this data comes from EEE, the EvalEval Coalition's results reporting scheme and community repository for standardised eval run data.

**Benchmark metadata:** the benchmark's measurement target, scoring, provenance, and known risks. This comes from AutoBenchmarkCards, which automatically and reliably extract information about a measurement instrument from conference papers and system cards.

**Model metadata:** release date, parameter count, weight accessibility, all automatically pulled from community catalogs (hub-stats, models.dev) covering both open and API-hosted models.

<div style="display: flex; flex-wrap: wrap; gap: 16px;">
  <iframe src="https://evalcards.evalevalai.com/evals/artificial-analysis-llms/mmlu-pro"
          style="flex: 1 1 400px; height: 800px; border: 1px solid #ddd; border-radius: 8px;"
          loading="lazy"
          title="MMLU-Pro Evaluation Card">
  </iframe>
  <iframe src="https://evalcards.evalevalai.com/models/openai/gpt-5.5"
          style="flex: 1 1 400px; height: 800px; border: 1px solid #ddd; border-radius: 8px;"
          loading="lazy"
          title="GPT-5.5 Model Card">
  </iframe>
</div>

Furthermore, Evaluation Cards is open, built by and for the wider evaluations community. Contributors span institutions, sectors, continents, and specializations.

<img src="/assets/img/blogs/evalcards_contributor_logos.webp"
    alt="EvalCards contributor affiliation logos"
    class="w-full h-auto my-8">
   

## Evaluation Cards needs you!

Evaluation Cards surfaces extremely valuable information that shouldn't be abstracted away. We’re looking for model developers to help foster transparency and ecological validity by contributing their data. We’re also looking for evaluators to share their data, setup, and config information. This way we can ensure the community is comparing evaluation data apples to apples. 

Organizations that contribute their own evaluation data earn a verification badge. Verified contributors have submitted over 40% of Evaluation Cards’ data, and, through upcoming partnerships and engagements from policy and research organizations in the evaluation ecosystem, our goal is to grow this number quickly. Learn how your organization can [become verified](https://evalcards.evalevalai.com/help/get-verified).


<img src="/assets/img/blogs/evalcards_verification_tooltip.gif"
     alt="EvalCards tooltip"
     style="display: block; margin: 1em 0; width: 400px;">

## Four new interpretive signals

Having good model and evaluation data allows Evaluation Cards to do something no other project has done. Across these records (making legible 100,000+ results at launch), Evaluation Cards computes **four interpretive signals** that reveal valuable insights into the state and quality of evaluations. Signals respond to desiderata shared by evaluations stakeholders in the course of our own user interview program:


**Reproducibility: Can someone else run this evaluation and get the same results?**

**Completeness: Is benchmark documentation sufficient to interpret scores?**

**Provenance: Who reported the score? And who has reproduced it?**

**Comparability: What is the measurement target and how faithfully do different setups evaluate against it?**

Flags divergences in setups or reporting parties that likely reflect scores resulting from similar configurations rather than capability measurement targets, ensuring comparability of reported results.

These signals come from unflattening conventional evaluation reporting, which usually treats results as a flat triple comprising a model, a benchmark name, and a score. But evals are more than numbers, they are interpretive claims. Flattening discards structure that exists in almost every benchmark. For example, MATH has subject splits that vary widely in difficulty level. SWE-bench reports across various languages and setups. Open LLM Leaderboard aggregates several sub-benchmarks into a single figure.

## A first glimpse of the entire evaluations ecosystem

The Evaluation Cards project has allowed us to see the state of evaluations as a whole. Aggregating the four signals across the evaluations reporting ecosystem provides invaluable insight into key questions: are models systematically achieving certain results on evaluations? And are those results meaningful?

Early observations across the corpus (5 June 2026 snapshot) reveal startling initial findings:

**Evaluation reproducibility appears shockingly poor**

Across more than 50,000 evaluation records, 96.5% are missing at least one field from the minimal set needed to re-run them. Max-tokens is absent 95.6% of the time, temperature 93.9% of the time. The gap appears to be worst amongst first-party reporters. Frontier models are no exception: 95% of GPT-5’s 213 documented results lack the parameters to reproduce them. Although sometimes these shortcomings are produced by data extraction failures, it points to a serious and pervasive problem.

**Benchmark documentation substantially hampers the maturity of evaluations**

Median completeness of benchmarks is a paltry 10.7% across all 635 benchmarks captured here. Scores are present, but documentation of construct definitions, validation, intended use, limitations, and provenance are missing far more often than not.

**Scores reported by two or more parties diverge substantially**

Nearly all (98.2%) of model-benchmark pairs are reported only by one party. Of the remainder, different parties report scores that vary substantially more than half the time (51.9%). Among safety benchmarks, third-parties make up most reporters—this could be because there are more third-party evaluators. Evaluation Cards surfaces these kinds of questions for further inquiry.

The field is doing good work. It is just doing that work in isolation. As a result, the divination of scores has been allowed to supplant the systematic production of scientific knowledge. Evaluation Cards reveals the extent of this potential loss. It also serves as a call to improve our practices of evaluation reporting. Otherwise the burden of interpretation will continue to fall on those least well positioned to accurately interpret evaluation results but often most responsible for making important technical governance or policy decisions.

## Evaluation Cards is for everyone!

The evaluations community includes a diversity of stakeholders who are interested in evaluation results for many reasons. That's why we've launched supporting different "reader modes" (Research and Summary) to support different user needs. Both modes read identical data. They differ only in how they display it. Users can easily toggle between modes without losing their place.

We are actively exploring additional stakeholder reader modes. Our roadmap is public, and ideas are welcome: https://changemap.co/evaleval/evalcards/

**Research mode**

Research reader mode was designed with AI evals researchers, model developers, and technical AI governance personae in mind. This mode foregrounds methodology and places at top information about missing fields, divergence because of setup differences, and full metric configuration.

**Summary mode**

Summary mode was designed for personae like nontechnical AI policy researchers, qualitative researchers, journalists and reporters, and readers who prefer narrative reporting. This mode presents more information in plain language, with benchmark-specific elaborations about the measurement target, central caveats, and intended uses.

Try it out using the toggle at top left:

<iframe src="https://evalcards.evalevalai.com/evals/helm-capabilities/gpqa"
        width="100%"
        height="800"
        style="border: 1px solid #ddd; border-radius: 8px;"
        loading="lazy"
        title="GPQA Evaluation Card">
</iframe>

## Adopt, use, and contribute to Evaluation Cards

Evaluation Cards is built as a participatory, openly-governed initiative. We mean for it to be shaped by the AI evaluation community over time, not shipped once and abandoned. All of the code is open. 

**Model developers:** Report your evaluations on Evaluation Cards so others can better understand your model’s performance. Review third-party reported results for discrepancies. Earn verification badges for uploading your own evaluation results!

**Evaluation developers:** Upload your evaluations so others can find them, run them, and use them to improve model performance or evaluations design.Review other evaluators’ results. Earn verification badges for uploading your own evaluation results

**Research and policy community:** Consult Evaluation Cards as a resource in your model-, evaluation-, or field-level analysis and cite us in papers, reports, or policy briefs. 

Check out our contributor guides with more details [here](https://evalcards.evalevalai.com/help#how-to-contribute).

**All stakeholders:**

- Spread the word! Evaluation Cards promotes ecological validity in direct proportion to the number of those who know about it, use it, and contribute to it.
- Explore the corpus: [Browse by model](https://evalcards.evalevalai.com/models)  |  [Browse by evaluation](https://evalcards.evalevalai.com/evals)
- [Help us build Evaluation Cards (also, we're hiring)
- Flag [missing data](https://huggingface.co/spaces/evaleval/general-eval-card/discussions) or [incorrect scores](https://github.com/evaleval/every_eval_ever/issues)
- [Become a verified contributor](https://evalcards.evalevalai.com/help/get-verified)
- [Give us your feedback](https://evalcards.evalevalai.com/feedback)

**What's next:**

- See the [Evaluation Cards roadmap](https://changemap.co/evaleval/evalcards/)
- Tutorials for integrations and use cases
- Research and contributor hackathons
- An annual EvalEvalIndex

**Catch up with the EvalEval Coalition:**

- Come to our [FAccT '26 Tutorial](https://evalevalai.com/events/2026-facct-tutorial/)
- Join our [ACL '26 workshop](https://evalevalai.com/events/2026-acl-workshop/)
- [Join the EvalEval community](https://evalevalai.com)
- [See our recent activity](https://evalevalai.com/events/)

```bibtex
@misc{ghosh2026evaluationcardsinterpretivelayer,
      title={Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting}, 
      author={Avijit Ghosh and Anka Reuel and Jenny Chim and Wm. Matthew Kennedy and Srishti Yadav and Jennifer Mickel and Yanan Long and Andrew Tran and Anastassia Kornilova and Damian Stachura and Kevin Klyman and Felix Friedrich and Jeba Sania and Max Lamparth and Jan Batzner and Anoop Mishra and Eliya Habba and Yixiong Hao and Nathan Heath and Shalaleh Rismani and Usman Gohar and Andrea Loehr and David Manheim and Ruchira Dhar and Sree Harsha Nelaturu and Aarush Sinha and Leshem Choshen and Drishti Sharma and Ishan Khire and Amit Saha and Subramanyam Sahoo and Michael Hardy and Michael Alexander Riegler and Kabir Manghnani and Michelle Lin and Yanan Jiang and Yilin Huang and Asaf Yehudai and Jessica Ji and Aris Hofmann and Mubashara Akhtar and Nuno Moniz and Yacine Jernite and Stella Biderman and Zeerak Talat and Sanmi Koyejo and Mykel Kochenderfer and Irene Solaiman},
      year={2026},
      eprint={2606.09809},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2606.09809}, 
}

```


[^1]: Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III, and Kate Crawford. 2021. Datasheets for datasets. Commun. ACM 64, 12 (December 2021), 86–92. https://doi.org/10.1145/3458723 
[^2]: Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, and Timnit Gebru. 2019. Model Cards for Model Reporting. In Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT* '19). Association for Computing Machinery, New York, NY, USA, 220–229. https://doi.org/10.1145/3287560.3287596 
[^3]: Anna Sokol, Elizabeth M. Daly, Michael Hind, David Piorkowski, Xiangliang Zhang, Nuno Moniz, and Nitesh V. Chawla. 2025. BenchmarkCards: Standardized Documentation for Large Language Model Benchmarks. In Proceedings of the Thirty-Ninth Annual Conference on Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks Track. Available at: https://openreview.net/forum?id=b2IJBWhGFu. 
[^4]: Leon Staufer, Mick Yang, Anka Reuel, and Stephen Casper. 2025. Audit Cards: Contextualizing AI Evaluations. arXiv:2504.13839 cs.CY. Available at: https://arxiv.org/abs/2504.13839.
[^5]: Furkan Gursoy and Ioannis A. Kakadiaris. 2022. System Cards for AI-Based Decision-Making for Public Policy. arXiv:2203.04754 cs.CY. Available at: https://arxiv.org/abs/2203.04754. 
[^6]: Anka Reuel, Amelia Hardy, Chandler Smith, Max Lamparth, Malcolm Hardy, and Mykel J. Kochenderfer. 2024. BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices. In Advances in Neural Information Processing Systems 37 (NeurIPS 2024), 21763–21813. https://doi.org/10.52202/079017-0685
