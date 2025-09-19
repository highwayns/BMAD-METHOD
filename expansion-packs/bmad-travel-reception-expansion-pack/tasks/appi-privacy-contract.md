# task: appi-privacy-contract

version: 1.0
role: legal-compliance
purpose: 明确APPI数据契约（字段/用途/存留/共享/脱敏）。
inputs: [字段/用途/存留, 第三方共享/脱敏]
outputs: [docs/legal/appi-privacy-contract.md]
steps:

- 渲染 templates/appi-privacy-contract-tmpl.yaml
- 执行 privacy-appi-check 清单
  acceptance:
- 合规明确
- 审批可查
