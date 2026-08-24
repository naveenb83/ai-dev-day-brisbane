---
tags:
  - L400
  - governance
---

# Responsible AI <span class="lvl lvl-400">L400</span>

## In plain terms

**Responsible AI** is making sure your AI is not just *capable* but *acceptable* —
fair, transparent, accountable and respectful of people. It's partly ethics,
partly risk management, and increasingly partly law. The practical question:
*"If this decision affected me, or made the news, would we be comfortable?"*

## How it works — the pillars

**Fairness & bias.** Models learn from human data, so they can inherit and amplify
its biases — treating groups differently in ways that are unfair or illegal
(hiring, lending, healthcare are high-stakes). You **test for disparate outcomes**
across groups, not just overall accuracy.

**Transparency & explainability.** People affected by an AI decision deserve to
know AI was involved and, ideally, *why* it decided as it did. For LLMs, showing
**sources/citations** and the **reasoning or the query run** (as Genie does) is a
practical form of transparency.

**Accountability & human oversight.** A human is responsible for outcomes — not
"the algorithm". Consequential decisions keep a **human in the loop** with real
authority to override.

**Privacy.** Respect what data you use and how — consent, minimisation, and
protection of personal information (ties into [Governance](governance.md) and
[Security](security.md)).

**Reliability & honesty.** The system should perform as claimed and be honest about
uncertainty rather than confidently wrong (back to
[why AI gets things wrong](../foundations/why-ai-gets-things-wrong.md)).

**Societal & environmental impact.** Consider downstream effects — on jobs, on
misinformation, and the energy/compute cost of large models.

!!! note "Regulation is arriving"
    Frameworks like the **EU AI Act**, the **NIST AI Risk Management Framework**,
    ISO/IEC standards and various national guidelines increasingly set
    expectations — especially for "high-risk" uses. You don't need to be a lawyer,
    but you should know these exist and involve the right people early. *(Specifics
    change; confirm current obligations for your jurisdiction and use case.)*

## How Databricks does it

Responsible AI is mostly a *practice*, supported by platform capabilities:

- **Unity Catalog** provides the governance backbone — access control, **lineage**
  (where data and models came from) and **audit** (who did what) — which underpins
  accountability and privacy.
- **MLflow** evaluation lets you test for quality *and* run fairness/safety checks,
  and tracing gives explainability into individual decisions.
- **Genie** and RAG surfacing **sources and generated SQL** support transparency.
- Data **masking** and permissions help meet privacy obligations.

## Pitfalls

!!! warning "Where good intentions fail"
    - **Only measuring average accuracy** hides unfair outcomes for subgroups.
    - **"The model decided"** as a shield — accountability stays with people.
    - **Bolting it on at the end** — bake fairness, transparency and oversight in
      from design, not after launch.
    - **Assuming compliance = ethics** (or vice versa) — you generally need both.

## See also

- **[Governance](governance.md)** — the controls that enable accountability.
- **[Security](security.md)** and **[Guardrails & safety](guardrails-and-safety.md)**.
- Glossary: **responsible AI**, **bias**, **fairness**, **explainability**, **human-in-the-loop**, **EU AI Act**.
