# Platform Governance Checklist

> 评分规则：每项使用 ✅/⚠️/❌/N/A，并提供 Notes 与 Evidence 链接。

## 1. 租户与环境边界

- 账户/环境（Dev/Stg/Prod）映射清晰
- 跨环境隔离（网络/权限/存储）有效

## 2. 账户/工作区/网络基线

- 区域/账单标签/私网/审计导出已配置
- Cluster Policies 与 Pools 已启用

## 3. 身份与权限（SCIM/SSO/RBAC/ABAC）

- 身份同步/SSO 单点与组映射
- 最小权限策略与继承通过验证

## 4. 数据治理（UC/分级/遮罩/审计）

- Metastore/External Locations/Storage Credentials
- 标签/分级/行列级策略/视图遮罩

## 5. 变更与发布（审批/回滚/追踪）

- 变更单/审批链/回滚预案齐全
- 发布准入 Gate 报告齐全

## 6. 文档与证据（模板齐全、可追溯）

- 文档完整、可追溯、可复现
