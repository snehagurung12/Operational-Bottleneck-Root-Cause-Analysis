CREATE OR REPLACE VIEW order_completion AS
SELECT 
    o.order_id,
    o.created_time,
    o.promised_dispatch,
    o.priority,
    o.customer_region,
    o.order_size,
    o.staff_count,
    MAX(e.end_time) AS completed_time,
    CASE 
        WHEN MAX(e.end_time) > o.promised_dispatch THEN 1 
        ELSE 0 
    END AS late_flag
FROM orders o
JOIN order_events e 
    ON o.order_id = e.order_id
GROUP BY 
    o.order_id,
    o.created_time,
    o.promised_dispatch,
    o.priority,
    o.customer_region,
    o.order_size,
    o.staff_count;