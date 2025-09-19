# task: group-visa

version: 1.0
role: visa-insurance-specialist
purpose: 组织团队签证材料与旅行社批件对齐。
inputs: [名单/护照/关系, 行程/酒店/交通, 旅行社资质与批件]
outputs: [docs/visa/group-visa-<group>.md]
steps:

- 渲染 templates/group-visa-package-tmpl.yaml
- 执行 minors-consent-check（若含未成年）
  acceptance:
- 名单与材料一致
- 批件有效
