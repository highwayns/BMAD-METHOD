# task: ugc-program

version: 1.0
role: content-branding
purpose: UGC 征集/激励/授权与使用。
outputs: [docs/campaign/ugc-program.md]
steps:

- 渲染 templates/ugc-program-tmpl.yaml
- 执行 image-rights-check
  acceptance:
- 授权闭环
