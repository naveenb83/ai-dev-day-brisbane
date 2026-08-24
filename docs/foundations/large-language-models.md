---
tags:
  - L100
---

# Large language models <span class="lvl lvl-100">L100</span>

## In plain terms

A **large language model (LLM)** is the engine behind tools like ChatGPT, Claude
and the assistants inside Databricks. At heart it does something surprisingly
simple: **given some text, it predicts the next chunk of text** — over and over,
a piece at a time, until it has written a full answer.

That's it. It's a very, very good **autocomplete** that has read an enormous
amount of text and learned the patterns of language, facts and reasoning that
tend to follow from what came before.

## How it works

A few ideas make LLMs make sense:

**Tokens.** The model doesn't read whole words; it reads **tokens** — small pieces
of text (a short word is one token; a long word might be two or three). "Brisbane"
might be one token; "unbelievable" might be "un", "believ", "able". The model
predicts one token at a time.

**Context window.** The model can only "see" a limited amount of text at once —
its **context window**, measured in tokens. Everything you want it to consider —
your question, the conversation so far, any documents you paste in — has to fit.
Modern models have large windows (tens or hundreds of thousands of tokens), but
it's never infinite. When people say a chat "forgot" something, it often fell out
of the window.

**Parameters.** During training, the model's "knowledge" is stored as billions of
numbers called **parameters** (or "weights"). "70 billion parameters" is a rough
size label. Bigger isn't always better — a smaller, newer model can beat an older,
larger one.

**Training vs. inference — the crucial distinction:**

| | **Training** | **Inference (using it)** |
| --- | --- | --- |
| What happens | The model *learns* from mountains of text | The model *answers* your prompt |
| When | Once, up front, by the model's makers | Every time you send a prompt |
| Cost | Enormous (weeks, huge compute) | Small (a fraction of a second to seconds) |
| Changes the model? | Yes — it sets the parameters | No — the model is frozen |

!!! tip "The one thing to remember"
    When *you* use an LLM, you are doing **inference**. You are **not** teaching
    it — it doesn't remember your chat tomorrow unless the system around it is
    built to store that. The model itself is frozen.

**Fine-tuning** is optional extra training on top of a base model to specialise
it (say, on your company's tone). It's powerful but usually *not* the first tool
you reach for — good prompting and giving the model the right documents
([RAG](../foundations/embeddings-and-vectors.md)) solve most problems first.

## How Databricks does it

You don't train these giant models yourself — you **use** ones that are already
trained:

- **Foundation Model APIs** give you instant access to leading open and
  commercial LLMs, billed per token (pay for what you use) or via reserved
  capacity for heavy workloads.
- The **AI Playground** is a chat screen in your workspace where you can try
  different models side by side, tune settings, and see the cost — a great first
  stop in the labs.
- When you *do* need a custom or fine-tuned model, **Mosaic AI** and **Model
  Serving** host it behind an endpoint so your apps can call it like any other.

Because it all sits on your data platform, the model can be pointed at *your*
governed data — which is where the real value shows up in later sections.

## Pitfalls

!!! warning "Common misunderstandings"
    - **"It knows everything up to today."** No — it has a **knowledge cut-off**
      (the date its training data ends) and won't know newer events unless you
      give it that information in the prompt.
    - **"Bigger model = better answer."** Not reliably. Match the model to the
      task; smaller models are cheaper and often plenty.
    - **"It's remembering our whole conversation."** Only what still fits in the
      **context window**.

## Try it

:material-flask: In **Lab 1** you'll send your first prompts in the AI Playground
and watch tokens, settings and cost in action.

## See also

- **[Prompts & completions](prompts-and-completions.md)** — how you actually talk to it.
- **[Why AI gets things wrong](why-ai-gets-things-wrong.md)** — the limits, honestly.
- Glossary: **token**, **context window**, **parameter**, **inference**, **fine-tuning**, **knowledge cut-off**.
