# task: build-guide-roster

version: 1.0
role: guide-leader-manager
purpose: 建立导游/领队花名册并结构化打标签。
inputs: [姓名/电话/语言, 区域覆盖, 证照到期, 特长与评分]
outputs: [docs/guide/roster.md]
steps:

- 渲染 templates/guide-roster-tmpl.yaml（逐条录入或批量导入CSV）
- 标注可用性与地理标签
  acceptance:
- 字段完整/证照到期有提醒
- 可用性/区域覆盖清晰
