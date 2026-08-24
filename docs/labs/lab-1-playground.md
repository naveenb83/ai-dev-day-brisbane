---
tags:
  - L100
  - prompting
---

# Lab 1 — First prompts <span class="lvl lvl-100">L100</span>

**~20 minutes**

## Goal

Talk to a real LLM in the **AI Playground**, feel how a **system prompt** and
**temperature** change the answer, and turn a weak prompt into a strong one.

## You'll learn

- The system/user message split and what temperature does — made real.
- That prompt quality drives answer quality (the whole [Prompt Library](../prompt-library/index.md) in miniature).

## Steps

1. **Open the AI Playground** (in the AI / Machine Learning area of the left nav).
   Pick a chat model from the dropdown.
2. **Send a plain prompt:**
   ```text
   Summarise the benefits of solar power.
   ```
   Read the answer. Fine, but generic.
3. **Add a system prompt.** Find the system-prompt box and set:
   ```text
   You are an energy analyst writing for busy executives. Be concise, concrete,
   and lead with the biggest point. Avoid hype.
   ```
   Re-send the same user prompt. Notice the tone and focus shift.
4. **Feel temperature.** Set **temperature to 0**, send:
   ```text
   Give me a tagline for a solar startup.
   ```
   Send it **twice** — the answers should be nearly identical. Now set
   **temperature to ~0.9** and send twice more — the answers should vary. That's
   randomness in action.
5. **Weak → strong.** Send this weak prompt, note the result:
   ```text
   Write about our solar product.
   ```
   Then send a strong one and compare:
   ```text
   You are a B2B copywriter. Write a 60-word blurb for a home solar battery,
   aimed at cost-conscious homeowners. Highlight savings and reliability. Plain
   tone, no buzzwords. End with a one-line call to action.
   ```
6. **Compare models (optional).** Switch the model dropdown and re-run a prompt.
   Notice differences in speed, style and length.

## Expected result

- The system prompt visibly changes tone/focus.
- Temperature 0 ≈ repeatable; high temperature ≈ varied.
- The strong prompt gives a tighter, more useful answer than the weak one.

## Stretch

- Ask the model to **reason step by step** on a small puzzle, then to give just
  the final answer — see [chain-of-thought](../prompt-library/prompt-patterns.md).
- Add an honesty rule (*"If unsure, say so"*) and ask something it can't know;
  see if it declines.

## Concepts

- **[Prompts & completions](../foundations/prompts-and-completions.md)** ·
  **[Anatomy of a good prompt](../prompt-library/anatomy-of-a-good-prompt.md)** ·
  Glossary: **system prompt**, **temperature**, **completion**.
