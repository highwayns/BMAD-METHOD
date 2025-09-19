# task: api-integration-setup

version: 1.0
role: tech-systems-dms-crm
purpose: 建立 API 集成编排与错误处理。
inputs: [端点/鉴权/速率/幂等, 触发/映射/错误处理]
outputs: [docs/sys/api-integration-<system>.md]
steps:

- 渲染 templates/api-integration-tmpl.yaml
- 执行 api-go-live-check 与 webhook-retry-idempotency-check
  acceptance:
- 成功率≥99%
- 可回溯与回滚
