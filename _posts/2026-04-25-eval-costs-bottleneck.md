---
layout: post
title: "AI evals are becoming the new compute bottleneck"
date: 2026-04-25
published: true
category: Research
image: /assets/img/blogs/eval-costs-bottleneck.png
image_contain: true
authors:
  - name: "Avijit Ghosh"
  - name: "Yifan Mai"
  - name: "Georgia Channing"
  - name: "Leshem Choshen"
tags:
  - "AI Evaluation"
  - "Cost"
  - "Benchmarks"
  - "Agents"
  - "Reliability"
  - "Compute"
description: "A field guide to evaluation costs: where the money goes, why old compression tricks break, and why agentic evals, training-in-the-loop benchmarks, and reliability measures are starting to break the bank."
---

<div class="eval-cost-article tex2jax_ignore mathjax_ignore">

<style>
.eval-cost-article {
  --eval-warn: var(--accent);
  --eval-warn-fg: var(--accent-fg);
  --eval-tint: var(--bg-subtle);
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  line-height: 1.66;
  color: var(--fg);
}
.eval-cost-article * { box-sizing: border-box; }
.eval-cost-article p { margin: 0 auto 20px; max-width: 760px; }
.eval-cost-article ul, .eval-cost-article ol { margin: 0 auto 24px; padding-left: 24px; max-width: 760px; }
.eval-cost-article li { margin-bottom: 8px; color: var(--fg); }
.eval-cost-article a {
  color: inherit;
  text-decoration-thickness: .055em;
  text-underline-offset: .17em;
  text-decoration-color: color-mix(in srgb, var(--accent) 55%, transparent);
}
.eval-cost-article a:hover {
  color: var(--accent);
  text-decoration-color: currentColor;
}
.eval-cost-article strong { font-weight: 700; color: var(--fg); }
.eval-cost-article em { color: inherit; }

/* Scoped headings — override .prose defaults */
.eval-cost-article h2 {
  max-width: 760px;
  margin: 72px auto 20px;
  padding-top: 24px;
  padding-bottom: 0;
  border-top: 1px solid var(--border-strong);
  border-bottom: 0;
  font-family: 'Inter', sans-serif;
  font-size: clamp(24px, 3.6vw, 35px);
  line-height: 1.14;
  font-weight: 650;
  letter-spacing: -0.03em;
}
.eval-cost-article h2:first-of-type {
  border-top: 0;
  padding-top: 0;
  margin-top: 8px;
}
.eval-cost-article h3 {
  max-width: 760px;
  margin: 34px auto 8px;
  font-family: 'Inter', sans-serif;
  font-size: 18px;
  line-height: 1.3;
  font-weight: 650;
  letter-spacing: -0.01em;
}

/* BLUF + callout */
.eval-cost-article .bluf {
  max-width: 760px;
  margin: 8px auto 36px;
  padding: 22px 26px 24px;
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-left: 3px solid var(--accent);
  border-radius: 4px;
  font-size: 16.5px;
  line-height: 1.62;
  color: var(--fg);
}
.eval-cost-article .bluf strong {
  display: block;
  margin-bottom: 8px;
  color: var(--accent);
  font-family: 'IBM Plex Mono', monospace;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
}
.eval-cost-article .callout {
  max-width: 760px;
  margin: 30px auto;
  padding: 18px 0 18px 20px;
  border-left: 3px solid var(--accent);
  font-size: 16.5px;
  line-height: 1.6;
}
.eval-cost-article .callout strong {
  color: var(--accent);
  font-family: 'Inter', sans-serif;
}

/* Citation block */
.eval-cost-article .citation-block {
  max-width: 760px;
  margin: 30px auto 12px;
  padding: 0;
}
.eval-cost-article .citation-block .citation-label {
  display: block;
  margin-bottom: 10px;
  color: var(--accent);
  font-family: 'IBM Plex Mono', monospace;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
}
.eval-cost-article .citation-block pre {
  margin: 0;
  padding: 18px 20px;
  background: var(--bg-subtle);
  color: var(--fg);
  border: 1px solid var(--border);
  border-left: 3px solid var(--accent);
  border-radius: 4px;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 12.5px;
  line-height: 1.55;
  overflow-x: auto;
  white-space: pre;
}
.eval-cost-article .citation-block code {
  background: transparent;
  color: inherit;
  padding: 0;
  font-size: inherit;
  font-family: inherit;
}

/* Figures */
.eval-cost-article .figure {
  max-width: 760px;
  width: 100%;
  margin: 46px auto;
  padding: 0;
  border-top: 1px solid var(--border-strong);
  border-bottom: 1px solid var(--border);
  overflow: visible;
  background: transparent;
}
.eval-cost-article .chart-title {
  margin: 16px 0 2px;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  font-weight: 650;
  line-height: 1.35;
  color: var(--fg);
}
.eval-cost-article .chart-subtitle {
  margin: 0 0 18px;
  color: var(--fg-muted);
  font-family: 'Inter', sans-serif;
  font-size: 12px;
  line-height: 1.45;
}
.eval-cost-article .chart-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 18px;
  margin: -6px 0 14px 228px;
  color: var(--fg-muted);
  font-size: 11.5px;
  line-height: 1.35;
}
.eval-cost-article .legend-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.eval-cost-article .legend-swatch {
  width: 18px;
  height: 3px;
  background: var(--fg);
  display: inline-block;
  position: relative;
}
.eval-cost-article .legend-swatch::before,
.eval-cost-article .legend-swatch::after {
  content: "";
  position: absolute;
  top: 50%;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: inherit;
  transform: translateY(-50%);
}
.eval-cost-article .legend-swatch::before { left: -3px; }
.eval-cost-article .legend-swatch::after { right: -3px; }
.eval-cost-article .legend-swatch.red { background: var(--eval-warn); }
.eval-cost-article .legend-swatch.block { width: 18px; height: 8px; }
.eval-cost-article .legend-swatch.block::before,
.eval-cost-article .legend-swatch.block::after { display: none; }
.eval-cost-article .responsive-chart {
  width: 100%;
  font-family: 'Inter', sans-serif;
  font-size: 12px;
}
.eval-cost-article .axis {
  display: grid;
  grid-template-columns: 210px minmax(0, 1fr) 88px;
  column-gap: 18px;
  align-items: end;
  margin: 0 0 8px;
  color: var(--fg-subtle);
}
.eval-cost-article .axis-scale {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  border-bottom: 1px solid var(--border-strong);
  padding-bottom: 4px;
}
.eval-cost-article .axis-scale span {
  text-align: center;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}
.eval-cost-article .axis-label {
  grid-column: 2;
  margin-top: 9px;
  color: var(--fg-muted);
  text-align: center;
  font-size: 11px;
}
.eval-cost-article .chart-row {
  display: grid;
  grid-template-columns: 210px minmax(0, 1fr) 88px;
  column-gap: 18px;
  align-items: center;
  min-height: 34px;
  padding: 4px 0;
}
.eval-cost-article .chart-label {
  color: var(--fg);
  font-weight: 520;
  line-height: 1.22;
  overflow-wrap: anywhere;
}
.eval-cost-article .chart-value {
  color: var(--fg-muted);
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 11.5px;
}
.eval-cost-article .range-track,
.eval-cost-article .bar-track {
  position: relative;
  height: 22px;
  background: repeating-linear-gradient(to right,
    transparent 0,
    transparent calc(20% - 1px),
    var(--border) calc(20% - 1px),
    var(--border) 20%);
}
.eval-cost-article .range-bar {
  position: absolute;
  top: 9px;
  left: var(--min);
  width: calc(var(--max) - var(--min));
  height: 3px;
  background: var(--series, var(--fg));
}
.eval-cost-article .range-bar::before,
.eval-cost-article .range-bar::after {
  content: "";
  position: absolute;
  top: 50%;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--series, var(--fg));
  transform: translateY(-50%);
}
.eval-cost-article .range-bar::before { left: -4px; }
.eval-cost-article .range-bar::after { right: -4px; }
.eval-cost-article .single-bar {
  position: absolute;
  left: 0;
  top: 6px;
  width: var(--max);
  height: 10px;
  background: var(--series, var(--fg));
}
.eval-cost-article .single-bar.thin {
  height: 4px;
  top: 9px;
  min-width: 3px;
  background: var(--eval-warn);
}
.eval-cost-article .figure-caption {
  max-width: 760px;
  margin: 14px auto 0;
  padding: 14px 0 18px;
  border-top: 1px solid var(--border);
  color: var(--fg-muted);
  font-family: 'Inter', sans-serif;
  font-size: 12.5px;
  line-height: 1.55;
}
.eval-cost-article .figure-caption strong { color: var(--fg); }

/* Table */
.eval-cost-article .table-wrap {
  max-width: 760px;
  width: 100%;
  margin: 28px auto 12px;
  overflow-x: auto;
  border-top: 1px solid var(--border-strong);
  border-bottom: 1px solid var(--border-strong);
  -webkit-overflow-scrolling: touch;
}
.eval-cost-article table {
  width: 100%;
  min-width: 820px;
  margin: 0;
  border-collapse: collapse;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  line-height: 1.45;
}
.eval-cost-article th,
.eval-cost-article td {
  padding: 10px 11px;
  text-align: left;
  vertical-align: top;
  border: 0;
  border-bottom: 1px solid var(--border);
  color: var(--fg);
}
.eval-cost-article th {
  background: var(--bg-subtle);
  font-size: 11px;
  font-weight: 650;
  letter-spacing: .05em;
  text-transform: uppercase;
}
.eval-cost-article tbody tr:last-child td { border-bottom: 0; }
.eval-cost-article .table-note {
  max-width: 760px;
  margin: 0 auto 28px;
  color: var(--fg-muted);
  font-family: 'Inter', sans-serif;
  font-size: 12.5px;
  line-height: 1.55;
}

/* Sources / hr */
.eval-cost-article hr {
  border: 0;
  border-top: 1px solid var(--border);
  margin: 46px auto;
  max-width: 760px;
}
.eval-cost-article .sources {
  max-width: 760px;
  margin: 58px auto 0;
  padding: 20px 0 24px;
  border-top: 1px solid var(--border-strong);
  color: var(--fg-muted);
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  line-height: 1.6;
}
.eval-cost-article .sources strong {
  color: var(--fg);
  text-transform: uppercase;
  letter-spacing: .1em;
  font-size: 11px;
}

@media (max-width: 760px) {
  .eval-cost-article { font-size: 16.5px; line-height: 1.68; }
  .eval-cost-article h2 { margin-top: 58px; letter-spacing: -0.025em; }
  .eval-cost-article .figure { margin: 36px auto; }
  .eval-cost-article .chart-title { font-size: 15px; }
  .eval-cost-article .chart-subtitle { margin-bottom: 12px; }
  .eval-cost-article .chart-legend {
    margin: 0 0 12px;
    gap: 8px 14px;
    font-size: 11px;
  }
  .eval-cost-article .axis {
    grid-template-columns: 1fr;
    row-gap: 5px;
    margin: 4px 0 8px;
  }
  .eval-cost-article .axis::before {
    content: "log scale, shown with only major ticks on mobile";
    color: var(--fg-muted);
    font-size: 11px;
  }
  .eval-cost-article .axis-scale {
    display: flex;
    justify-content: space-between;
    gap: 4px;
    border-bottom: 0;
    padding: 0;
    font-size: 10px;
  }
  .eval-cost-article .axis-scale span { text-align: left; white-space: nowrap; }
  .eval-cost-article .axis-scale span:nth-child(even) { display: none; }
  .eval-cost-article .axis-label { grid-column: 1; text-align: left; margin-top: 0; }
  .eval-cost-article .chart-row {
    grid-template-columns: minmax(0, 1fr) auto;
    column-gap: 12px;
    row-gap: 6px;
    padding: 10px 0 12px;
    border-top: 1px solid var(--border);
  }
  .eval-cost-article .chart-label { font-size: 13.5px; overflow-wrap: normal; }
  .eval-cost-article .chart-value { font-size: 11px; white-space: nowrap; text-align: right; }
  .eval-cost-article .range-track,
  .eval-cost-article .bar-track {
    grid-column: 1 / -1;
    height: 20px;
    background: repeating-linear-gradient(to right,
      transparent 0,
      transparent calc(33.333% - 1px),
      var(--border) calc(33.333% - 1px),
      var(--border) 33.333%);
    border: 0;
  }
  .eval-cost-article .range-bar { top: 8px; height: 4px; }
  .eval-cost-article .range-bar::before,
  .eval-cost-article .range-bar::after { width: 7px; height: 7px; }
  .eval-cost-article .single-bar { top: 5px; height: 10px; }
  .eval-cost-article .single-bar.thin { top: 8px; height: 4px; }
  .eval-cost-article table { min-width: 760px; }
}
</style>

<p class="bluf"><strong>Summary.</strong> AI evaluation has crossed a cost threshold that changes who can do it. The Holistic Agent Leaderboard (HAL) recently spent about $40,000 to run 21,730 agent rollouts across 9 models and 9 benchmarks. A single GAIA run on a frontier model can cost $2,829 before caching. Now, just imagine comparing the effects of scaffolds vs. models, in <a href="https://www.exgentic.ai/">Exgentic</a> or scaling agentic steps to millions, like in <a href="https://www.aisi.gov.uk/blog/evidence-for-inference-scaling-in-ai-cyber-tasks-increased-evaluation-budgets-reveal-higher-success-rates">UK-AISI</a>. In scientific ML, The Well costs about 960 H100-hours to evaluate one new architecture and 3,840 H100-hours for a full four-baseline sweep. While compression techniques have been proposed for static benchmarks, new agent benchmarks are noisy, scaffold-sensitive, and only partly compressible. Training-in-the-loop benchmarks are expensive by construction, and when you try to add reliability to these evals, repeated runs further multiply the cost.</p>

<h2 id="making-static-llm-benchmarks-cheaper">Making static LLM benchmarks cheaper</h2>

<p>The cost problem started before agents. When Stanford's CRFM released <a href="https://arxiv.org/abs/2211.09110" rel="noopener noreferrer" target="_blank">HELM</a> in 2022, full-coverage evaluation already required roughly $10,000 or 4,000+ GPU-hours per model. <a href="https://arxiv.org/abs/2308.11696v5" rel="noopener noreferrer" target="_blank">Perlitz et al. (2023)</a> restate that figure, and <a href="https://research.ibm.com/blog/efficient-llm-benchmarking" rel="noopener noreferrer" target="_blank">IBM Research</a> notes that putting Granite-13B through HELM "can consume as many as 1,000 GPU hours." Multiplied across HELM's 30 models and 42 scenarios, the aggregate ran into the high six figures. </p>

<p>The more striking observation came from <a href="https://arxiv.org/abs/2308.11696v5" rel="noopener noreferrer" target="_blank">Perlitz et al.'s analysis</a> of <a href="https://arxiv.org/abs/2304.01373" rel="noopener noreferrer" target="_blank">EleutherAI's Pythia</a> checkpoints, developers pay for evaluation even more. Pythia released 154 checkpoints across 16 model sizes so the community could study training dynamics. Running the LM Evaluation Harness across all those checkpoints turns eval into a multiplier on training: <a href="https://arxiv.org/abs/2308.11696v5" rel="noopener noreferrer" target="_blank">Perlitz et al. (2024)</a> noted that evaluation costs "may even surpass those of pretraining when evaluating checkpoints." For small models, evaluation becomes the dominant compute line item across the whole development cycle. When we scale inference-time compute, we scale evaluation costs.</p>

<p>Perlitz et al. then asked how much of HELM actually carried the rankings. The result was uncomfortable: a 100× to 200× reduction in compute preserved nearly the same ordering, and even a 400× reduction still grouped models into the same coarse tiers. Flash-HELM turned that finding into a coarse-to-fine procedure: run cheap evaluations first, then spend high-resolution compute only on the top candidates. Much of HELM's compute was not discovering new information. It was confirming rankings that the field could have inferred much more cheaply.</p>

<p>Other work reached the same conclusion from different angles. <a href="https://arxiv.org/abs/2402.14992">tinyBenchmarks</a> compressed MMLU from 14,000 items to 100 anchor items at about 2% error using Item Response Theory. The Open LLM Leaderboard collapsed from 29,000 examples to 180. <a href="https://arxiv.org/abs/2309.08638">Anchor Points</a> showed that as few as 1 to 30 examples could rank-order 77 LLMs on GLUE, and <a href="https://arxiv.org/abs/2511.04689">others</a> followed, reducing dataset sizes by 90\%. Static benchmarks had a weakness you could exploit: model differences often concentrate in a small subset of items, so ranking can survive aggressive subsampling.</p>

<p>That trick weakened sharply once benchmarks moved from static predictions to agents.</p>

<h2 id="agent-evals-are-messier">Agent evals are messier</h2>

<p>The cleanest public accounting of agent evaluation comes from the <a href="https://arxiv.org/abs/2510.11977" rel="noopener noreferrer" target="_blank">Holistic Agent Leaderboard</a> (Kapoor et al., ICLR 2026). HAL runs standardized agent harnesses across nine benchmarks covering coding, web navigation, science tasks, and customer service, with shared scaffolds and centralized cost tracking. The headline cost: $40,000 for 21,730 rollouts across 9 models and 9 benchmarks. By April 2026, the leaderboard had grown to 26,597 rollouts. <a href="https://arxiv.org/abs/2603.23749" rel="noopener noreferrer" target="_blank">Ndzomga's independent reproduction</a> arrives at almost the same number: $46,000 across 242 agent runs.</p>

<p>The aggregate number hides the important part: the cost of a single benchmark run varies by four orders of magnitude across HAL tasks, and by three orders within some individual benchmarks.</p>

<figure class="figure" id="agent-cost-spread">
<div class="chart-title">Per-run cost spread on agent benchmarks</div>
<div class="chart-subtitle">USD per one agent configuration on the full benchmark, log scale, HAL April 2026</div>
<div aria-label="Color legend" class="chart-legend">
<span class="legend-item"><span class="legend-swatch"></span>Maximum below $1,000</span>
<span class="legend-item"><span class="legend-swatch red"></span>Maximum at or above $1,000</span>
</div>
<div aria-label="Per-run cost ranges on agent benchmarks from 19 cents to 2829 dollars." class="responsive-chart" role="img">
<div class="axis"><span></span><div class="axis-scale"><span>$0.10</span><span>$1</span><span>$10</span><span>$100</span><span>$1k</span><span>$10k</span></div><span></span><div class="axis-label">Per-run cost (USD, log scale)</div></div>
<div class="chart-row"><div class="chart-label">ScienceAgentBench</div><div class="range-track"><span class="range-bar" style="--min:5.56%;--max:57.33%;"></span></div><div class="chart-value">$0.19–$77</div></div>
<div class="chart-row"><div class="chart-label">TAU-bench Airline</div><div class="range-track"><span class="range-bar" style="--min:9.83%;--max:65.11%;"></span></div><div class="chart-value">$0.31–$180</div></div>
<div class="chart-row"><div class="chart-label">CORE-Bench Hard</div><div class="range-track"><span class="range-bar" style="--min:26.02%;--max:74.15%;"></span></div><div class="chart-value">$2–$510</div></div>
<div class="chart-row"><div class="chart-label">SciCode</div><div class="range-track"><span class="range-bar" style="--min:1.58%;--max:75.92%;"></span></div><div class="chart-value">$0.12–$625</div></div>
<div class="chart-row"><div class="chart-label">SWE-bench Verified Mini</div><div class="range-track"><span class="range-bar" style="--min:32.04%;--max:84.08%;--series:var(--eval-warn);"></span></div><div class="chart-value">$4–$1,600</div></div>
<div class="chart-row"><div class="chart-label">Online Mind2Web</div><div class="range-track"><span class="range-bar" style="--min:33.98%;--max:84.14%;--series:var(--eval-warn);"></span></div><div class="chart-value">$5–$1,610</div></div>
<div class="chart-row"><div class="chart-label">GAIA</div><div class="range-track"><span class="range-bar" style="--min:37.84%;--max:89.03%;--series:var(--eval-warn);"></span></div><div class="chart-value">$7.80–$2,829</div></div>
</div>
<figcaption class="figure-caption"><strong>Figure 1.</strong> Each bar shows the minimum-to-maximum cost across HAL configurations on a single benchmark. Highlighted bars cross the round $1,000-per-run threshold. A "run" is one full agent evaluation across all tasks. Within-benchmark spread reflects the model × scaffold × token-budget product. Source: live HAL leaderboard, April 2026.</figcaption>
</figure>

<p>Behind these numbers is a blunt pricing fact. Claude Opus 4.1 charges $15 per million input tokens and $75 per million output. Gemini 2.0 Flash charges $0.10 and $0.40, a two-order-of-magnitude spread on input alone. Agent benchmarks rarely benchmark "the model" in isolation. They benchmark a model × scaffold × token-budget product, and small scaffold choices can multiply costs 10×.</p>

<p>Worse, higher spend does not reliably buy better results. On <a href="https://hal.cs.princeton.edu/online_mind2web">Online Mind2Web</a>, Browser-Use with Claude Sonnet 4 cost $1,577 for 40% accuracy. SeeAct with GPT-5 Medium hit 42% for $171. The HAL paper notes "a 9× difference in cost despite just a two-percentage-point difference in accuracy." On <a href="https://hal.cs.princeton.edu/gaia">GAIA</a>, an HAL Generalist with o3 Medium cost $2,828 for 28.5% accuracy, while a different agent hit 57.6% for $1,686. <a href="https://arxiv.org/abs/2511.14136">CLEAR</a> finds across 6 SOTA agents on 300 enterprise tasks that "accuracy-optimal configurations cost 4.4 to 10.8× more than Pareto-efficient alternatives" with comparable real-world performance.</p>

<p>The static-era toolkit should have helped, but it has only gone so far. Ndzomga's mid-difficulty filter, which selects tasks with 30 to 70% historical pass rates, achieves a 2× to 3.5× reduction while preserving rank fidelity under scaffold and temporal shifts. That is useful, but it falls far short of the 100× to 200× gains available for static benchmarks. The mechanics explain why: when each item is a multi-turn rollout with its own variance, the expensive object is not the large number of questions. It is the unavoidable long trajectory per single question.</p>

<h2 id="some-evals-are-just-training">Some evals are just training</h2>

<p>Some benchmarks escape the API-cost framing altogether because their evaluation protocol trains models from scratch.</p>

<p><a href="https://arxiv.org/abs/2412.00568" rel="noopener noreferrer" target="_blank">The Well</a> (NeurIPS 2024 D&amp;B) gives the cleanest current example. It bundles 16 scientific machine-learning datasets spanning biological systems, fluid dynamics, magnetohydrodynamics, supernova explosions, viscoelastic instability, and active matter, totaling 15 TB. The protocol leaves little room to economize: train each baseline model for 12 hours on a single H100, try five learning rates per (model, dataset) pair, repeat across four architectures and 16 datasets. The full sweep consumes 3,840 H100-hours, or roughly $7,700 to $11,500 under the conversion assumptions below. A single new architecture still costs about 960 H100-hours.</p>

<p>This is the asymmetry that makes The Well important. Training one neural operator can take a single 12-hour H100 run, while evaluating it across the benchmark requires 80 such trainings. In this corner of ML, evaluation compute exceeds training compute by roughly two orders of magnitude, reversing the old deep-learning mental model.</p>

<p>The same pattern recurs across SciML. <a href="https://arxiv.org/abs/2210.07182" rel="noopener noreferrer" target="_blank">PDEBench</a> covers 11 PDE families with per-submission training in the 50 to 200 GPU-hour range per architecture. <a href="https://arxiv.org/abs/2410.07095" rel="noopener noreferrer" target="_blank">MLE-Bench</a> (OpenAI) sits between agent and training regimes. Each agent attempt at one of 75 Kaggle competitions runs 24 hours on a single A10 GPU, training real ML pipelines. The paper is explicit: "A single run of our main experiment setup of 24 hours per competition attempt requires 24 hours × 75 competitions = 1,800 GPU hours of compute," plus o1-preview consuming 127.5M input and 15M output tokens per seed. Three seeds × six models for a comparison study lands comfortably in six figures.</p>

<p><a href="https://metr.org/AI_R_D_Evaluation_Report.pdf" rel="noopener noreferrer" target="_blank">METR's RE-Bench</a> caps each of seven research engineering environments at 8 hours on 1 to 6 H100s. A single-agent eval across the suite runs about 500 to 600 H100-hours; the human baseline, with 71 expert attempts, raises the implicit budget much further. Because the benchmark gives agents and humans the same wall-clock compute, a real-time training process sets the cost floor. A token budget no longer bounds it from above.</p>

<p><a href="https://arxiv.org/abs/2602.15112" rel="noopener noreferrer" target="_blank">ResearchGym</a> (ICLR 2026) makes the agent run actual ML research. Five test tasks (39 sub-tasks) drawn from ICML, ICLR, ACL, and CVPR orals, with the proposed methods withheld. The agent has to propose hypotheses, train models, and beat the original authors' baselines. The budget is tight: $10 in API plus 12 to 24 hours on a single GPU under 24 GB per task. A full pass (5 tasks × 24h × 3 seeds) consumes about 360 GPU-hours per agent.</p>

<p><a href="https://arxiv.org/abs/2504.01848" rel="noopener noreferrer" target="_blank">PaperBench</a> is where the cost picture turns brutal. Twenty ICML 2024 Spotlight or Oral papers must be replicated from scratch, graded against rubric trees with 8,316 leaf-node criteria. Each rollout uses an A10 GPU for 12 hours. The costs are easy to state and hard to absorb:</p>

<ul>
<li>$400 in API per o1 IterativeAgent rollout, times 20 papers, comes to about $8,000 per evaluation.</li>
<li>Grading runs $66 per paper with the o3-mini judge, or $1,320 for the full benchmark.</li>
<li>Using o1 as judge would push grading to about $830 per paper.</li>
</ul>

<p>PaperBench Code-Dev drops execution on purpose. That choice halves rollout cost to about $4,000 and cuts grading to $10 per paper (85% lower). OpenAI built the variant because many groups cannot afford the full benchmark; the paper says so directly.</p>

<p>The historical precedent is <a href="https://arxiv.org/abs/1902.09635" rel="noopener noreferrer" target="_blank">NAS-Bench-101</a>, whose tabular construction required over 100 TPU-years of training. Without that one-time investment, every NAS algorithm comparison would have cost 1 to 100+ GPU-hours per run, which would have made comparison pricier than the algorithms themselves.</p>

<figure class="figure" id="training-loop-costs">
<div class="chart-title">Cost per single evaluation, training-in-the-loop benchmarks</div>
<div class="chart-subtitle">USD per one model or agent through the full benchmark protocol, log scale</div>
<div aria-label="Color legend" class="chart-legend">
<span class="legend-item"><span class="legend-swatch"></span>Below $5,000</span>
<span class="legend-item"><span class="legend-swatch red"></span>$5,000 or more</span>
</div>
<div aria-label="Training-in-the-loop benchmark costs range from about 540 dollars to 11500 dollars." class="responsive-chart" role="img">
<div class="axis"><span></span><div class="axis-scale"><span>$100</span><span>$500</span><span>$1k</span><span>$5k</span><span>$10k</span><span>$20k</span></div><span></span><div class="axis-label">USD per single evaluation (log scale)</div></div>
<div class="chart-row"><div class="chart-label">ResearchGym (1 seed)</div><div class="range-track"><span class="range-bar" style="--min:31.83%;--max:47.83%;"></span></div><div class="chart-value">$540–$1,260</div></div>
<div class="chart-row"><div class="chart-label">RE-Bench (full agent)</div><div class="range-track"><span class="range-bar" style="--min:46.91%;--max:53.56%;"></span></div><div class="chart-value">$1,200–$1,800</div></div>
<div class="chart-row"><div class="chart-label">The Well (per architecture)</div><div class="range-track"><span class="range-bar" style="--min:54.77%;--max:62.37%;"></span></div><div class="chart-value">$1,920–$2,880</div></div>
<div class="chart-row"><div class="chart-label">MLE-Bench (1 seed)</div><div class="range-track"><span class="range-bar" style="--min:61.15%;--max:63.16%;"></span></div><div class="chart-value">~$2,800</div></div>
<div class="chart-row"><div class="chart-label">PaperBench Code-Dev</div><div class="range-track"><span class="range-bar" style="--min:70.68%;--max:70.68%;"></span></div><div class="chart-value">~$4,200</div></div>
<div class="chart-row"><div class="chart-label">The Well (full sweep)</div><div class="range-track"><span class="range-bar" style="--min:82.01%;--max:89.60%;--series:var(--eval-warn);"></span></div><div class="chart-value">$7,700–$11,500</div></div>
<div class="chart-row"><div class="chart-label">PaperBench (full)</div><div class="range-track"><span class="range-bar" style="--min:85.97%;--max:85.97%;--series:var(--eval-warn);"></span></div><div class="chart-value">~$9,500</div></div>
</div>
<figcaption class="figure-caption"><strong>Figure 2.</strong> All values in USD per single evaluation of one model or agent through the full benchmark protocol. GPU costs converted at $2.50/H100-hr, $1.50/A10-hr; API and grading costs included where applicable. Highlighted bars denote benchmarks costing at least the round $5,000-per-evaluation threshold. The most expensive of these match the most expensive agent benchmarks (Figure 1) but require GPU compute that has no API substitute.</figcaption>
</figure>

<p>These benchmarks have a hard floor because compression changes what they measure. If you shrink them by 200×, you no longer test the original premise. A neural operator cannot demonstrate generalization to a Navier-Stokes regime on 5% of the dataset, because the model has to be retrained. The HELM toolkit does not transfer.</p>

<p>As benchmarks move closer to real work, compression gets harder: static prediction leaves room for large savings, agent rollouts leave less, and in-the-loop training leaves almost none.</p>

<figure class="figure" id="compression-factors">
<div class="chart-title">Compression factors achievable by benchmark type</div>
<div class="chart-subtitle">Maximum reduction in evaluation compute that preserves model-rank fidelity, log scale</div>
<div aria-label="Color legend" class="chart-legend">
<span class="legend-item"><span class="legend-swatch block"></span>Measured compression</span>
<span class="legend-item"><span class="legend-swatch block red"></span>No general compression method</span>
</div>
<div aria-label="Static benchmarks compress by about 100 to 200 times, agent benchmarks by 2 to 3.5 times, and training-in-the-loop benchmarks by about 1 time." class="responsive-chart" role="img">
<div class="axis"><span></span><div class="axis-scale"><span>1×</span><span>10×</span><span>100×</span><span>1k×</span><span>10k×</span><span></span></div><span></span><div class="axis-label">Compression factor (log scale)</div></div>
<div class="chart-row"><div class="chart-label">Static benchmarks</div><div class="bar-track"><span class="single-bar" style="--max:57.53%;"></span></div><div class="chart-value">100–200×</div></div>
<div class="chart-row"><div class="chart-label">Agentic benchmarks</div><div class="bar-track"><span class="single-bar" style="--max:13.60%;"></span></div><div class="chart-value">2–3.5×</div></div>
<div class="chart-row"><div class="chart-label">Training-in-the-loop</div><div class="bar-track"><span class="single-bar thin" style="--max:.8%;"></span></div><div class="chart-value">~1×</div></div>
</div>
<figcaption class="figure-caption"><strong>Figure 3.</strong> The toolkit for compressing evaluation does not transfer as benchmarks become more complex. Solid bars show measured compression ranges. The highlighted bar is not a cost threshold; it flags the ~1× baseline where no general compression method exists. Static benchmarks routinely compress 100–200× without losing rankings. Agent benchmarks compress 2–3.5× at best. Training-in-the-loop benchmarks resist subsampling because the unit being evaluated <em>is</em> the trained model.</figcaption>
</figure>

<h2 id="reliability-is-the-expensive-part">Reliability is the expensive part</h2>

<p>Most of the costs above buy only single-run measurements with limited statistical power. When you measure reliability across repeated runs, static benchmarks, agent benchmarks, and training-in-the-loop benchmarks all become more expensive.</p>

<p>Agent reliability can fall hard when you stop treating one run as evidence. The best-known example comes from Yao et al.'s τ-bench, later reframed in CLEAR (Mehta, 2025): performance can drop from 60% on a single run to 25% under 8-run consistency. <a href="https://arxiv.org/abs/2407.01502" rel="noopener noreferrer" target="_blank">Kapoor et al.'s "AI Agents That Matter"</a> found that simple baseline agents Pareto-dominate complex SOTA agents (Reflexion, LDB, LATS) on HumanEval at 50× lower cost, and that 7 of 10 popular agent benchmarks lacked adequate holdout sets. The HAL paper notes that a "do-nothing" agent passes 38% of τ-bench airline tasks under the original construction. HAL's own log analysis revealed data leakage in the TAU-bench Few Shot scaffold, forcing its removal in December 2025.</p>

<p>The most recent reliability accounting comes from <a href="https://arxiv.org/abs/2602.16666" rel="noopener noreferrer" target="_blank">Rabanser, Kapoor et al.'s "Towards a Science of AI Agent Reliability"</a>, which proposes twelve metrics across consistency, robustness, predictability, and safety. Their finding: "recent capability gains have only yielded small improvements in reliability." HAL's internal analysis shows how much fragility hides behind aggregate accuracy. On SciCode and CORE-Bench, agents almost never completed a run without a tool-calling failure. On AssistantBench and CORE-Bench, environmental errors occurred in roughly 40% of runs. Agents violated explicit benchmark instructions in their final answer over 60% of the time on failed tasks.</p>

<div class="callout">
<strong>The reliability multiplier in practice.</strong> A statistically credible HAL-style evaluation with k = 8 reruns per cell takes the $40K aggregate to roughly $320K. The same multiplier on PaperBench's $9,500-per-run cost pushes a single agent's evaluation past $75K. On The Well, a multi-seed protocol takes the per-architecture cost from ~960 H100-hours to several thousand. Reliability doesn't require new cost categories. It inflates the ones that already exist.
</div>

<p>HAL has paused new model evaluations to focus on reliability, which makes the issue plain: the field's headline numbers still carry too much noise, and reducing that noise costs real money. The figures above are floors, not ceilings, and those floors already exclude many evaluators.</p>

<h2 id="what-this-means-for-ml-as-a-field">What this means for ML as a field</h2>

<p>The data point to three consequences that reinforce one another.</p>

<h3>Eval cost is now an accountability barrier</h3>

<p>Academic groups, AI Safety Institutes, and journalists now hit the budget constraint before the technical one when they try to evaluate frontier agents independently. A single GAIA run can exceed an annual graduate student travel budget. A single PaperBench evaluation, including the LLM judge, runs about $9,500. Three-seed comparisons of six models, the kind of study one might publish, push above $150,000. The established practice of "running a benchmark once and reporting the accuracy number" is no more rigorous than crash-testing one car in perfect weather, but moving past it requires money the academic system does not currently allocate as research compute.</p>

<h3>The compute divide now includes evaluation</h3>

<p><a href="https://www.science.org/doi/10.1126/science.ade2420" rel="noopener noreferrer" target="_blank">Ahmed, Wahed and Thompson (Science 2023)</a> documented that industry models in 2021 were 29× larger than academic ones by parameter count, and that about 70% of AI PhDs went to industry in 2020 versus 21% in 2004. The original "compute divide" story mostly ignored evaluation because evaluation used to look cheap next to training. Many benchmarks have reversed that relationship. A lab that can fine-tune a 7B model can no longer assume it can afford the benchmarks the field takes seriously.</p>

<h3>Cost-blind leaderboards reward waste</h3>

<p>When leaderboards report raw accuracy and omit cost, researchers can rationally pour tokens into a problem until the number ticks up. The HAL paper finds that higher reasoning effort actually reduces accuracy in the majority of runs, which exposes the deeper pathology: extra inference compute does not reliably improve even the metric it is supposed to optimize. Pareto frontiers fix the comparison by ranking accuracy against cost. HAL implements them, but most leaderboards still do not.</p>

<p>If only frontier-lab compute budgets can produce statistically reliable benchmark numbers on the highest-cost agentic and scientific benchmarks, the social process of evaluating AI systems becomes concentrated inside the same labs that build them, rendering external validation partial, and sometimes absent, unless someone subsidizes the cost directly.</p>

<h2 id="cost-summary">Cost summary across benchmark types</h2>

<div aria-label="Cost summary across benchmark types" class="table-wrap" role="region" tabindex="0">
<table>
<thead>
<tr>
<th>Benchmark</th>
<th>Type</th>
<th>USD per single evaluation</th>
<th>What "one evaluation" means</th>
</tr>
</thead>
<tbody>
<tr><td>HELM (per LLM, 2022)</td><td>Static LLM</td><td>~$8,000 – $10,000</td><td>One LLM through full HELM (~4,000 GPU-hrs)</td></tr>
<tr><td>ScienceAgentBench</td><td>Agentic, science</td><td>$0.19 – $77</td><td>One agent config across 102 tasks</td></tr>
<tr><td>TAU-bench Airline</td><td>Agentic</td><td>$0.31 – $180</td><td>One agent across all airline tasks</td></tr>
<tr><td>SciCode</td><td>Agentic, science</td><td>$0.12 – $625</td><td>One agent across 338 sub-problems</td></tr>
<tr><td>CORE-Bench Hard</td><td>Agentic, replication</td><td>$2 – $510</td><td>One agent across 45 papers</td></tr>
<tr><td>SWE-bench Verified Mini</td><td>Agentic, coding</td><td>$4 – $1,600</td><td>One agent across 50 issues</td></tr>
<tr><td>Online Mind2Web</td><td>Agentic, web</td><td>$5 – $1,610</td><td>One agent across 300 web tasks</td></tr>
<tr><td>GAIA</td><td>Agentic, multimodal</td><td>$7.80 – $2,829</td><td>One agent across GAIA tasks</td></tr>
<tr><td>ResearchGym (per seed)</td><td>ML research, training</td><td>$540 – $1,260</td><td>5 tasks × 24h GPU + API</td></tr>
<tr><td>RE-Bench (full agent)</td><td>ML R&amp;D, training</td><td>$1,200 – $1,800</td><td>7 environments × 8h on H100</td></tr>
<tr><td>The Well (per architecture)</td><td>SciML, training</td><td>$1,920 – $2,880</td><td>5 LRs × 16 datasets × 12h H100</td></tr>
<tr><td>MLE-Bench (1 seed)</td><td>ML R&amp;D, training</td><td>~$2,700 – $3,000</td><td>75 Kaggle competitions × 24h on A10</td></tr>
<tr><td>PaperBench Code-Dev</td><td>Scientific, code only</td><td>~$4,200</td><td>One agent across 20 papers, no execution</td></tr>
<tr><td>The Well (full sweep)</td><td>SciML, training</td><td>$7,700 – $11,500</td><td>4 architectures, full protocol</td></tr>
<tr><td>PaperBench (full)</td><td>Scientific</td><td>~$9,500</td><td>One agent across 20 papers, full protocol</td></tr>
<tr><td>HAL aggregate</td><td>9 benchmarks × 9 models</td><td>~$40,000</td><td>All 81 cells, single seed each</td></tr>
</tbody>
</table>
</div>

<p class="table-note">All figures normalized to USD per single evaluation. GPU compute converted at $2.50/H100-hour, $1.50/A10-hour; API and grading costs included where applicable. Pythia ("eval can exceed pretraining"), PDEBench (50–200 GPU-hours per architecture without specified hardware), and NAS-Bench-101's 100 TPU-year construction cost are excluded because they do not normalize cleanly to a per-evaluation USD figure.</p>

<h2 id="stop-paying-twice">Stop paying twice for the same eval</h2>

<p>One reason these numbers stay high is that the field keeps re-running the same evaluations. A frontier lab pays for a HAL sweep, an academic group pays again for a partial reproduction, an audit organization pays a third time for the model versions it cares about, and a journalist pays a fourth to spot-check the leaderboard. Most of those runs cover overlapping models on overlapping benchmarks. Almost none of the underlying instance-level outputs end up in a place where the next team can build on them, because results get reported as a single accuracy number in a PDF, in a model card table, or in a leaderboard entry that hides scaffold, prompt, and seed. The cost figures above are large in part because the field is paying retail every time, on artifacts the rest of the community could not reuse if it wanted to.</p>

<p>Standardized documentation is the cheapest lever available here, and it is the one reliability work needs anyway. If a $9,500 PaperBench rollout exports its full grading trace in a shared schema, the next group studying the same papers can spend its budget on new perturbations instead of repeating the baseline. If a multi-seed HAL run publishes per-trajectory tool-call logs, agent reliability research can answer questions that a single accuracy number cannot. The saving compounds: even a 2× reuse rate on the high-cost benchmarks would put more money back in the ecosystem than every compression technique combined.</p>

<div class="callout">
<strong>Every Eval Ever.</strong> The EvalEval Coalition's <a href="https://evalevalai.com/projects/every-eval-ever/">Every Eval Ever</a> project is the standardized format we use for this. It bundles a metadata schema, validators, and converters from popular harnesses such as <a href="https://github.com/stanford-crfm/helm">HELM</a>, <a href="https://github.com/EleutherAI/lm-evaluation-harness">lm-eval-harness</a>, and <a href="https://inspect.aisi.org.uk/">Inspect AI</a>, so existing eval logs can be transformed into a shared format with one step. The community repository on <a href="https://huggingface.co/datasets/evaleval/EEE_datastore">Hugging Face</a> already hosts results from dozens of contributors, with an open <a href="https://evalevalai.com/events/shared-task-every-eval-ever/">Shared Task</a> for adding more. If you ran one of the costly evaluations in this post, depositing the artifacts in a unified, transparent, verifiable and reproducible manner is the highest-leverage cost-reduction move available to the rest of the field.
</div>

<h2 id="where-this-leaves-us">Where this leaves us</h2>

<p>The economics have changed. Not long ago, training was expensive and evaluation was cheap. For frontier LLMs trained at $50 million to $100 million, evaluation still looks like a rounding error, but that rounding error now costs tens of thousands of dollars per benchmark run and often leaves noisy results behind. For neural operators, ML research agents, and replication benchmarks, the ratio has flipped: a credible evaluation can cost more than training the candidate model.</p>

<p>The field already knows how to make static evaluation cheaper. Flash-HELM, tinyBenchmarks, and Anchor Points work. Agent evaluation has only partial fixes: mid-difficulty filtering helps, and Pareto-front leaderboards help, but the toolkit remains thin. Training-in-the-loop evaluation has no general compression method; tabular precomputation and tight budget caps can reduce cost only by narrowing what the benchmark measures. Reliability adds another layer because repeated runs raise the price of every protocol.</p>

<p>The field still talks as if capability sets the main constraint, but evaluation points to reliability as the tighter one. Governance institutions should want to measure the gap between single-run accuracy and pass^k consistency, yet that gap costs the most to measure. Static-benchmark compression does not transfer to agent or training-in-the-loop benchmarks, and mid-difficulty filtering remains the only credible partial substitute. Cost-blind leaderboards now mislead by design, because they reward extra spending without reporting what that spending bought.</p>

<p>Evaluation now has its own compute budgets, statistical methods, and failure modes. Its price also shapes who gets to evaluate powerful systems in the first place. Whoever can pay for the evaluation gets to write the leaderboard.</p>


<div class="sources">
<strong>Sources:</strong> Perlitz et al. <a href="https://arxiv.org/abs/2308.11696v5" rel="noopener noreferrer" target="_blank">arXiv:2308.11696</a>; Garikaparthi et al. <a href="https://arxiv.org/abs/2602.15112" rel="noopener noreferrer" target="_blank">arXiv:2602.15112</a>; Starace et al. <a href="https://arxiv.org/abs/2504.01848" rel="noopener noreferrer" target="_blank">arXiv:2504.01848</a> (PaperBench); Mehta <a href="https://arxiv.org/abs/2511.14136" rel="noopener noreferrer" target="_blank">arXiv:2511.14136</a> (CLEAR); Ndzomga <a href="https://arxiv.org/abs/2603.23749" rel="noopener noreferrer" target="_blank">arXiv:2603.23749</a>; Kapoor et al. <a href="https://arxiv.org/abs/2510.11977" rel="noopener noreferrer" target="_blank">arXiv:2510.11977</a> (HAL); Tian et al. <a href="https://arxiv.org/abs/2407.13168" rel="noopener noreferrer" target="_blank">arXiv:2407.13168</a> (SciCode); Chen et al. <a href="https://arxiv.org/abs/2410.05080" rel="noopener noreferrer" target="_blank">arXiv:2410.05080</a> (ScienceAgentBench); Siegel et al. <a href="https://arxiv.org/abs/2409.11363" rel="noopener noreferrer" target="_blank">arXiv:2409.11363</a> (CORE-Bench); Chan et al. <a href="https://arxiv.org/abs/2410.07095" rel="noopener noreferrer" target="_blank">arXiv:2410.07095</a> (MLE-Bench); METR <a href="https://arxiv.org/abs/2411.15114" rel="noopener noreferrer" target="_blank">arXiv:2411.15114</a> (RE-Bench); Ohana et al. <a href="https://arxiv.org/abs/2412.00568" rel="noopener noreferrer" target="_blank">arXiv:2412.00568</a> (The Well); Polo et al. <a href="https://arxiv.org/abs/2402.14992" rel="noopener noreferrer" target="_blank">arXiv:2402.14992</a> (tinyBenchmarks); Vivek et al. <a href="https://arxiv.org/abs/2309.08638" rel="noopener noreferrer" target="_blank">arXiv:2309.08638</a> (Anchor Points); Rabanser et al. <a href="https://arxiv.org/abs/2602.16666" rel="noopener noreferrer" target="_blank">arXiv:2602.16666</a>; live HAL leaderboard <a href="https://hal.cs.princeton.edu" rel="noopener noreferrer" target="_blank">hal.cs.princeton.edu</a>.
</div>


<div class="citation-block">
<span class="citation-label">BibTeX Citation</span>
<pre><code>{% raw %}@misc{ghosh2026evalbottleneck,
  author       = {Ghosh, Avijit and Mai, Yifan and Channing, Georgia and Choshen, Leshem},
  title        = {{AI} evals are becoming the new compute bottleneck},
  year         = {2026},
  month        = apr,
  howpublished = {EvalEval Coalition Blog},
  url          = {https://evalevalai.com/research/2026/04/25/eval-costs-bottleneck/}
}{% endraw %}</code></pre>
</div>

</div>
