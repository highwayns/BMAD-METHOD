ALTER TABLE {{catalog}}.{{schema}}.{{table}}
ADD CONSTRAINT not_null_pk CHECK (id IS NOT NULL);