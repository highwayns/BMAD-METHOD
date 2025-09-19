# task: consent-log

version: 1.0
role: legal-compliance
purpose: 维护用户同意与撤回记录，支撑查证。
inputs: [主体/内容/时间/渠道/撤回]
outputs: [docs/legal/consent-log-<period>.md]
steps:

- 渲染 templates/consent-log-tmpl.yaml
- 执行 cookie-consent-check 清单
  acceptance:
- 记录齐全
- 可检索导出
