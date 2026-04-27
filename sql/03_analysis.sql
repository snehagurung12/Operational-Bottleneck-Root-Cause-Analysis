-- Bottleneck
SELECT stage, AVG(duration_minutes)
FROM order_events
GROUP BY stage
ORDER BY AVG(duration_minutes) DESC;

-- Root cause
SELECT stage, issue_type, AVG(duration_minutes)
FROM order_events
GROUP BY stage, issue_type;

-- SLA breach
SELECT 
    COUNT(*) AS total_orders,
    SUM(late_flag) AS late_orders
FROM order_completion;