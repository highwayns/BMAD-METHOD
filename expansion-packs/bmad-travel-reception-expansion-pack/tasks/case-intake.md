# task: case-intake

version: 1.0
role: customer-service-care-lead
purpose: 规范化受理客户问题，完整采集事实与权限。
inputs: [客户身份与订单, 问题与证据, 紧急度与期望]
outputs: [docs/care/case-intake-<case_id>.md]
steps:

- 渲染 templates/case-intake-tmpl.yaml（逐节提问）
- 执行 intake-check 清单
  acceptance:
- 字段完整/隐私授权到位
- 期望与时限明确
