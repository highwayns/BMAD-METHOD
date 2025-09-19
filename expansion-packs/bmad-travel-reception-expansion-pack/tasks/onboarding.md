# task: onboarding

version: 1.0
role: guide-leader-manager
purpose: 完成导游/领队入职与合规留痕。
inputs: [身份/许可/保险, 税务/发票, 培训记录]
outputs: [docs/guide/onboarding-<name>.md]
steps:

- 渲染 templates/guide-onboarding-tmpl.yaml（逐节提问）
- 执行 guide-onboarding-check 清单
  acceptance:
- 证照有效/培训通过
- APPI/敏感话题完成宣导
