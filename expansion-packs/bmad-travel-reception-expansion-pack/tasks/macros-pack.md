# task: macros-pack

version: 1.0
role: customer-service-care-lead
purpose: 整理多渠道多语言宏模板包，提高响应一致性。
inputs: [场景/渠道/语言/消息]
outputs: [docs/care/macros-pack-<version>.md]
steps:

- 渲染 templates/macros-pack-tmpl.yaml
- 与KB联动并A/B测试
  acceptance:
- 命中率↑，处理时长↓
- 投诉率不过度上升
