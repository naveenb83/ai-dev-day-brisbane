---
tags:
  - L100
---

# Navigate by level

The **L100 → L400** scale is borrowed from the way training content is often
graded. It describes **depth**, not importance — an L100 idea can matter more to
your job than an L400 one. Use it to find the right *starting* altitude.

## What each level means

### <span class="lvl lvl-100">L100</span> — Foundations

**Who it's for:** anyone. No technical background assumed.

**What you'll get:** the mental models — what AI, machine learning and
generative AI are, what a large language model does, what a "prompt" is, and why
these tools sometimes get things confidently wrong.

**You'll know you're ready to move on when** you can explain, to a colleague,
the difference between *training* a model and *using* one.

### <span class="lvl lvl-200">L200</span> — Working with AI

**Who it's for:** people who want to *apply* AI to real work — analysts,
domain experts, product folk, curious managers.

**What you'll get:** how to prompt well, how AI can answer questions over *your*
data (retrieval / RAG), what vector search is, how to get reliable structured
output, and why we evaluate AI instead of trusting it blindly.

**You'll know you're ready to move on when** you can take a real task and decide
whether it needs a plain prompt, retrieval over your documents, or something more.

### <span class="lvl lvl-300">L300</span> — Building with AI

**Who it's for:** builders — engineers, data scientists, technical PMs.

**What you'll get:** what an *agent* is (a model that can use tools, remember,
and take steps), how agents are wired together, what "harnesses" and multi-agent
systems are, and the frameworks that run them in production.

**You'll know you're ready to move on when** you can sketch how an agent would
solve a task end-to-end, including where it might fail.

### <span class="lvl lvl-400">L400</span> — Production & governance

**Who it's for:** people taking AI to production and keeping it there.

**What you'll get:** evaluation at scale, observability and tracing, guardrails,
security and data protection, and controlling cost and performance — the
"well-architected" concerns.

**You'll know you're set when** you can say what would have to be true before you'd
let an AI feature touch real customers and real data.

## A worked example: the same idea at four levels

Take one topic — **"AI answering questions over your documents"** — and watch it
deepen:

| Level | The same idea, deeper |
| --- | --- |
| <span class="lvl lvl-100">L100</span> | *"You can ask the AI questions about your own files, not just general knowledge."* |
| <span class="lvl lvl-200">L200</span> | *This is **retrieval-augmented generation (RAG)**: we find the relevant chunks of your documents and give them to the model as context.* |
| <span class="lvl lvl-300">L300</span> | *You build a pipeline: chunk documents → embed them → store in a **vector index** → retrieve top matches → feed to the model, with an agent deciding when to search.* |
| <span class="lvl lvl-400">L400</span> | *You **evaluate** retrieval quality and groundedness, **trace** every call, guard against prompt injection and data leakage, and watch cost per query in production.* |

Same concept. Four audiences. That's the whole idea of this site.

## See also

- **[How to use this site](index.md)**
- **[Prerequisites](prerequisites.md)** — before the hands-on labs
