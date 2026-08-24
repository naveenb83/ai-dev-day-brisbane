---
tags:
  - L400
  - evaluation
---

# Evaluation at scale <span class="lvl lvl-400">L400</span>

## In plain terms

[At L200](../working-with-ai/why-we-evaluate.md) we said "measure quality instead
of guessing". At L400 that becomes a **continuous discipline**: evaluate before
every release, keep evaluating in production, and never let a change ship without
proof it didn't make things worse. Evaluation stops being a one-off and becomes
part of the pipeline — like automated tests for AI.

## How it works

**A golden dataset.** Maintain a curated set of representative inputs with
known-good answers or clear grading criteria — and keep growing it, especially
with the real failures you discover. This is your regression suite.

**Judges you trust.** At scale you can't hand-grade everything, so you use
**LLM-as-a-judge** scorers for correctness, groundedness, relevance, safety and
tone. Crucially, you **calibrate the judges against human labels** on a sample so
you know they agree with people; a judge you haven't validated is just another
opinion.

**Regression gates.** Every prompt, model or retrieval change is scored against
the golden set *before* it ships. If the score drops, it doesn't ship. This is how
you improve without silently regressing.

**Online + offline.**

- **Offline:** evaluate against your dataset in development (fast, controlled).
- **Online:** score a sample of *real production traffic* continuously, so you
  catch problems your dataset didn't anticipate.

!!! example "Why this matters"
    A model-provider upgrade "should" be an improvement. Without a regression gate,
    it silently changes behaviour on 15% of your cases — some worse. With one, you
    catch it before users do, and decide deliberately.

## How Databricks does it

- **Mosaic AI Agent Evaluation / MLflow** runs your eval set against an app or
  agent with built-in judges (correctness, groundedness, safety, relevance,
  guideline-adherence) or custom scorers you define.
- Evaluation datasets can be **built from real traces**, so your golden set grows
  from actual usage rather than guesswork.
- The same scorers run in **production monitoring** on sampled traffic, and
  judges can be **aligned** to your domain experts' judgement.
- Results are tracked in **MLflow**, so you can compare versions and gate releases.

## Pitfalls

!!! warning "Evaluation done badly is worse than none"
    - **Stale or tiny datasets** stop reflecting reality — grow them from
      production failures.
    - **Uncalibrated judges** can be confidently wrong; check against humans.
    - **Gaming a single metric** (chasing correctness while safety or cost
      degrades). Watch the set of metrics together.
    - **No online evaluation** — offline scores can look great while real traffic
      quietly drifts.

## Try it

:material-flask: **Lab 6** builds an eval set, runs judges, and traces results in
MLflow. *(Labs added in a later section.)*

## See also

- **[Why we evaluate](../working-with-ai/why-we-evaluate.md)** — the L200 basics.
- **[Observability & LLMOps](observability-and-llmops.md)** — where online eval lives.
- Glossary: **golden dataset**, **LLM-as-a-judge**, **regression gate**, **groundedness**, **online evaluation**.
