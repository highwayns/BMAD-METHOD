-- Tasks/DT/SOS pipeline examples (illustrative)
CREATE TASK T_BRONZE_LOAD WAREHOUSE=WH_ETL SCHEDULE='USING CRON 0 */1 * * * UTC' AS CALL SP_LOAD();
