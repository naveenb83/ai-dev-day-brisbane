---
tags:
  - L300
  - vibe-coding
---

# From prototype to production <span class="lvl lvl-300">L300</span>

## In plain terms

The demo that wowed the room is maybe **10% of the work**. "It runs on my screen"
and "real people depend on it every day" are separated by a stretch of
unglamorous but essential engineering. Knowing that gap exists — and roughly
what's in it — is what keeps AI projects from dying at the demo.

!!! quote "The trap"
    *"But it already works!"* A prototype proves an idea is **possible**.
    Production proves it's **reliable, safe, affordable and supportable** — for
    everyone, every time, including when things go wrong.

## How it works — the journey

Think of four gates between a prototype and production:

```
 PROTOTYPE ──► HARDEN ──► DEPLOY ──► OPERATE
 "it works"    "it works   "others    "it keeps
               reliably     can use    working &
               & safely"    it"        improving"
```

### 1. Harden — make it robust
- **Handle the unhappy paths:** bad input, empty results, timeouts, errors.
- **Add tests** and get them passing (see [Best practices](best-practices.md)).
- **Secure it:** secrets out of code, least-privilege data access, validate all
  input. For AI features, defend against
  [prompt injection](../production-governance/security.md) *(covered in L400)*.
- **Right-size it:** will it hold up with real data volumes and real users?

### 2. Deploy — make it reachable and repeatable
- **One-click, repeatable deploys** — not manual clicking. Infrastructure and
  config live in version control.
- **Separate environments:** dev → staging → production, so you test changes
  before users feel them.
- **CI/CD:** automated checks run on every change before it goes live.

### 3. Operate — keep it healthy
- **Monitoring & logging:** know when it breaks *before* users tell you.
- **For AI features:** ongoing **evaluation** and **tracing** to catch quality
  drift, plus **cost** tracking (model calls add up). This is the
  **[Production & Governance (L400)](../production-governance/index.md)** discipline.
- **A way to roll back** quickly when a change goes wrong.

### 4. Support — make it someone's job
- **Ownership, documentation, and a plan** for updates and incidents. Software
  without an owner rots.

!!! tip "For AI features specifically"
    Add these to the checklist: an **evaluation set** so you can prove changes
    help; **guardrails** on inputs and outputs; **human-in-the-loop** for
    consequential actions; and a **model/prompt version** you can pin and roll
    back. All expanded in L400.

## How Databricks does it

- **Databricks Apps** host your application close to your data and models.
- **Databricks Asset Bundles** define your project (code, jobs, config) as
  version-controlled files, giving you **repeatable deploys** across dev/staging/
  prod and easy **CI/CD**.
- **Model Serving** deploys AI models/agents behind managed, scalable endpoints.
- **MLflow** provides evaluation, tracing and monitoring; **Unity Catalog**
  provides the governance, lineage and audit that production demands.
- See **[Shipping on Databricks](shipping-on-databricks.md)** for how these fit.

## Pitfalls

!!! warning "Why prototypes stall"
    - **Underestimating the 90%.** Budget for hardening and operations, not just
      the demo.
    - **No environments / no rollback.** Editing production directly is how outages
      happen.
    - **Ignoring cost until the bill arrives.** For AI, measure cost per request
      early.
    - **No owner.** Decide who keeps it alive before launch.

## See also

- **[Best practices](best-practices.md)** — the habits that make hardening easy.
- **[Shipping on Databricks](shipping-on-databricks.md)** — the deploy mechanics.
- **[Production & Governance (L400)](../production-governance/index.md)** — operating AI for real.
- Glossary: **CI/CD**, **staging**, **rollback**, **monitoring**, **guardrails**.
