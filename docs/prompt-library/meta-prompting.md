---
tags:
  - L200
  - L300
  - prompting
---

# Meta-prompting <span class="lvl lvl-200">L200</span>

## In plain terms

**Meta-prompting is using AI to write and improve your prompts.** Stuck on how to
ask? Don't agonise — ask the model to help you ask. It's one of the highest-return
tricks in this whole library, and it means you never start from a blank page.

## How it works — three moves

### 1. Ask it to write the prompt

Describe your goal in whatever words you have, and let the model draft a proper
prompt:

```text
I want a prompt that will {your goal, in plain words}.
Write me a strong, reusable prompt for that. Include a clear role, the inputs it
should expect (as {placeholders}), explicit constraints, and an output format.
Then explain your choices in one line each.
```

### 2. Ask it to critique and improve a prompt

Paste a prompt that isn't quite working:

```text
Here is a prompt I'm using. Critique it for clarity, ambiguity and missing
constraints, then give me an improved version. Point out anything that could
cause it to hallucinate or go off-format.

--- PROMPT ---
{paste your prompt}
--- END PROMPT ---
```

### 3. Ask it to interview you first

The best move when you're not even sure what you want:

```text
I want to build a prompt for {rough goal}, but I'm not sure of the details.
Ask me up to 6 questions, one batch, that you need answered to write an excellent
prompt. After I answer, write the prompt.
```

This flips it around: the model gathers the role, audience, constraints and
format *from you*, then assembles a far better prompt than you'd have written cold.

!!! example "Why it works so well"
    A good prompt needs role, context, constraints and format. You often know your
    *goal* but not how to express all four. The model is excellent at turning "I
    want X" into a structured brief — so let it do the structuring.

## Levelling up

- **Generate the few-shot examples.** Ask the model to invent good input→output
  examples for a [few-shot prompt](prompt-patterns.md).
- **Make it a template.** "Now turn that into a reusable template with
  `{placeholders}` for the parts that change."
- **Optimise systematically.** For prompts that ship in software, teams use
  automated **prompt optimisation** — the system tries variations against an
  [evaluation set](../working-with-ai/why-we-evaluate.md) and keeps what scores
  best. → *On Databricks:* MLflow supports evaluation-driven prompt optimisation.

## Pitfalls

!!! warning "Still your job to check"
    - **Review the generated prompt** — it can add constraints you didn't want.
    - **Test it** on real inputs before trusting it, especially for anything
      factual.
    - **Watch for over-engineering** — a bloated prompt isn't better; keep it as
      simple as works.

## See also

- **[Anatomy of a good prompt](anatomy-of-a-good-prompt.md)** — what "good" it's aiming for.
- **[Templates](templates.md)** — where your meta-prompted prompts can live.
- Glossary: **meta-prompting**, **prompt template**, **few-shot**, **evaluation set**.
