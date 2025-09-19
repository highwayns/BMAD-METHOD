# task: supplier-compliance-audit

version: 1.0
role: legal-compliance
purpose: 供应商合规审计与整改建议。
inputs: [资质/保险/培训/事故记录]
outputs: [reports/legal/supplier-audit-<vendor>.md]
steps:

- 渲染 templates/supplier-compliance-audit-tmpl.yaml
- 执行 supplier-compliance-check 清单
  acceptance:
- 问题闭环
- 复核通过
