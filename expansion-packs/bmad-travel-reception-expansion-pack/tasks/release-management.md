# task: release-management

version: 1.0
role: tech-systems-dms-crm
purpose: 组织发布/割接与回滚预案。
inputs: [变更条目/影响/回滚/验证]
outputs: [docs/sys/release-<date>.md]
steps:

- 渲染 templates/release-notes-tmpl.yaml
- 执行 release-cutover-check 清单
  acceptance:
- 无重大回退
- 业务低影响
