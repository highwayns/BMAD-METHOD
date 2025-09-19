# task: reconciliation-ledger

version: 1.0
role: finance-billing-specialist
purpose: 维护对账台账与责任/期限闭环。
inputs: [差异/金额/责任人/截止]
outputs: [reports/reconciliation-ledger-<period>.md]
steps:

- 渲染 templates/reconciliation-ledger-tmpl.yaml
- 周期复核与升级
  acceptance:
- 闭环率≥95%
- 超期可见
