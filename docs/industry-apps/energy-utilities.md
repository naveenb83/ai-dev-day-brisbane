---
tags:
  - Industry Apps
---

# Energy & Utilities — App Lab

The **`workshop_demo.energy_utilities`** schema covers a utility's core:
supply accounts, smart meters, **half-hourly consumption**, tariffs and network
outages — with a `is_vulnerable` flag that changes who you protect first.

## The data at a glance

| Table | What it holds |
| --- | --- |
| `meter_readings` | Half-hourly `consumption_kwh` for a ~2,000-meter sample over ~2 years. |
| `meters` | `meter_id` → `customer_id`, `meter_type`, `tariff_code`, `region`. |
| `customers` | Supply accounts with `account_type`, `region`, `is_vulnerable`. |
| `tariffs` | `tariff_code`, `unit_rate`, `standing_charge` (cost consumption). |
| `outages` | `cause`, `started_at`, `restored_at`, `duration_minutes`, `customers_affected` (log-normal). |

## Featured app: Smart-Meter Consumption & Anomaly Explorer

An operations app that plots a meter's **half-hourly load profile**, costs it
against its tariff, and flags **anomalous days** — consumption that deviates
from the meter's own daily-and-seasonal pattern (a naive average won't cut it).

### One-shot prompt

```text
Build a Databricks App using apx (React + FastAPI) called "Meter Consumption & Anomaly Explorer".
It reads (read-only) from workshop_demo.energy_utilities via a SQL warehouse using the
Databricks SQL connector.

Backend (FastAPI), parameterized:
- GET /api/meters?region= -> meters joined to customers: meter_id, region, tariff_code,
  is_vulnerable, account_type.
- GET /api/meter/{meter_id}/profile?from=&to= -> half-hourly consumption_kwh from meter_readings,
  plus a rolling average baseline (e.g. same-half-hour mean over prior weeks).
- GET /api/meter/{meter_id}/anomalies -> days where daily kWh deviates > X standard deviations
  from the meter's own seasonal/day-of-week baseline; return date, actual, expected, z-score.
- GET /api/meter/{meter_id}/cost -> monthly cost = consumption * tariffs.unit_rate + standing_charge.
- GET /api/kpis?region= -> total kWh, avg daily load, count of anomalous meters, % vulnerable.

Frontend (React):
- KPI tiles + a region filter.
- A meter picker; selecting one shows a half-hourly load-profile line chart (actual vs baseline).
- An anomaly table with severity, and a monthly cost bar chart.
- Highlight vulnerable-customer meters with a badge.
Aggregate in SQL; keep charts responsive for dense time series.
```

!!! tip "Run it"
    Reads only. `meter_readings` is dense — always filter by `meter_id` and a
    date range in the query, never pull it all to the browser.

## Enhancements

| # | Enhancement | What it adds | Data / Databricks feature |
| --- | --- | --- | --- |
| 1 | **Demand forecast** | Forecast regional load for the next 14 days. | `ai_forecast` over `meter_readings` |
| 2 | **Vulnerable-customer outage priority** | Rank live/likely outages by vulnerable customers affected. | `outages`, `customers.is_vulnerable` |
| 3 | **Tariff optimiser** | Show each customer the cheapest eligible tariff for their profile. | `meter_readings` × `tariffs` |
| 4 | **Outage impact war-room** | Total customer-minutes lost by cause and region. | `outages.duration_minutes`, `customers_affected` |
| 5 | **Demand-response targeting** | Find high-peak meters worth enrolling in DR programs. | peak analysis on `meter_readings` |
| 6 | **Ask-your-grid (Genie)** | "Which region had the most outage minutes last quarter?" | [Genie Space](../working-with-ai/genie-ask-your-data.md) |

## More app ideas for energy

| App | What it does |
| --- | --- |
| **Outage Impact War-Room** | Live-style board of outages ranked by customer-minutes lost and vulnerable exposure. |
| **Tariff Optimiser** | Per-customer "you could save $X on tariff Y" using their actual load profile. |
| **Demand Forecasting** | Regional load forecast with weather-free seasonality and scenario sliders. |
| **Vulnerable Customer Care** | A care dashboard prioritising priority-service customers during disruptions. |
| **Load Profiling & Segmentation** | Clusters meters into load archetypes (flat, evening-peak, solar-shape). |

## Concepts & labs

- [AI over your data](../working-with-ai/ai-over-your-data.md) ·
  [Genie](../working-with-ai/genie-ask-your-data.md) ·
  [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)
</content>
