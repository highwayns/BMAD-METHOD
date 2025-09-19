# task: asset-shotlist

version: 1.0
role: content-branding
purpose: 拍摄清单与授权风险提示。
outputs: [docs/asset/shotlist.md]
steps:

- 渲染 templates/asset-shotlist-tmpl.yaml
- 执行 image-rights-check
  acceptance:
- 场景/授权明确
