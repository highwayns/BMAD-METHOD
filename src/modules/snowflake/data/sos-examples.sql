-- Search Optimization Service examples (illustrative)
ALTER TABLE SILVER.ORDERS ADD SEARCH OPTIMIZATION ON EQUALITY(order_id), SUBSTRING(email);
