---
tags:
  - L100
  - prompting
---

# Prompts & completions <span class="lvl lvl-100">L100</span>

## In plain terms

A **prompt** is what you send the model — your instructions and question. The
**completion** (or "response") is what it sends back. Talking to an LLM is just a
loop of prompts and completions.

The quality of the completion depends enormously on the prompt. Same model, vague
prompt → vague answer; same model, clear prompt → useful answer. That's why
there's a whole **[Prompt Library](../index.md)** in this site. *(Added in a later
section.)*

## How it works

Most chat models see three kinds of message:

- **System message** — the standing instructions that set the model's role and
  rules ("You are a careful financial analyst. Answer only from the data
  provided. If unsure, say so."). Set once, applies to the whole conversation.
- **User message** — what the person types.
- **Assistant message** — what the model replied. Past turns are fed back in so
  the model has context for the next reply.

A couple of dials change the *style* of the completion:

**Temperature** controls randomness:

- **Low (near 0)** → focused, consistent, repeatable. Best for facts, extraction,
  code, anything where you want the *same* answer each time.
- **High (near 1)** → varied, creative, surprising. Good for brainstorming and
  drafting.

!!! example "Same prompt, different temperature"
    *Prompt:* "Give me a name for a coffee shop."

    - **Temperature 0** → "The Daily Grind" (and again, and again).
    - **Temperature 0.9** → "Bean There", "Foam & Fable", "Steamwork" — different
      each time.

**Max tokens** caps how long the answer can be. If a response gets cut off
mid-sentence, the limit was probably too low.

## How Databricks does it

In the **AI Playground** you can set the **system prompt**, type user messages,
and drag the **temperature** and **max tokens** sliders to feel their effect —
all without writing code. When you move to building, the same three message types
and settings appear in the **Foundation Model APIs**, so what you learn in the
Playground transfers directly to your apps and agents.

## Pitfalls

!!! warning "Prompt traps for beginners"
    - **Being vague.** "Summarise this" vs "Summarise this in 3 bullet points for
      a busy executive, focusing on risks." The second gets a far better answer.
    - **Asking for facts at high temperature.** If you want accuracy and
      repeatability, turn temperature *down*.
    - **Assuming it remembers.** If it lost the thread, the relevant text may have
      dropped out of the [context window](large-language-models.md) — re-paste it.

## Try it

:material-flask: **Lab 1** has you write a system prompt and watch how temperature
changes the answer. *(Labs added in a later section.)*

## See also

- **[Large language models](large-language-models.md)** — what's producing the completion.
- **[Prompt Library](../index.md)** — how to write prompts that work. *(Added later.)*
- Glossary: **prompt**, **completion**, **system prompt**, **temperature**, **max tokens**.
