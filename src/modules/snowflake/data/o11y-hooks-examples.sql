-- Link dashboards/alerts to release id
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY WHERE QUERY_TAG='release:2025-09-19';
