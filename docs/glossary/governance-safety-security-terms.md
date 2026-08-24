---
tags:
  - L400
  - governance
---

# Glossary — Governance, safety & security

Keeping AI safe, fair and controlled. See
[Governance](../production-governance/governance.md),
[Security](../production-governance/security.md) and
[Guardrails & safety](../production-governance/guardrails-and-safety.md).

**Responsible AI**
:   Making AI fair, transparent, accountable and respectful of people — ethics plus
    risk management plus (increasingly) law.

**Bias**
:   Systematic unfairness a model inherits from its training data, potentially
    treating groups differently. Tested via outcomes across subgroups, not just
    overall accuracy.

**Fairness**
:   Ensuring AI doesn't produce unjust or discriminatory outcomes for particular
    groups.

**Toxicity / content safety**
:   Harmful, offensive or unsafe content — detected and blocked by safety filters.

**Explainability / transparency**
:   Being able to show that AI was used and, ideally, why it decided as it did
    (e.g. citations, the SQL Genie ran).

**Alignment**
:   Model makers' work (e.g. via RLHF) to make models helpful, honest and harmless
    by default. Your app-level guardrails sit on top; don't rely on alignment alone.

**RLHF (reinforcement learning from human feedback)**
:   Training that nudges a model toward answers humans prefer, using human ratings.

**DPO (direct preference optimisation)**
:   A simpler, popular alternative to RLHF for preference tuning.

**Guardrail**
:   An independent check around the model enforcing rules on inputs/outputs
    (topic limits, safety filters, PII redaction, format validation). Stronger than
    prompt instructions because it's outside the model.

**Content moderation**
:   Filtering inputs/outputs for unsafe or disallowed content.

**PII / PHI**
:   Personally Identifiable Information / Protected Health Information — sensitive
    personal data needing special handling. → *On Databricks:* detect/redact with
    `ai_mask`; control with Unity Catalog masks.

**Data governance**
:   The rules and controls for who can access and use which data, and proving it.

**RBAC (role-based access control)**
:   Permissions attached to roles ("analysts can read sales"). Simple, coarse.

**ABAC (attribute-based access control)**
:   Permissions based on attributes of data/user/context ("mask columns tagged PII
    unless the user is in compliance"). Finer-grained, scales via tags/policies.

**Column mask / row filter**
:   Fine-grained controls that hide sensitive columns or restrict which rows a user
    sees. → *On Databricks:* enforced by Unity Catalog and respected by Genie, RAG
    and AI Functions.

**Classification tags**
:   Labels on data (PII, confidential, etc.) that access policies act on
    automatically.

**Lineage**
:   A map of where data and models came from and what depends on them — for impact
    analysis, debugging and provenance.

**Audit**
:   An immutable record of who accessed or changed what, when — for security and
    compliance.

**Least privilege**
:   Granting the minimum access needed. The strongest safeguard against leakage —
    the model can't reveal what it can't reach.

**Prompt injection**
:   An attack that smuggles instructions into text the model reads, hijacking its
    behaviour. **Direct** (in the user's message) or **indirect** (hidden in a
    retrieved document/web page/email) — the latter is especially dangerous for
    agents.

**Jailbreak**
:   Tricking a model past its safety training via role-play or clever framing.

**Data leakage / exfiltration**
:   The model revealing data it shouldn't — secrets, other users' data, sensitive
    records — sometimes via a tool that sends data out.

**Red teaming**
:   Proactively attacking your own system to find and fix weaknesses.

**Secret scope**
:   A secure store for credentials/keys so they stay out of code and prompts.
    → *On Databricks:* Databricks secret scopes.

**Compliance / EU AI Act / NIST AI RMF**
:   Legal and standards frameworks setting expectations for AI, especially
    high-risk uses. *(Evolving; confirm current obligations for your context.)*
