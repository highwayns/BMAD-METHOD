# task: content-strategy

version: 1.0
role: content-branding
purpose: 输出季度内容策略与渠道分配。
outputs: [docs/content/strategy-<yyq>.md]
steps:

- 渲染 templates/content-strategy-tmpl.yaml
- 执行 seasonality-calendar-check
  acceptance:
- 旺季覆盖, KPI量化
