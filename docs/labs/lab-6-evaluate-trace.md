---
tags:
  - L400
  - evaluation
---

# Lab 6 — Evaluate & trace <span class="lvl lvl-400">L400</span>

**~30 minutes** · notebook (Python)

## Goal

Stop trusting demos. Build a small **evaluation set**, **score** your Lab 4/5
assistant with MLflow, and read a **trace** to see exactly what it did. This is
the discipline that separates "seemed fine" from "shippable".

## You'll learn

- How to measure quality (correctness, groundedness) instead of eyeballing.
- How tracing turns a wrong answer from a mystery into a fixable bug.

!!! note "APIs evolve"
    MLflow's GenAI evaluation and tracing APIs change across versions. The shape
    below is stable; confirm exact function names in the current MLflow docs or the
    `databricks-mlflow-evaluation` guidance in your workspace.

## Steps

1. **Turn on tracing** so each call is recorded:
   ```python
   import mlflow
   mlflow.set_experiment("/Users/<you>/ai-dev-day-eval")
   mlflow.<framework>.autolog()   # or trace your function with @mlflow.trace
   ```
2. **Build a tiny eval set** — real questions with expected answers:
   ```python
   eval_data = [
     {"question": "How long do I have for a refund?", "expected": "30 days"},
     {"question": "Is the panel in stock?",           "expected": "out of stock"},
     {"question": "Do you ship overseas?",            "expected": "I don't know / not stated"},
   ]
   ```
3. **Run evaluation with judges** for correctness and groundedness:
   ```python
   # illustrative — confirm current API
   results = mlflow.genai.evaluate(
       data=eval_data,
       predict_fn=my_assistant,          # your Lab 4/5 function
       scorers=[correctness, groundedness, relevance],
   )
   print(results.metrics)
   ```
4. **Read the scores.** Where did it score low? The "ship overseas" case should
   reward a truthful "I don't know" and punish a hallucinated yes.
5. **Open a trace.** For a failing case, inspect the trace: what context was
   retrieved? Was the tool called? Was the prompt what you expected? Locate *where*
   it went wrong.
6. **Improve and re-run.** Tweak the prompt or retrieval, run the same eval, and
   confirm the score went **up** — a [regression gate](../production-governance/evaluation-at-scale.md)
   in miniature.

## Expected result

- A metrics summary across your eval set, a trace you can read step by step, and a
  measurable improvement after one change — proof you're now *measuring*, not
  guessing.

## Stretch

- Add a **safety** scorer and a deliberately edgy question.
- Grow the eval set with a failure you found in Labs 4/5 — that's how a golden
  dataset is built.
- Discuss what **online** evaluation on live traffic would add (see
  [Observability & LLMOps](../production-governance/observability-and-llmops.md)).

## Concepts

- **[Why we evaluate](../working-with-ai/why-we-evaluate.md)** ·
  **[Evaluation at scale](../production-governance/evaluation-at-scale.md)** ·
  **[Observability & LLMOps](../production-governance/observability-and-llmops.md)** ·
  Glossary: **evaluation set**, **LLM-as-a-judge**, **groundedness**, **trace / tracing**.
