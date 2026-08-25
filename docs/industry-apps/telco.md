---
tags:
  - Industry Apps
---

# Telco — App Lab

The **`workshop_demo.telco`** schema is a mobile carrier: subscribers, plans,
**call detail records (CDR)**, network cells and a `churn_labels` table. Churn is
driven by dropped calls, low usage and out-of-contract status — signal that lives
in the CDR and subscriber tables, not just the base rate.

## The data at a glance

| Table | What it holds |
| --- | --- |
| `churn_labels` | Per subscriber: `churned` + 90-day features (`data_mb_90d`, `dropped_calls_90d`, `records_90d`). |
| `cdr` | Call detail records (90 days): `cell_id`, `technology`, `record_type`, `duration_seconds`, `data_mb`, `dropped`. |
| `subscribers` | `plan_id`, `region`, `activated_on`, `contract_months`, `device_brand`. |
| `plans` | `plan_name`, `monthly_price`, `included_minutes`, `included_data_gb`. |
| `network_cells` | `site_name`, `region`, `technology`, `capacity_mbps` (find congestion). |

## Featured app: Churn & Network Quality Cockpit

A cockpit that links **who's likely to churn** with **the network experience
behind it** — dropped calls, congested cells, wrong-plan usage — so a retention
team can act on causes, not just scores.

### One-shot prompt

```text
Build a Databricks App using apx (React + FastAPI) called "Churn & Network Quality Cockpit".
It reads (read-only) from workshop_demo.telco via a SQL warehouse using the Databricks SQL connector.

Backend (FastAPI), parameterized:
- GET /api/at-risk?region= -> churn_labels joined to subscribers and plans: subscriber_id, region,
  plan_name, monthly_price, contract_months, data_mb_90d, dropped_calls_90d, churned (known label);
  compute a risk score from high dropped_calls + low usage + out-of-contract; order desc.
- GET /api/subscriber/{id} -> profile + plan + 90-day usage summary from cdr (calls, minutes, data_mb,
  dropped count) and the cells they used most.
- GET /api/network/congestion -> from cdr joined to network_cells: traffic and dropped-call rate per
  cell vs capacity_mbps; flag congested cells; group by region and technology.
- GET /api/kpis?region= -> subscriber count, churn rate, ARPU (avg monthly_price), avg dropped-call rate.

Frontend (React):
- KPI tiles (churn rate, ARPU, dropped-call rate).
- An at-risk subscriber worklist with risk badge and region filter.
- A subscriber drawer: usage summary + "your worst cells" list.
- A network panel: table/heatmap of congested cells (dropped rate vs capacity), tech filter.
Aggregate in SQL; keep CDR queries bounded by time and subscriber.
```

!!! tip "Run it"
    Reads only. `cdr` is high-volume — always aggregate by subscriber/cell/time
    window in SQL.

## Enhancements

| # | Enhancement | What it adds | Data / Databricks feature |
| --- | --- | --- | --- |
| 1 | **ML churn model** | Classifier on 90-day CDR + subscriber features. | `churn_labels` + `cdr` → Model Serving |
| 2 | **Plan-fit upsell** | Match actual usage to the best plan (over/under-provisioned). | `cdr` usage vs `plans` allowances |
| 3 | **Network congestion map** | Cell-level dropped-call and load hotspots. | `cdr`, `network_cells.capacity_mbps` |
| 4 | **Dropped-call root cause** | Correlate drops with older `technology` and cells. | `cdr.dropped`, `network_cells.technology` |
| 5 | **Renewal targeting** | Prioritise out-of-contract, high-value subscribers. | `subscribers.contract_months`, `plans` |
| 6 | **Ask-your-network (Genie)** | "Which region has the highest dropped-call rate on 4G?" | [Genie Space](../working-with-ai/genie-ask-your-data.md) |

## More app ideas for telco

| App | What it does |
| --- | --- |
| **Network Congestion Map** | Ranks cells by load vs capacity and dropped-call rate. |
| **Plan Optimiser / Upsell** | Recommends the right plan from real usage patterns. |
| **Dropped-Call Root Cause** | Attributes drops to technology, cell and region. |
| **Contract Renewal Targeting** | Finds out-of-contract subscribers worth retaining. |
| **Win-Back Campaign** | Profiles churned subscribers for targeted win-back offers. |

## Concepts & labs

- [Why we evaluate](../working-with-ai/why-we-evaluate.md) ·
  [AI over your data](../working-with-ai/ai-over-your-data.md) ·
  [Genie](../working-with-ai/genie-ask-your-data.md) ·
  [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)
</content>
