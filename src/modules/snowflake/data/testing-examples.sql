-- dbt test patterns + custom SQL assertions (illustrative)
SELECT 'unique_user_id' AS test, COUNT(*) - COUNT(DISTINCT user_id) AS failures FROM DIM_USER;
