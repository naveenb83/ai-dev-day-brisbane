---
tags:
  - L200
  - L300
  - vibe-coding
---

# Best practices <span class="lvl lvl-200">L200</span> <span class="lvl lvl-300">L300</span>

## In plain terms

AI can write code fast; whether that code is *good* is up to you. These are the
habits that separate people who ship reliable software with AI from people who
ship confident-looking bugs. None of them are hard — they're mostly about staying
in control.

## How it works — the ten habits

### 1. Spec before vibe
Say what you want *before* asking for code: the goal, the inputs and outputs, the
constraints, what "done" looks like. A one-paragraph brief produces dramatically
better results than "build me an app". This is prompting applied to building.

### 2. Small steps, not big bangs
Ask for one focused change at a time and run it. A 400-line dump you can't follow
is a liability; ten reviewed 40-line steps are an asset.

### 3. Review every change — understand before you accept
!!! danger "The golden rule"
    **Never accept code you don't understand.** If you can't explain what a change
    does, ask the AI to explain it, simplify it, or don't merge it. "The AI wrote
    it" is not an answer when it breaks in production.

### 4. Use version control from line one
Commit early and often (git). It's your undo button and your record of what
changed — essential when the AI makes a sweeping edit you need to unwind.

### 5. Test what matters
Ask the AI to write tests, then **read them** — do they check the real behaviour,
or trivially pass? Tests are how you keep "it worked once" from becoming "it works
every time".

### 6. Guard the secrets and the data
Never paste credentials, tokens or sensitive/customer data into a prompt. Keep
secrets in a proper secret store; use governed data access, not copy-paste.

### 7. Watch for hallucinated code
Models invent plausible-looking library names, functions and APIs that don't
exist. If it won't run or a package looks unfamiliar, verify it's real before
trusting it.

### 8. Keep a human in the loop for anything that acts
Code that deletes data, sends messages, or spends money gets extra scrutiny and,
ideally, a confirmation step. Blast radius should match your confidence.

### 9. Mind licensing and provenance
Generated code can resemble training data. For anything you'll ship, be aware of
your organisation's policy on AI-generated code and third-party licences.

### 10. Leave the campsite tidy
Ask the AI to explain, document and refactor as you go. Readable code with a clear
README is what makes a prototype *maintainable* rather than a dead end.

!!! tip "Ways of working"
    Treat the AI like a fast, eager junior teammate: brilliant at drafts, needs
    clear direction and careful review, and improves when you give specific
    feedback. You are the senior engineer in the room — even if you've never coded
    before, *you* own the judgement.

## How Databricks does it

- **Secrets** belong in Databricks **secret scopes**, never in code or prompts.
- **Governed data** access via **Unity Catalog** means your prototype uses real
  permissions, not exported spreadsheets.
- **Databricks Asset Bundles** put your project under version control and make
  deploys repeatable and reviewable — the opposite of clicking around the UI.
- **MLflow** tracks experiments and, for AI features, evaluations — so "better" is
  measured, not asserted.

## Pitfalls

!!! warning "The failure modes these prevent"
    - Shipping code nobody understands → unmaintainable, unfixable.
    - Leaked secrets/data → security incident.
    - No tests / no version control → can't tell what broke or roll back.
    - Trusting hallucinated APIs → mysterious runtime failures.

## See also

- **[From prototype to production](from-prototype-to-production.md)** — the next step.
- **[Prompt Library](../index.md)** — writing the specs and asks. *(Added later.)*
- **[Security & prompt injection](../index.md)** — for AI features. *(Added later.)*
- Glossary: **code review**, **version control**, **secret scope**, **test**, **hallucination**.
