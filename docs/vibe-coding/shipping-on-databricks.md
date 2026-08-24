---
tags:
  - L300
  - vibe-coding
---

# Shipping on Databricks <span class="lvl lvl-300">L300</span>

This page is the concrete "how do I actually deploy it?" companion to
[From prototype to production](from-prototype-to-production.md). It maps the
generic dev→prod pieces onto the specific Databricks tools.

## The moving parts

| You need to… | On Databricks | Why |
| --- | --- | --- |
| Host a web app / UI | **Databricks Apps** | Runs your app next to your data and models, with workspace auth |
| Serve a model or agent | **Model Serving** | Managed, scalable endpoints for LLMs, custom models and agents |
| Define the project as code | **Databricks Asset Bundles** | Version-controlled config for repeatable, reviewable deploys |
| Move safely dev → staging → prod | **Bundle targets** | One definition, multiple environments |
| Run scheduled/back-end work | **Jobs / pipelines** | Batch inference, data prep, retraining |
| Govern data, models, tools | **Unity Catalog** | Permissions, lineage, audit across everything |
| Evaluate & monitor AI quality | **MLflow** | Eval sets, tracing, production monitoring |
| Store secrets | **Secret scopes** | Keep credentials out of code and prompts |

## A typical shape

```
   Your repo (in version control)
        │  databricks.yml  (Asset Bundle: app + job + config + targets)
        ▼
   databricks bundle deploy --target dev      ← test here
        │  (CI runs checks on every change)
        ▼
   databricks bundle deploy --target prod      ← promote when green
        │
        ├─► Databricks App        (the UI users see)
        ├─► Model Serving endpoint (the AI behind it)
        └─► Jobs / pipelines       (the data work behind that)
                     └─ all governed by Unity Catalog, observed by MLflow
```

The point: **your whole application — app, model, jobs and config — is defined in
files, version-controlled, and deployed the same way every time.** That's what
turns "it works on my machine" into something a team can run.

!!! tip "Start simple"
    You don't need all of this on day one. A Databricks App calling a Foundation
    Model API is a complete, shippable thing. Add bundles, CI/CD, serving and
    monitoring as the project earns them.

## How this connects to the labs

The hands-on labs build the *pieces* — prompts, AI Functions, Genie, RAG, an
agent, evaluation. Shipping is how you'd wrap those into something durable
afterwards. *(Labs added in a later section.)*

## Pitfalls

!!! warning "Deploy-time gotchas"
    - **Clicking instead of bundling.** Manual UI changes aren't repeatable or
      reviewable — put it in a bundle.
    - **One environment.** Test in dev/staging, not on your users.
    - **Forgetting the endpoint costs.** A serving endpoint left running costs
      money; size and monitor it.
    - **Skipping governance.** Wire Unity Catalog in from the start, not as an
      afterthought.

## See also

- **[From prototype to production](from-prototype-to-production.md)** — the why and the journey.
- **[Building agents on Databricks](../building-with-ai/building-agents-on-databricks.md)** — deploying agents.
- **Production & Governance (L400)** — operating it well. *(Added later.)*
- Glossary: **Databricks Apps**, **Asset Bundle**, **Model Serving**, **CI/CD**, **secret scope**.
