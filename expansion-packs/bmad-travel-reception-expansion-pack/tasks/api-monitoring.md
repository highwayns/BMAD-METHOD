# task: api-monitoring

version: 1.0
role: tech-systems-dms-crm
purpose: 建立 API/Webhook 监控、报警与SLO。
inputs: [指标/阈值/错误预算]
outputs: [runbooks/monitoring-api.md]
steps:

- 渲染 templates/slo-error-budget-tmpl.yaml
- 执行 slo-monitoring-check 清单
  acceptance:
- 误报低/漏报低
- SLO达标
