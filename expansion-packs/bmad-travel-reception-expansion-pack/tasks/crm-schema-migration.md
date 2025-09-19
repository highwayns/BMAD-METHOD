# task: crm-schema-migration

version: 1.0
role: tech-systems-dms-crm
purpose: 设计并实施 CRM 对象模型与字段变更。
inputs: [对象/字段/关系/历史迁移]
outputs: [docs/sys/crm-schema-change-<date>.md]
steps:

- 渲染 templates/crm-object-model-tmpl.yaml
- 执行 release-cutover-check 与 change-management-check
  acceptance:
- 零数据丢失
- 回滚有据
