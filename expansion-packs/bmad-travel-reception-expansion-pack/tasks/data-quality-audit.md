# task: data-quality-audit

version: 1.0
role: tech-systems-dms-crm
purpose: 数据质量巡检与修复闭环。
inputs: [维度/阈值/告警/工单]
outputs: [reports/sys/data-quality-<period>.md]
steps:

- 渲染 templates/kpi-dashboard-spec-tmpl.yaml（质量指标）
- 执行 data-quality-check 清单
  acceptance:
- 质量指标提升
- 修复闭环
