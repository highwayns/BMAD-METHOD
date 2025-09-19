# task: subprocessor-register

version: 1.0
role: legal-compliance
purpose: 维护受托方与次处理者登记与合同保障。
inputs: [名称/用途/数据/地点/保障]
outputs: [docs/legal/subprocessor-register.md]
steps:

- 渲染 templates/subprocessor-register-tmpl.yaml
- 周期复核
  acceptance:
- 名单更新及时
- 保障条款有效
