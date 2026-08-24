---
tags:
  - L400
  - governance
---

# Governance <span class="lvl lvl-400">L400</span>

## In plain terms

**Governance** is the boring-sounding thing that makes everything else safe: a
single, enforced answer to **"who is allowed to see and do what — with which data,
models and tools — and can we prove it later?"** For AI it's non-negotiable,
because an AI feature is only ever as safe as the data and permissions behind it.

## How it works — the building blocks

**Access control.** Grant the least access needed. Two common models:

- **RBAC (role-based):** permissions attached to *roles* ("analysts can read the
  sales schema"). Simple, coarse.
- **ABAC (attribute-based):** permissions based on *attributes* of the data, user
  or context ("mask any column tagged `PII` unless the user is in `compliance`").
  Finer-grained and scalable across many tables via tags/policies.

**Fine-grained controls.** Beyond table-level: **column masking** (hide/blur
sensitive fields), **row filters** (each user sees only their rows), and
**classification tags** (label data as PII, PHI, confidential…) that policies act
on automatically.

**Lineage.** A map of where data (and models) came from and what depends on them —
essential for impact analysis, debugging, and proving provenance.

**Audit.** An immutable record of who accessed or changed what, when — for
security investigations and compliance.

**Identity.** Users and groups synced from your identity provider (via SCIM/SSO),
so permissions follow real organisational identity, not local accounts.

!!! note "Why this is the foundation of AI safety"
    The strongest guardrail against leakage isn't a clever filter — it's that
    **the model was never granted access to the sensitive data in the first
    place.** Governance is what makes "least privilege" real. An AI assistant
    inherits its user's permissions; get governance right and the assistant
    simply *can't* surface what the user couldn't already see.

## How Databricks does it

**Unity Catalog** is the unified governance layer across data *and* AI:

- One permission model over tables, files (**volumes**), **models**, **functions**
  (agent tools) and features — so an agent's data, model and tools are all
  governed the same way.
- **RBAC and ABAC** (tags, governed tag policies), **column masks** and **row
  filters** enforce fine-grained access — and these are respected by **Genie**,
  RAG and AI Functions automatically.
- Built-in **lineage** and **audit** (via system tables) across the whole platform.
- **Identity federation** (SCIM/SSO) so access maps to your org's identity.

Because AI runs *inside* this governed platform, your existing data permissions
extend to AI features without a separate, bolt-on security model.

## Pitfalls

!!! warning "Governance gaps that bite"
    - **Over-granting "to make it work."** Broad access is a breach waiting to
      happen — start least-privilege.
    - **Governing data but not tools/models.** An agent's *tools* need governance
      too, or they're a backdoor.
    - **Assuming the AI adds its own security.** It inherits permissions — if the
      data's exposed, so is the AI's answer.
    - **No audit until you need it.** Turn it on before the incident, not after.

## See also

- **[Security](security.md)** — threats least-privilege defends against.
- **[Responsible AI](responsible-ai.md)** — accountability and privacy.
- Glossary: **Unity Catalog**, **RBAC**, **ABAC**, **column mask**, **row filter**, **lineage**, **audit**.
