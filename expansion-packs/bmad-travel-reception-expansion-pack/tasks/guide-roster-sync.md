# task: guide-roster-sync

version: 1.0
role: tech-systems-dms-crm
purpose: 导游/领队排班与CRM/服务台一致。
inputs: [档案/资质/限制/排班/替代]
outputs: [docs/sys/guide-roster-sync.md]
steps:

- 渲染 templates/api-integration-tmpl.yaml
- 执行 access-review-check 清单
  acceptance:
- 资质有效
- 工单可路由
