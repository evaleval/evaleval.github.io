---
layout: post
title: "Field Notes: Challenges in GenAI Evaluation Science"
date: 2026-03-25
published: true
category: Research
image: "/assets/img/blogs/field-notes-interview.svg"
authors:
  - name: "Robert Scholz"
  - name: "Chad Atalla"
  - name: "Prajna Soni"
  - name: "Leon Staufer"
  - name: "Agathe Balayn"
  - name: "Vilém Zouhar"
  - name: "Namrata Mukhija"
  - name: "Tahsin Mayeesha"
  - name: "Patricia Paskov"
  - name: "Subho Majumdar"
  - name: "the EvalEval Coalition"
tags:
  - "Evaluation Science"
  - "AI Evaluation"
  - "LLMs"
  - "Validity"
  - "Interpretability"
  - "Benchmarking"
description: "Early themes from expert interviews on the challenges of evaluating generative AI systems, spanning validity, practicality, and interpretability."
---

Our [initial post launching the Science of Evaluations workstream]({{ site.baseurl }}{% post_url 2025-07-13-eval-science-kickoff %}) outlined a research agenda to document the scientific foundations of generative AI (GenAI) evaluation through systematic reviews, sociotechnical analysis, and gap identification.

Since the launch, we have conducted an extensive literature review and semi-structured interviews with experts across the field to gain insights into prevailing approaches, methodological assumptions, and persistent challenges in evaluation practices. In this post, we provide an update on where that work stands today, share early themes emerging from our analysis, and highlight where additional input would be most valuable as the workstream moves forward.

We use 'evaluation' broadly to refer to the methods used to gather and interpret evidence about a GenAI system[^1] regarding its performance, capabilities, propensities, and direct impacts. These include methods such as benchmarking, targeted in-context evaluations, system monitoring, automated red‑teaming, and human uplift studies. While GenAI evaluation can span many modalities, this post focuses on text-centered systems.

To date, we have conducted **15 semi-structured interviews** (approximately 30 minutes each) with practitioners across leading AI labs, academia, government-linked institutions (including AI safety institutes), and evaluation-focused startups and non-profits. Their work spans development of evaluations, creation of policy, application of evaluations to models and products, and interpretation of evaluations for design and deployment decision making. Interviewees were selected in roughly equal proportions across each type of organization based on recent publications and snowball sampling, focusing on those actively shaping evaluation practice in the large language model (LLM) ecosystem. The interviews probed into methodologies, conceptual and statistical challenges, operational constraints, and gaps in the field of AI evaluations.

Here we draw on the first eight fully annotated interviews. Our findings center on three key themes: **validity**, **practicality**, and **interpretability**. The open questions and challenges within these themes can serve as a useful guide for researchers, policymakers, auditors, and engineers in the AI evaluation community, shaping future research directions and informing how decision-makers interpret and act on evaluation results. We discuss each of the themes in turn below.

---

## Validity

Validity emerged as a central challenge in interviews about the GenAI evaluation space and is receiving increasing attention across the community.[^2] Broadly, validity refers to the extent to which a measurement meaningfully captures the construct/behavior it claims to measure.

Interviewees highlighted challenges across multiple aspects of validity, namely **construct validity** (whether the concept of interest is clearly specified and theoretically grounded), **content validity** (whether test items and scoring criteria appropriately reflect the construct), and **ecological validity** (whether test items capture real-world usage[^3]).

Across interviews, a clear message emerged: evaluation results can only be trusted if they are grounded in a precise specification (systematization) of the concept of interest. Terms like "bias" and "quality" are often used loosely, and this ambiguity trickles down to the measurement instruments on which evaluations depend. As a result, it is difficult to determine what evaluation results actually mean with respect to the concept of interest.

As interviewees put it:

> "We can have **50 different benchmarks** that all talk about measuring bias, but **none of them say exactly what bias is** \[...\] I have no way of knowing which one to trust because they haven't specified precisely what concept they were trying to capture." (P1)

> "Words mean different things to different people. We have to make sure that when we say we're measuring misinformation, **we are tightly defined.** \[...\] We call that context specification." (P2)

The consequences extend to the test items themselves, where misalignment between test items and the target construct can undermine an entire benchmark:

> "A lot of benchmarks have stuff that is kind of nonsense, and oftentimes **not even particularly related to what the benchmark is trying to measure.** So, for example, in \[a popular benchmark professedly testing hazardous biosecurity knowledge\], there are some history questions about facts about American and Soviet bio weapons programs in the seventies" (P3)

Interviewees also expressed dataset-related concerns associated with ecological validity. Prior to deployment, developers may lack access to relevant real-world usage data. Even after deployment, this data may not be accessible due to privacy considerations or may be unusable due to a low signal-to-noise ratio for rare concepts of interest. This prompts developers to turn to synthetic data, which comes with its own set of challenges:

> "We use a lot of synthetic \[data.\] Basically, the pipeline is a rejection sampling pipeline where you have one model generate and another model filter \[...\] Often, what we found is that **the first thing \[language models\] generate looks almost correct**, and then if you look at it for longer \[...\] it makes you realize, this is not optimal." (P4)

> "We still really struggle with **ecological validity of synthetic data.** \[...\] But, using real data is also not ideal because, if you're looking for some rare phenomenon, the signal-to-noise ratio is going to be really low in real sample data. So synthetic is important for us to get a stronger signal." (P1)

Even when the concept of interest is well-defined and the dataset is carefully constructed, evaluations can quickly lose relevance as usage shifts. Users may interact with a model differently as it becomes more capable, and developers may change how models are integrated into products. Such distributional shifts can quietly violate the assumptions underlying evaluation datasets.

> "**The distribution is changing very quickly**… how a consumer uses a certain product that has AI with an old AI model might be very different from how they use the same product." (P5)

---

## Practicality

Interviewees emphasized that evaluation design is also shaped by real operational constraints (e.g., budgets, timelines, privacy), citing engineering and compute costs as key blockers, which influence how concepts of interest are prioritized.

> "There are, you know, a lot of risks \[...\] we have \[an\] internal repository where we're tracking risks, and it's a lot. **We don't have evaluations for all those risks.** Especially if we're trying to make it easier for \[our\] teams, we have to build these evaluations in the central platform in a central way, and that is \[...\] quite resource-intensive to do that." (P6)

> "It's a balancing step \[...\] **is performing that evaluation actually worth it** with respect to the burdens and the benefits?" (P7)

Even when compute resources are not a problem, many GenAI evaluation tasks examine complex sociotechnical concepts that require substantial expertise to annotate and validate accurately. Accessing such expertise at large scales requires infrastructure and costs that developers may be unwilling to pay, favoring instead LLM-based judges.

> "**We never use human judges.** … It just doesn't scale like you would have to set up a pipeline, and then the humans don't have time. It's a coordination issue." (P4)

More capable systems introduce further challenges. As new models and agentic systems emerge, evaluations become harder and more costly. Agent environments increase complexity, variance, and expense:

> "As the models get more capable, **it is harder and harder work to get good evals** \[...\] They are deployed as agents and environments \[…\] that have greater complexity: Firstly, the variance in their performance is much much greater. There's a lot more randomness in their interaction with the environment. And secondly, the cost goes up." (P5)

---

## Interpretability and Reporting

Interviewees also highlighted challenges in interpreting the evidence underlying evaluative claims. As benchmarks grow larger and more complex, translating results into relevant analyses for a variety of decision makers is becoming harder and more tooling-dependent (e.g., AI agents take 100s of steps to solve a single long horizon task, intermingling tool calls with reasoning tokens, making it hard for a single person to process them without access to tooling), furthering practicality issues.

As evaluation benchmarks grow in size, individual human review becomes impractical:

> "Increasingly, as the benchmarks get bigger and more complicated, it's **harder to have this intuitive feel for the data.** You're more reliant on external tooling and systems to sanity check things than you were in the past." (P5)

> "**Humans are just not capable of inspecting 10,000 runs** through an environment. And so we need a lot of AI assistance to understand what is going on." (P5)

More broadly, interviewees noted that stronger grounding in basic statistical practice could improve rigor and the reliability of resulting claims:

> "There are **massive, very common, huge statistical issues** in the way that people go about doing their evaluations, whether it's not including error bars, whether it's conflating statistical significance with effect size, whether it's just interpreting statistics sometimes." (P3)

Ultimately, evaluation results are intended to inform decisions about AI models and systems in the real world. It remains a major challenge to build evaluations that stakeholders can trust at decision time:

> "We know that the stakeholders who are using our evaluations to make decisions really want to be able to interpret them objectively. If they see that we conducted an evaluation and the output was a 3% failure rate, they want to know **how that translates to what we expect for real users in the real world**, does that mean that 3% of users on a day-to-day basis will experience harmful outputs?" (P1)

By synthesizing these challenges and open questions alongside emerging best practices and recommendations, we aim to help address them within the Science of Evaluations and broader evaluation practice space.

---

## What's Next?

This work is ongoing; we continue to analyze additional interviews and advance our literature review, synthesizing insights across AI and adjacent fields to learn established methodologies and identify where important gaps remain. We are also expanding our stakeholder interviews to ensure that the priorities we identify reflect the perspectives of researchers, practitioners, policymakers, and auditors across industries and geographies.

As we enter the next phase of the Science of Evaluations workstream, we welcome input from those developing or applying evaluation methods for generative AI and large language models (LLMs). This includes teams at labs engaged with development and evaluation of models, alongside academics, civil society, and industry practitioners. Responses will be reported only in anonymized, aggregated form, as in the current post.

If you are interested in contributing, suggesting interviewees, or sharing relevant work, we invite you to reach out at [core@evalevalai.com](mailto:core@evalevalai.com). We see this effort as collaborative and ecosystem-wide, and we welcome participation as we continue to build the scientific foundations for AI evaluation.

[^1]: For the purposes of this post, we adopt a broad, simplified interpretation of 'evaluation.' We recognize that in rigorous practice, measurement and evaluation are not synonymous (the distinction is concisely described in [*Measurement to Meaning*](https://arxiv.org/pdf/2505.10573)).
[^2]: Quite a few studies have recently raised the issue of validity, e.g. [*Measuring what Matters*](https://openreview.net/pdf?id=mdA5lVvNcU), [*Evaluating Generative AI Systems Is a Social Science Measurement Challenge*](https://arxiv.org/pdf/2502.00561), [*Toward an evaluation science for generative AI systems*](https://arxiv.org/pdf/2503.05336), [*Understanding and Meeting Practitioner Needs*](https://aclanthology.org/2025.findings-acl.947/), [*Stereotyping Norwegian Salmon*](https://aclanthology.org/2021.acl-long.81/).
[^3]: The concept of [ecological validity](https://en.wikipedia.org/wiki/Ecological_validity) was originally conceived in a different context and may carry additional nuance beyond our usage here.
