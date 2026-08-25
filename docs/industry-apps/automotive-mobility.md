---
tags:
  - Industry Apps
---

# Automotive & Mobility — App Lab

The **`workshop_demo.automotive_mobility`** schema is the richest in the catalog:
20 tables covering the full vehicle lifecycle for a synthetic Toyota/Lexus parc —
from build and sale through ownership, service, parts, warranty, recalls and
connected telemetry (including EV charging and battery health).

## The data at a glance

| Table | What it holds |
| --- | --- |
| `vehicle360` | One row per VIN: specs, current owner, service/warranty history, open recalls, `battery_soh_pct`. |
| `customer360` | One row per owner: `lifetime_value`, `service_visits`, `service_defection_flag`, `next_best_action`. |
| `parts360` | One row per part: 12-month consumption, inventory, and `claims_per_1000_vehicles` (R/1000). |
| `warranty_claims` | Claims traceable to repair order and part, with `failure_code` and `total_amount`. |
| `service_orders` / `service_order_parts` | Repair orders (`pay_type` = warranty vs customer) and parts consumed. |
| `telematics_events` | ~60 days of connected-vehicle telemetry (`dtc_code`, `state_of_charge_pct`, harsh braking). |

## Featured app: Warranty Early-Warning Console

A dashboard for the quality team that surfaces **parts failing earlier than they
should**. It ranks parts by `claims_per_1000_vehicles`, shows the cost and volume
trend of warranty claims, and lets an analyst drill from a suspect part into the
specific repair orders, failure codes and suppliers behind it.

### One-shot prompt

```text
Build a Databricks App using apx (React + FastAPI) called "Warranty Early-Warning Console".
It reads (read-only) from the Unity Catalog schema workshop_demo.automotive_mobility via a
SQL warehouse, using the Databricks SQL connector and the app's SQL warehouse.

Backend (FastAPI), parameterized queries:
- GET /api/parts/at-risk  -> from parts360: part_number, description, supplier_name,
  units_consumed_12m, warranty_claims_12m, claims_per_1000_vehicles, on_hand_total; ordered by
  claims_per_1000_vehicles desc; support ?min_volume= to ignore low-volume noise.
- GET /api/part/{part_number}/claims -> from warranty_claims joined to service_orders on ro_id:
  claim_date, vin, dealer_id, failure_code, parts_amount, labour_amount, total_amount, status.
- GET /api/part/{part_number}/supplier -> from parts + suppliers: supplier_name, tier,
  quality_rating, lead_time_days, superseded_by.
- GET /api/kpis -> total warranty $ (sum total_amount), claim count, top failure_code, distinct
  parts with claims_per_1000_vehicles above a threshold.

Frontend (React):
- KPI tiles: total warranty cost, open claims, worst part by R/1000.
- A sortable "at-risk parts" table with a red/amber/green severity badge on claims_per_1000_vehicles.
- A detail drawer: claims-over-time line chart + a claims table + the supplier scorecard.
- Filters for supplier tier and minimum 12-month volume.
Keep it clean, responsive, and fast (aggregate in SQL, not in the browser).
```

!!! tip "Run it"
    Reads only — no deep clone needed. Grant the app's service principal `SELECT`
    on `workshop_demo.automotive_mobility`.

## Enhancements

| # | Enhancement | What it adds | Data / Databricks feature |
| --- | --- | --- | --- |
| 1 | **Plain-English failure summaries** | Summarise the free-text `complaint` across a part's repair orders into one paragraph. | `service_orders.complaint` + `ai_query`/`ai_summarize` |
| 2 | **Early-failure prediction** | Score each part's probability of a warranty spike next quarter. | Train on `warranty_claims` history → Model Serving endpoint |
| 3 | **Supplier scorecard** | Rank suppliers by claims-per-part, quality rating and lead time. | `suppliers`, `parts360` |
| 4 | **Recall completion tracker** | Show outstanding recall work by campaign and dealer. | `recall_campaigns`, `campaign_vehicles.completed` |
| 5 | **EV battery-health watchlist** | Flag BEV/PHEV VINs with low `battery_soh_pct` for proactive outreach. | `vehicle360.battery_soh_pct`, `charging_sessions` |
| 6 | **Ask-your-warranty (Genie)** | Let non-analysts ask "which model year has the most steering claims?" in English. | [Genie Space](../working-with-ai/genie-ask-your-data.md) over the schema |

## More app ideas for automotive

| App | What it does |
| --- | --- |
| **Service Loyalty & Defection** | Targets owners who stopped servicing (`customer360.service_defection_flag`) with a `next_best_action`. |
| **EV Charging Insights** | Analyses `charging_sessions` (kWh, cost, duration) to profile EV usage and charger utilisation. |
| **Fleet Telematics Safety** | Scores drivers on `trips.driver_score` and harsh-event flags from `telematics_events`. |
| **Parts Inventory Optimiser** | Uses `parts_inventory` stockout days + `parts360` demand to recommend reorder points. |
| **Predictive DTC Monitor** | Watches `telematics_events.dtc_code` against `dtc_codes` severity to pre-empt breakdowns. |

## Concepts & labs

- [AI over your data](../working-with-ai/ai-over-your-data.md) ·
  [Genie](../working-with-ai/genie-ask-your-data.md) ·
  [Building agents on Databricks](../building-with-ai/building-agents-on-databricks.md) ·
  [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)
</content>
