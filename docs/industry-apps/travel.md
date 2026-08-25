---
tags:
  - Industry Apps
---

# Travel & Hospitality — App Lab

The **`workshop_demo.travel`** schema is a travel seller: customers with loyalty
tiers, **bookings** with margins, booking components, destinations and a
`cancellation_labels` table. Cancellations are driven by lead time, product type
and loyalty — real signal — and margins vary sharply by product.

## The data at a glance

| Table | What it holds |
| --- | --- |
| `bookings` | `destination_code`, `product_type`, `channel`, `lead_time_days`, `gross_value`, `margin_pct`, `margin_amount`. |
| `cancellation_labels` | Per booking: `cancelled`, `cancelled_at`, `cancellation_reason`, `refund_amount`. |
| `customers` | `loyalty_tier`, `corporate_account`, `home_city`, `first_booked_on`. |
| `booking_items` | Components (`component_type`, `supplier_name`, `item_amount`) — don't sum to `gross_value` (reconciliation target). |
| `destinations` | `country`, `city`, `route_type`, `typical_flight_hours`. |

## Featured app: Booking Cancellation Risk & Margin Dashboard

A revenue app that flags **bookings likely to cancel** (short lead time, flights
vs packages, tier), quantifies the **margin and refund exposure**, and shows
where cancellations concentrate by destination and product.

### One-shot prompt

```text
Build a Databricks App using apx (React + FastAPI) called "Cancellation Risk & Margin Dashboard".
It reads (read-only) from workshop_demo.travel via a SQL warehouse using the Databricks SQL connector.

Backend (FastAPI), parameterized:
- GET /api/at-risk?product_type=&channel= -> bookings joined to customers, destinations and
  cancellation_labels: booking_id, destination city/country, product_type, lead_time_days, passengers,
  gross_value, margin_amount, loyalty_tier, corporate_account, cancelled (known label); compute a
  cancellation risk score from short lead_time + product_type + non-loyal/individual; order by
  margin-at-risk desc.
- GET /api/booking/{id} -> full detail: customer, destination, booking_items (component_type,
  supplier_name, item_amount) and reconciliation vs gross_value.
- GET /api/kpis?from=&to= -> bookings, cancellation rate, gross value, total margin, refund exposure.
- GET /api/breakdown -> cancellation rate and margin by product_type and by destination country.

Frontend (React):
- KPI tiles (cancellation rate, margin, refund exposure).
- An at-risk bookings table with risk badge, margin-at-risk, and product/channel filters.
- A booking drawer showing components and a reconciliation flag when items != gross_value.
- A breakdown chart: cancellation rate and margin by product type.
Aggregate in SQL; keep it responsive.
```

!!! tip "Run it"
    Reads only. `booking_items` deliberately don't reconcile to `gross_value` —
    that's the data-quality target, surface it rather than hide it.

## Enhancements

| # | Enhancement | What it adds | Data / Databricks feature |
| --- | --- | --- | --- |
| 1 | **ML cancellation model** | Trained classifier on lead time, product, loyalty. | `cancellation_labels` + `bookings` → Model Serving |
| 2 | **Dynamic pricing by segment** | Suggest price/margin by tier and lead time. | `bookings.margin_pct`, `customers.loyalty_tier` |
| 3 | **Lead-time revenue optimisation** | Show how margin/cancellation vary with `lead_time_days`. | `bookings` |
| 4 | **Loyalty tier ROI** | Value each tier by margin, cancellation and repeat rate. | `customers.loyalty_tier`, `bookings` |
| 5 | **Reconciliation checker** | Flag bookings whose items don't sum to `gross_value`. | `booking_items` vs `bookings.gross_value` |
| 6 | **Ask-your-bookings (Genie)** | "Which destinations have the highest cancellation rate?" | [Genie Space](../working-with-ai/genie-ask-your-data.md) |

## More app ideas for travel

| App | What it does |
| --- | --- |
| **Dynamic Pricing Engine** | Recommends price/margin by segment, lead time and product. |
| **Destination Demand Forecast** | Projects bookings by destination and season. |
| **Loyalty Tier ROI** | Quantifies the value and behaviour of each loyalty tier. |
| **Ancillary & Package Upsell** | Finds cross-sell from `booking_items` component mix. |
| **Corporate Account Performance** | Tracks volume, margin and cancellations for corporate clients. |

## Concepts & labs

- [Why we evaluate](../working-with-ai/why-we-evaluate.md) ·
  [AI over your data](../working-with-ai/ai-over-your-data.md) ·
  [Genie](../working-with-ai/genie-ask-your-data.md) ·
  [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)
</content>
