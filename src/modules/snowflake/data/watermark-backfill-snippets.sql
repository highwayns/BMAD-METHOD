-- Watermark/Checkpoint table
CREATE TABLE IF NOT EXISTS META_CHECKPOINTS (pipeline STRING, watermark_ts TIMESTAMP, updated_at TIMESTAMP);
