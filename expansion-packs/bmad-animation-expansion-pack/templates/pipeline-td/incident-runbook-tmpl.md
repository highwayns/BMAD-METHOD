---
template_id: pipeline-td/incident-runbook
version: 1
purpose: 故障应急 Runbook
fields:
  severity: { type: string, enum: [SEV1, SEV2, SEV3] }
  contacts: { type: table, columns: [role, name, phone] }
  steps: { type: table, columns: [step, owner, expected] }
  postmortem: { type: list, items: string }
outputs:
  - dr/incident-runbook.md
---

# Incident Runbook ({{severity}})

## Contacts

{{contacts}}

## Steps

{{steps}}

## Postmortem

- {{postmortem}}
