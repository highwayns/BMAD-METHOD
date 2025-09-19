# task: transport-sync

version: 1.0
role: tech-systems-dms-crm
purpose: 车辆/车次/司机/小时数与CRM同步。
inputs: [映射/排班/替代/异常]
outputs: [docs/sys/transport-sync.md]
steps:

- 渲染 templates/api-integration-tmpl.yaml
- 执行 api-go-live-check 清单
  acceptance:
- 调度一致
- 异常可追溯
