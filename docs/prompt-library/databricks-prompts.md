---
tags:
  - L200
  - L300
  - prompting
---

# Databricks-flavoured prompts <span class="lvl lvl-300">L300</span>

The same prompting craft, applied to the specific places you'll write prompts on
Databricks. The [anatomy](anatomy-of-a-good-prompt.md) and
[patterns](prompt-patterns.md) all still apply.

## Genie: instructions & example queries

Genie's accuracy comes mostly from **how you describe your data**, not clever
phrasing. Treat its configuration as prompting-for-data:

**General instructions for a Genie Space:**

```text
You answer questions about {business area} using the tables provided.
- "Revenue" means {exact definition / which column}.
- "Active customer" means {definition}.
- Default the time period to the last complete month unless asked otherwise.
- Amounts are in {currency}; always show the currency.
- If a question can't be answered from these tables, say so — don't invent.
```

**Certify example queries** (question → trusted SQL) for the questions that matter,
so Genie has proven patterns to follow. Add clear **column descriptions** and
define shared terms as **metric views**. See
[Genie](../working-with-ai/genie-ask-your-data.md).

## AI Functions: prompts inside SQL

With `ai_query` and friends, the prompt is an argument. Keep it explicit:

```sql
SELECT
  review_id,
  ai_query(
    'your-endpoint',
    'Classify this review as PROMOTER, PASSIVE or DETRACTOR based only on its ' ||
    'content. Reply with one word.\n\nReview: ' || review_text
  ) AS nps_bucket
FROM reviews;
```

Prefer the purpose-built functions when they fit — they're simpler and more
reliable:

```sql
SELECT
  ticket_id,
  ai_classify(body, ARRAY('billing','bug','feature','other')) AS category,
  ai_summarize(body, 25)                                      AS summary
FROM support_tickets;
```

See [AI over your data](../working-with-ai/ai-over-your-data.md).

## Agent system prompts

An agent's system prompt sets its job, its limits, and how it should use tools.
A solid skeleton:

```text
You are {agent role} for {organisation/domain}. Your job is to {goal}.

Tools available: {list each tool and when to use it}.

Rules:
- Prefer tools/retrieved data over your own knowledge for anything factual.
- Never take an action that {writes / sends / spends} without explicit user
  confirmation.
- If a tool fails or returns nothing, say so — do not fabricate a result.
- Answer only within {scope}; if asked outside it, decline politely.
- Cite the data/source behind factual claims.

Answer style: {concise / structured / tone}.
```

Pair this with [guardrails](../production-governance/guardrails-and-safety.md) —
the prompt sets intent; guardrails enforce it. See
[Building agents on Databricks](../building-with-ai/building-agents-on-databricks.md).

## Vibe-coding prompts (Databricks Assistant & friends)

Give the assistant the context it can't guess:

```text
Context: Databricks workspace, {Python/SQL}, data in Unity Catalog table
{catalog.schema.table} (columns: {…}). Use the Databricks SDK / Spark as
appropriate; do not hard-code secrets — read from a secret scope.

Task: {what you want built}.

Constraints: {perf, libraries allowed, style}. Add error handling and a quick
test. Explain how to run it. Don't use APIs you're unsure exist.
```

See [Best practices](../vibe-coding/best-practices.md).

## The through-line

Whether it's a Genie instruction, an `ai_query` string, an agent system prompt or
a coding ask, the same rules hold: **be explicit about role, source, constraints
and format, and tell it what to do when unsure.**

## See also

- **[Templates](templates.md)** — general-purpose versions.
- **[Meta-prompting](meta-prompting.md)** — get help writing these.
- Glossary: **Genie Space**, **AI Functions**, **`ai_query`**, **system prompt**, **metric view**.
