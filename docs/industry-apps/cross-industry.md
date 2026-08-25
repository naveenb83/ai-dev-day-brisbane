---
tags:
  - Industry Apps
---

# Cross-Industry (Starter) — App Lab

The **`workshop_demo.cross_industry`** schema is deliberately generic:
customers, products, sales and web clickstream. It's the **fastest place to
start** — no domain knowledge required — and the patterns you build here
(funnels, cohorts, segmentation) transfer to every other industry.

## The data at a glance

| Table | What it holds |
| --- | --- |
| `customers` | `customer_id`, name, city, country, `plan`, `signed_up_on`. |
| `products` | `product_id`, `category`, `cost_price`, `unit_price` (margin is computable). |
| `sales` | Order lines: `customer_id`, `product_id`, `quantity`, `amount`, `ordered_at`, `channel` (weekly seasonality). |
| `web_events` | Clickstream: `session_id`, `event_type`, `occurred_at`, `device`, `path` (funnel + sessionisation). |

## Featured app: Funnel & Cohort Explorer

A product-analytics app that turns raw clickstream and orders into two views
every growth team wants: a **conversion funnel** (view → cart → purchase from
`web_events.event_type`) and a **cohort-retention grid** (repeat-purchase rate by
signup month from `customers` + `sales`).

### One-shot prompt

```text
Build a Databricks App using apx (React + FastAPI) called "Funnel & Cohort Explorer".
It reads (read-only) from workshop_demo.cross_industry via a SQL warehouse using the
Databricks SQL connector.

Backend (FastAPI), parameterized:
- GET /api/funnel?from=&to=&device= -> counts of distinct sessions per event_type stage
  from web_events (e.g. page_view -> add_to_cart -> checkout -> purchase), returned in stage
  order with step-to-step conversion %.
- GET /api/cohorts -> from customers + sales: cohort by signed_up_on month; for each cohort,
  the % of customers with a purchase in months 0..N after signup (retention triangle).
- GET /api/kpis -> revenue (sum amount), orders, unique buyers, avg order value, top channel.
- GET /api/revenue-trend?grain=week -> revenue over time from sales.ordered_at.

Frontend (React):
- KPI tiles across the top.
- A horizontal funnel chart with conversion % between stages, plus a device filter.
- A cohort-retention heatmap (cohort month down, period across, colour = retention %).
- A revenue trend line chart with a weekly/monthly toggle.
Do all aggregation in SQL; keep the UI clean and responsive.
```

!!! tip "Run it"
    Reads only. Grant the app SP `SELECT` on `workshop_demo.cross_industry`.

## Enhancements

| # | Enhancement | What it adds | Data / Databricks feature |
| --- | --- | --- | --- |
| 1 | **RFM segmentation** | Bucket customers by Recency/Frequency/Monetary into actionable segments. | `sales` aggregates per `customer_id` |
| 2 | **Product affinity** | "Customers who bought X also bought Y" from co-occurrence in orders. | `sales` grouped by `order_id` |
| 3 | **Revenue forecast** | Project next 8 weeks of revenue with confidence bands. | `ai_forecast` over `sales.ordered_at` |
| 4 | **Channel attribution** | Compare revenue and conversion by `channel` and `device`. | `sales.channel`, `web_events.device` |
| 5 | **Churn/inactivity flag** | Flag customers with no orders in N days for win-back. | `sales` recency per customer |
| 6 | **Ask-your-metrics (Genie)** | Natural-language questions over the whole schema. | [Genie Space](../working-with-ai/genie-ask-your-data.md) |

## More app ideas for cross-industry

| App | What it does |
| --- | --- |
| **RFM Segmentation Studio** | Interactive R/F/M scoring with drag-able thresholds and segment sizes. |
| **Product Affinity Recommender** | Surfaces top cross-sell pairs and a "recommended for" lookup by product. |
| **Cohort Retention Dashboard** | Retention triangles sliced by plan, country or acquisition channel. |
| **Sessionisation & Drop-off** | Rebuilds sessions from `web_events` and finds where users abandon. |
| **Revenue Forecaster** | Weekly revenue projection with seasonality and scenario sliders. |

## Concepts & labs

- [AI over your data](../working-with-ai/ai-over-your-data.md) ·
  [Genie](../working-with-ai/genie-ask-your-data.md) ·
  [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)
</content>
