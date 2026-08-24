---
tags:
  - L100
---

# Lab 0 — Setup check <span class="lvl lvl-100">L100</span>

**~10 minutes**

## Goal

Confirm the three things every other lab needs: you can **sign in**, you can **run
SQL**, and you can **use AI features**. Fix any access problem now, with a
facilitator on hand — not mid-way through Lab 4.

## You'll learn

- Where things live in a Databricks workspace.
- That your account has the access the labs assume.

## Steps

1. **Sign in.** Open the workspace URL your facilitator gave you and log in. You
   should land on the workspace home.
2. **Find your bearings.** In the left-hand navigation, note the areas you'll use:
   **SQL** (editor / warehouses), **Catalog** (your data, under Unity Catalog),
   and the **AI / Machine Learning** area (Playground, Serving).
3. **Confirm a SQL warehouse.** Open the **SQL editor**. Check there's a running
   (or startable) **SQL warehouse** selected. Run:
   ```sql
   SELECT current_user() AS me, current_catalog() AS catalog;
   ```
   You should see your username and a catalog name.
4. **Confirm your workspace/schema.** Ask your facilitator which **catalog and
   schema** you should write to (e.g. `training.<your_name>`). Create a scratch
   table to prove you can write:
   ```sql
   CREATE TABLE IF NOT EXISTS {your_catalog}.{your_schema}.hello_ai (id INT, note STRING);
   INSERT INTO {your_catalog}.{your_schema}.hello_ai VALUES (1, 'it works');
   SELECT * FROM {your_catalog}.{your_schema}.hello_ai;
   ```
5. **Confirm AI access.** Run a tiny AI Function to prove models are reachable
   from SQL:
   ```sql
   SELECT ai_gen('Say hello to the Brisbane AI Dev Day in one short sentence.') AS greeting;
   ```
   If you get a friendly sentence back, your AI access works. 🎉

## Expected result

- Query in step 3 returns your user + catalog.
- Step 4 creates and reads a table.
- Step 5 returns a generated sentence.

## If something fails

!!! warning "Don't push through — flag it"
    - **No warehouse / can't run SQL** → ask a facilitator to assign one.
    - **Permission denied on the table** → confirm the catalog/schema you're
      allowed to write to.
    - **AI function error** → your workspace may need AI features enabled or a
      different function name; a facilitator can sort it.

## Stretch

- Try `SELECT ai_analyze_sentiment('I love this event');` and see what comes back.

## Concepts

- **[Prerequisites](../start-here/prerequisites.md)** ·
  **[How Databricks does it](../foundations/how-databricks-does-it.md)** ·
  Glossary: **Unity Catalog**, **AI Functions**.
