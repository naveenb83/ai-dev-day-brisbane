---
tags:
  - L400
---

# Cost & performance <span class="lvl lvl-400">L400</span>

## In plain terms

AI feels free in a demo and expensive at scale. Every model call costs money and
takes time, and **thousands of users × many calls each** adds up fast. Managing
cost and performance is what keeps an AI feature viable once it's real — and it's
mostly about doing *less work* and *right-sizing* the model.

## How it works

### What drives cost

- **Tokens.** You pay per token, **in and out**. Long prompts (big retrieved
  contexts, long histories) and long answers both cost more. Trimming context is
  the biggest lever.
- **Model size.** Bigger models cost more per token and are slower. A smaller
  model that passes your [eval](evaluation-at-scale.md) is pure savings.
- **Number of calls.** Agents and multi-step chains multiply calls per request.
- **Always-on compute.** A serving endpoint left running costs money even when
  idle.

### What drives latency

- **Model size** and **output length** (it generates one token at a time).
- **Number of steps** (each agent hop is another round-trip).
- **Retrieval and tool** time.
- **Time to first token (TTFT)** vs total time — streaming the answer improves the
  *felt* speed even if total time is the same.

### The levers (roughly in order of impact)

1. **Right-size the model.** Use the smallest model that passes eval; **route**
   easy requests to a cheap model and only hard ones to a big model.
2. **Shrink the prompt.** Retrieve fewer, better chunks; summarise history; drop
   dead context.
3. **Cache.** **Prompt caching** reuses the cost of a repeated context prefix;
   cache whole answers to common questions.
4. **Batch** offline work (bulk AI Functions) rather than one call at a time.
5. **Cap the work.** Limit agent steps, max output tokens, and set budgets.
6. **Distil** a small model to match a big one on your task (see
   [Customizing a model](../building-with-ai/model-customization.md)).
7. **Stream** output for better perceived latency.

!!! tip "Measure per-request cost early"
    Estimate **cost per request × expected volume** *before* launch. A $0.02
    request is fine at 1,000/day and a five-figure monthly bill at 1,000,000/day.
    The demo won't warn you — the math will.

## How Databricks does it

- **Foundation Model APIs** offer **pay-per-token** (variable, great for spiky or
  low volume) and **provisioned throughput** (reserved capacity, predictable cost
  and latency for steady high volume) — pick per workload.
- **Batch inference** and **AI Functions** process large volumes efficiently.
- **Model Serving** endpoints **autoscale** (including scale-to-zero options) so
  you're not paying for idle capacity.
- **MLflow / system tables** let you attribute **cost and usage** per endpoint,
  model or feature, so optimisation is data-driven.

## Pitfalls

!!! warning "Bill-shock and lag"
    - **Defaulting to the biggest model** for everything — often overkill.
    - **Unbounded agents** looping up cost and latency — always cap.
    - **Bloated context** — the quiet, constant tax on every call.
    - **Idle endpoints** billing 24/7 — autoscale / scale-to-zero.
    - **No cost visibility** — you can't optimise what you don't measure.

## See also

- **[Deployment & serving](deployment-and-serving.md)** — the endpoints you're sizing.
- **[Customizing a model](../building-with-ai/model-customization.md)** — distillation for cost.
- Glossary: **token**, **prompt caching**, **provisioned throughput**, **pay-per-token**, **TTFT**, **autoscaling**, **model routing**.
