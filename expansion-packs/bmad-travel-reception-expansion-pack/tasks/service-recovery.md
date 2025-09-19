# task: service-recovery

version: 1.0
role: onsite-ops-lead
purpose: 规范现场服务补救并量化成本与回执。
inputs: [案例/责任, 补偿/替代/退款, 证据/回执]
outputs: [reports/service-recovery-YYYYMMDD.md]
steps:

- 渲染 templates/service-recovery-tmpl.yaml
- 与投诉与财务联动并归档
  acceptance:
- 补救闭环与凭证齐全
- 客户确认在案
