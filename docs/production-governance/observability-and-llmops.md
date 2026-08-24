---
tags:
  - L400
  - evaluation
---

# Observability & LLMOps <span class="lvl lvl-400">L400</span>

## In plain terms

Once an AI feature is live, **"it seemed fine in testing" isn't enough** — you need
to *see* what it's actually doing with real users, in real time. **Observability**
is being able to answer "what happened, and why?" for any request.
**LLMOps** is the whole practice of running LLM-powered systems reliably — the AI
cousin of DevOps/MLOps.

## How it works

**Tracing.** A **trace** records everything about one request: the prompt, the
retrieved context, every tool call and its result, the model's output, plus
latency and token counts at each step. When something goes wrong, the trace tells
you *where* — was it bad retrieval, a failed tool, or the model itself? Without
tracing, a wrong answer is a mystery.

**Monitoring & metrics.** Track the health signals over time:

- **Quality** — sampled evaluation scores (correctness, groundedness…).
- **Operational** — latency, error rate, throughput, token usage.
- **Cost** — spend per request, per feature, per day.
- **Usage** — volume, popular queries, failure clusters.

**Drift detection.** AI systems degrade quietly. **Drift** is when reality moves
away from what you built for — users ask new kinds of questions, your data
changes, or a model update shifts behaviour. Monitoring quality on live traffic is
how you catch drift before it becomes a complaint.

**Feedback loops.** Capture thumbs-up/down and corrections, feed real failures back
into your [golden dataset](evaluation-at-scale.md), and close the loop: observe →
evaluate → improve → redeploy.

```
   Production traffic ─► Traces ─► Monitor (quality/cost/latency/drift)
          ▲                                   │
          │                                   ▼
     Redeploy ◄── Improve ◄── Evaluate ◄── Flag failures + user feedback
```

## How Databricks does it

- **MLflow Tracing** captures end-to-end traces of your app/agent — every step,
  input and output — viewable and queryable.
- **MLflow production monitoring** scores sampled live traffic with the same
  judges you use offline, and surfaces quality/operational metrics on dashboards.
- Traces and metrics live alongside your **Unity Catalog** governed assets, and
  feed back into evaluation datasets, closing the observe→improve loop.

## Pitfalls

!!! warning "Flying blind"
    - **No tracing** = un-debuggable failures. Instrument from day one.
    - **Only operational metrics** (latency/errors) miss **quality** drift — a
      fast, cheap, *wrong* answer still looks "green".
    - **No feedback capture** wastes your best source of eval data: real failures.
    - **Alert fatigue** — monitor what you'll act on; tune thresholds.

## See also

- **[Evaluation at scale](evaluation-at-scale.md)** — the scoring that monitoring uses.
- **[Cost & performance](cost-and-performance.md)** — the operational metrics.
- Glossary: **observability**, **trace / tracing**, **LLMOps**, **drift**, **monitoring**, **feedback loop**.
