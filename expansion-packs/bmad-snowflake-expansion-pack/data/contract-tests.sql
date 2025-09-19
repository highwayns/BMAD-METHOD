-- Contract test examples (illustrative)
-- Uniqueness
SELECT 'order_id_unique' AS test, COUNT(*) - COUNT(DISTINCT order_id) AS failures
FROM ORDERS_SILVER
HAVING failures = 0;

-- Range check
SELECT 'amount_non_negative' AS test, COUNT(*) AS failures
FROM ORDERS_SILVER WHERE amount < 0;
