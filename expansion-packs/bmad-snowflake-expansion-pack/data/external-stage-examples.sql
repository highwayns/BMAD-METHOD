-- Example external stage (S3 as example)
CREATE STAGE IF NOT EXISTS STG_ORDERS
  URL='s3://bucket/path/'
  CREDENTIALS=(AWS_KEY_ID='...' AWS_SECRET_KEY='...')
  FILE_FORMAT=FF_JSON;
