# task: insurance-quote

version: 1.0
role: visa-insurance-specialist
purpose: 根据旅行计划生成保险方案并说明除外责任。
inputs: [旅行天数/目的地/活动/病史, 取消/行李/延误需求]
outputs: [docs/insurance/quote-<traveler>.md]
steps:

- 渲染 templates/insurance-quote-tmpl.yaml（逐节提问）
- 执行 insurance-eligibility-check 与 preexisting-exclusion-check
  acceptance:
- 方案A/B/C清晰与价格明确
- 风险与除外已提示
