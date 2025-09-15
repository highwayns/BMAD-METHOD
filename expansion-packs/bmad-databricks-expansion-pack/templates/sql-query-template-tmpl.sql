-- SQL Template
-- params: {{params}}
WITH base AS (
  SELECT *
  FROM {{table}}
)
SELECT *
FROM base
-- footer: owner={{owner}} version={{version}} run_at={{run_at}}
