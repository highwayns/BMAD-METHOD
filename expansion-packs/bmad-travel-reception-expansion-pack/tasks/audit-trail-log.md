# task: audit-trail-log

version: 1.0
role: finance-billing-specialist
purpose: 维护审计日志，固化证据链。
inputs: [动作/人/时间/证据]
outputs: [reports/audit-trail-<period>.md]
steps:

- 渲染 templates/audit-trail-log-tmpl.yaml
- 归档影像与回执
  acceptance:
- 可追溯
- 覆盖关键动作
