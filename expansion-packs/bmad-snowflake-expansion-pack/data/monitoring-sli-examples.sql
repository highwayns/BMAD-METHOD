-- Monitoring SLI examples
-- Freshness
SELECT DATEDIFF('minute', MAX(load_end_time), CURRENT_TIMESTAMP()) AS lag_minutes
FROM LOAD_AUDIT WHERE table_name = 'ORDERS_SILVER';

-- Availability (toy example)
SELECT 100.0 - (SUM(downtime_minutes)/ (30*24*60))*100 AS availability_pct
FROM PLATFORM_AVAILABILITY WHERE month = DATE_TRUNC('month', CURRENT_DATE());
