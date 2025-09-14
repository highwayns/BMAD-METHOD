# Handoff Contracts

| From      | To            | Trigger            | Inputs                 | Outputs                                     | Acceptance     |
| --------- | ------------- | ------------------ | ---------------------- | ------------------------------------------- | -------------- |
| Contract  | Architect     | Contract Locked    | data-contract.md       | database-schema-spec.md                     | 命名/口径一致  |
| Architect | ELT/Streaming | RBAC Ready         | rbac-role-hierarchy.md | stage/fileformat + snowpipe + streams/tasks | 摄取与流式成功 |
| ELT/AE    | Release/QA    | Semantic DQ Passed | dq_rules.csv + 报告    | github-actions-snowflake.yml                | CI 通过        |
