---
tags:
  - L200
  - prompting
---

# Prompting that works <span class="lvl lvl-200">L200</span>

## In plain terms

A good prompt is less like a search query and more like a **clear brief to a
capable new colleague**. Tell them who they are, what you want, what to work from,
and what the output should look like — and you get great work. Leave it vague and
you get vague work.

This page is the *practical* version; the full patterns and copy-paste templates
live in the **[Prompt Library](../index.md)** *(added in a later section)*.

## How it works — the anatomy of a strong prompt

Five ingredients cover almost everything:

1. **Role** — who the model should be. *"You are a meticulous financial analyst."*
2. **Context / input** — the material to work from. *"Here is last quarter's
   report: …"*
3. **Task** — what to do, specifically. *"List the three biggest cost drivers."*
4. **Constraints** — rules and boundaries. *"Use only the figures provided. If a
   number isn't there, say so. Don't speculate."*
5. **Output format** — the exact shape you want. *"Answer as a markdown table with
   columns Driver, Amount, % of total."*

!!! example "Vague → strong"
    **Vague:** "Summarise this report."

    **Strong:** "You are a financial analyst. Using **only** the report below,
    write a 4-bullet summary for a time-poor executive, leading with the biggest
    risk. If the report doesn't state a figure, write 'not stated' — don't guess.
    \n\nReport: «…»"

    The strong version fixes the role, the source, the audience, the length, the
    ordering, *and* the honesty rule.

Two techniques worth knowing by name:

- **Few-shot prompting** — show 1–3 worked examples of input → desired output. The
  model copies the pattern. Brilliant for consistent formatting or classification.
- **Chain-of-thought** — ask it to "think step by step" or "show your reasoning"
  before the final answer. Improves multi-step and maths-y tasks. (For final
  answers meant for users, ask it to reason, then give a clean conclusion.)

## How Databricks does it

- Draft and test prompts interactively in the **AI Playground**, then lift the
  winning **system prompt** straight into your app or agent via **Foundation Model
  APIs** — same messages, same behaviour.
- When a prompt becomes part of a product, treat it like code: version it, and use
  **MLflow** to evaluate whether a prompt change actually improved answers (see
  [Why we evaluate](why-we-evaluate.md)).

## Pitfalls

!!! warning "The usual suspects"
    - **No source, then surprised by hallucination.** If you want facts, *provide*
      the facts and say "use only these".
    - **Burying the instruction.** Put the key task up front and the long context
      after; don't hide "in one sentence" at the end of a wall of text.
    - **Asking for creativity and precision at once.** Split the job, or set
      [temperature](../foundations/prompts-and-completions.md) to match.

## Try it

:material-flask: **Lab 1** builds a strong prompt step by step and compares it to a
weak one. *(Labs added in a later section.)*

## See also

- **[Prompt Library](../index.md)** — patterns, templates, meta-prompting. *(Added later.)*
- **[Prompts & completions](../foundations/prompts-and-completions.md)** — the L100 basics.
- Glossary: **few-shot**, **chain-of-thought**, **system prompt**.
