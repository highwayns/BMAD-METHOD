# task: vendor-safety-audit

version: 1.0
role: risk-safety-manager
purpose: 审计供应商安全能力并输出CAPA。
inputs: [资质/保险/事故/SOP/训练, 评分/整改/复核]
outputs: [reports/vendor-safety-audit-<vendor>.md]
steps:

- 渲染 templates/vendor-safety-audit-tmpl.yaml
- 执行 vendor-safety-audit-check 清单
  acceptance:
- 评分客观可证
- CAPA闭环
