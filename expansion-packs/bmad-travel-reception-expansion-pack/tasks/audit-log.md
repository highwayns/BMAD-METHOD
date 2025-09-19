# task: audit-log

version: 1.0
role: tech-systems-dms-crm
purpose: 定义审计日志范围/保留与导出。
inputs: [对象/字段/操作/保留/导出]
outputs: [docs/sys/audit-log.md]
steps:

- 渲染 templates/ops-runbook-tmpl.yaml（审计版）
- 执行 audit-trail-check 清单
  acceptance:
- 取证足够
- 检索高效
