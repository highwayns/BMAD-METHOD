# task: contract-review

version: 1.0
role: legal-compliance
purpose: 完成合同重点条款评审并出具意见。
inputs: [甲乙方/标的/金额/期限, SLA/赔偿/不可抗力/争议, IP/品牌/肖像]
outputs: [docs/legal/contract-review-<counterparty>.md]
steps:

- 渲染 templates/contract-review-tmpl.yaml
- 执行 contract-legal-check 清单
  acceptance:
- 关键风险标注与建议
- 审批记录在案
