---
layout: post
title: "The Hidden Social Costs of AI"
date: 2025-11-12
published: true
category: Research 
image: 
authors:
  - name: "Abdul Hameed"
  - name: "Afifah Kashif"
  - name: "Andrew Tran"
  - name: "Usman Gohar"
tags:
  - "AI Evaluation"
  - "LLMs"
  - "Social Impact"
description: "As AI continues to grow more powerful, who carries the hidden social costs of its effects?"
---

As AI continues to grow more powerful, who carries the hidden social costs of its effects?

While still far from reaching universal adoption, many organizations post 'release reports' alongside new AI models. However, many reports typically focus on detailing the technical capabilities of models and often overlook, or in some cases, completely omitting any social impact risks evaluation.

Our paper, *[Who Evaluates AI’s Social Impacts? Mapping Coverage And Gaps In First And Third Party Evaluations](https://arxiv.org/abs/2511.05613)*, argues for more transparent and consistent reporting standards that document and put greater emphasis on social impact issues.

In our study, we analyze 186 first-party reports released at the time of an AI model’s release, 183 post-release reports, and incorporate developer interviews to understand the incentives behind model reporting. Release reports were analyzed based on seven social impact dimensions: Bias and Harm, Sensitive Content, Performance Disparity, Environmental Costs and Emissions, Privacy and Data, Financial Costs, and Moderation Labor ([Solaiman et. al. 2023](https://arxiv.org/abs/2306.05949v1)). 

Our findings showed that there was a significant gap between release-time and post-release reports of social impact in AI evaluations.

Using a scale ranging from 0--3, we quantify how well the reports provided details of each social impact dimension. First-party release-time reports averaged just 0.72 out of 3, compared to 2.62 for post-release reports. Additionally, we found that certain categories, such as environmental cost and emission, have decreased substantially since late 2023. Our developer interviews gave us further insight into why this was happening. As one developer put it:

> **"The environment has become a touchy subject, and companies don’t want to make themselves look bad, so they just don’t report anything."**

## Differences in Industry and Academia

In general, our findings show that companies such as Meta, Google, Anthropic, and more provided strong evaluations for their earlier models (e.g., Llama 1 and Llama 2), but fell short on scoring for recent releases.

In recent years, both academic and independent organizations have produced more rigorous evaluations across the social impact categories than their industry counterparts. However, these groups face intrinsic limitations due to limited access to internal data. In general, academic and independent organizations lack access to “internal data” such as compute metrics or data center location. This gap in information leads to reports that lack thorough social impact information.

## Efforts to Close the Gap

This project, led by the Evaluating Evaluations (EvalEval) Coalition, highlights a growing discrepancy: as AI’s popularity increases, the transparency needed for governance is shrinking. Fixing this requires standardized reporting frameworks, shared tools, and safety policies that make safe reporting both accessible and possible.

## Explore Our Work

* [Paper](https://arxiv.org/abs/2511.05613)
* [Dataset](https://huggingface.co/datasets/evaleval/social_impact_eval_annotations)
* [Code](https://github.com/evaleval/social_impact_eval_annotations_code)
