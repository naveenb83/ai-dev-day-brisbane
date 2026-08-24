---
tags:
  - L100
---

# Glossary — Core AI & ML concepts

The foundational vocabulary. See also
[LLM mechanics](llm-mechanics.md) for the language-model specifics.

**Artificial intelligence (AI)**
:   The broad field of getting computers to do things we'd call "intelligent" —
    understanding language, recognising images, making decisions. An umbrella
    term, not a single technology.

**Machine learning (ML)**
:   Building systems that **learn patterns from data** instead of being programmed
    with explicit rules. The dominant approach to modern AI.

**Deep learning**
:   Machine learning using **neural networks** with many layers. Behind most recent
    breakthroughs, including large language models.

**Neural network**
:   A model loosely inspired by the brain — layers of simple mathematical units
    whose connection strengths (weights) are learned from data.

**Generative AI (GenAI)**
:   AI that **creates new content** — text, images, audio, code — rather than only
    classifying or predicting. The focus of most of today's excitement.

**Predictive / classical ML**
:   ML that outputs a number or category (fraud score, churn yes/no, demand
    forecast). Most existing business ML is this kind; still hugely valuable.

**Model**
:   The output of training — a file of learned numbers (parameters) that turns
    inputs into outputs. "The model" is the thing you run to get predictions or
    generations.

**Parameters / weights**
:   The billions of numbers inside a model that encode what it learned. "70B
    parameters" is a rough size label; bigger is not always better.

**Training**
:   The (usually one-time, expensive) process of learning a model's parameters from
    data. Contrast with *inference*.

**Inference**
:   **Using** a trained model to get an answer. This is what happens every time you
    send a prompt — it does not change the model.

**Pre-training**
:   The initial, massive training of a foundation model on broad data. Done by
    model makers; rarely by end users.

**Fine-tuning**
:   Extra training on top of a pre-trained model to specialise it (a style, format
    or narrow skill). Changes behaviour, not reliably facts — use *RAG* for facts.
    → *On Databricks:* Mosaic AI Model Training.

**Foundation model**
:   A large, general model pre-trained on broad data that can be adapted to many
    tasks (e.g. the big LLMs). → *On Databricks:* served via Foundation Model APIs.

**Base vs. instruct model**
:   A **base** model just continues text; an **instruct** (instruction-tuned) model
    is trained to follow instructions and chat. You almost always want the instruct
    version for assistants.

**Supervised learning**
:   Learning from **labelled** examples (input → known correct output), e.g. emails
    labelled spam/not-spam.

**Unsupervised learning**
:   Finding structure in **unlabelled** data (e.g. clustering similar customers) —
    no correct answers provided.

**Reinforcement learning (RL)**
:   Learning by **trial and reward** — an agent takes actions and is rewarded for
    good outcomes. Underlies techniques like RLHF.

**Dataset**
:   The collection of examples used to train or evaluate a model. Quality and
    representativeness matter enormously.

**Label / ground truth**
:   The known-correct answer for an example, used to train (supervised) or grade
    (evaluation) a model.

**Feature**
:   An input variable a model uses (e.g. "customer age"). In classical ML you often
    engineer features; LLMs mostly work from raw text.

**Overfitting**
:   When a model memorises its training data instead of learning general patterns —
    it looks great in training and fails on new data.

**Generalisation**
:   The ability to perform well on **new, unseen** inputs — the actual goal of
    learning.

**Benchmark**
:   A standard test used to compare models (e.g. reasoning or coding benchmarks).
    Useful signal, but rarely matches *your* task — validate on your own data.

**Modality / multimodal**
:   A **modality** is a type of data (text, image, audio, video). A **multimodal**
    model handles more than one — e.g. reads an image and answers in text.

**Diffusion model**
:   The model family behind most AI **image generation** — it turns noise into an
    image guided by a prompt.

**Mixture of experts (MoE)**
:   A model design that routes each input to a subset of specialised sub-networks
    ("experts"), giving large capacity at lower running cost per token.

**Distillation**
:   Training a small, cheap model to imitate a larger one on your task — a common
    way to cut cost and latency. See [cost & performance](cost-performance-serving-terms.md).
