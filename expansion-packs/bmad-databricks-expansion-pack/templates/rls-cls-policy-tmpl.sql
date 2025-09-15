-- RLS/CLS Policy
CREATE OR REPLACE FUNCTION policy_rls() RETURN BOOLEAN;
-- 示例：region = current_user_region()
-- 列遮罩：CASE WHEN has_pii_role() THEN col ELSE NULL END
