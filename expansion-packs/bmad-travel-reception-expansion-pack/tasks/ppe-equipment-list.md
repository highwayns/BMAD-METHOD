# task: ppe-equipment-list

version: 1.0
role: risk-safety-manager
purpose: 维护PPE/装备清单与日检制度。
inputs: [名称/数量/位置/责任人]
outputs: [docs/risk/ppe-list.md]
steps:

- 渲染 templates/ppe-equipment-list-tmpl.yaml
- 执行 ppe-daily-check 清单
  acceptance:
- 在位可用
- 日检有据
