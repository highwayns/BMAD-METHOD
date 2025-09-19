# task: lead-routing-config

version: 1.0
role: tech-systems-dms-crm
purpose: 配置线索分配规则与SLA监控。
inputs: [区域/语言/渠道/优先级, SLA/备援/重分配]
outputs: [docs/sys/lead-routing-<region>.md]
steps:

- 渲染 templates/lead-routing-rules-tmpl.yaml
- 执行 lead-routing-check 清单
  acceptance:
- 首响达标
- 无长时间滞留
