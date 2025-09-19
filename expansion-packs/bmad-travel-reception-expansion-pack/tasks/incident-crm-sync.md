# task: incident-crm-sync

version: 1.0
role: tech-systems-dms-crm
purpose: 风险事件/投诉工单与CRM/客服平台同步。
inputs: [事件/等级/字段映射/SLA]
outputs: [docs/sys/incident-sync.md]
steps:

- 渲染 templates/ticketing-sla-tmpl.yaml
- 执行 slo-monitoring-check 清单
  acceptance:
- 升级及时
- 报告一致
