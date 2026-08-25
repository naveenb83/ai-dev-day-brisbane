---
tags:
  - Industry Apps
---

# Mining — App Lab

The **`workshop_demo.mining`** schema is a heavy-asset operation: sites, a
mobile/fixed **asset fleet**, sensor telemetry, daily production and a
`failure_labels` table (does an asset fail in the next 30 days?). Bearing temp
and vibration drift with cumulative hours, so the failure signal is genuinely in
the telemetry.

## The data at a glance

| Table | What it holds |
| --- | --- |
| `failure_labels` | Per asset: `failed_within_30d`, `failure_mode`, `downtime_hours`, `avg_bearing_temp_c`, `max_vibration_mm_s`. |
| `sensor_readings` | Asset telemetry (90 days): `engine_temp_c`, `bearing_temp_c`, `vibration_mm_s`, `oil_pressure_kpa`, `payload_tonnes`. |
| `assets` | `asset_type`, `model`, `site_id`, `operating_hours`, `replacement_value`. |
| `production_daily` | `tonnes_mined`, `tonnes_shipped`, `grade_pct`, `equipment_availability_pct`, `unplanned_downtime_hours`. |
| `sites` | `site_name`, `commodity`, `state`, `target_grade_pct`. |

## Featured app: Asset Failure Predictor (30-Day)

A reliability app that ranks the fleet by **30-day failure risk**, trends the
tell-tale sensors (bearing temperature, vibration) for a selected asset, and ties
predicted downtime to production impact.

### One-shot prompt

```text
Build a Databricks App using apx (React + FastAPI) called "Asset Failure Predictor".
It reads (read-only) from workshop_demo.mining via a SQL warehouse using the Databricks SQL connector.

Backend (FastAPI), parameterized:
- GET /api/fleet?site_id=&asset_type= -> failure_labels joined to assets and sites: asset_id,
  asset_type, model, site_name, commodity, operating_hours, avg_bearing_temp_c, max_vibration_mm_s,
  failed_within_30d (known label); compute a risk score from bearing temp + vibration + operating_hours;
  order desc.
- GET /api/asset/{id}/telemetry?from=&to= -> bearing_temp_c, vibration_mm_s, oil_pressure_kpa over
  time from sensor_readings, downsampled to hourly averages.
- GET /api/site/{id}/production -> production_daily: tonnes_mined, tonnes_shipped, grade_pct,
  equipment_availability_pct, unplanned_downtime_hours over time.
- GET /api/kpis?site_id= -> assets at risk, avg availability %, total unplanned downtime hours,
  tonnes shipped this period.

Frontend (React):
- KPI tiles (assets at risk, availability, downtime).
- A fleet table with a risk badge and site/asset-type filters.
- Asset detail: line chart of bearing temperature + vibration with a risk threshold line.
- Site production panel: tonnes mined vs shipped bar chart and availability trend.
Downsample telemetry in SQL; keep it responsive.
```

!!! tip "Run it"
    Reads only. `failure_labels` is deliberately imbalanced — evaluate any model
    on precision/recall, not accuracy.

## Enhancements

| # | Enhancement | What it adds | Data / Databricks feature |
| --- | --- | --- | --- |
| 1 | **ML failure model** | Rolling-feature classifier for 30-day failure. | `sensor_readings` + `failure_labels` → Model Serving |
| 2 | **Production forecast** | Project tonnes mined/shipped by site. | `ai_forecast` over `production_daily` |
| 3 | **Downtime attribution** | Break unplanned downtime out by asset and failure mode. | `failure_labels`, `production_daily` |
| 4 | **Fleet utilisation** | Operating-hours and availability heatmap across the fleet. | `assets.operating_hours`, `production_daily` |
| 5 | **Grade tracking** | Compare head `grade_pct` to `target_grade_pct` by site. | `production_daily`, `sites` |
| 6 | **Ask-your-mine (Genie)** | "Which haul trucks are most at risk this week?" | [Genie Space](../working-with-ai/genie-ask-your-data.md) |

## More app ideas for mining

| App | What it does |
| --- | --- |
| **Production Planning** | Forecasts tonnage and flags sites tracking below target grade. |
| **Fleet Utilisation Analyser** | Utilisation and availability by asset type, model and site. |
| **Equipment Health Trending** | Long-run bearing/vibration trends with maintenance annotations. |
| **Downtime Root-Cause** | Attributes lost tonnes to failure modes and assets. |
| **Capacity Planning** | Models throughput ceilings from availability and fleet mix. |

## Concepts & labs

- [Why we evaluate](../working-with-ai/why-we-evaluate.md) ·
  [AI over your data](../working-with-ai/ai-over-your-data.md) ·
  [Genie](../working-with-ai/genie-ask-your-data.md) ·
  [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)
</content>
