---
tags:
  - L200
  - prompting
---

# Templates <span class="lvl lvl-200">L200</span>

Copy, paste, fill the `{blanks}`. These use the
[five-part anatomy](anatomy-of-a-good-prompt.md) so they're reliable out of the
box. Adjust freely.

## Summarise

```text
You are a {domain} analyst. Summarise the text below for {audience}.
Focus on {what matters — e.g. risks, decisions, actions}.
Use only the text provided; if something isn't stated, omit it.

Output: {N} bullet points, each ≤ 20 words, most important first.

--- TEXT ---
{paste}
--- END TEXT ---
```

## Extract structured data

```text
Extract the following fields from the document. Return ONLY valid JSON:
{
  "{field1}": "string or null",
  "{field2}": "string or null",
  "{amount}": "number or null"
}
If a field is not present, use null. Do not guess.

--- DOCUMENT ---
{paste}
--- END DOCUMENT ---
```

## Classify

```text
Classify each item into exactly one: {LABEL_A}, {LABEL_B}, {LABEL_C}.

Examples:
"{example 1}" -> {LABEL_A}
"{example 2}" -> {LABEL_B}

Return a table: item | label. If ambiguous, choose the closest and add "(low
confidence)".

Items:
{list}
```

## Draft (email / message / doc)

```text
You are {role}. Write a {type, e.g. email} to {recipient} that {goal}.
Tone: {professional / warm / direct}. Length: {constraint}.
Include: {must-have points}. Avoid: {no-gos}.
End with {call to action}.

Context you can use:
{background}
```

## Rewrite / improve

```text
Rewrite the text below to be {clearer / shorter / more formal / plain-English}.
Keep the meaning and all facts. Do not add new claims.
Return the rewrite only.

--- TEXT ---
{paste}
--- END TEXT ---
```

## Explain (to a specific audience)

```text
Explain {topic} to {audience — e.g. a non-technical executive}.
Assume no prior knowledge. Use one everyday analogy. Max {N} sentences.
End with why it matters to them.
```

## Brainstorm / options

```text
Act as a {role}. Give me {N} distinct {ideas/approaches} for {goal}.
For each: a one-line description, the main benefit, and the main risk.
Aim for genuinely different options, not variations of one.
```

## Analyse / decide

```text
You are a {role}. Using only the data below, answer: {question}.
Show your reasoning briefly, then give a clear recommendation.
State your confidence (high/medium/low) and what would change your mind.
If the data is insufficient, say what's missing.

--- DATA ---
{paste}
--- END DATA ---
```

## Q&A over provided content (mini-RAG by hand)

```text
Answer the question using ONLY the sources below. Quote the source for each
claim. If the answer isn't in the sources, say "Not found in the provided
sources."

Question: {question}

--- SOURCES ---
[1] {source 1}
[2] {source 2}
--- END SOURCES ---
```

## Code (vibe coding)

```text
Language/stack: {e.g. Python, FastAPI}.
Goal: {what the code should do}.
Inputs: {…}. Outputs: {…}. Constraints: {perf, style, libs allowed}.
Write the code, then briefly explain how it works and how to run it.
Include basic error handling and a test. Don't use libraries you're unsure exist.
```

See [Best practices](../vibe-coding/best-practices.md) before shipping generated
code.

## See also

- **[Prompt patterns](prompt-patterns.md)** — techniques inside these templates.
- **[Databricks-flavoured prompts](databricks-prompts.md)** — platform-specific versions.
