# task: rights-tracker

version: 1.0
role: content-branding
purpose: 版权台账（到期提醒/证据链接）。
outputs: [docs/legal/rights-tracker.md]
steps:

- 渲染 templates/rights-tracker-tmpl.yaml
  acceptance:
- 100%资产入账
