# task: fx-rate-table

version: 1.0
role: finance-billing-specialist
purpose: 维护汇率表并记录来源。
inputs: [日期/来源/币种/买入/卖出]
outputs: [docs/fin/fx-table-<period>.md]
steps:

- 渲染 templates/fx-rate-table-tmpl.yaml
- 对账系统汇率
  acceptance:
- 来源明确
- 与系统一致
