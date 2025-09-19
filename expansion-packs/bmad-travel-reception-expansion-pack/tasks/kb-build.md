# task: kb-build

version: 1.0
role: customer-service-care-lead
purpose: 建设高频问题知识库文章。
inputs: [主题与标签, 场景/步骤/话术, 更新频率]
outputs: [docs/care/kb/<topic>.md]
steps:

- 渲染 templates/kb-article-tmpl.yaml
- 发布并纳入宏模板
  acceptance:
- 可复用度高
- 质检过稿
