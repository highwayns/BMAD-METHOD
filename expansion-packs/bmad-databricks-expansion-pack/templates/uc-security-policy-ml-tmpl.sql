-- UC Security Policy
GRANT USAGE ON CATALOG {{catalog}} TO `{{role}}`;
GRANT USAGE ON SCHEMA {{catalog}}.{{schema}} TO `{{role}}`;
GRANT SELECT ON ALL TABLES IN SCHEMA {{catalog}}.{{schema}} TO `{{role}}`;
