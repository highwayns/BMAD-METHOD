# task: keyword-map

version: 1.0
role: content-branding
purpose: 多语言关键词地图（JP/EN/CN）。
outputs: [docs/content/keyword-map.md]
steps:

- 渲染 templates/keyword-map-tmpl.yaml
- 执行 seo-onpage-check（词-页映射）
  acceptance:
- 词-页唯一映射
