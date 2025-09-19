# task: compliance-matrix

version: 1.0
role: legal-compliance
purpose: 输出合规要求矩阵与证据责任。
inputs: [法规/要求/责任/证据]
outputs: [docs/legal/compliance-matrix.md]
steps:

- 渲染 templates/compliance-matrix-tmpl.yaml
- 与风险/运营/客服对齐
  acceptance:
- 责任清晰
- 证据充足
