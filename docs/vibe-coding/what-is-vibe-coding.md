---
tags:
  - L200
  - vibe-coding
---

# What is vibe coding? <span class="lvl lvl-200">L200</span>

## In plain terms

**Vibe coding** is building software by **describing what you want in plain
language** and letting an AI assistant write and change the code — you steer, it
types. Instead of remembering exact syntax, you say *"add a page that lists orders
and lets me mark them shipped,"* review what the AI produces, and iterate.

The term started half-jokingly — coding by "vibes", trusting the flow — but the
serious version is a real shift in how software gets made: **the human sets
intent, judgement and taste; the AI handles the mechanical typing and lookup.**

## How it works

A typical loop looks like this:

```
   You describe a goal ─►  AI proposes code/edits ─►  You review & run it
        ▲                                                     │
        └──────────  refine: "close, but also…"  ◄────────────┘
```

- You work in an **AI coding assistant** (in your editor, terminal or workspace).
- It can see your project, write new files, edit existing ones, run commands and
  read the errors — then fix them.
- You review each change, run it, and give feedback in natural language.

It shines for: **prototypes and demos**, boilerplate, unfamiliar languages or
APIs, one-off scripts and data wrangling, tests, and explaining or refactoring
existing code.

!!! note "Who it's for"
    Not just engineers. A business analyst can stand up a working prototype to
    show an idea; an engineer can move several times faster on the boring parts.
    The skill that matters shifts from *typing code* to **describing intent
    clearly and reviewing output critically** — which is why the
    [Prompt Library](../index.md) matters here too. *(Added in a later section.)*

## How Databricks does it

- The **Databricks Assistant** brings vibe-coding help *inside the workspace* —
  writing and fixing SQL, Python and notebook code, explaining errors, and aware
  of your tables and code context.
- You can build full applications and host them as **Databricks Apps**, and use
  AI assistants (in the workspace or your local editor) to generate the app code.
- Because it's on the platform, what you build can reach your **governed data and
  models** directly — the prototype isn't a toy disconnected from real data.

## Pitfalls

!!! danger "Vibes are not a quality bar"
    Fast-and-loose is fine for a throwaway prototype. It is **not** fine for
    anything real. AI-written code can be subtly wrong, insecure, or built on
    made-up APIs — and it looks confident either way. Everything in
    **[Best practices](best-practices.md)** exists because of this. **Review
    every change. Test it. Never ship code you don't understand.**

## See also

- **[AI coding tools](ai-coding-tools.md)** — what to use.
- **[Best practices](best-practices.md)** — doing it safely.
- Glossary: **vibe coding**, **AI coding assistant**, **prompt**, **code review**.
