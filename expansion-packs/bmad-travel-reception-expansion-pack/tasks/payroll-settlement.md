# task: payroll-settlement

version: 1.0
role: guide-leader-manager
purpose: 完成导游薪酬结算与凭证归档。
inputs: [规则, 任务/时长/里程/金额, 发票/回执]
outputs: [reports/guide-payroll-<period>.md]
steps:

- 渲染 templates/payroll-settlement-tmpl.yaml
- 执行 payroll-audit-check 清单
  acceptance:
- 金额与证据匹配
- 税票齐全
