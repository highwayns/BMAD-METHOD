# task: visa-denial-appeal

version: 1.0
role: visa-insurance-specialist
purpose: 拒签后复核原因，制定申诉或再申请方案。
inputs: [拒签原因, 补强材料, 决策与时间线]
outputs: [docs/visa/denial-appeal-<traveler>.md]
steps:

- 渲染 templates/visa-denial-appeal-tmpl.yaml
- 与客户沟通风险与等待期
  acceptance:
- 方案可执行
- 风险披露到位
