# task: performance-dashboard

version: 1.0
role: content-branding
purpose: 指标仪表盘与归因口径。
outputs: [docs/kpi/performance-dashboard.md]
steps:

- 渲染 templates/performance-dashboard-tmpl.yaml
  acceptance:
- 指标可复算
