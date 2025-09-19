# task: campaign-sync

version: 1.0
role: tech-systems-dms-crm
purpose: 规范活动 brief 与字段映射，闭环回传。
inputs: [目标/受众/字段映射/ID/回传]
outputs: [docs/sys/campaign-sync-<campaign>.md]
steps:

- 渲染 templates/campaign-brief-sync-tmpl.yaml
- 执行 data-quality-check 清单
  acceptance:
- 名单准确
- 归因可用
