-- Pipeline metadata tables (audit & checkpoint)
CREATE TABLE IF NOT EXISTS META_LOAD_AUDIT (
  pipeline STRING, run_id STRING, start_ts TIMESTAMP, end_ts TIMESTAMP, status STRING, rows_loaded NUMBER, error_msg STRING
);
CREATE TABLE IF NOT EXISTS META_CHECKPOINTS (
  pipeline STRING, checkpoint_key STRING, checkpoint_val STRING, updated_at TIMESTAMP
);
