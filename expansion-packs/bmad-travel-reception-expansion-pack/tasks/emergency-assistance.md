# task: emergency-assistance

version: 1.0
role: visa-insurance-specialist
purpose: 提供保险援助流程与就医/转运/报案指引。
inputs: [保单信息, 援助热线, 就医/转运/报案流程]
outputs: [docs/insurance/emergency-assist-<traveler>.md]
steps:

- 渲染 templates/emergency-assistance-brief-tmpl.yaml
- 与客户确认已读与回执
  acceptance:
- 流程清晰
- 回执在案
