---
tags:
  - L100
---

# What is AI, really? <span class="lvl lvl-100">L100</span>

## In plain terms

"AI" (artificial intelligence) is a broad umbrella for **computer systems that do
things we'd normally call "intelligent"** — recognising a face, understanding a
sentence, recommending a film, writing an email. It's not one technology; it's a
goal, pursued lots of different ways.

The words you keep hearing are really **nested inside each other**, like Russian
dolls:

```
┌─────────────────────────────────────────────────────────┐
│ Artificial Intelligence (AI)                              │
│  "make computers do smart-seeming things"                 │
│                                                           │
│   ┌─────────────────────────────────────────────────┐   │
│   │ Machine Learning (ML)                             │   │
│   │  "learn patterns from data instead of being       │   │
│   │   hand-coded with rules"                          │   │
│   │                                                   │   │
│   │   ┌───────────────────────────────────────────┐  │   │
│   │   │ Deep Learning                              │  │   │
│   │   │  "ML using large neural networks"          │  │   │
│   │   │                                            │  │   │
│   │   │   ┌────────────────────────────────────┐  │  │   │
│   │   │   │ Generative AI                       │  │  │   │
│   │   │   │  "creates new content: text,        │  │  │   │
│   │   │   │   images, audio, code"              │  │  │   │
│   │   │   └────────────────────────────────────┘  │  │   │
│   │   └───────────────────────────────────────────┘  │   │
│   └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## How it works

**Machine learning (ML)** is the big shift that made modern AI work. Instead of a
programmer writing rules ("if the email contains 'free money', mark as spam"), you
show the computer *thousands of examples* and it **learns the patterns itself**.
The output of that learning is a **model** — a file full of numbers that captures
the patterns.

- **Traditional software:** rules in → answers out. A human writes every rule.
- **Machine learning:** examples in → a model out. The model then turns new
  inputs into answers.

**Deep learning** is ML done with **neural networks** — layers of simple maths
loosely inspired by how brains connect neurons. Given enough data and computing
power, deep networks learn astonishingly rich patterns (this is what cracked
image recognition and speech).

**Generative AI** is the newest layer. Earlier ML mostly *classified* or
*predicted* ("is this spam? yes/no", "what will sales be?"). Generative models
**produce new content** — a paragraph, a picture, a snippet of code — that didn't
exist before. The **large language model** behind ChatGPT-style tools is
generative AI for text.

!!! note "Two words you'll hear a lot"
    - **Predictive / classical ML** — predicts a number or a category (fraud
      score, churn yes/no, next month's demand). Still hugely useful; most
      business ML is this.
    - **Generative AI (GenAI)** — creates content and holds a conversation.
      That's the star of this event, but it doesn't replace the other kind.

## How Databricks does it

Databricks is a **data and AI platform**, so all four layers live in one place:

- **Classical ML** — train and manage predictive models (fraud, churn, forecasts)
  with built-in tooling and experiment tracking.
- **Deep learning** — run the same, at scale, on GPUs when you need them.
- **Generative AI** — use ready-made large language models through **Foundation
  Model APIs**, try them in the **AI Playground**, and build apps and agents with
  **Mosaic AI**.

The umbrella name for the AI capabilities is **Mosaic AI**. You'll meet the
specific pieces (Genie, AI Functions, Vector Search, Agent Bricks) as we go —
each is just one of these layers made easy to use.

## Pitfalls

!!! warning "AI is not magic, and not one thing"
    - Don't assume "AI" means a chatbot. A demand forecast is AI too.
    - Generative AI is powerful *and* imperfect — it can be fluent and wrong at
      the same time. We cover that in
      **[Why AI gets things wrong](why-ai-gets-things-wrong.md)**.

## See also

- **[Large language models](large-language-models.md)** — the engine behind GenAI.
- **[How Databricks does it](how-databricks-does-it.md)** — the platform view.
- Glossary: **model**, **machine learning**, **generative AI**, **neural network**.
