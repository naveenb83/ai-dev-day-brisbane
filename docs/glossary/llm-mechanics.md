---
tags:
  - L100
  - L200
---

# Glossary — LLM mechanics

How large language models actually work. See also
[Core concepts](core-concepts.md) and [Prompting](prompting-terms.md).

**Large language model (LLM)**
:   A model trained on huge amounts of text that generates language by predicting
    the next chunk of text, one piece at a time. The engine behind chat assistants.

**Token**
:   The small pieces of text an LLM reads and writes — roughly ¾ of a word each.
    Models process and are priced by tokens, not words.

**Tokenisation**
:   The process of splitting text into tokens before the model sees it.

**Context window**
:   The maximum amount of text (in tokens) a model can consider at once — your
    prompt, the conversation, and any pasted documents must all fit. When a chat
    "forgets", something fell out of the window.

**Prompt**
:   The input you send the model — instructions plus question and any context.

**Completion / response**
:   What the model generates back.

**System / user / assistant messages**
:   The three roles in a chat: the **system** message sets standing rules and
    persona; **user** messages are what the person says; **assistant** messages are
    the model's replies (fed back as context).

**System prompt**
:   The standing instructions that define the model's role and rules for a whole
    conversation.

**Embedding**
:   A list of numbers (a *vector*) that represents the **meaning** of a piece of
    text, so similar meanings get similar numbers. Powers semantic search and RAG.

**Vector**
:   An ordered list of numbers. An embedding is a vector; "vectors" is shorthand for
    the numeric representations of meaning.

**Transformer**
:   The neural-network architecture behind modern LLMs, built around *attention*.

**Attention / self-attention**
:   The mechanism that lets a model weigh which earlier tokens matter most when
    producing the next one — how it "keeps track" of context.

**Autoregressive**
:   Generating output one token at a time, each new token conditioned on all the
    previous ones. Why longer answers take longer.

**Temperature**
:   A dial for randomness. Low (≈0) = focused, consistent, repeatable (good for
    facts); high (≈1) = varied, creative.

**Top-p (nucleus) / top-k sampling**
:   Other dials controlling how the next token is chosen — restricting choices to
    the most probable options. Like temperature, they trade focus for variety.

**Logits / probabilities**
:   The raw scores the model assigns to each possible next token before one is
    picked. Sampling settings act on these.

**Max tokens**
:   A cap on how long the response can be. Too low and answers get cut off.

**Stop sequence**
:   A string that tells the model to stop generating when it produces it — used to
    bound output.

**Hallucination**
:   A confident, fluent, **made-up** answer — a fabricated fact, citation or number.
    The defining risk of LLMs. Mitigated by grounding and evaluation.

**Grounding**
:   Anchoring a model's answer in provided, trustworthy information (your documents,
    query results) rather than its memory. The main defence against hallucination.

**Knowledge cut-off**
:   The date a model's training data ends. It won't reliably know anything newer
    unless you supply it in the prompt.

**Fine-tuning** · **Distillation** · **Quantisation**
:   Ways to adapt or shrink models — *fine-tuning* specialises behaviour;
    *distillation* trains a small model to imitate a big one; *quantisation*
    compresses a model (lower-precision numbers) to run cheaper/faster with a small
    quality trade-off. See [Core concepts](core-concepts.md).

**Multimodal**
:   Able to handle more than one data type — e.g. take an image plus text and
    answer in text.

**Time to first token (TTFT)**
:   How long until the model starts responding. Low TTFT + streaming makes a system
    *feel* fast even if the full answer takes a while.

**Tokens per second**
:   Generation speed once it starts. Higher = faster answers.

**Streaming**
:   Sending the answer token-by-token as it's generated, so the user sees it appear
    live rather than waiting for the whole thing.

**Speculative decoding**
:   A speed-up where a small model drafts tokens that a big model quickly verifies —
    faster generation at the same quality.
