import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

np.random.seed(42)
random.seed(42)

os.makedirs("data/raw", exist_ok=True)

stages = ["Order Received", "Picking", "Packing", "Quality Check", "Dispatch"]
regions = ["Kathmandu", "Pokhara", "Chitwan", "Biratnagar", "Lalitpur"]
priorities = ["Low", "Normal", "High"]
issue_types = ["None", "Staff Shortage", "Inventory Missing", "System Delay", "Rework"]

orders = []
events = []

base_date = datetime(2026, 1, 1, 8, 0)

for i in range(1, 301):
    order_id = f"ORD{i:04d}"
    created_time = base_date + timedelta(
        days=random.randint(0, 30),
        hours=random.randint(0, 9),
        minutes=random.randint(0, 59)
    )

    priority = random.choice(priorities)
    region = random.choice(regions)
    order_size = random.randint(1, 20)
    staff_count = random.randint(2, 10)
    promised_dispatch = created_time + timedelta(hours=random.choice([8, 12, 24]))

    orders.append([
        order_id,
        created_time,
        promised_dispatch,
        priority,
        region,
        order_size,
        staff_count
    ])

    current_time = created_time

    for stage in stages:
        base_minutes = {
            "Order Received": 10,
            "Picking": 45,
            "Packing": 30,
            "Quality Check": 25,
            "Dispatch": 35
        }[stage]

        issue = random.choices(
            issue_types,
            weights=[70, 10, 8, 7, 5],
            k=1
        )[0]

        delay_extra = 0
        if issue == "Staff Shortage":
            delay_extra += random.randint(20, 90)
        elif issue == "Inventory Missing":
            delay_extra += random.randint(30, 120)
        elif issue == "System Delay":
            delay_extra += random.randint(15, 75)
        elif issue == "Rework":
            delay_extra += random.randint(20, 80)

        duration = base_minutes + (order_size * 2) - staff_count + random.randint(-5, 20) + delay_extra
        duration = max(duration, 5)

        start_time = current_time
        end_time = start_time + timedelta(minutes=duration)

        events.append([
            order_id,
            stage,
            start_time,
            end_time,
            issue,
            duration
        ])

        current_time = end_time + timedelta(minutes=random.randint(5, 30))

orders_df = pd.DataFrame(orders, columns=[
    "order_id",
    "created_time",
    "promised_dispatch",
    "priority",
    "customer_region",
    "order_size",
    "staff_count"
])

events_df = pd.DataFrame(events, columns=[
    "order_id",
    "stage",
    "start_time",
    "end_time",
    "issue_type",
    "duration_minutes"
])

orders_df.to_csv("data/raw/orders.csv", index=False)
events_df.to_csv("data/raw/order_events.csv", index=False)

print("Dataset created successfully")
print("orders.csv:", len(orders_df), "rows")
print("order_events.csv:", len(events_df), "rows")