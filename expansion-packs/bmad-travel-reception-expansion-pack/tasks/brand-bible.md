# task: brand-bible

version: 1.0
role: content-branding
purpose: 建立品牌圣经（视觉/语调/禁用/法务护栏）。
inputs: [愿景/定位/语调, 视觉规范, 法务/APPI护栏]
outputs: [docs/brand/brand-bible.md]
steps:

- 渲染 templates/brand-bible-tmpl.yaml（逐节提问）
- 执行 brand-consistency-check 与 legal-ip-privacy-check
  acceptance:
- 跨渠道一致
- 授权与隐私合规
