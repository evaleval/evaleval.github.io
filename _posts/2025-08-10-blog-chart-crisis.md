---
layout: post
title: "The AI Evaluation Chart Crisis"
date: 2025-08-09
published: true
category: Documentation
image: "https://images.unsplash.com/photo-1677442136019-21780ecad995?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80"
authors:
  - name: "Andrew Tran"
  - name: "Leshem Choshen"
  - name: "Jennifer Mickel"
  - name: "Avijit Ghosh (for the EvalEval Coalition)"

tags:
  - "Tag1"
  - "Tag2"
description: "A brief excerpt of your post goes here."
---

This past week, Anthropic and OpenAI drew attention with the release of their latest AI models, Claude Opus 4.1 and GPT-5. While they demonstrated advancements in state-of-the-art performance, the presentation of evaluation results from both companies sparked important discussions in the machine learning community about best practices for accurate communication. In particular, charts used to showcase performance demonstrated broader issues in the AI evaluation ecosystem: a lack of balance between competitive benchmarking and statistical rigor.

### Learning from recent errors

Following Thursday’s release of GPT-5, social media was [ablaze](https://x.com/graphcrimes?s=21&t=DGhtzlwtn9OagRKXx6ySYw) with discussions surrounding the presentation choices for the figures OpenAI released rather than performance improvements of GPT-5. In one example, a bar chart used to claim GPT-5 is better than its predecessor o3 at coding—[the most common application of large language models by some metrics](https://www.anthropic.com/research/clio)—showed GPT-5’s 52.8% on SWE-bench Verified as taller than o3’s 69.1%.


<blockquote class="twitter-tweet"><p lang="en" dir="ltr">which is larger, 52.8 or 69.1? <a href="https://t.co/6Lr2iNQ29g">pic.twitter.com/6Lr2iNQ29g</a></p>&mdash; will brown (@willccbb) <a href="https://twitter.com/willccbb/status/1953503727517938135?ref_src=twsrc%5Etfw">August 7, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 


While AI model capabilities continue to grow, the field could benefit from clear presentations that maintain users’ excitement about new capabilities, rather than second-guessing what is presented to them. However, skepticism has followed many recent releases, including those from other major AI labs.

![ChatGPT conversation failing to identify chart error](path-to-img)

OpenAI has been in the spotlight for its lack of transparency and rigor in the evaluations it uses during major launches. For the launch of GPT-4, for example, [OpenAI](https://x.com/cHHillee/status/1635790330854526981) claimed perfect performance on Codeforces tasks released before 2021 and failed each task released afterwards, a [result](https://www.aisnakeoil.com/p/gpt-4-and-professional-benchmarks) of train-test contamination. While OpenAI has disputed these claims and undertaken notable efforts to improve transparency by releasing system cards and publishing a Safety Evaluations Hub, concerns remain over the [lack of transparency](https://arxiv.org/abs/2407.12929) around evaluations. 


Anthropic has also faced similar scrutiny. In November 2024, it released a blog [post](https://www.anthropic.com/research/statistical-approach-to-model-evals) and [paper](https://arxiv.org/abs/2411.00640) on a statistical approach to model evaluations, recommending the use of error bars in charts as a best practice across the industry. Nevertheless, in its recent release of Claude Opus 4.1, the company omitted its own suggestions, attracting online criticism from the community.


<blockquote class="twitter-tweet"><p lang="en" dir="ltr">hey wasn&#39;t this the same company that made a beautiful shiny &quot;research&quot; post about how AI evals should include error bars or something like that. or did they decide the CLT doesn&#39;t apply when it would imply no effect<a href="https://t.co/HXddeYeIyO">https://t.co/HXddeYeIyO</a></p>&mdash; jessica dai (@jessicadai_) <a href="https://twitter.com/jessicadai_/status/1952940745675162114?ref_src=twsrc%5Etfw">August 6, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



Meta, similarly, is another developer that has also encountered [criticism](https://www.interconnects.ai/p/llama-4) after its release of Llama 4 amid [concerns](https://www.zdnet.com/article/metas-llama-4-herd-controversy-and-ai-contamination-explained/) of train-test contamination. While such cases sometimes make for light humor, misleading AI evaluation results have serious implications. In today's hypercompetitive AI landscape, these charts double as research outputs and marketing materials that have the potential to shape AI investment decisions and consumer adoption, thus making rigorous and transparent evaluations more important than ever. 


### The High-Stakes World of AI Evaluations

The pressure to produce compelling evaluation results has never been higher. AI companies now operate in an environment where evaluations serve multiple critical functions:

- **Evaluations as Product Marketing**: In a market where technical differences between frontier models are increasingly subtle, evaluation benchmarks have become the primary means for companies to differentiate their products. A few percentage points gain on a flagship benchmark can result in additional market share. Strong evaluation results often serve as a green light for model releases, with product timelines directly tied to benchmark performance.
- **Investment and Valuation**: Venture capitalists and public markets increasingly rely on evaluation metrics to assess company progress, competitive positioning, and procurement decisions — due in large part to a lack of understanding of the [limitations](https://arxiv.org/abs/2503.05336) of existing automated evaluations. Charts showing eval results are a direct revenue factor.
- **Accelerated Release Timelines**: Companies are rushing to push models to market faster than ever before. According to the [Financial Times](https://www.ft.com/content/8253b66e-ade7-4d1f-993b-2d0779c7e7d8), pre-deployment evaluation periods have [shortened](https://metr.github.io/autonomy-evals-guide/openai-o3-report/) dramatically as companies race to maintain competitive advantage, especially with [increased competition](https://www.interconnects.ai/p/kimi-k2-and-when-deepseek-moments?publication_id=48206&post_id=168259687&isFreemail=true&r=2e&triedRedirect=true) from strong open models released by companies such as Meta, Mistral, DeepSeek, Alibaba, MoonshotAI, and Zhipu AI. Compressed timelines put enormous pressure on evaluation teams to produce results quickly, increasing the risk of lower quality assessments.
- **Heightened Risk Awareness**: Paradoxically, while companies are moving faster, they are also more paranoid about potential risks. [OpenAI](https://openai.com/index/preparing-for-future-ai-capabilities-in-biology/), [Anthropic](https://www-cdn.anthropic.com/07b2a3f9902ee19fe39a36ca638e5ae987bc64dd.pdf), and [Google DeepMind](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2-5-Deep-Think-Model-Card.pdf) have all crossed their internal thresholds for biological risk, triggering additional safety mitigations. At the same time, third-party evaluators are facing additional restrictions, with METR [disclosing](https://metr.github.io/autonomy-evals-guide/gpt-5-report/) in its post on GPT-5 that, for the first time, “OpenAI’s comms and legal team required review and approval of this post” before publication. As governments implement AI regulations such as the EU AI Act, safety evaluation results become important legal defenses to justify launches of increasingly powerful AI systems.


Evaluations must simultaneously serve as marketing materials, release Key Performance Indicators (KPIs), and risk assessment tools—all while being produced (and translated into charts and figures) under intense time pressure.


### Common Chart Mistakes

Even carefully planned evaluation charts can be misleading if they leave out underlying context or data. Within the AI research community, small numerical changes may fall within a statistical margin of error, yet companies face immense pressure to show meaningful progress. This leads to predictable visualization errors:

- **No Acknowledgement of Uncertainty**: Without error bars or other visual cues indicating variability, charts can hide statistical uncertainty and prevent readers from assessing whether improvements are statistically significant or simply noise. For example, error bars are useful for evaluations with repeated experiments and many examples, while other approaches may be appropriate for small or non-independent datasets.
- **Truncated Axes**: Compressed scales exaggerate performance increases, making incremental improvements appear like major breakthroughs which are crucial when trying to justify a new model release.
- **Selective Reporting**: Cherry-picked results that support the narrative without providing counter-examples or failed experiments, often driven by the need to present a compelling product story.
- **Missing Context**: Omits critical details like test set size, variance, methodology changes, or comparison conditions, making replication difficult and hiding potential confounding factors. In many cases evaluation data is not public, so charts are impossible to reproduce. Ideally, details important to interpreting results should at least be included in captions or footnotes.


### Our Road Towards Better Evaluation Results

Issues with charts are just one of the many challenges that the AI evaluation ecosystem faces. At EvalEval, we recognize that fixing AI evaluation documentation means collaboratively creating processes that can serve multiple stakeholders without compromising scientific integrity.


Some of our ongoing [projects](https://evalevalai.com/projects/) to improve AI evaluation include:


- **Evaluation Cards**: Standardized documentation effort that shows eval sources across different categories and how complete the different evaluations are via an easy-to-understand UX.
- **Eval Infrastructure**: Sharing evaluation is key for reproducibility, clarity, and progress. We build a unified, extensible framework for sharing evaluations across diverse tools by pioneering a universal format to share eval logs.
- **Eval Science**: A Best Practices Framework to help define what constitutes a scientifically valid evaluation and how to create one.

The AI community faces a choice: continue allowing business pressures to compromise evaluation integrity, or develop new standards that serve both scientific rigor and legitimate business needs. The stakes are too high: for science, public trust, and ultimately for the technology itself, to accept misleading presentations as the norm. 


We invite the broader community to explore our work and join our mission to establish evaluation practices worthy of the transformative technology we're building. The future of AI depends not just on better models, but on better ways of understanding and communicating what those models can actually do.
