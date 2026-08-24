---
tags:
  - L200
  - vibe-coding
---

# AI coding tools <span class="lvl lvl-200">L200</span>

## In plain terms

AI coding assistants come in a few shapes. You don't need them all — you need to
know the *kinds*, so you can pick the right one for the job.

## How it works — the landscape

| Shape | What it does | Feels like |
| --- | --- | --- |
| **Autocomplete** | Suggests the next line/block as you type | A smarter tab-complete |
| **Chat-in-editor** | Ask questions / request edits in a side panel | Pair-programmer on call |
| **Agentic / terminal** | Reads your whole project, edits many files, runs commands and tests, iterates | Delegating a task to a junior dev |
| **In-platform assistant** | The above, built into a data/AI platform and aware of your data | A colleague who knows your warehouse |

They vary in **how much context they see** (one file vs the whole repo vs your
data), **how much they can do** (suggest vs act), and **how much you review**
(every keystroke vs a batch of changes). More capability = more need for
discipline.

!!! note "The common engine"
    Under the hood these are **[harnesses](../building-with-ai/harnesses-and-meta-harnesses.md)**
    around an LLM — the assistant is the harness that feeds the model your code,
    runs the tools, and applies the edits. The quality you feel is the model *and*
    the harness together.

## How Databricks does it

- **Databricks Assistant** is the in-platform assistant: context-aware help for
  SQL, Python and notebooks, error explanations, and code generation grounded in
  your **Unity Catalog** tables — right where your data already lives.
- For building and shipping apps, you can pair a coding assistant (in the
  workspace or your local editor) with **Databricks Apps** for hosting and
  **Databricks Asset Bundles** for repeatable deploys (see
  [Shipping on Databricks](shipping-on-databricks.md)).
- Assistants can also help write the AI features themselves — prompts, AI
  Functions, agent code — closing the loop between "building software" and
  "building AI".

## Pitfalls

!!! warning "Choosing and using tools well"
    - **More autonomy ≠ better for beginners.** An agentic tool that edits 30
      files is powerful but easy to lose control of — start smaller until you can
      review confidently.
    - **Context limits still apply.** If the tool can't see the relevant code, its
      suggestions will be off. Point it at the right files.
    - **Don't paste secrets or sensitive data** into any assistant. Use the
      platform's governed access instead.

## See also

- **[What is vibe coding?](what-is-vibe-coding.md)** — the practice.
- **[Best practices](best-practices.md)** — using any tool responsibly.
- Glossary: **AI coding assistant**, **agentic coding**, **Databricks Assistant**, **context window**.
