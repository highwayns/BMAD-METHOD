-- Row access for purpose limitation / region
CREATE ROW ACCESS POLICY IF NOT EXISTS RAP_REGION AS (region STRING) RETURNS BOOLEAN -> region = CURRENT_REGION();
