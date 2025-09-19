# task: incident-report-rca

version: 1.0
role: risk-safety-manager
purpose: 记录事故并完成RCA与CAPA闭环。
inputs: [时间线/参与人/证据, 根因/CAPA/期限/负责人]
outputs: [reports/incident-rca-<id>.md]
steps:

- 渲染 templates/incident-report-rca-tmpl.yaml
- 执行 incident-investigation-check 清单
  acceptance:
- 事实完整/根因可信
- CAPA按期追踪
