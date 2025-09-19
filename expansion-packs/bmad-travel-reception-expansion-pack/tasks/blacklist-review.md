# task: blacklist-review

version: 1.0
role: guide-leader-manager
purpose: 更新导游黑白名单/观察名单并形成决定。
inputs: [投诉/事故/违约/优秀案例, 证据与口径]
outputs: [reports/guide-blacklist-review-<period>.md]
steps:

- 渲染 templates/blacklist-review-tmpl.yaml
- 记录决策与复核时间表
  acceptance:
- 证据充分/结论清晰
- 复核在案
