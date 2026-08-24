---
tags:
  - L200
  - L300
  - prompting
---

# Prompt patterns <span class="lvl lvl-200">L200</span>

Reusable techniques you slot into the [prompt skeleton](anatomy-of-a-good-prompt.md).
Mix and match.

## Few-shot: show, don't just tell

Give 1–3 examples of input → desired output. The model copies the pattern —
brilliant for consistent formatting and classification.

```text
Classify each message as: BILLING, BUG, or FEATURE.

Examples:
"I was charged twice" -> BILLING
"The app crashes on login" -> BUG
"Can you add dark mode?" -> FEATURE

Now classify:
"My invoice is wrong" ->
```

!!! tip "When to use"
    Reach for few-shot whenever output *shape* matters, or the task is fuzzy to
    describe but easy to demonstrate.

## Chain-of-thought: ask for reasoning

For multi-step or numerical tasks, tell the model to work through it before
answering.

```text
Work through this step by step, then give the final answer on its own line
prefixed "ANSWER:".

{problem}
```

For user-facing answers, ask it to *reason internally, then give a clean
conclusion* so users see the result, not the working.

## Persona / role: set expertise and posture

```text
You are a senior security engineer reviewing code for vulnerabilities. You are
thorough and sceptical, and you explain risks in plain language for non-experts.
```

The role shifts vocabulary, depth and priorities.

## Decomposition: break a big ask into steps

Either ask for the steps explicitly, or [chain prompts](anatomy-of-a-good-prompt.md)
where each output feeds the next.

```text
Plan before you write. First list the sections this report needs and one line
on each. Wait for my "go", then write section by section.
```

## Structured output: get clean data

Ask for a precise shape (usually JSON) so code — or a person — can use it directly.

```text
Return ONLY valid JSON matching:
{
  "sentiment": "positive" | "neutral" | "negative",
  "themes": ["string"],
  "urgent": boolean
}
No prose, no markdown fences.
```

See [structured output & tools](../working-with-ai/structured-output-and-tools.md).

## Guardrail phrases: bound behaviour

Small lines that prevent big problems:

- *"Use only the information provided above."* — reduces hallucination.
- *"If you are not sure, say 'I don't know'."* — licenses honesty.
- *"Cite the source line for each claim."* — enables verification.
- *"Do not include any personal data in your answer."* — safety.
- *"If the request is outside {scope}, say so and stop."* — keeps it on-mission.

!!! warning "Prompt phrases are not security"
    These improve behaviour but can be overridden by a determined user or a
    [prompt injection](../production-governance/security.md). For real enforcement
    use [guardrails](../production-governance/guardrails-and-safety.md) outside the
    model.

## Refinement: iterate in the chat

You rarely nail it first try. Steer:

- *"Good, but make it half the length and lead with the risk."*
- *"Redo bullet 3 — it's not supported by the source."*
- *"Give me two more options in a different tone."*

## See also

- **[Anatomy of a good prompt](anatomy-of-a-good-prompt.md)** — the base structure.
- **[Meta-prompting](meta-prompting.md)** — get AI to apply these for you.
- Glossary: **few-shot**, **chain-of-thought**, **ReAct**, **structured output**, **persona prompting**.
