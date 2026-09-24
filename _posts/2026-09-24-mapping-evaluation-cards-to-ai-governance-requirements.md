---
layout: post
title: "Mapping Every Eval Ever to Emerging AI Governance Requirements in California, the EU, and the UK"
date: 2026-09-24
published: true
wide: true
title_spaced: true
category: Infrastructure
image: "/assets/img/blogs/eee-governance-crosswalk-banner.webp"
authors:
  - name: "Avijit Ghosh"
  - name: "David Manheim"
  - name: "Andrew Tran"
  - name: "Wm. Matthew Kennedy"
  - name: "Irene Solaiman"
tags:
  - "infrastructure"
  - "evaluation reporting"
  - "AI governance"
  - "independent evaluation"
description: "We broke AI governance requirements from California, the EU and the UK into the evidence they ask for, and mapped each piece against Every Eval Ever and related open documentation schemas."
---

<div class="governance-post" markdown="1">

<style>
.governance-post .crosswalk-figure {
  margin: 2.5rem 0;
  border: 1px solid var(--border);
  border-radius: 4px;
  background: var(--bg);
  overflow: hidden;
}

.governance-post .crosswalk-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0.5rem 0.75rem;
  border-bottom: 1px solid var(--border);
  background: var(--bg-subtle);
}

.governance-post .crosswalk-label {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.68rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--fg-muted);
}

.governance-post .crosswalk-actions {
  display: flex;
  gap: 0.5rem;
  flex-shrink: 0;
}

.governance-post .crosswalk-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.3rem 0.7rem;
  border: 1px solid var(--border-strong);
  border-radius: 9999px;
  background: var(--bg);
  color: var(--fg) !important;
  font-size: 0.78rem;
  font-weight: 500;
  line-height: 1.4;
  text-decoration: none !important;
  cursor: pointer;
}

.governance-post .crosswalk-btn:hover {
  border-color: var(--accent);
  color: var(--accent) !important;
}

.governance-post .crosswalk-figure iframe {
  display: block;
  width: 100%;
  /* Replaced with the embed's content height once it loads */
  height: 1400px;
  border: 0;
  background: var(--bg);
}

.governance-post .crosswalk-figure figcaption {
  padding: 0.6rem 0.75rem;
  border-top: 1px solid var(--border);
  font-size: 0.85rem;
  color: var(--fg-muted);
}

@media (max-width: 640px) {
  .governance-post .crosswalk-label { display: none; }
  .governance-post .crosswalk-toolbar { justify-content: flex-end; }
}
/* References, styled after the costs post's Sources block */
.governance-post .sources {
  margin: 58px 0 0;
  padding: 20px 0 24px;
  border-top: 1px solid var(--border-strong);
  color: var(--fg-muted);
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  line-height: 1.6;
}
.governance-post .sources strong {
  color: var(--fg);
  text-transform: uppercase;
  letter-spacing: .1em;
  font-size: 11px;
}
.governance-post .source-list {
  list-style: decimal;
  margin: 14px 0 0;
  padding-left: 26px;
  max-width: none;
  font-size: 12.5px;
  line-height: 1.55;
}
.governance-post .source-list li {
  margin-bottom: 5px;
  padding-left: 2px;
  break-inside: avoid;
}
.governance-post .source-list li::marker {
  color: var(--fg-subtle);
  font-variant-numeric: tabular-nums;
}
.governance-post .source-list cite {
  font-style: italic;
  color: var(--fg);
}
</style>

In recent days, there has been renewed interest in what independent assessment of AI systems should look like in practice.

## A push for independent assessment

On September 18, California Governor Gavin Newsom [issued an executive order](https://www.gov.ca.gov/2026/09/18/governor-newsom-issues-executive-order-to-accelerate-independent-oversight-and-advance-the-creation-of-an-ai-kill-switch/) accelerating the state's work on independent AI oversight. Among other things, the order asks state agencies to develop recommendations around embedding independent verification organizations inside frontier AI companies to conduct regular audits and evaluations, independently verifying safety frameworks and risk assessments, and maintaining independent verification of emergency shutdown mechanisms. California has also recently created frameworks for [independent verification organizations](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB813) and a [registry for AI auditors](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB1405).

This builds on a broader shift toward technical evaluation and assurance around the world. The UK's AI Safety Institute has been [conducting independent evaluations of advanced AI systems](https://www.gov.uk/government/publications/ai-safety-institute-approach-to-evaluations/ai-safety-institute-approach-to-evaluations) since 2023. In the EU, the AI Act [requires providers of general-purpose AI models with systemic risk](https://artificialintelligenceact.eu/article/55/) to conduct and document state-of-the-art model evaluations, including adversarial testing, while the [GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) provides more detailed guidance on evaluation and risk assessment. Similar efforts elsewhere, such as Singapore's [AI Verify](https://aiverifyfoundation.sg/what-is-ai-verify/), are also pushing toward more structured approaches to testing, documentation, and independent scrutiny.

## The evidence question

Across these approaches, a practical implementation question keeps coming up: **once an evaluation is conducted, how should its evidence be recorded and communicated?**

Policymakers need to know what was tested and how. Evaluators need enough methodological detail to interpret or reproduce results. Developers increasingly face requests for similar evidence in different formats. Shared reporting conventions can make that evidence easier to reuse across research, assurance, and governance processes.

## Mapping requirements to Every Eval Ever

This is where our work at EvalEval fits into a **broader open evaluation ecosystem**. Through [Every Eval Ever](https://github.com/evaleval/every_eval_ever) and the wider [Evaluation Cards](/projects/eval-cards/) ecosystem, we are working on shared, open infrastructure for documenting evaluation results in ways that make them easier to find, compare, reproduce, and reuse.

We wanted to understand how far that existing infrastructure could already support emerging governance requirements.

So we broke requirements from California, the EU, and the UK into the individual pieces of evidence that would need to be recorded, then mapped those pieces against EEE and related documentation schemas.

## What the mapping found

For the **60 pieces of evidence across 40 requirements whose natural home is evaluation or benchmark reporting**, EEE can already represent **56 of 60**. Fifty-one are captured through dedicated, typed fields. Adding [AutoBenchmarkCards](https://arxiv.org/abs/2512.09577) makes two additional pieces structured at the benchmark level.

The remaining gaps are useful because they point to places where evaluation reporting can get better. They include representing evaluations that do not fit neatly into per-sample records, such as human-uplift studies; comparing results with and without mitigations; documenting random sample-selection methods; and recording why particular trajectories or additional samples were selected.

## Where other standards fit

Other governance requirements naturally sit elsewhere in the open evaluation ecosystem. Questions about evaluator independence, conflicts of interest, access arrangements, credentials, and regulator-facing processes belong in standards focused on evaluators themselves. [AEF-1](https://aievaluatorforum.org/), for example, focuses on operating conditions for independent third-party evaluators. Model-level information has a natural home in [model cards](https://arxiv.org/abs/1810.03993), while incident and flaw reporting is being developed through efforts such as [FLARE-AI](https://arxiv.org/abs/2606.31567).

Seen together, these efforts suggest an ecosystem of complementary open standards. Evaluator standards can describe who is qualified to perform an assessment. Model cards can document the system being assessed. Evaluation reporting standards can record what was tested, how it was tested, and what happened. Incident-reporting standards can capture failures that emerge after deployment.

The more these pieces can work together, the more useful the underlying evidence becomes. Evaluators can produce records in a common form, developers can reuse them across reporting contexts, researchers can compare evaluations across organizations, and policymakers can draw on existing structured evidence when designing new governance mechanisms.

## Explore the crosswalk

**The interactive visualization below shows our current crosswalk.** It shows which pieces of governance evidence an [Evaluation Card](https://arxiv.org/abs/2606.09809) can hold, with each field color-coded by where it comes from: *reported* fields that evaluators fill in and submit through Every Eval Ever, and *auto-pulled* benchmark metadata that Evaluation Cards brings in from AutoBenchmarkCards. What a reporter controls is what they submit through EEE. Open it in a new tab for the most room, and hover any band for the source text and field definitions.

<figure class="crosswalk-figure" id="crosswalk">
  <div class="crosswalk-toolbar">
    <span class="crosswalk-label">Governance evidence crosswalk</span>
    <div class="crosswalk-actions">
      <a class="crosswalk-btn" href="{{ '/assets/embeds/governance-evidence-crosswalk.html' | relative_url }}" target="_blank" rel="noopener">
        <i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i> Open in new tab
      </a>
    </div>
  </div>
  <iframe
    src="{{ '/assets/embeds/governance-evidence-crosswalk.html' | relative_url }}"
    title="Interactive Sankey diagram mapping governance evidence to evaluation schema fields"
    loading="lazy"></iframe>
  <figcaption>Each band links one piece of required evidence to an Evaluation Card field that could record it: blue for fields the evaluator reports through Every Eval Ever, violet for benchmark metadata pulled in from AutoBenchmarkCards. Hover a band or node for the source quote, field definition and mapping rationale; click to pin.</figcaption>
</figure>

This is a living analysis, and we expect the schema to keep evolving as governance requirements become more concrete. The gaps surfaced here give us a useful roadmap for improving EEE, while the broader crosswalk helps clarify how evaluation reporting can contribute to a larger open ecosystem for independent AI assessment.


<div class="sources">
<strong>References</strong>
<ol class="source-list">
<li>Mitchell et al. (2019). <cite>Model Cards for Model Reporting</cite>. <a href="https://arxiv.org/abs/1810.03993" rel="noopener noreferrer" target="_blank">arXiv:1810.03993</a>.</li>
<li>UK AI Safety Institute (2024). <cite>AI Safety Institute approach to evaluations</cite>. <a href="https://www.gov.uk/government/publications/ai-safety-institute-approach-to-evaluations/ai-safety-institute-approach-to-evaluations" rel="noopener noreferrer" target="_blank">gov.uk</a>.</li>
<li>European Union (2024). <cite>Regulation (EU) 2024/1689 (Artificial Intelligence Act)</cite>. <a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj" rel="noopener noreferrer" target="_blank">eur-lex.europa.eu</a>; <a href="https://artificialintelligenceact.eu/article/55/" rel="noopener noreferrer" target="_blank">Article 55</a>.</li>
<li>European Commission (2025). <cite>The General-Purpose AI Code of Practice</cite>. <a href="https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai" rel="noopener noreferrer" target="_blank">digital-strategy.ec.europa.eu</a>.</li>
<li>Hofmann et al. (2025). <cite>Auto-BenchmarkCard: Automated Synthesis of Benchmark Documentation</cite>. <a href="https://arxiv.org/abs/2512.09577" rel="noopener noreferrer" target="_blank">arXiv:2512.09577</a>.</li>
<li>Batzner et al. (2026). <cite>Every Eval Ever: A Unifying Schema and Community Repository for AI Evaluation Results</cite>. <a href="https://arxiv.org/abs/2606.14516" rel="noopener noreferrer" target="_blank">arXiv:2606.14516</a>; <a href="https://github.com/evaleval/every_eval_ever" rel="noopener noreferrer" target="_blank">GitHub</a>.</li>
<li>California Legislature (2026). <cite>AB 1405: Artificial intelligence: auditors: registration</cite>. <a href="https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB1405" rel="noopener noreferrer" target="_blank">leginfo.legislature.ca.gov</a>.</li>
<li>California Legislature (2026). <cite>SB 813: Independent verification organizations</cite>. <a href="https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB813" rel="noopener noreferrer" target="_blank">leginfo.legislature.ca.gov</a>.</li>
<li>Ghosh et al. (2026). <cite>Evaluation Cards: An Interpretive Layer for AI Evaluation Reporting</cite>. <a href="https://arxiv.org/abs/2606.09809" rel="noopener noreferrer" target="_blank">arXiv:2606.09809</a>.</li>
<li>Governor of California (2026). <cite>Governor Newsom issues executive order to accelerate independent oversight and advance the creation of an AI kill switch</cite>. <a href="https://www.gov.ca.gov/2026/09/18/governor-newsom-issues-executive-order-to-accelerate-independent-oversight-and-advance-the-creation-of-an-ai-kill-switch/" rel="noopener noreferrer" target="_blank">gov.ca.gov</a>.</li>
<li>Longpre et al. (2026). <cite>FLARE-AI: Flaw Reporting for AI</cite>. <a href="https://arxiv.org/abs/2606.31567" rel="noopener noreferrer" target="_blank">arXiv:2606.31567</a>.</li>
<li>AI Evaluator Forum (live). <cite>AEF-1: Minimum Operating Conditions for Independent Third-Party AI Evaluations</cite>. <a href="https://aievaluatorforum.org/initiatives/minimum-operating-conditions" rel="noopener noreferrer" target="_blank">aievaluatorforum.org</a>.</li>
<li>AI Verify Foundation (live). <cite>What is AI Verify?</cite>. <a href="https://aiverifyfoundation.sg/what-is-ai-verify/" rel="noopener noreferrer" target="_blank">aiverifyfoundation.sg</a>.</li>
</ol>
</div>

</div>

<script>
(function () {
  var frame = document.querySelector('#crosswalk iframe');
  if (!frame) return;

  // Same-origin embed, so size the frame to its content instead of guessing a height
  function fit() {
    try {
      var doc = frame.contentDocument;
      if (doc && doc.body) frame.style.height = doc.documentElement.scrollHeight + 'px';
    } catch (e) {}
  }

  frame.addEventListener('load', function () {
    fit();
    try { new ResizeObserver(fit).observe(frame.contentDocument.body); } catch (e) {}
  });
})();
</script>
