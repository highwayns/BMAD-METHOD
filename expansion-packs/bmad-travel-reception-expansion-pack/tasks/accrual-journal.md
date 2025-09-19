# task: accrual-journal

version: 1.0
role: finance-billing-specialist
purpose: 期间应计/摊销/递延分录与依据留存。
inputs: [科目/金额/期间, 说明与依据]
outputs: [docs/fin/accrual-<period>.md]
steps:

- 渲染 templates/accrual-journal-tmpl.yaml
- 归档依据与复核
  acceptance:
- 分录准确
- 依据齐全
