# task: crisis-comms-playbook

version: 1.0
role: content-branding
purpose: 危机公关剧本与演练记录。
outputs: [docs/crisis/crisis-comms-playbook.md]
steps:

- 渲染 templates/crisis-comms-playbook-tmpl.yaml
- 执行 crisis-readiness-check
  acceptance:
- 口径统一、可演练
