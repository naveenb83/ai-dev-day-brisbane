---
tags:
  - Industry Apps
---

# Retail — App Lab

The **`workshop_demo.retail`** schema is a multi-store retailer: stores,
products, orders, **order items** (for baskets) and **daily inventory**. When
`on_hand` trends to zero while `units_sold` rises, you have a stockout — and
that's the app that pays for itself.

## The data at a glance

| Table | What it holds |
| --- | --- |
| `inventory_daily` | Per store/product/day: `on_hand`, `on_order`, `units_sold` (stockout signal). |
| `order_items` | `product_id`, `quantity`, `unit_price`, `line_amount`, `discount_pct` (basket analysis). |
| `orders` | Basket headers: `store_id`, `customer_id`, `ordered_at`, `channel`. |
| `products` | `category`, `brand`, `unit_cost`, `unit_price` (margin computable). |
| `stores` | `store_name`, `city`, `region`, `square_feet`. |

## Featured app: Stockout & Inventory Health Monitor

A merchandising app that flags **products about to stock out** (falling
`on_hand`, rising `units_sold`), quantifies the **at-risk revenue**, and lets a
planner drill into any store/product's inventory-vs-sales trend.

### One-shot prompt

```text
Build a Databricks App using apx (React + FastAPI) called "Inventory Health Monitor".
It reads (read-only) from workshop_demo.retail via a SQL warehouse using the Databricks SQL connector.

Backend (FastAPI), parameterized:
- GET /api/at-risk?region=&category= -> from inventory_daily (latest snapshots) joined to stores and
  products: rows where on_hand is low/zero while recent units_sold is rising; return store_name,
  product_name, category, on_hand, on_order, recent daily units_sold, and an at-risk revenue estimate
  (units_sold * unit_price); order by at-risk revenue desc.
- GET /api/trend?store_id=&product_id= -> inventory_daily time series: on_hand, on_order, units_sold.
- GET /api/kpis?region= -> out-of-stock SKU count, stores affected, at-risk revenue,
  inventory turnover by category (units_sold vs avg on_hand).
- GET /api/stores -> store list for filters.

Frontend (React):
- KPI tiles (out-of-stock SKUs, stores affected, at-risk revenue).
- An at-risk table with a severity badge and region/category filters, sortable by at-risk revenue.
- A detail chart: on_hand vs units_sold over time for a selected store/product (stockout crossing highlighted).
- An inventory-turnover bar chart by category.
Aggregate in SQL; keep it responsive.
```

!!! tip "Run it"
    Reads only. To let planners set reorder overrides, deep-clone a
    `reorder_overrides` table into your own schema and write there.

## Enhancements

| # | Enhancement | What it adds | Data / Databricks feature |
| --- | --- | --- | --- |
| 1 | **Demand forecast** | Per-SKU/store sales forecast to drive reorder points. | `ai_forecast` over `inventory_daily.units_sold` |
| 2 | **Basket / cross-sell** | "Bought together" pairs from shared `order_id`. | `order_items` co-occurrence |
| 3 | **Markdown optimiser** | Recommend markdowns for slow, overstocked SKUs. | `inventory_daily`, `products` margin |
| 4 | **Same-store sales** | Comparable-store growth, controlling for store age. | `orders`, `stores.opened_on` |
| 5 | **Inventory turnover** | Turns by category/brand to free up working capital. | `inventory_daily`, `products` |
| 6 | **Ask-your-shelves (Genie)** | "Which category has the most stockouts in NSW?" | [Genie Space](../working-with-ai/genie-ask-your-data.md) |

## More app ideas for retail

| App | What it does |
| --- | --- |
| **Basket Analysis & Cross-Sell** | Top product pairs and a "recommended add-on" lookup. |
| **Demand Forecaster** | SKU-store forecasts with seasonality and reorder suggestions. |
| **Store Performance Board** | Sales, margin and turnover per store and region. |
| **Markdown Optimiser** | Flags aged/overstocked lines and models markdown lift. |
| **Promotional Lift Analyser** | Measures uplift from `discount_pct` on order items. |

## Concepts & labs

- [AI over your data](../working-with-ai/ai-over-your-data.md) ·
  [Genie](../working-with-ai/genie-ask-your-data.md) ·
  [Shipping on Databricks](../vibe-coding/shipping-on-databricks.md)
</content>
