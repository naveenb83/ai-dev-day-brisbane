---
tags:
  - L400
---

# Deployment & serving <span class="lvl lvl-400">L400</span>

## In plain terms

A model or agent is useless until something can *call* it reliably. **Serving** is
putting it behind an **endpoint** — a stable address your apps hit to get answers —
that stays up, scales with demand, and doesn't fall over at the worst moment.
It's the plumbing between "we built it" and "the business uses it".

## How it works

An **endpoint** wraps your model/agent and handles the operational realities:

- **Scaling.** Handle 1 request or 10,000/minute by adding capacity automatically
  (**autoscaling**), and shrink back — ideally to zero — when idle to save money.
- **Reliability.** Health checks, retries, and **fallbacks** (e.g. drop to a
  simpler model if the primary is down) so a hiccup isn't an outage.
- **Rate limits & quotas.** Protect the system (and your bill) from runaway or
  abusive traffic.
- **Versioning & safe rollout.** Ship a new model/prompt version to a *slice* of
  traffic first (canary / A-B), watch the metrics, then roll forward — or **roll
  back** instantly if it regresses.
- **Streaming.** Return tokens as they're generated for a responsive feel.
- **Security & governance.** Authenticated access, and permissions that follow
  your governance model.

```
   App ─► Endpoint ─► [ current version  ──►  most traffic ]
                      [ new version      ──►  small % (canary) ]
                          │ metrics look good?  promote : roll back
```

**Deployment patterns** you'll meet:

- **Real-time / online** — synchronous answers for interactive use (chat, apps).
- **Batch** — score a big dataset offline on a schedule (bulk enrichment,
  reports). Cheaper per item; not interactive.
- **Streaming** — process events as they arrive.

## How Databricks does it

- **Mosaic AI Model Serving** hosts foundation models, custom/fine-tuned models
  and **agents** behind managed endpoints, with **autoscaling** (and scale-to-zero
  options), **versioning** and **A/B traffic splitting**.
- Endpoints integrate with **Unity Catalog** (governed access), **MLflow**
  (the model/agent artifact, plus tracing and monitoring), and **Foundation Model
  APIs** for hosted models — so serving, governance and observability are one
  stack, not three.
- **Batch inference** and **AI Functions** cover the offline/bulk pattern;
  **Databricks Apps** and **Asset Bundles** wrap it all into a shippable product
  (see [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)).

## Pitfalls

!!! warning "Serving gotchas"
    - **No autoscaling** — either you fall over under load or pay for idle
      capacity. Configure it.
    - **Big-bang releases** — always canary and keep a rollback path.
    - **No rate limits** — one bad client can take you down or blow the budget.
    - **Endpoint sprawl** — idle endpoints quietly billing; track and retire them.

## See also

- **[Cost & performance](cost-and-performance.md)** — sizing and pay models.
- **[Observability & LLMOps](observability-and-llmops.md)** — watching live endpoints.
- **[Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)** — the full deploy.
- Glossary: **endpoint**, **Model Serving**, **autoscaling**, **canary / A-B**, **rollback**, **batch inference**, **rate limit**.
