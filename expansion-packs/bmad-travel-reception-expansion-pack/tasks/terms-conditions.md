# task: terms-conditions

version: 1.0
role: legal-compliance
purpose: 维护条款/政策版本与生效机制。
inputs: [名称/版本/变更点/生效]
outputs: [docs/legal/terms-<name>-<ver>.md]
steps:

- 渲染 templates/terms-conditions-tmpl.yaml
- 执行 tos-policy-check 清单
  acceptance:
- 公示与同意证据在案
- 版本比对清晰
