# task: consulate-requirements-matrix

version: 1.0
role: visa-insurance-specialist
purpose: 维护不同受理中心/领区的材料与流程差异矩阵。
inputs: [地区/受理中心, 预约/指纹/邮寄/面试, 特殊材料]
outputs: [docs/visa/consulate-matrix.md]
steps:

- 渲染 templates/consulate-requirements-matrix-tmpl.yaml
- 定期复核与更新
  acceptance:
- 字段完整/差异明确
- 更新时间记录
