---
tags:
  - L100
  - governance
---

# Why AI gets things wrong <span class="lvl lvl-100">L100</span>

## In plain terms

Modern AI is fluent, fast and confident — and that's exactly the trap. **A wrong
answer looks just as polished as a right one.** Understanding *why* it errs is the
single most important thing a beginner can learn, because it tells you when to
trust it and when to check.

## How it works

A few root causes explain most mistakes:

**1. It predicts plausible text, not verified truth.** An LLM generates what
*tends to follow* — the most likely next words. Usually that's correct because
correct things are common in its training. But when it doesn't know, it will still
produce confident-sounding words. That's a **hallucination**: a fabricated fact,
citation or number, delivered with total confidence.

**2. Knowledge cut-off.** The model only learned from data up to a certain date.
Ask about anything newer — a policy that changed last week, yesterday's results —
and it either won't know or will guess.

**3. It has no live access to your world by default.** Out of the box it can't see
your database, your files or the internet. Ask "what's our refund policy?" and a
bare model will *invent* a plausible one. (The fix is to *give* it the real
document — that's RAG.)

**4. It's sensitive to how you ask.** Ambiguous prompts produce ambiguous answers.
Leading questions can nudge it toward the answer you hinted at.

**5. Bias in, bias out.** It learned from human text, so it can reflect the biases
in that text.

!!! danger "The cardinal rule"
    **Never treat an AI answer as automatically true — especially for facts,
    numbers, names, dates, legal or medical content, or anything you'll act on.**
    Verify against a trusted source. Fluency is not evidence.

## How Databricks does it

The platform is built to *reduce* these failure modes rather than pretend they
don't exist:

- **Ground answers in your data.** With **RAG** and **Vector Search**, the model
  answers from *your* documents, and **Genie** answers questions by running real
  SQL against your governed tables — not from memory.
- **Measure quality instead of hoping.** **Mosaic AI evaluation** and **MLflow**
  let you score answers for correctness and *groundedness* (did it actually use
  the source?) — the L400 discipline.
- **Trace everything.** You can see exactly what the model was shown and why it
  answered as it did, so a wrong answer is debuggable, not mysterious.
- **Govern the data.** **Unity Catalog** controls what data a model or user can
  even see, reducing the chance of leaking or misusing sensitive information.

## Pitfalls

!!! warning "Habits that keep you safe"
    - Ask the model to **cite its source** or **say when it's unsure** — and treat
      "I'm not sure" as a *good* answer.
    - For anything factual, **give it the facts** in the prompt rather than
      relying on its memory.
    - **Keep a human in the loop** for consequential decisions.

## See also

- **[Large language models](large-language-models.md)** — why prediction ≠ truth.
- **[Embeddings & vectors](embeddings-and-vectors.md)** — how we feed it real content.
- Glossary: **hallucination**, **knowledge cut-off**, **grounding**, **groundedness**, **bias**.
