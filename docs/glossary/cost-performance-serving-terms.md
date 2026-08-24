---
tags:
  - L400
---

# Glossary — Cost, performance & serving

Making AI fast, reliable and affordable. See
[Cost & performance](../production-governance/cost-and-performance.md) and
[Deployment & serving](../production-governance/deployment-and-serving.md).

**Inference cost**
:   What it costs to run a model per request — driven mainly by tokens and model
    size, multiplied by volume.

**Token pricing / pay-per-token**
:   Being billed per token in and out. Long prompts and long answers both cost more.
    → *On Databricks:* a Foundation Model APIs pricing option, good for spiky/low
    volume.

**Provisioned throughput**
:   Reserved model capacity for predictable cost and latency at steady high volume.
    → *On Databricks:* the alternative to pay-per-token for heavy workloads.

**Batch inference**
:   Processing a large dataset offline in bulk (not interactive) — cheaper per item.
    → *On Databricks:* AI Functions / batch jobs.

**Prompt caching**
:   Reusing the cost/computation of a repeated context prefix across calls to cut
    cost and latency.

**Latency**
:   How long a request takes to answer. Driven by model size, output length and
    number of steps.

**Throughput**
:   How many requests a system handles per unit time.

**Time to first token (TTFT)**
:   Delay before the answer starts. Low TTFT + streaming improves perceived speed.

**GPU**
:   The specialised hardware that runs large models. Powerful and costly — a big
    part of why inference isn't free.

**Endpoint**
:   The stable address your apps call to use a served model/agent.

**Model serving**
:   Hosting a model/agent behind a managed endpoint that handles scaling,
    reliability and versioning. → *On Databricks:* Mosaic AI Model Serving.

**Autoscaling / scale-to-zero**
:   Automatically adding capacity under load and shrinking (ideally to zero) when
    idle, so you don't pay for unused compute.

**Model routing**
:   Sending easy requests to a cheap model and only hard ones to a big model, to
    balance quality and cost.

**Fallback**
:   Automatically switching to an alternative (e.g. a simpler model) if the primary
    fails — for reliability.

**Rate limit / quota**
:   Caps on request volume to protect the system and the budget from runaway or
    abusive traffic.

**Canary / A-B rollout**
:   Releasing a new version to a small slice of traffic first, watching metrics,
    then promoting or rolling back.

**Rollback**
:   Reverting to the previous working version quickly when a change regresses.

**Quantisation**
:   Compressing a model to lower-precision numbers so it runs cheaper/faster, with a
    small quality trade-off.
