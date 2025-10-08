ALTER TABLE {{catalog}}.{{schema}}.{{table}}
ADD CONSTRAINT valid_pk CHECK (id IS NOT NULL);