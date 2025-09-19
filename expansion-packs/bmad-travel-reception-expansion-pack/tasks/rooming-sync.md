# task: rooming-sync

version: 1.0
role: tech-systems-dms-crm
purpose: 房态/名单/配房与CRM同步。
inputs: [字段映射/时序/冲突策略]
outputs: [docs/sys/rooming-sync.md]
steps:

- 渲染 templates/api-integration-tmpl.yaml
- 执行 data-quality-check 清单
  acceptance:
- 名单准确
- 冲突最小化
