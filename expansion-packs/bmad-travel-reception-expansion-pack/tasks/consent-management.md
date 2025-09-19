# task: consent-management

version: 1.0
role: tech-systems-dms-crm
purpose: 搭建同意与偏好中心并全链路同步退订/黑名单。
inputs: [渠道/目的/默认/保留期]
outputs: [docs/sys/consent-center.md]
steps:

- 渲染 templates/consent-preference-center-tmpl.yaml
- 执行 consent-compliance-check 清单
  acceptance:
- 同意记录完备
- 退订生效及时
