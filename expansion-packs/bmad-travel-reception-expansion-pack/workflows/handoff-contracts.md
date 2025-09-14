# Handoff Contracts

| From        | To               | Trigger          | Inputs                  | Outputs                   | Acceptance      |
| ----------- | ---------------- | ---------------- | ----------------------- | ------------------------- | --------------- |
| Sales       | Itinerary Design | Intake Approved  | client_requirements.md  | draft itinerary           | 预算/偏好一致   |
| Itinerary   | Contracting      | Itinerary Locked | draft itinerary         | vendor shortlist & quotes | SLA/资质符合    |
| Contracting | Booking          | Contracts Signed | quotes + contracts      | confirmed bookings        | 控位/房单可用   |
| Booking     | On-site Ops      | Vouchers Ready   | bookings.csv + vouchers | ops pack                  | 日程/联系人完整 |
| On-site     | Finance          | Tour Complete    | daily logs + approvals  | invoice package           | 对账一致        |
| Finance     | Account          | Payment Posted   | invoice + receipt       | closure report            | KPI/复盘完成    |
