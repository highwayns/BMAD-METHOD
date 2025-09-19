# task: whistleblowing-procedure

version: 1.0
role: legal-compliance
purpose: 设计举报与调查流程，保护举报人。
inputs: [渠道/匿名/受理/调查/反馈]
outputs: [docs/legal/whistleblowing-procedure.md]
steps:

- 渲染 templates/whistleblowing-procedure-tmpl.yaml
- 与ABAC与人事联动
  acceptance:
- 保密与保护措施到位
- 时限明确
