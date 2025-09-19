# task: insurance-policy-issue

version: 1.0
role: visa-insurance-specialist
purpose: 出具保单并完成交付与回执归档。
inputs: [被保险人信息, 计划/保额, 发票/回执]
outputs: [docs/insurance/policy-<policy_no>.md]
steps:

- 渲染 templates/insurance-policy-issue-tmpl.yaml
- 与财务对齐发票抬头
  acceptance:
- 保单/发票/回执齐全
- 字段口径一致
