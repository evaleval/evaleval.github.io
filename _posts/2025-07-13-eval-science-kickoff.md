---
layout: post
title: "The Science of Evaluations: Workstream Kickoff Post"
date: 2025-07-13
category: Research
published: true
image: "https://images.unsplash.com/photo-1677442136019-21780ecad995?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80"
authors:
  - name: "Subho Majumdar"
    url: "https://shubhobm.github.io/"
  - name: "Patricia Paskov"
    url: "https://www.prpaskov.com/"
tags:
  - "Evaluation Science"
  - "Metrics"
  - "Validity"
description: "Exploring novel approaches to evaluating large language models beyond traditional metrics, with focus on robustness, alignment, and real-world performance."
---

Rigorous evaluations provide decision makers with detailed information about the capabilities, risks, and opportunities of AI systems. At their best, evaluations enhance understanding of the AI systems[^1] and, in turn, increase the window of opportunity for societal preparedness and resilience for an increasingly AI-oriented world[^2]. 

Current evaluations, however, lack robustness, reliability, and validity. Robustness refers to the stability of evaluation results against minor perturbations in input data or evaluation conditions—a critical distinction in AI contexts where small input changes can dramatically affect outputs. Reliability concerns consistent measurement across different evaluation runs. Validity spans multiple dimensions: claim validity (whether conclusions drawn from evaluation performance are justified and appropriate), construct validity (whether evaluations actually measure claimed capabilities), content validity (whether evaluations comprehensively cover all relevant aspects of capabilities being assessed), and external validity (whether results generalize beyond specific evaluation conditions to real-world applications). 

Many researchers and practitioners in the evaluation ecosystem have accordingly called for more rigorous evaluations that address these measurement challenges, guided by commonly understood best practices in adjacent and analogous fields (see [References](https://docs.google.com/document/d/1ZZ24pDwJ92_lpLyH0ev1pfrJfINZIzR4r0zkJFk2iNI/edit?tab=t.0#bookmark=id.cfeiyg1xcell)). As part of the EvalEval Coalition, we are coming together as a group of researchers and practitioners to set the conceptual foundations for a scientific approach to evaluations on which subsequent technical projects can build. In this effort, we will:

1. **Assess the current state of evaluation science.** We will systematically review published research and preprints on the science of evaluations. This assessment will include scoping reviews, meta-analyses, and critiques[^3] of current approaches. We plan to do this assessment through a sociotechnical lens—with focus on (a) open and reproducible scientific methods to implement evaluations of AI systems, and (b)  governance mechanisms for independent third-party audits, such as red teaming, certification frameworks, data access protocols, and disclosure standards.
2. **Identify critical gaps and priorities in evaluations science.** Through literature synthesis and stakeholder interviews with a diverse group of researchers, practitioners, and policymakers, we will map open research questions, missing methodological tools, under-addressed areas of capabilities and risks, and validity-related challenges in existing evaluations.

Design and execute research to tackle a prioritized subset of these gaps where our coalition has relevant expertise.

In carrying out this work we will aim to bridge the gap between rigorous best practices and pragmatic implementation details, producing impactful research and tools that improve the AI evaluation ecosystem. If you’d like to join us, join the slack community!

---

[^1]: “AI models can be thought of as the raw, mathematical essence that is often the ‘engine’ of AI applications. An AI system is a combination of several components, including one or more AI models, that is designed to be particularly useful to humans in some way.” ([Bengio et al. 2025](https://www.gov.uk/government/publications/international-ai-safety-report-2025/international-ai-safety-report-2025))

[^2]: For example, AI evaluations form the foundation of major GPAI providers’ [frontier AI safety policies](https://metr.org/faisc), a core [EU AI Act mandate](https://artificialintelligenceact.eu/article/55/) for frontier model providers, and one of [three key functions](https://www.gov.uk/government/publications/ai-safety-institute-approach-to-evaluations/ai-safety-institute-approach-to-evaluations) for the UK AI Safety Institute.

[^3]: See, for example, the [The Leaderboard Illusion](https://arxiv.org/abs/2504.20879).
