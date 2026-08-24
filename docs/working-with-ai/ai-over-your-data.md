---
tags:
  - L200
---

# AI over your data <span class="lvl lvl-200">L200</span>

## In plain terms

So far we've talked about asking an AI *one* question at a time. But a lot of real
value is **applying AI to a whole table at once** — classify 100,000 support
tickets, summarise every product review, extract the invoice number from 50,000
scanned documents. You want AI as a **column in your data**, not a chat window.

## How it works

The pattern is "AI as a function": you write something close to ordinary SQL, and
each row gets sent to a model and comes back enriched.

```sql
-- pseudo-code shape (see the Databricks section for the real functions)
SELECT
  ticket_id,
  ai_classify(body, ARRAY('billing','bug','feature','other')) AS category,
  ai_summarize(body, 20)                                       AS short_summary
FROM support_tickets;
```

The mental shift: instead of writing rules to categorise text, you **describe the
categories and let the model decide** — at the scale of your warehouse.

## How Databricks does it

Databricks provides **AI Functions** — SQL functions that call models for you, so
analysts (not just ML engineers) can use AI:

| Function | What it does |
| --- | --- |
| `ai_query()` | Send any prompt to any serving endpoint from SQL |
| `ai_classify()` | Sort text into labels you supply |
| `ai_extract()` | Pull named fields out of text |
| `ai_summarize()` | Condense long text |
| `ai_analyze_sentiment()` | Positive / negative / neutral |
| `ai_translate()` | Translate between languages |
| `ai_mask()` | Redact sensitive values |
| `ai_gen()` | Free-form generation from a prompt |
| `ai_parse_document()` | Turn PDFs/images into structured text |
| `ai_forecast()` | Forecast a time series |

Because they run **inside the platform**, they operate on your **governed** tables
under **Unity Catalog** — no exporting data to an outside service. You can run
them ad hoc in a SQL editor or bake them into a **pipeline** that enriches data
continuously.

!!! tip "This is often the fastest ROI in the room"
    Many "we need AI" problems are really "we have a big pile of text/PDFs and need
    it structured." A few lines of AI Functions can do that today, no app required.

## Pitfalls

!!! warning "Use responsibly"
    - **Cost scales with rows.** Running a model over millions of rows costs real
      money — test on a sample first, and pick a right-sized model.
    - **Validate the labels.** Spot-check `ai_classify` / `ai_extract` output;
      models are good, not perfect. Pair with [evaluation](why-we-evaluate.md).
    - **Mind sensitive data.** Use `ai_mask` and Unity Catalog controls when text
      may contain PII.

## Try it

:material-flask: **Lab 2** runs `ai_classify` and `ai_summarize` over a sample
table. *(Labs added in a later section.)*

## See also

- **[Genie: ask your data](genie-ask-your-data.md)** — the conversational cousin.
- **[Why we evaluate](why-we-evaluate.md)** — checking bulk AI output.
- Glossary: **AI Functions**, **`ai_query`**, **serving endpoint**, **Unity Catalog**.
