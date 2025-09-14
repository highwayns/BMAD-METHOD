# Handoff Contracts

| From      | To            | Trigger            | Inputs               | Outputs                                        | Acceptance     |
| --------- | ------------- | ------------------ | -------------------- | ---------------------------------------------- | -------------- |
| Contract  | Architect     | Contract Locked    | data-contract.md     | delta-table-spec.md                            | 命名/口径一致  |
| Architect | DLT/Streaming | UC Policy Ready    | uc-catalog-policy.md | dlt-design.md + streaming-autoloader-design.md | 摄取与流式成功 |
| DE/AE     | Release/QA    | Semantic DQ Passed | dq_rules.csv + 报告  | github-actions-databricks.yml                  | CI 通过        |
