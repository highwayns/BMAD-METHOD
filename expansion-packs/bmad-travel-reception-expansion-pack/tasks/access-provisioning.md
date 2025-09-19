# task: access-provisioning

version: 1.0
role: tech-systems-dms-crm
purpose: 账户与访问开通/回收与审计。
inputs: [角色/权限/期限/审批]
outputs: [docs/sys/access-<batch>.md]
steps:

- 渲染 templates/agency-onboarding-tmpl.yaml（改写为账户开通）
- 执行 access-review-check 清单
  acceptance:
- 最小权限
- 审计可查
