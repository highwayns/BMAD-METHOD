-- Smoke/freshness after deploy
SELECT COUNT(*) FROM GOLD.ORDERS WHERE ORDER_DATE >= CURRENT_DATE()-1;
