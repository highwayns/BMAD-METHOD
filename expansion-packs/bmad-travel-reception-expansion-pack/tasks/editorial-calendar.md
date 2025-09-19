# task: editorial-calendar

version: 1.0
role: content-branding
purpose: 编辑日历与素材需求清单。
outputs: [docs/content/editorial-calendar.md]
steps:

- 渲染 templates/editorial-calendar-tmpl.yaml
  acceptance:
- 6周滚动节奏
