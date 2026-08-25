---
tags:
  - Industry Apps
---

# Industry App Labs

Every other section of this site teaches a **concept**. This one turns concepts
into **shipped apps**. Each page below takes a real, industry-specific dataset
that already lives in your workshop Databricks workspace and shows you how to
build a working **Databricks App** on top of it — starting from a single
copy-paste prompt.

The data lives in the **`workshop_demo`** Unity Catalog — **one schema per
industry**, all **fully synthetic** and **read-only**.

## How each page works

Each industry page gives you:

1. **The data at a glance** — the key tables you'll build on.
2. **A featured app** — one concrete app worth building, with a **one-shot
   prompt** you paste into your AI coding tool to generate the whole thing. We
   target **apx (React + FastAPI)** — see
   [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md).
3. **~6 enhancements** — a table of ways to make the app smarter once it runs.
4. **~5 more app ideas** — other apps the same data supports, in a table.

!!! tip "Running the prompts"
    The apps read directly from `workshop_demo`, which is **read-only** — fine
    for dashboards and read apps. If your app needs to **write** (save notes,
    annotations, model scores), **deep-clone** the tables into your own schema
    first:
    ```sql
    CREATE TABLE my_catalog.my_schema.orders
      DEEP CLONE workshop_demo.retail.orders;
    ```
    Your app's service principal needs `SELECT` on whatever it reads — grant it,
    or clone into a schema you own.

!!! warning "Synthetic data only"
    Everything in `workshop_demo` is generated — no real customers, patients or
    accounts. Never wire these apps to real, sensitive data in a shared training
    workspace.

## Pick your industry

<div class="grid cards" markdown>

-   :material-car: **[Automotive & Mobility](automotive-mobility.md)**

    ---

    Vehicles, dealers, service, warranty, telematics and EV charging across a
    Toyota/Lexus parc.

-   :material-cart: **[Cross-Industry (Starter)](cross-industry.md)**

    ---

    Generic customers, products, sales and web clickstream — the fastest place
    to start.

-   :material-flash: **[Energy & Utilities](energy-utilities.md)**

    ---

    Smart-meter readings, tariffs, outages and vulnerable-customer care.

-   :material-bank: **[Financial Services](financial-services.md)**

    ---

    Accounts, card transactions, fraud labels, loans and arrears.

-   :material-hospital-box: **[Healthcare](healthcare.md)**

    ---

    Encounters, diagnoses, claims and 30-day readmission outcomes.

-   :material-factory: **[Manufacturing](manufacturing.md)**

    ---

    Machines, 5-minute sensor telemetry, work orders and defects.

-   :material-movie: **[Media & Entertainment](media.md)**

    ---

    Streaming viewers, subscriptions, view events and churn.

-   :material-pickaxe: **[Mining](mining.md)**

    ---

    Asset fleet, sensor telemetry, daily production and 30-day failure labels.

-   :material-city: **[Public Sector](public-sector.md)**

    ---

    Citizen service requests, permits, budgets and SLA compliance.

-   :material-store: **[Retail](retail.md)**

    ---

    Stores, products, orders, order items and daily inventory.

-   :material-cash-multiple: **[Superannuation](superannuation.md)**

    ---

    Members, contributions, holdings and rollout (retention) outcomes.

-   :material-signal: **[Telco](telco.md)**

    ---

    Subscribers, plans, call detail records, network cells and churn.

-   :material-airplane: **[Travel & Hospitality](travel.md)**

    ---

    Bookings, cancellations, destinations, loyalty tiers and margins.

</div>

## Before you build

- **New to Databricks Apps?** Do [Lab 5 — Build an agent](../labs/lab-5-build-an-agent.md)
  and read [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md) first.
- **Want the app to answer questions in English?** Almost every app here pairs
  well with a [Genie Space](../working-with-ai/genie-ask-your-data.md) over the
  same schema.
- **Adding AI to a column?** [AI over your data](../working-with-ai/ai-over-your-data.md)
  and [Lab 2 — AI Functions](../labs/lab-2-ai-functions.md) show the SQL
  `ai_*` functions the enhancements lean on.
</content>
