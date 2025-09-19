# task: visa-doc-collection

version: 1.0
role: visa-insurance-specialist
purpose: 收集并核对签证材料，输出缺失与问题清单。
inputs: [护照/照片/表格, 在职/财力/旅行史, 机票/酒店/行程]
outputs: [docs/visa/doc-collection-<traveler>.md]
steps:

- 渲染 templates/visa-doc-collection-tmpl.yaml
- 执行 photo-spec-check / financial-proof-check / employment-proof-check
  acceptance:
- 缺失项一目了然
- 改善建议明确
