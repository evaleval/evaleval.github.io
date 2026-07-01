---
layout: post
title: "When AI Benchmarks Stop Measuring Progress"
date: 2026-06-30
published: false
category: # Infrastructure | Research | Organization | Tooling | Documentation | Datasets
image: "https://images.unsplash.com/photo-1677442136019-21780ecad995?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80"
authors:
  - name: Mubashara Akhtar, Jeba Sania, Jocelyn D’Arcy, Leshem Choshen
tags:
  - "Benchmarks"
  - "Evaluation"
description: "Many popular AI benchmarks are losing their ability to separate leading models. Our ICML paper studies this growing problem of benchmark saturation."
---

## When AI Benchmarks Stop Measuring Progress

AI progress is often measured with benchmarks like MMLU, HumanEval, and ARC-AGI. But what happens when the best models score almost the same?

In our ICML paper "[When AI Benchmarks Plateau: A Systematic Study of Benchmark Saturation](https://arxiv.org/pdf/2602.16763)", we study this growing problem: many popular benchmarks are losing their ability to separate between leading models.

### Saturation, When Benchmarks Stop Measuring Progress

Benchmarks are useful when they can tell strong models apart from weaker ones. However, over time, top models start clustering together on benchmarks' leaderboards. A model might score 91%, another 92%, and another 92.3%. **The differences are so small that they may just reflect evaluation noise rather than real capability gains.** This is what we call benchmark saturation.

Saturation is not the same as getting a perfect score. If the benchmark can no longer reliably measure differences between leading models, it stops being a useful measurement - even if plenty of room for improvement remains.

### Measuring Saturation

To understand how widespread this problem is, we analyzed 60 benchmarks covering reasoning, coding, knowledge, multilingual tasks, factuality, and agentic systems.

We also developed an index to measure saturation. Instead of looking only at leaderboard scores, we asked: *Can this benchmark still reliably tell top models apart?* If score differences are smaller than the benchmark's uncertainty, then those differences may not be meaningful.

The result: Nearly **half of the benchmarks we studied already show high levels of saturation**, meaning they have limited ability to distinguish between today's leading models.

### Common Assumptions Don't Hold

We also tested several popular assumptions about what makes benchmarks last longer:

- "Keep the test set private."
- "Use open-ended generation instead of multiple-choice questions."
- "Evaluate models in many languages."

Surprisingly, none of these factors showed a strong relationship with benchmark saturation once benchmark age was taken into account.

*What seemed to matter more?* If benchmarks are measurement tools, they need maintenance. Based on our findings, benchmark creators should consider:

- Larger and more diverse evaluation sets
- Dynamic benchmark updates
- Adversarial data collection
- Uncertainty-aware reporting
- Explicit criteria for benchmark revision or retirement

### Saturation Isn't Always Bad

If models genuinely master a capability, a saturated benchmark may be evidence of real progress - BUT the challenge is figuring out whether a benchmark is saturated because:

- Models have solved the task, or
- The benchmark has stopped measuring meaningful differences.

**As models continue to improve, telling these two apart will become increasingly important.**

### Explore our Work

- Paper: [https://arxiv.org/pdf/2602.16763](https://arxiv.org/pdf/2602.16763)
- Code & dataset: [https://github.com/evaleval/benchmark-saturation](https://github.com/evaleval/benchmark-saturation)
