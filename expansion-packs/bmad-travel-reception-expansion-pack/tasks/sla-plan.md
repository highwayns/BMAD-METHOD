# task: sla-plan

version: 1.0
role: customer-service-care-lead
purpose: 设定渠道首响与完全解决SLA与升级矩阵。
inputs: [渠道与目标, 升级规则]
outputs: [docs/care/sla-plan.md]
steps:

- 渲染 templates/sla-plan-tmpl.yaml
- 执行 sla-health-check 清单
  acceptance:
- 阈值清晰/监控可用
- 升级路径畅通
