# task: vip-brief

version: 1.0
role: onsite-ops-lead
purpose: 为VIP/要客制定专属动线与隐私安保要点。
inputs: [语言/饮食/安保/隐私, 专属动线/会见]
outputs: [docs/onsite/vip-brief-<group>.md]
steps:

- 渲染 templates/vip-briefing-tmpl.yaml
- 与现场与车队联动
  acceptance:
- 动线清晰/隐私受控
- 责任人明确
