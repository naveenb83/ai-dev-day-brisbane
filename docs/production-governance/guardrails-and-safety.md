---
tags:
  - L400
  - governance
---

# Guardrails & safety <span class="lvl lvl-400">L400</span>

## In plain terms

A capable model will, if asked, happily produce things you don't want it to —
off-topic answers, unsafe content, leaked data, made-up promises. **Guardrails**
are the checks around the model that keep its **inputs and outputs inside the
lines** you've defined. Think of them as the seatbelts and speed limiter, not the
driver.

## How it works

Guardrails sit on both sides of the model:

```
   User input ─► [INPUT guardrails] ─► model/agent ─► [OUTPUT guardrails] ─► user
                  block / sanitise                     check / filter / redact
```

**Input guardrails** — before the model sees it:

- **Topic / scope limits** — refuse or redirect off-mission requests.
- **Injection & abuse detection** — spot attempts to hijack the system (see
  [Security](security.md)).
- **PII detection** — catch sensitive data going *in*.

**Output guardrails** — before the user sees it:

- **Content safety filters** — block toxic, unsafe or disallowed content.
- **Groundedness / factuality checks** — flag answers not supported by sources.
- **PII redaction** — mask sensitive data on the way *out*.
- **Format & policy validation** — enforce structure and business rules.

Guardrails can be **rules** (fast, deterministic — regex, allow/deny lists,
schemas) or **model-based** (a classifier or LLM judging safety/relevance). Most
real systems combine both.

!!! note "Guardrails ≠ prompt instructions"
    Telling the model "don't discuss competitors" in the prompt is a *request* it
    can be talked out of. A guardrail is an *independent check* outside the model
    that enforces the rule regardless of what the model says. Defence in depth: use
    both.

**Alignment** is the model-maker's broader effort (via techniques like
[RLHF](../building-with-ai/model-customization.md)) to make models helpful,
honest and harmless by default. Guardrails are *your* application-level layer on
top — you can't rely on the base model's alignment alone for your specific rules.

## How Databricks does it

- **AI Functions** like `ai_mask` help detect and redact PII in text.
- **Mosaic AI** supports safety guardrails on serving/inference, and **MLflow**
  judges (safety, groundedness, guideline-adherence) let you *measure* whether
  guardrails are working.
- **Unity Catalog** enforces the hard boundary — what data the model can reach at
  all (see [Governance](governance.md)) — so the strongest guardrail is often "it
  never had access in the first place".

## Pitfalls

!!! warning "Guardrail failure modes"
    - **Prompt-only 'guardrails'** are bypassable — enforce outside the model too.
    - **Over-blocking** frustrates users (false positives); tune and measure.
    - **Under-blocking** on the risky path (actions, PII, safety) is dangerous;
      err strict there.
    - **Set-and-forget.** Attacks and usage evolve — monitor and update.

## See also

- **[Security](security.md)** — the adversarial threats guardrails defend against.
- **[Responsible AI](responsible-ai.md)** — the bigger safety picture.
- Glossary: **guardrail**, **content moderation**, **PII**, **alignment**, **RLHF**.
