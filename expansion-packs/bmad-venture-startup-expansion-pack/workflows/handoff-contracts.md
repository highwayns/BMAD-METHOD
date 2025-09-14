# Handoff Contracts

| From        | To          | Trigger           | Inputs                 | Outputs                  | Acceptance       |
| ----------- | ----------- | ----------------- | ---------------------- | ------------------------ | ---------------- |
| Strategy    | Product     | PMF Gate Ready    | insights + PMF targets | prioritized roadmap      | 假设与指标对齐   |
| Product     | Engineering | Sprint Kickoff    | specs + designs        | implemented features     | 质量门通过       |
| Engineering | DevOps      | Release Candidate | build + infra plan     | deployment               | 自动化与回滚就绪 |
| DevOps      | Security    | New Integration   | architecture + vendors | DPA/SCC + risk memo      | 风险可控         |
| Data        | Growth      | Tracking Live     | schemas + events       | dashboards + experiments | 因果归因成立     |
| Growth      | Sales       | MQL Threshold     | lead list + scores     | SQL/pipeline             | SLA 满足         |
| Sales       | CS          | Closed-Won        | contract + SLA         | onboarding plan          | 健康评分路径     |
| CFO         | Board Ops   | Q Close           | runway + metrics       | board pack               | 一致与可审计     |
