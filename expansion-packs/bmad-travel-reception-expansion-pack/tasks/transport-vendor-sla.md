# task: transport-vendor-sla

version: 1.0
role: transport-logistics-coordinator
purpose: 季度评审运输供应商SLA并形成改进闭环。
inputs: [近90天KPI, 投诉与替代车调用]
outputs: [reports/transport-vendor-sla-YYYYQ.md]
steps:

- 渲染 templates/transport-vendor-sla-tmpl.yaml
- 输出改进行动
  acceptance:
- 证据充分
- 闭环跟踪
