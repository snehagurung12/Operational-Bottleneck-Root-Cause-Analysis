# Operational Bottlenecks & Root Cause Analysis

**Tools:** PostgreSQL · Python · Power BI · GitHub  
**Domain:** Operations Analytics · Process Intelligence · Data Engineering

---

## Project Overview

A complete end-to-end analytics pipeline that identifies operational bottlenecks, measures SLA performance, and uncovers root causes of delays across a 300-order, 1,500-event workflow dataset.

Built to simulate a real-world operations intelligence system — from raw data ingestion through PostgreSQL, Python ETL processing, to an interactive Power BI dashboard with 4 analytical pages.

---

## Key Findings

- **Picking** is the primary bottleneck at **81.7 min avg** — 67% longer than the fastest stage
- **Staff Shortage** drives **32%** of all issue events (133 out of 415)
- **SLA Compliance** sits at **93.3%** — 20 orders missed promised dispatch
- **3 issue types** (Staff Shortage, Inventory Missing, System Delay) cause **83% of all delays**
- **Quality Check** has the highest issue concentration — 31 Staff Shortage events alone

---

## Dashboard Pages

| Page | Title | What It Answers |
|---|---|---|
| 1 | Executive Overview | What is the overall operational health? |
| 2 | Bottleneck Explorer | Where exactly is time being lost? |
| 3 | Root Cause Analysis | Why are delays happening? |
| 4 | Cloud Pipeline | How does the data pipeline work end to end? |

---

## Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| Data Storage | PostgreSQL | Raw data ingestion and KPI views |
| Processing | Python (Pandas) | ETL, cleaning, feature engineering |
| Visualisation | Power BI | 4-page interactive dashboard |
| Version Control | GitHub | Project showcase and documentation |

---

## Project Architecture

Operational-Bottleneck-Root-Cause-Analysis/

│
├── data/

│ ├── raw/

│ └── processed/

│

├── notebooks/

│ └── delay_prediction.ipynb
│
├── sql/

│ ├── 01_table_creation.sql

│ ├── 02_views.sql

│ └── 03_analysis.sql

│
├── powerbi/

│ └── dashboard.pbix
│
├── reports/

├── README.md

---

---

## Dataset

| Table | Rows | Description |
|---|---|---|
| orders | 300 | Order ID, region, priority, staff count, timestamps |
| order_events | 1,500 | Stage-level events with issue type and duration |

**5 pipeline stages:** Order Received → Picking → Packing → Quality Check → Dispatch  
**4 issue types:** Staff Shortage · Inventory Missing · System Delay · Rework  
**5 regions:** Chitwan · Lalitpur · Biratnagar · Kathmandu · Pokhara

---

## DAX Measures Used

```dax
-- Cycle Time per Order
Cycle Time Minutes = 
VAR OrderStart = orders[created_time]
VAR OrderEnd = 
    CALCULATE(
        MAX(order_events[end_time]),
        FILTER(order_events, order_events[order_id] = EARLIER(orders[order_id]))
    )
RETURN DATEDIFF(OrderStart, OrderEnd, MINUTE)

-- Issue Event Count (excluding None)
Issue Event Count = 
CALCULATE(
    COUNTROWS(order_events),
    order_events[issue_type] <> "None"
)

-- SLA Compliance
SLA Compliance % = 
DIVIDE(
    CALCULATE(COUNTROWS(orders), orders[Is Delayed] = 0),
    COUNTROWS(orders)
) * 100
```

---

## Business Recommendations

1. **Staff reallocation** — Picking and Quality Check need dedicated staffing during peak hours
2. **Inventory sync** — Real-time inventory tracking would eliminate 26% of all issue events
3. **IT infrastructure review** — 102 System Delay events concentrated in Picking and QC suggest latency at decision handoffs
4. **Intake quality control** — 20 Rework events at Order Received stage cascade into downstream delays

---

## Skills Demonstrated

- End-to-end data pipeline design
- SQL query writing and view creation
- Python data processing and ETL
- Power BI dashboard development with DAX
- Root cause analysis methodology
- Operational KPI framework design
- Data storytelling across multiple analytical layers

---

## Author

**Sneha Gurung**  
[GitHub](https://github.com/snehagurung12)


