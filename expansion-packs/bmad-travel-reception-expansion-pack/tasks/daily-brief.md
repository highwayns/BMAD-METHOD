# task: daily-brief

version: 1.0
role: guide-leader-manager
purpose: 生成出团前 Briefing 并对齐安全与无障碍要点。
inputs: [团名/日期/人数/语言, 值班/联系人, 站点/集合点/安全]
outputs: [docs/guide/daily-brief-YYYYMMDD.md]
steps:

- 渲染 templates/daily-briefing-tmpl.yaml
- 执行 daily-brief-check 清单
  acceptance:
- 关键信息完整
- 安全与无障碍已覆盖
