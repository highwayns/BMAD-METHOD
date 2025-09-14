# Handoff Contracts

| From          | To            | Trigger             | Inputs                 | Outputs          | Acceptance       |
| ------------- | ------------- | ------------------- | ---------------------- | ---------------- | ---------------- |
| Intake        | Cell/Organoid | Consent & Approvals | donors.csv + approvals | cell_lines.csv   | 合规/去标识/完整 |
| Cell/Organoid | Process/QC    | Culture Ready       | cell_lines.csv         | batch record     | 支原体/无菌通过  |
| Process/QC    | Animal        | Release Passed      | qc_results.csv         | study request    | CQAs 全部达标    |
| Animal        | Data          | Study Complete      | raw data               | analysis package | 元数据齐全       |
| Data          | Tech Transfer | Package Ready       | analysis + SOP         | transfer kit     | 可复现/冷链就绪  |
