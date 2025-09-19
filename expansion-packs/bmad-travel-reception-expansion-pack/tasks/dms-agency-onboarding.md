# task: dms-agency-onboarding

version: 1.0
role: tech-systems-dms-crm
purpose: 完成代理/经销商准入与门户/API对接。
inputs: [等级/账期/返点/配额, 门户/API/联系人]
outputs: [docs/sys/dms-agency-<partner>.md]
steps:

- 渲染 templates/agency-onboarding-tmpl.yaml
- 执行 access-review-check 与 api-go-live-check
  acceptance:
- 账号/权限正确
- 调用稳定
