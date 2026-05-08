---
layout: event
title: 2026 ACL Workshop on Evaluating Evaluations (EvalEval)
subtitle: Examining Best Practices for Utilizing and Developing Generative Model Evaluations
team: Mubashara Akhtar, Jan Batzner, Leshem Choshen, Avijit Ghosh, Usman Gohar, Jennifer Mickel, Ichhya Pant, Zeerak Talat
status: active
order: 1
category: Organization
event_date: 2026-7-04
location: Room Harbor A
host: EvalEval
description:  |
  This workshop focuses on AI evaluation in practice, centering the tensions and collaborations between model developers and evaluation researchers and aims to surface practical insights from across the evaluation ecosystem.
---

## 📖 Background 
As Generative AI systems are increasingly integrated into real-world products and decision-making pipelines, evaluation has become a central yet challenging component of responsible AI development.[^1] While evaluation research has advanced rapidly, gaps persist between research and practice: model developers often prioritize scalability and integration into development workflows, while evaluation researchers emphasize rigor, validity, and sociotechnical considerations. [The EvalEval coalition's multi author effort](https://arxiv.org/abs/2511.05613) mapping first- and third-party social impact evaluations shows a clear division of labor, where developers underreport or deprioritize key impacts such as environmental costs, data provenance, and labor practices, while third-party evaluators provide broader but necessarily incomplete coverage, leaving critical gaps in accountability and comparability.[^2]

This workshop focuses on AI evaluation in practice, centering the tensions and collaborations between model developers and evaluation researchers. Through a call for papers on contemporary challenges spanning methodological rigor, sociotechnical perspectives, scalability, community-informed evaluation, and real-world use alongside invited panels, the workshop aims to surface practical insights from across the evaluation ecosystem. The workshop will also host a [shared task for building a unifying, standardized database of LLM Evaluations](https://evalevalai.com/events/shared-task-every-eval-ever/), encouraging shared infrastructure and actionable evaluation practices.

## 📝 Topics

Themes for submission include, but are not limited to:

### 1. Evaluation Methodology and Measurement Theory

* **Conceptualization**: Operationalization and construct definition issues in evaluations of generative AI;
* **Validity**: Construct, convergent, and discriminant validity of existing evaluations;
* **Reliability**: Robustness, consistency, and generalizability of evaluation methods;
* **Metrics**: Design, selection, and limitations of evaluation metrics, benchmarks, and scoring methods;
* **Reproducibility**: Cross-model and cross-context reproducibility, standardization, and aggregation of evaluation results.

### 2. Evaluation Infrastructure, Cost, and Stakeholders

* **Infrastructure**: Evaluation harnesses, tooling, platforms, and scalability of evaluation setups;[^3]
* **Financial costs**: Monetary costs of evaluations and documentation frameworks for tracking them;
* **Documentation**: Transparency and reporting standards for evaluation processes and their limitations;
* **Stakeholders**: Who evaluates, the relationship between evaluators and system developers, and the role of independent and third-party audits.

### 3. Evaluating Sociotechnical Impacts

State of sociotechnical evaluations of generative AI systems, drawing on categories such as those in the [EvalEval social impact taxonomy](https://zeerak.org/papers/Evaluating_the_Social_Impact_of_Generative_AI_Systems_in_Systems_and_Society__preprint_.pdf):<sup><a href="#fn:1">1</a></sup>

* **Bias, stereotypes, and representational harms**: Evaluations of stereotypes, disparate performance, inequality, marginalization, and community erasure;
* **Cultural values and sensitive content**: Evaluations of linguistic diversity, sensitive content, trustworthiness, overreliance on outputs, and imposing norms and values;
* **Privacy and data protection**: Evaluations of memorization, data leakage, contextual integrity, and personal privacy and sense of self;
* **Labor and creativity**: Evaluations of data and content moderation labor, intellectual property, ownership, and labor market impacts;
* **Ecosystem and environment**: Evaluations of environmental costs, carbon emissions, and widening resource gaps.

## 🗓️ Schedule

### 👋 2:00 PM – 2:05 PM | Welcome and Introduction *(5 mins)*
**Jennifer Mickel**, EvalEval Workshop Co-Chair

---

### 🎙️ 2:05 PM – 2:45 PM | Panel Presentation *(30 mins panel + 10 mins Q&A)*
**Moderator:** Leshem Chosen, MIT CSAIL

This panel brings together model developers and evaluation researchers to examine how evaluations are designed, interpreted, and used in real-world model development. We will surface key tensions carefully balancing between speed vs. rigor, benchmarks vs. deployment needs, and generality vs. task-specificity while highlighting points of productive collaboration. The discussion aims to bridge perspectives from both communities and identify concrete pathways for more aligned, impactful evaluation practices in NLP.

**👥 Panelists:**
- [Angelina Wang](https://angelina-wang.github.io/), Cornell Tech
- [Michal Shmueli-Scheuer](https://research.ibm.com/people/michal-shmueli-scheuer), IBM
- [Sebastian Gehrman](https://sebastiangehrmann.github.io/), Bloomberg

---

### ☕ 2:45 PM – 2:50 PM | BREAK *(5 mins)*

---

### 🗣️ 2:50 PM – 3:50 PM | Six Oral Presentations *(60 mins)*
**Moderator:** Usman Gohar, Iowa State University

📄 [Rigorous Interpretation Is a Form of Evaluation](https://openreview.net/forum?id=5DPXnrt8vU&referrer=%5BProgram%20Chair%20Console%5D(%2Fgroup%3Fid%3Daclweb.org%2FACL%2F2026%2FWorkshop%2FEvalEval%2FProgram_Chairs%23submission-status))
[Isabelle Lee](https://openreview.net/profile?id=~Isabelle_Lee1), [Emmy Liu](https://openreview.net/profile?id=~Emmy_Liu1), [Cathy Jiao](https://openreview.net/profile?id=~Cathy_Jiao1), [Brihi Joshi](https://openreview.net/profile?id=~Brihi_Joshi1), [Dani Yogatama](https://openreview.net/profile?id=~Dani_Yogatama2), [Fazl Barez](https://openreview.net/profile?id=~Fazl_Barez1), [Michael Saxon](https://openreview.net/profile?id=~Michael_Saxon1)

📄 [Graduating the Benchmark Scale: Lessons from Thermometry](https://openreview.net/forum?id=EJSwPvVTpm&referrer=%5BProgram%20Chair%20Console%5D(%2Fgroup%3Fid%3Daclweb.org%2FACL%2F2026%2FWorkshop%2FEvalEval%2FProgram_Chairs%23submission-status))
[Sean Trott](https://openreview.net/profile?id=~Sean_Trott1), [Oisín Parkinson-Coombs](https://openreview.net/profile?id=~Ois%C3%ADn_Parkinson-Coombs1)

📄 [One Persona, Many Cues, Different Results: How Sociodemographic Cues Impact LLM Personalization](https://openreview.net/forum?id=oKiZ4EgUa5&referrer=%5BProgram%20Chair%20Console%5D(%2Fgroup%3Fid%3Daclweb.org%2FACL%2F2026%2FWorkshop%2FEvalEval%2FProgram_Chairs%23submission-status))
[Franziska Weeber](https://openreview.net/profile?id=~Franziska_Weeber1), [Vera Neplenbroek](https://openreview.net/profile?id=~Vera_Neplenbroek1), [Jan Batzner](https://openreview.net/profile?id=~Jan_Batzner1), [Sebastian Padó](https://openreview.net/profile?id=~Sebastian_Pad%C3%B32)

📄 [Becoming Experienced Judges: Selective Test-Time Learning for Evaluators](https://openreview.net/forum?id=Jxa0lJWZ5b&referrer=%5BProgram%20Chair%20Console%5D(%2Fgroup%3Fid%3Daclweb.org%2FACL%2F2026%2FWorkshop%2FEvalEval%2FProgram_Chairs%23submission-status))
[Seungyeon Jwa](https://openreview.net/profile?id=~Seungyeon_Jwa1), [Daechul Ahn](https://openreview.net/profile?id=~Daechul_Ahn4), [Reokyoung Kim](https://openreview.net/profile?id=~Reokyoung_Kim1), [Dongyeop Kang](https://openreview.net/profile?id=~Dongyeop_Kang2), [Jonghyun Choi](https://openreview.net/profile?id=~Jonghyun_Choi1)

📄 [LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://openreview.net/forum?id=g6sqdWLzV0&referrer=%5BProgram%20Chair%20Console%5D(%2Fgroup%3Fid%3Daclweb.org%2FACL%2F2026%2FWorkshop%2FEvalEval%2FProgram_Chairs%23submission-status))
[Lukas Helff](https://openreview.net/profile?id=~Lukas_Helff1), [Quentin Delfosse](https://openreview.net/profile?id=~Quentin_Delfosse1), [David Steinmann](https://openreview.net/profile?id=~David_Steinmann1), [Ruben Härle](https://openreview.net/profile?id=~Ruben_H%C3%A4rle1), [Hikaru Shindo](https://openreview.net/profile?id=~Hikaru_Shindo1), [Patrick Schramowski](https://openreview.net/profile?id=~Patrick_Schramowski1), [Wolfgang Stammer](https://openreview.net/profile?id=~Wolfgang_Stammer1), [Kristian Kersting](https://openreview.net/profile?id=~Kristian_Kersting1), [Felix Friedrich](https://openreview.net/profile?id=~Felix_Friedrich1)

📄 [Community-Centered Measurement of Cultural Content in AI Images](https://openreview.net/forum?id=GwJ6ypeh66&referrer=%5BProgram%20Chair%20Console%5D(%2Fgroup%3Fid%3Daclweb.org%2FACL%2F2026%2FWorkshop%2FEvalEval%2FProgram_Chairs%23submission-status))
[Nari Johnson](https://openreview.net/profile?id=~Nari_Johnson1), [Deepthi Sudharsan](https://openreview.net/profile?id=~Deepthi_Sudharsan1), [Hamna](https://openreview.net/profile?id=~Hamna1), [Samantha Dalal](https://openreview.net/profile?id=~Samantha_Dalal1), [Theo Holroyd](https://openreview.net/profile?id=~Theo_Holroyd1), [Anja Thieme](https://openreview.net/profile?id=~Anja_Thieme1), [Hoda Heidari](https://openreview.net/profile?id=~Hoda_Heidari2), [Daniela Massiceti](https://openreview.net/profile?id=~Daniela_Massiceti1), [Jennifer Wortman Vaughan](https://openreview.net/profile?id=~Jennifer_Wortman_Vaughan1), [Cecily Morrison](https://openreview.net/profile?id=~Cecily_Morrison1)

---

### 🪧 3:50 PM – 4:20 PM | Poster Presentations *(60 mins)*
**Moderator:** Usman Gohar, University of Iowa

---

### ☕ 4:20 PM – 4:25 PM | BREAK *(5 mins)*

---

### 🔬 4:25 PM – 5:15 PM | Shared Task *(50 mins)*
**Moderator:** Jan Batzner, Technical University Munich

As the cost of genAI model evaluation is rapidly increasing, researchers, non-profits, small companies, and civil society orgs need to rely on existing evaluation data on the web. Evaluation data refers to Large Language Model evaluations on popular benchmarks or domain-specific tasks, which are commonly saved under Hugging Face leaderboards or reported in research papers. However, with numerous evaluation frameworks emerging across research and industry, evaluation data is scattered across different platforms, stored in inconsistent formats, and lacks standardization that would enable meaningful comparison and meta-analysis.

The [Every Eval Ever](https://github.com/evaleval/every_eval_ever) Shared Task aims to address this fragmentation by establishing a unified metadata schema for LLM evaluations to populate a comprehensive, standardized database of evaluation results. Qualifying contributors will be invited to join the paper write-up as co-authors. 🖊️

---

### 🏆 5:15 PM – 5:25 PM | EvalEval Community Awards *(10 mins)*
**Moderator:** Leshem Chosen, MIT CSAIL & IBM Research

---

### 🎤 5:25 PM – 5:30 PM | Closing Remarks *(5 mins)*
**Ichhya Pant**, EvalEval Workshop Co-Chair

## 📄 Submission Guidelines
We welcome the following types of submissions:

**Paper lengths:**
- 📑 **Full papers**: 6–8 pages (excluding references and supplementary material)
- 📝 **Short papers**: Up to 4 pages (excluding references and supplementary material)
- 📋 **Tiny papers**: Up to 2 pages (excluding references and supplementary material), e.g. extended abstracts.

**Submission types:**
- 🔬 **Research papers** presenting original empirical or theoretical results
- 💡 **Positions & Provocations** that introduce novel perspectives or challenge conventional wisdom around broader social impact evaluation for generative AI

All submission types are welcome at any length tier. Accepted papers will be presented as posters, with a subset selected for spotlight oral presentation. All papers will be assessed based on their relevance to the workshop themes.

Papers should be submitted in the [conference-provided format](https://github.com/acl-org/acl-style-files). The review process will be two-way anonymized; therefore, all identifying information must be removed from submissions.

## 📚 Publication
Submissions may include **unpublished** work as well as **previously published or accepted** papers, provided they do not violate dual-submission policies. Therefore, e.g., ACL 2026 Findings and Main papers, as well as ARR papers can be submitted. 

Submissions are **non-archival** by default, but upon acceptance authors may opt in to **archival** publication. All accepted paper titles will be made publicly available.

## 📅 Important Dates 
- **Submission Deadline**: March 19th, 2026 ~~March 12th, 2026~~
- **Notification of Acceptance**: April 28, 2026
- **Camera-ready paper due**: May 14, 2026
- **Workshop at ACL in San Diego**: July 3-4, 2026 

All deadlines are specified in Anywhere on Earth (AoE).


## 🚀 Submission Site 
All submissions to may be [made via OpenReview](https://openreview.net/group?id=aclweb.org/ACL/2026/Workshop/EvalEval).


## 🔍 Reviewer Recruitment
To support a fair, high-quality, and sustainable review process, we adopt a reciprocal reviewer recruitment expectation. Authors submitting papers to the workshop will be expected to serve as reviewers, helping ensure sufficient reviewing capacity and timely feedback for all submissions. This expectation must be clearly indicated during paper submission through the OpenReview system.

## 🧑‍🔬 Program Chairs 
- Mubashara Akhtar, ETH Zurich & ETH AI Center
- Jan Batzner, Weizenbaum Institute, Technical University Munich
- Leshem Choshen, MIT, IBM Research, MIT-IBM Watson AI Lab
- Avijit Ghosh, Hugging Face
- Usman Gohar, Iowa State University
- Jennifer Mickel, Eleuther AI 
- Ichhya Pant, Independent 
- Zeerak Talat, University of Edinburgh


## 🏛️ Organizers 
[EvalEval Coalition](/about/)


## 📬 Workshop Contact 
- Ichhya Pant: [ipant@gwu.edu](mailto:ipant@gwu.edu)
- Jennifer Mickel: [jamickel@utexas.edu](mailto:jamickel@utexas.edu)
- Jan Batzner: [jan.batzner@weizenbaum-institut.de](mailto:jan.batzner@weizenbaum-institut.de)


## ❓ FAQ
**I'm waiting for my ARR decision — can I still submit to EvalEval?**
Yes! If your paper is later accepted at ACL, you would simply choose our non-archival option.

**Can I also submit in the ICML format?**
No, please use the [ARR formatting](https://github.com/acl-org/acl-style-files).

**Can I attend this workshop online?**
The workshop is in-person at ACL 2026 in San Diego. At least one author of each accepted paper must present on-site.

**My position paper is 6 pages. Does that work?**
Yes, all submission types (research and positions/provocations) are welcome at any of the three length tiers.

**What makes a good position paper?**
We had great success with positions at our last NeurIPS workshop! For instance, [Cintaqia et al. (2025):](https://neurips.cc/virtual/2025/loc/san-diego/poster/121948) *Stop the Nonconsensual Use of Nude Images in Research* — first presented at EvalEval, then a full NeurIPS position! Congratulations!


[^1]: Solaiman, Talat et al. (2025). "Evaluating the Social Impact of Generative AI Systems in Systems and Society." In *The Oxford Handbook of the Foundations and Regulation of Generative AI*.
[^2]: Reuel, Ghosh, Chim et al. (2025). "Who Evaluates AI's Social Impacts? Mapping Coverage and Gaps in First and Third Party Evaluations." Preprint.
[^3]: [ACL Shared Task](https://evalevalai.com/events/shared-task-every-eval-ever/)