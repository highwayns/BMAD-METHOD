-- Batch scoring job (illustrative)
CREATE OR REPLACE TASK T_SCORE_DAILY WAREHOUSE=WH_ML SCHEDULE='USING CRON 0 2 * * * UTC' AS
MERGE INTO GOLD.SCORES t USING STAGING.NEW_SCORES s ON t.user_id = s.user_id
WHEN MATCHED THEN UPDATE SET score = s.score, updated_at = CURRENT_TIMESTAMP()
WHEN NOT MATCHED THEN INSERT (user_id, score, updated_at) VALUES(s.user_id, s.score, CURRENT_TIMESTAMP());
