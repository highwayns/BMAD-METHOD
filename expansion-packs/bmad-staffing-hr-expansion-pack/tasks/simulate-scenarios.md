# Task: simulate-scenarios

- 输入：需求信号（客户/站点/岗位/班次）、供给池（技能/等级/可用性）、约束（工时/加班/证照）、SLA/成本阈值
- 输出：覆盖率、利用率、成本、OT、风险热力图；推荐方案与变更单
- 方法：Baseline/Optimistic/Pessimistic/Surge；蒙特卡洛；线性/整数规划（可选）
- 验收：Coverage ≥ 95% 且 Cost ≤ 预算 或签批例外；生成证据与版本号
