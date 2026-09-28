---
layout: post
title: "Mapping Evaluation Cards to Emerging AI Governance Requirements in California, the EU, and the UK"
date: 2026-09-28
published: true
wide: true
title_spaced: true
category: Infrastructure
image: "/assets/img/blogs/eee-governance-crosswalk-banner.webp"
authors:
  - name: "Avijit Ghosh"
  - name: "David Manheim"
  - name: "Andrew Tran"
  - name: "Sree Harsha Nelaturu"
  - name: "Jessica Ji"
  - name: "Jan Batzner"
  - name: "Wm. Matthew Kennedy"
  - name: "Usman Gohar"
  - name: "Anka Reuel"
  - name: "Irene Solaiman"
tags:
  - "infrastructure"
  - "evaluation reporting"
  - "ai governance"
  - "independent evaluation"
description: "We analyzed prominent policy and regulatory frameworks for evaluation reporting and determined that Evaluation Cards can not only meet required information disclosure needs but also serve as a shared standard for developers to communicate with policymakers."
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

## A push for independent assessment

On September 18, California Governor Gavin Newsom [issued an executive order](https://www.gov.ca.gov/2026/09/18/governor-newsom-issues-executive-order-to-accelerate-independent-oversight-and-advance-the-creation-of-an-ai-kill-switch/) accelerating the state's work on independent AI oversight. Among other things, the order asks state agencies to develop recommendations for embedding independent verification organizations within frontier AI companies to conduct regular audits and evaluations, verify safety frameworks and risk assessments, and maintain independent verification of emergency shutdown mechanisms. California has also recently created frameworks for independent verification organizations ([SB 813](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB813)) and a registry for AI auditors ([AB 1405](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB1405)).

This builds on a broader shift toward technical evaluation and assurance around the world. The UK's AI Security Institute (AISI) has been [conducting independent evaluations of advanced AI systems](https://www.gov.uk/government/publications/ai-safety-institute-approach-to-evaluations/ai-safety-institute-approach-to-evaluations) since 2023, including pre- and post-deployment assessments of potentially harmful capabilities, and Parliament's Joint Committee on Human Rights (JCHR) recently called for new statutory safeguards against the human rights risks posed by AI in its report on [Human Rights and the Regulation of AI](https://publications.parliament.uk/pa/jt5902/jtselect/jtrights/160/report.html). In the EU, the [AI Act](https://artificialintelligenceact.eu/article/55/) requires providers of general-purpose AI models that pose systemic risk to conduct and document state-of-the-art model evaluations, including adversarial testing, while the [GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) further develops expectations for pre-deployment evaluation, post-market monitoring, and external evaluations. The European AI Office is also developing independence and qualification requirements for external evaluators of systemic-risk GPAI models. Similar efforts elsewhere, such as Singapore's [AI Verify](https://aiverifyfoundation.sg/what-is-ai-verify/), are pushing toward more structured approaches to testing, documentation, and independent scrutiny.

## The evidence question

Across these approaches, a practical implementation question keeps coming up: **once an evaluation is conducted, how should its evidence be recorded and communicated?**

Policymakers need to know what was tested and how. Evaluators and auditors need enough methodological detail, including completed metadata, to interpret or reproduce results. Developers increasingly face requests for similar evidence in different formats. Shared reporting conventions can streamline that evidence across research, assurance, and governance processes.

Shared reporting can also reduce the burden on oversight bodies. When providers report evaluation evidence in different formats and at varying levels of detail, regulators have to spend additional time locating, interpreting, and comparing the information they need. Standardized, structured reporting can make that process easier and also enable more reliable automated parsing and analysis of evaluation evidence.

Such a common baseline can also support other governance processes. In California, for example, the state will need to evaluate and compare prospective Independent Verification Organizations as it develops its designation regime. SB 813 requires applicants to provide information about the benchmarks, technologies, metrics, and methodologies they propose using, and directs the state to develop the regime with attention to consistency, comparability, and avoiding duplicative requirements where practicable. A common format for describing evaluation evidence could make that information easier to assess across applicants and over time.

## Mapping requirements to Evaluation Cards

This is where our work at EvalEval fits into a **broader open evaluation ecosystem**. Through [Every Eval Ever](https://github.com/evaleval/every_eval_ever) and the wider [Evaluation Cards](/projects/eval-cards/) effort, we are working on shared, open infrastructure for documenting evaluation results in ways that make them easier to find, compare, analyze, reproduce, and reuse.

We are currently working with public-sector evaluators to put this infrastructure into practice. In our [collaboration with the UK AI Security Institute](/infrastructure/2026/09/22/uk-aisi-evaleval-reproducible-benchmark-results/), AISI is making publicly reported evaluation methods and findings available through Evaluation Cards where appropriate, including verified results, context, and configuration information. Feedback from AISI has also helped shape the Every Eval Ever (EEE) schema itself. This gives us a concrete example of how open reporting infrastructure can support independent evaluation: results produced by an evaluator can be published in a shared structure and compared with evidence from the wider ecosystem.

To understand how far this infrastructure could support emerging governance requirements, we reviewed **40 requirements across the California ([AB 1405](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB1405), [SB 813](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB813)), EU ([AI Act](https://artificialintelligenceact.eu/article/55/), [GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)), and UK ([JCHR report](https://publications.parliament.uk/pa/jt5902/jtselect/jtrights/160/report.html)) instruments in our crosswalk and broke each requirement into the discrete pieces of evidence needed to satisfy it. This produced 281 evidence elements in total.**

We then classified each element according to its **unit of record**. We treated an element as evaluation-reporting evidence when it primarily describes an evaluation run, its methodology, configuration, benchmark, results, or the conditions under which it was conducted. We classify this as information that can reasonably be attached to an evaluation record. Evidence about an evaluator's institutional independence or qualifications, a model as a whole, an incident, organizational governance, or a regulatory process was instead assigned to the corresponding evaluator-, model-, incident-, organization-, or regulator-level record. On this basis, **60 of the 281 elements fall within the scope of evaluation reporting**, while the remaining 221 belong in other kinds of records.

For each of those 60 elements, we then asked whether EEE or AutoBenchmarkCards contains a field whose unit and meaning match the required evidence, and whether that information can be represented in a structured field, in free text only, or not at all. **Evaluation Cards unifies evaluator-reported information from EEE with benchmark metadata automatically supplied by AutoBenchmarkCards, as shown in the [visualization](#crosswalk).**[^aef]

## What the mapping found

Of the **60 evidence elements in scope for evaluation reporting, EEE can already represent 56**. Fifty-one are captured through dedicated, typed fields; another five can currently be recorded through free-text fields supplied by the evaluator or other reporter.

For example, requirements in the EU's General-Purpose AI (GPAI) Code of Practice to document an evaluation's tooling and resource constraints map onto existing EEE fields for tools available during an evaluation and token limits, while requirements to record whether an evaluation was conducted internally or by an external evaluator map to `source_metadata.evaluator_relationship`.

Evaluation Cards can combine those submissions with benchmark-level information automatically pulled from [AutoBenchmarkCards](https://arxiv.org/abs/2512.09577). In our crosswalk, AutoBenchmarkCards turns two of the five elements that EEE captures only in free text (benchmark data type and benchmark languages) into structured metadata. This increases the number represented through structured fields from **51 to 53**.

## Where other standards fit

Our research on evaluation reporting standards is one part of the broader push towards independent assessment. Questions about evaluator independence, conflicts of interest, access arrangements, credentials, and regulator-facing processes belong in standards focused on evaluators themselves. [AEF-1](https://aievaluatorforum.org/initiatives/minimum-operating-conditions), for example, addresses operating conditions for independent third-party evaluators. Model-level information has a natural home in [model cards](https://arxiv.org/abs/1810.03993), while incident and flaw reporting is being developed through efforts such as [FLARE-AI](https://arxiv.org/abs/2606.31567).

These efforts can work as complementary layers: evaluator standards establish expectations for who performs an assessment and under what conditions; model cards document the system being assessed; evaluation reporting standards record what was tested, how, and with what results; and incident-reporting standards capture failures that emerge after deployment. Making those layers interoperable can allow the same underlying evidence to travel more easily between evaluators, developers, researchers, and oversight bodies without asking each actor to reinvent its documentation from scratch.

## Explore the map

**The interactive visualization below presents our current mapping.** It shows which pieces of governance evidence an [Evaluation Card](https://arxiv.org/abs/2606.09809) can address, with each field color-coded by where it comes from: *reported* fields that evaluators fill in and submit through Every Eval Ever, and *auto-pulled* benchmark metadata that Evaluation Cards brings in from AutoBenchmarkCards. What a reporter controls is what they submit through EEE. Open it in a new tab for the most room, and hover over any band for the source text and field definitions.

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
  <figcaption>Each band links one piece of required evidence to an Evaluation Card field that could record it: blue for fields the evaluator reports through Every Eval Ever, violet for benchmark metadata pulled in from AutoBenchmarkCards. Hover a band or node for the source quote, field definition, and mapping rationale; click to pin.</figcaption>
</figure>

Evaluation Cards are designed to be living documents that grow with multi-stakeholder input over time. We therefore believe that the relationship between governance requirements and evaluation infrastructure should be bidirectional: new policy requirements can help identify where Evaluation Cards need to become more expressive, while existing schemas can give policymakers a concrete, machine-readable way to specify and compare the evaluation evidence they are asking for. Our mapping shows that the same reporting infrastructure can already support a substantial share of the evaluation-specific evidence appearing across California, the EU, and the UK, while making clear where complementary standards or new fields are still needed. We hope regulators, evaluators, developers, and researchers will use the crosswalk as a practical reference and share feedback from real-world use so that Evaluation Cards can continue to evolve alongside emerging governance requirements.

[^aef]: AEF-1 appears separately as an optional overlay because it primarily describes the evaluator rather than the evaluation itself, although some of its requirements overlap with evaluation-reporting evidence.

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
<li>EvalEval Coalition &amp; UK AI Security Institute (2026). <cite>How UK AISI and EvalEval Are Making Benchmark Results Reproducible</cite>. <a href="/infrastructure/2026/09/22/uk-aisi-evaleval-reproducible-benchmark-results/">evalevalai.com</a>.</li>
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
