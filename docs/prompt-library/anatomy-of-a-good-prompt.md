---
tags:
  - L200
  - prompting
---

# Anatomy of a good prompt <span class="lvl lvl-200">L200</span>

## The five parts

Almost every strong prompt contains these, in roughly this order:

| # | Part | Question it answers | Example |
| --- | --- | --- | --- |
| 1 | **Role** | Who should the model be? | "You are a careful financial analyst." |
| 2 | **Context / input** | What should it work from? | "Here is the Q3 report: «…»" |
| 3 | **Task** | What exactly should it do? | "List the three largest cost increases." |
| 4 | **Constraints** | What are the rules? | "Use only the figures given. If a number is missing, say 'not stated'." |
| 5 | **Output format** | What should the answer look like? | "A markdown table: Item, Q2, Q3, Change." |

!!! tip "Add a sixth for anything factual: the honesty rule"
    Tell the model **what to do when it doesn't know**: *"If the answer isn't in
    the provided text, say 'I don't know' — do not guess."* This single line
    prevents a huge share of hallucinations.

## A reusable skeleton

Copy this and fill the blanks:

```text
You are a {ROLE — expertise + posture, e.g. "meticulous data analyst who
double-checks numbers"}.

Your task: {TASK — one clear sentence of what to produce}.

Work only from the material below. If something isn't stated, say so rather
than guessing.

--- MATERIAL ---
{CONTEXT / INPUT — the document, data, or details}
--- END MATERIAL ---

Constraints:
- {constraint 1, e.g. "Audience: a time-poor executive."}
- {constraint 2, e.g. "Length: max 5 bullet points."}
- {constraint 3, e.g. "Tone: plain, no jargon."}

Output format:
{FORMAT — exact shape, e.g. "Markdown bullets, each starting with the metric name
in bold."}
```

## Why order and structure matter

- **Put the task and rules where they won't get lost.** State the task up front
  *and* keep constraints together; don't bury "in one sentence" at the end of a
  wall of text.
- **Separate instructions from input** with clear delimiters (`--- MATERIAL ---`,
  triple backticks, or XML-like tags). It stops the model confusing your data for
  your instructions — and blunts some [prompt injection](../production-governance/security.md).
- **Be specific about the output.** "A table with these columns" beats "summarise
  it" every time, and makes the result usable by a person *or* a program.

## A worked build

Watch a weak prompt grow:

=== "Weak"

    ```text
    Summarise this feedback.
    ```

=== "Better"

    ```text
    Summarise this customer feedback in 5 bullet points.
    ```

=== "Strong"

    ```text
    You are a product analyst. From the customer feedback below, produce:
    1. The top 3 themes, each with a one-line description and how many comments
       mention it.
    2. The single most urgent issue.
    Use only the feedback provided. If sentiment is unclear, mark it "mixed".

    Output: a markdown table for the themes, then a bold "Most urgent:" line.

    --- FEEDBACK ---
    «paste feedback»
    --- END FEEDBACK ---
    ```

The strong version fixes the role, the exact deliverables, the counting, the
uncertainty rule, and the format. Same model — far better, more reliable answer.

## See also

- **[Prompt patterns](prompt-patterns.md)** — techniques to slot into the skeleton.
- **[Templates](templates.md)** — ready-made versions by use case.
- Glossary: **prompt engineering**, **delimiters**, **system prompt**, **structured output**.
