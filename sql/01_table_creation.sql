DROP TABLE IF EXISTS order_events CASCADE;
DROP TABLE IF EXISTS orders CASCADE;

CREATE TABLE orders (
    order_id VARCHAR(20) PRIMARY KEY,
    created_time TIMESTAMP,
    promised_dispatch TIMESTAMP,
    priority VARCHAR(10),
    customer_region VARCHAR(50),
    order_size INT,
    staff_count INT
);

CREATE TABLE order_events (
    event_id SERIAL PRIMARY KEY,
    order_id VARCHAR(20),
    stage VARCHAR(50),
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    issue_type VARCHAR(50),
    duration_minutes INT
);