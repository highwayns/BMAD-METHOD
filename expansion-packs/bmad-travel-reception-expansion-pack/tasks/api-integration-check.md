# task: api-integration-check

version: 1.0
role: vendor-procurement-manager
purpose: 推进 API/门户对接与上线验收。
inputs: [认证/速率/重试/回执, 错误码/报警/回滚]
outputs: [docs/vendor/api-integration-<vendor>.md]
steps:

- 渲染 templates/api-integration-checklist-tmpl.yaml
- 执行 api-go-live-check 清单
  acceptance:
- 核心链路稳定
- 回滚与报警可用
