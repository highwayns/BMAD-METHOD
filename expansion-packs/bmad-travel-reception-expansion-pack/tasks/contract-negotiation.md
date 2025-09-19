# task: contract-negotiation

version: 1.0
role: sales-account-manager
purpose: 完成价格、SLA、数据、取消/变更等关键条款谈判与记录。
inputs: [proposal, 条款库, 审批链]
outputs: [docs/sales/contract-negotiation.md]
steps:

- templates/contract-negotiation-tmpl.yaml 渲染
- 折扣权限链审核记录
- 输出签署清单与时间表
  acceptance:
- 条款留痕与审批通过
- 风险与例外条款标注
