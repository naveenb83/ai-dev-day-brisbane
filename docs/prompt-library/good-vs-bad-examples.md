---
tags:
  - L200
  - prompting
---

# Good vs bad examples <span class="lvl lvl-200">L200</span>

The fastest way to learn prompting is to see weak prompts fixed. Each example
shows the problem, the fix, and *why*.

## 1. The vague ask

=== "❌ Bad"

    ```text
    Write about our product.
    ```
    *Gets:* generic marketing fluff that could be about anything.

=== "✅ Good"

    ```text
    You are a B2B copywriter. Write a 100-word product blurb for {product},
    aimed at {audience}, highlighting {top 2 benefits}. Tone: confident, plain.
    Avoid buzzwords like "revolutionary" and "synergy".
    ```
    *Why:* role + audience + length + focus + tone + explicit no-gos.

## 2. Facts without a source

=== "❌ Bad"

    ```text
    What is our refund policy?
    ```
    *Gets:* a confident, **invented** policy (the model has never seen yours).

=== "✅ Good"

    ```text
    Using ONLY the policy text below, answer: what is our refund window and what
    are the exceptions? If it's not stated, say "not specified".

    --- POLICY ---
    {paste the real policy}
    --- END POLICY ---
    ```
    *Why:* grounding in the real document + an honesty rule kills the
    hallucination.

## 3. No format, unusable output

=== "❌ Bad"

    ```text
    Pull out the key numbers from this report.
    ```
    *Gets:* a rambling paragraph you can't paste into a spreadsheet.

=== "✅ Good"

    ```text
    Extract the figures below as JSON: {"revenue": number, "growth_pct": number,
    "headcount": number}. Use null if a figure is missing. Return JSON only.

    --- REPORT ---
    {paste}
    --- END REPORT ---
    ```
    *Why:* a precise schema makes the output usable by a person or a program.

## 4. Creativity and precision in one breath

=== "❌ Bad"

    ```text
    Give me an exciting, creative summary of these exact quarterly figures.
    ```
    *Gets:* flair that fudges the numbers.

=== "✅ Good"

    ```text
    Step 1: State the figures exactly as given, as a table.
    Step 2: Then write a 2-sentence upbeat caption — without changing any number.
    ```
    *Why:* separates the precise task from the creative one so neither corrupts
    the other.

## 5. Everything at once

=== "❌ Bad"

    ```text
    Analyse this data, find problems, fix them, write the report, and make slides.
    ```
    *Gets:* a shallow attempt at everything, mastery of nothing.

=== "✅ Good"

    ```text
    We'll do this in steps. Step 1 only: list the top 3 data-quality problems you
    see, with evidence. Wait for my go before proposing fixes.
    ```
    *Why:* [decomposition](prompt-patterns.md) — one focused step beats a
    scattered mega-request, and you stay in control.

## 6. Leading the witness

=== "❌ Bad"

    ```text
    This campaign was a huge success, right? Summarise why it worked.
    ```
    *Gets:* flattering confirmation, ignoring what failed.

=== "✅ Good"

    ```text
    Assess this campaign objectively from the data below. Cover what worked AND
    what didn't. If the data is mixed or insufficient, say so.
    ```
    *Why:* removes the bias nudge and licenses an honest, balanced answer.

## The pattern behind every fix

> Add a **role**, **ground it in real input**, **say exactly what you want and in
> what format**, **give it permission to say "I don't know"**, and **split
> creative from precise**.

## See also

- **[Anatomy of a good prompt](anatomy-of-a-good-prompt.md)** — the structure these use.
- **[Templates](templates.md)** — the good versions, ready to fill in.
