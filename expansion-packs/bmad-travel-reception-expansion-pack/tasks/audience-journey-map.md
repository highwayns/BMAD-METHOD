# task: audience-journey-map

version: 1.0
role: content-branding
purpose: 受众×旅程×痛点×内容主题地图。
outputs: [docs/content/audience-journey.md]
steps:

- 渲染 templates/audience-journey-map-tmpl.yaml
  acceptance:
- 阶段覆盖完整
