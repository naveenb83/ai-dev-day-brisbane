---
tags:
  - L200
---

# Lab 3 — Ask your data (Genie) <span class="lvl lvl-200">L200</span>

**~25 minutes**

## Goal

Build a **Genie Space** so anyone can ask questions of a dataset **in plain
English** and get answers backed by real SQL — and see how *curation* drives
accuracy.

## You'll learn

- That text-to-SQL trust comes from good **metadata**, not magic.
- How to add instructions and examples that make Genie reliable.

## Steps

1. **Create a small sales table** (or use one your facilitator provides):
   ```sql
   CREATE OR REPLACE TABLE {your_catalog}.{your_schema}.sales AS
   SELECT * FROM VALUES
     ('2026-06-01','QLD','Battery', 3, 4500.00),
     ('2026-06-03','NSW','Panel',  10, 8000.00),
     ('2026-07-02','QLD','Panel',   5, 4000.00),
     ('2026-07-18','VIC','Battery', 2, 3000.00),
     ('2026-08-05','QLD','Battery', 4, 6000.00)
   AS t(sale_date, state, product, units, revenue);
   ```
2. **Add descriptions** so Genie understands the columns (this is the key step):
   ```sql
   COMMENT ON TABLE {your_catalog}.{your_schema}.sales IS
     'One row per sale. revenue is in AUD.';
   ALTER TABLE {your_catalog}.{your_schema}.sales ALTER COLUMN state
     COMMENT 'Australian state/territory code (QLD, NSW, VIC, ...)';
   ALTER TABLE {your_catalog}.{your_schema}.sales ALTER COLUMN revenue
     COMMENT 'Sale amount in AUD';
   ```
3. **Create a Genie Space** (in the AI/BI or Genie area of the workspace) and add
   your `sales` table to it.
4. **Add general instructions** to the Space:
   ```text
   Answers are about product sales. "Revenue" is the revenue column in AUD.
   When asked by state, group by the state column. If a question can't be
   answered from this table, say so.
   ```
5. **Ask questions in English:**
   - "What was total revenue in QLD?"
   - "Which product sold the most units?"
   - "Show monthly revenue as a chart."
   For each, **open the generated SQL** and check it matches what you meant.
6. **Certify a good example.** Save a question→SQL pair that worked as a trusted
   example, so Genie reuses that pattern.
7. **Break it, then fix it.** Ask something ambiguous ("best state?"). Watch it
   guess. Add an instruction clarifying "best = highest revenue" and re-ask.

## Expected result

- A Genie Space that answers your questions with correct numbers, showing its
  SQL — and noticeably better answers after you add instructions/examples.

## Stretch

- Define a shared term (e.g. a "big sale" = revenue > 5000) in the instructions
  and ask about it.
- Discuss what would be needed to trust this on 50 real tables (see the Genie
  Accuracy ideas in [Genie](../working-with-ai/genie-ask-your-data.md)).

## Concepts

- **[Genie: ask your data](../working-with-ai/genie-ask-your-data.md)** ·
  **[Databricks-flavoured prompts](../prompt-library/databricks-prompts.md)** ·
  Glossary: **Genie**, **text-to-SQL**, **certified query**, **metric view**.
