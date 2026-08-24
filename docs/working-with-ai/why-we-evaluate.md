---
tags:
  - L200
  - evaluation
---

# Why we evaluate <span class="lvl lvl-200">L200</span>

## In plain terms

With normal software, a test passes or fails. With AI, the same input can give
slightly different, "sort of right" answers — so "does it work?" becomes "**how
good is it, on average, on the things I care about?**" **Evaluation** is how you
answer that with evidence instead of vibes.

If you remember one thing: **you cannot improve what you don't measure, and you
can't measure AI quality by eyeballing a handful of demos.**

## How it works

The recipe is the same whether you're checking a prompt, a RAG assistant or a
Genie Space:

1. **Build an evaluation set** — a collection of representative inputs, ideally
   with known-good answers or clear criteria. Even 20–50 realistic examples beats
   guessing.
2. **Pick what "good" means** — the metrics that matter for *your* task, e.g.:
    - **Correctness** — is the answer right?
    - **Groundedness** — is it actually supported by the retrieved source (not
      made up)?
    - **Relevance / helpfulness** — does it address the question?
    - **Safety / tone** — is it appropriate?
    - **Cost & latency** — is it affordable and fast enough?
3. **Score every example** — by exact rules where possible, and increasingly with
   an **LLM-as-a-judge**: a separate model prompted to grade answers against your
   criteria (fast and scalable; validate it against human judgement).
4. **Compare and iterate** — change the prompt/model/retrieval, re-run, and keep
   what genuinely improves the score.

!!! example "Why demos lie"
    A RAG bot might dazzle on the three questions you tried on stage and fail on
    40% of the real ones. Only an eval set over realistic questions reveals that
    *before* your users do.

## How Databricks does it

- **Mosaic AI / MLflow evaluation** runs your eval set against an app or agent and
  scores it with built-in judges (correctness, groundedness, safety, relevance)
  or your own custom ones.
- **MLflow Tracing** records each call — the prompt, the retrieved context, the
  tools used, the output — so a bad score is *debuggable*.
- The same harness powers **production monitoring**: keep scoring real traffic so
  quality drift is caught early (the L400 story).

## Pitfalls

!!! warning "Do it honestly"
    - **Tiny or unrepresentative eval sets** flatter you. Cover the messy, real
      cases, not just easy ones.
    - **Unchecked LLM judges** can be biased or lenient. Calibrate against human
      labels on a sample.
    - **Optimising one metric** (e.g. correctness) can wreck another (cost,
      safety). Watch the trade-offs together.

## Try it

:material-flask: **Lab 6** evaluates and traces an agent with MLflow.

## See also

- **[Retrieval & RAG](retrieval-and-rag.md)** — groundedness lives here.
- **[Production & governance (L400)](../production-governance/index.md)** — evaluation at scale.
- Glossary: **evaluation set**, **LLM-as-a-judge**, **groundedness**, **tracing**.
