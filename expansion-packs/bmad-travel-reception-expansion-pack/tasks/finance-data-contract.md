# task: finance-data-contract

version: 1.0
role: finance-billing-specialist
purpose: 明确财务数据契约（字段/口径/安全）。
inputs: [字段/必填/校验, 货币/税价/时区/汇率]
outputs: [docs/fin/data-contract-<domain>.md]
steps:

- 渲染 templates/finance-data-contract-tmpl.yaml
- 执行 privacy-appi-check 清单
  acceptance:
- 字段/口径一致
- 合规可用
