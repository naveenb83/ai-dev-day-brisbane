---
tags:
  - Industry Apps
---

# Manufacturing — App Lab

The **`workshop_demo.manufacturing`** schema is a factory-floor dataset:
machines, **5-minute sensor telemetry**, production work orders and quality
defects. Temperature and vibration drift upward with wear, so rolling features
genuinely predict defects — this is a real predictive-maintenance sandbox.

## The data at a glance

| Table | What it holds |
| --- | --- |
| `sensor_readings` | 5-minute telemetry (last 104 days): `temperature_c`, `vibration_mm_s`, `spindle_rpm`, `power_kw`. |
| `work_orders` | Production runs: `units_planned` vs `units_produced`, `shift`, `duration_minutes`. |
| `defects` | Raised against work orders: `defect_type`, `severity`, `units_affected`, `shift`. |
| `machines` | `machine_type`, `plant`, `line`, `rated_throughput_per_hour`. |

## Featured app: Predictive Maintenance & OEE Dashboard

A plant dashboard that trends **machine health** (rising temperature/vibration),
overlays **defect spikes**, and computes an **OEE-style yield gap**
(`units_produced` vs `units_planned`) so a supervisor can act before quality
slips.

### One-shot prompt

```text
Build a Databricks App using apx (React + FastAPI) called "Predictive Maintenance & OEE Dashboard".
It reads (read-only) from workshop_demo.manufacturing via a SQL warehouse using the Databricks
SQL connector.

Backend (FastAPI), parameterized:
- GET /api/machines?plant= -> machines with latest health: join machines to the most recent
  sensor_readings (avg temperature_c, vibration_mm_s over last 24h) and a wear trend flag.
- GET /api/machine/{id}/telemetry?from=&to= -> time series of temperature_c and vibration_mm_s
  from sensor_readings, downsampled sensibly (e.g. hourly averages) for charting.
- GET /api/machine/{id}/defects -> defects joined to work_orders: detected_at, defect_type,
  severity, units_affected, shift.
- GET /api/kpis?plant= -> yield gap % (1 - sum(units_produced)/sum(units_planned)), defect rate,
  count of machines trending hot, worst line.
- GET /api/shift-comparison -> defect rate and yield gap by shift.

Frontend (React):
- KPI tiles (yield gap, defect rate, machines at risk).
- A machine list with health badges (temp/vibration trend) and a plant filter.
- A detail view: dual-axis line chart (temperature + vibration) with defect markers overlaid.
- A shift-comparison bar chart (defects tend to rise on night shift).
Downsample dense telemetry in SQL; keep charts smooth.
```

!!! tip "Run it"
    Reads only. `sensor_readings` is high-frequency — always aggregate by time
    bucket in SQL before returning to the browser.

## Enhancements

| # | Enhancement | What it adds | Data / Databricks feature |
| --- | --- | --- | --- |
| 1 | **Defect-risk model** | Predict next-shift defect probability from rolling sensor features. | `sensor_readings` + `defects` → Model Serving |
| 2 | **Yield-gap root cause** | Attribute lost units to machine, line and shift. | `work_orders`, `defects` |
| 3 | **Shift performance** | Compare output and quality across shifts. | `work_orders.shift`, `defects.shift` |
| 4 | **Downtime attribution** | Estimate downtime from planned-vs-produced gaps. | `work_orders.duration_minutes` |
| 5 | **Sensor anomaly alerts** | Flag machines breaching temp/vibration thresholds now. | `sensor_readings` rolling stats |
| 6 | **Ask-your-plant (Genie)** | "Which line has the worst defect rate this month?" | [Genie Space](../working-with-ai/genie-ask-your-data.md) |

## More app ideas for manufacturing

| App | What it does |
| --- | --- |
| **Quality Defect Analytics** | Pareto of defect types and severity by line, plant and shift. |
| **Shift Performance Board** | Head-to-head output and quality across shifts and crews. |
| **OEE Optimiser** | Availability × performance × quality with drill-down to the loss. |
| **Asset Replacement ROI** | Ranks machines where repair cost > replacement value trend. |
| **Sensor Anomaly Monitor** | Live-style watchlist of machines drifting out of spec. |

## Concepts & labs

- [Why we evaluate](../working-with-ai/why-we-evaluate.md) ·
  [AI over your data](../working-with-ai/ai-over-your-data.md) ·
  [Genie](../working-with-ai/genie-ask-your-data.md) ·
  [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)
</content>
