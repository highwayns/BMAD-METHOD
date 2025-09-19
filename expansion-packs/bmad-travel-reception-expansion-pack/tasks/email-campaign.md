# task: email-campaign

version: 1.0
role: content-branding
purpose: 邮件活动策划与可达性。
outputs: [docs/campaign/email-campaign.md]
steps:

- 渲染 templates/email-campaign-tmpl.yaml
- 执行 email-deliverability-check
  acceptance:
- 可达与退订有效
