---
tags:
  - L300
---

# Customizing a model <span class="lvl lvl-300">L300</span>

## In plain terms

Sooner or later someone asks: *"Can we train it on our data?"* Usually the honest
answer is **"you probably don't need to — and there are cheaper things to try
first."** This page lays out the ladder of ways to make a model behave the way you
want, from easiest to hardest, so you pick the right rung.

## How it works — the customization ladder

Climb only as high as you must; each rung is more effort and cost than the last.

1. **Prompt engineering.** Change *what you ask* and how. Free, instant, and solves
   a surprising amount. Always start here. (See
   [Prompting that works](../working-with-ai/prompting-that-works.md).)
2. **Give it context (RAG).** Feed the model your documents/data at query time so
   it answers from *your* content. Fixes "it doesn't know our stuff" without
   touching the model. (See [Retrieval & RAG](../working-with-ai/retrieval-and-rag.md).)
3. **Tools & agents.** Let it fetch live data and take actions. Fixes "it can't
   reach our systems." (See [What is an agent?](what-is-an-agent.md).)
4. **Fine-tuning.** *Actually* adjust the model's weights on your examples, to bake
   in a style, format or narrow skill. Reach for this when prompting + RAG can't get
   consistency, or you need a smaller/cheaper model to match a big one on a
   specific task.
5. **Train from scratch.** Almost never. Reserved for a handful of organisations
   with unique data and huge budgets.

!!! tip "The rule of thumb"
    **Prompting → RAG → tools → fine-tuning → (rarely) pre-training.** Most
    business value lives in the first three. Fine-tuning changes *behaviour and
    style*; it does **not** reliably teach new facts — use RAG for facts.

### Fine-tuning, without the jargon

- **Full fine-tuning** updates all the weights — powerful, expensive, needs lots
  of data.
- **Parameter-efficient fine-tuning (PEFT), e.g. LoRA**, updates a small add-on
  instead of the whole model — far cheaper and the usual choice.
- **Instruction tuning** teaches a base model to follow instructions; **preference
  tuning (RLHF / DPO)** nudges it toward answers humans prefer. These are mostly
  done by model makers, but you can apply lighter versions.
- **Distillation** trains a small, cheap model to imitate a big one on your task —
  great for cutting cost and latency once you have a working large-model solution.

## How Databricks does it

- **Foundation Model APIs** cover rungs 1–3 out of the box (prompting, embeddings
  for RAG, tool calling).
- **Mosaic AI Model Training / fine-tuning** handles rung 4 — fine-tune open models
  (including efficient methods) on your governed data, tracked in **MLflow** and
  deployed to **Model Serving**.
- Custom or fine-tuned models are registered in **Unity Catalog** and served behind
  an endpoint like any other, so the rest of your stack doesn't change.

## Pitfalls

!!! warning "Fine-tuning traps"
    - **Using it to add facts.** It won't reliably memorise your knowledge base —
      that's RAG's job. Fine-tune for *form*, retrieve for *facts*.
    - **Too little / poor data.** Fine-tuning on a small or noisy dataset can make
      a model *worse*. Quality and quantity both matter.
    - **Skipping evaluation.** Always measure the fine-tuned model against the base
      model on a real eval set — sometimes prompting alone wins.
    - **Maintenance debt.** A fine-tuned model is frozen at its data; the frontier
      moves. Re-evaluate periodically.

## See also

- **[Retrieval & RAG](../working-with-ai/retrieval-and-rag.md)** — the facts route.
- **[Why we evaluate](../working-with-ai/why-we-evaluate.md)** — proving customization helped.
- Glossary: **fine-tuning**, **LoRA / PEFT**, **RLHF**, **DPO**, **distillation**, **pre-training**.
