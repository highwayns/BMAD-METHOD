# task: policy-register

version: 1.0
role: legal-compliance
purpose: 建立政策登记册并维护版本与适用范围。
inputs: [名称/版本/生效/负责人, 适用范围/关联政策]
outputs: [docs/legal/policy-register.md]
steps:

- 渲染 templates/policy-register-tmpl.yaml（逐节提问）
- 执行 tos-policy-check 清单
  acceptance:
- 版本与生效信息明确
- 关联政策可追溯
