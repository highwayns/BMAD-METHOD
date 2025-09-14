# Handoff Contracts

| From       | To            | Trigger             | Inputs                   | Outputs        | Acceptance        |
| ---------- | ------------- | ------------------- | ------------------------ | -------------- | ----------------- |
| Front Desk | Triage        | Patient Arrived     | appointment_schedule.csv | triage record  | 等级/等待时限达标 |
| Triage     | Physician     | Triage Complete     | triage record            | orders (CPOE)  | 完整与可执行      |
| Physician  | Lab/Radiology | Orders Placed       | orders                   | results        | TAT 与关键值告警  |
| Physician  | Pharmacy      | Medication Orders   | eRx                      | dispensed meds | 交叉校验通过      |
| Ward/OR    | Nursing       | Admission/Procedure | orders & plan            | care plan      | SBAR 完整         |
| Nursing    | Billing/RCM   | Discharge           | services docs            | claim          | 编码与对账正确    |
| Billing    | Follow-up     | Claim Filed         | claim id                 | follow-up plan | 回访计划就绪      |
