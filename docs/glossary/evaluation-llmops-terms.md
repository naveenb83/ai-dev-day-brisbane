---
tags:
  - L400
  - evaluation
---

# Glossary — Evaluation & LLMOps

Proving quality and running AI reliably. See
[Why we evaluate](../working-with-ai/why-we-evaluate.md) and
[Observability & LLMOps](../production-governance/observability-and-llmops.md).

**Evaluation (eval)**
:   Measuring how good AI outputs are against criteria or known-good answers —
    the AI equivalent of testing.

**Evaluation set / golden dataset**
:   A curated collection of representative inputs (ideally with correct answers) used
    to score a system. Your regression suite; grow it from real failures.

**Ground truth**
:   The known-correct answer for an evaluation example.

**LLM-as-a-judge**
:   Using a separate model, prompted with your criteria, to grade outputs at scale.
    Fast and scalable — but must be **calibrated** against human judgement.

**Correctness**
:   Is the answer factually right? A core eval metric.

**Groundedness / faithfulness**
:   Is the answer actually supported by the provided source (not invented)? The key
    metric for RAG.

**Relevance**
:   Does the answer address the question asked?

**Hallucination rate**
:   How often the system produces made-up content — a metric to drive down.

**Precision / recall / F1**
:   Classic accuracy metrics — *precision* = of what it flagged, how much was right;
    *recall* = of what it should have flagged, how much it caught; *F1* balances the
    two.

**BLEU / ROUGE**
:   Older text-overlap metrics comparing output to a reference. Useful for
    translation/summarisation, weak for open-ended quality — LLM judges are common
    now.

**Human evaluation**
:   People grading outputs. The gold standard for calibrating automated judges;
    doesn't scale alone.

**A/B testing**
:   Comparing two versions on live traffic to see which performs better.

**Regression gate**
:   An automatic check that blocks a change if it lowers eval scores — how you
    improve without silently getting worse.

**Trace / tracing**
:   A detailed record of one request — prompt, retrieved context, tool calls,
    output, latency, tokens — enabling debugging. → *On Databricks:* MLflow Tracing.

**Observability**
:   Being able to answer "what happened and why?" for any request, via traces and
    metrics.

**Monitoring**
:   Watching quality, cost, latency and usage over time in production, with alerts.

**Drift**
:   Gradual divergence between what a system was built for and current reality
    (new questions, changed data, model updates) — caught by monitoring.

**Feedback loop**
:   Capturing user feedback and real failures and feeding them back into evaluation
    and improvement.

**LLMOps / MLOps**
:   The practice and tooling for deploying, monitoring and maintaining LLM (or ML)
    systems reliably — the AI cousin of DevOps.

**Red teaming**
:   Deliberately attacking your own system to find weaknesses (unsafe outputs,
    injection, leakage) before adversaries do.

**Benchmark / leaderboard**
:   Standard tests / public rankings comparing models. Directional signal; validate
    on your own task.

**Prompt versioning**
:   Tracking prompts like code so changes are reviewable and roll-back-able, and
    their impact is measured.
