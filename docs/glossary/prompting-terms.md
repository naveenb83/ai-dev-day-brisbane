---
tags:
  - L200
  - prompting
---

# Glossary — Prompting

The vocabulary of talking to models well. See the
[Prompt Library](../prompt-library/index.md) for patterns and templates.

**Prompt engineering**
:   The craft of writing inputs that reliably get good outputs — role, context,
    task, constraints and format.

**Zero-shot prompting**
:   Asking the model to do a task with **no examples** — just instructions. Works
    for straightforward tasks.

**One-shot / few-shot prompting**
:   Giving **one** or **a few** worked examples of input → desired output so the
    model copies the pattern. Great for consistent formatting and classification.

**Chain-of-thought (CoT)**
:   Prompting the model to **reason step by step** before answering. Improves
    multi-step and mathematical tasks.

**ReAct (reason + act)**
:   A pattern where a model alternates reasoning with taking actions (tool calls) —
    the backbone of many agents.

**Tree-of-thought**
:   Exploring several reasoning paths and picking the best — a more elaborate
    cousin of chain-of-thought for hard problems.

**Self-consistency**
:   Sampling several answers and taking the most common/consistent one to improve
    reliability.

**Role / persona prompting**
:   Telling the model who to be ("You are a meticulous financial analyst") to shape
    tone and focus.

**Delimiters**
:   Markers (quotes, triple backticks, XML-like tags) that separate instructions
    from input, reducing confusion and some injection risk.

**Prompt template**
:   A reusable prompt with fill-in-the-blanks for the changing parts — how prompts
    become repeatable building blocks in software.

**Prompt chaining**
:   Breaking a task into several prompts where each step's output feeds the next.

**Structured output**
:   Asking the model to return machine-readable data (usually JSON) instead of
    prose, so code can use it directly.

**JSON mode / output schema**
:   A setting/spec that forces the model's output into a defined JSON shape. See
    [structured output & tools](../working-with-ai/structured-output-and-tools.md).

**Meta-prompting**
:   Using AI to **write or improve prompts** — asking a model to draft, critique or
    optimise a prompt for you.

**Negative prompting**
:   Telling the model what **not** to do or include. Useful, but weaker than
    positive instructions and not a security control.

**Grounded prompting**
:   Including the source material in the prompt and instructing "use only this" —
    the prompt-level habit that reduces hallucination.

**Guardrail**
:   A check around the model that enforces rules on inputs/outputs, independent of
    the prompt. See [governance/safety](governance-safety-security-terms.md).
