<!-- Powered by BMAD™ Core -->

# Snowflake Infrastructure & Platform Checklist

用于生产前系统性验证 Snowflake 平台的安全、合规、可靠性与实现质量（角色：DevOps/Platform）。

## 1. SECURITY & COMPLIANCE

### 1.1 Access Management

- [ ] 最小权限 RBAC；服务账号有审计记录

### 1.2 Data Protection

- [ ] 存储与传输加密启用；KMS/Secrets 管理

### 1.3 Network Security

- [ ] PrivateLink/VPN/WAF/分段策略与流量图已落地

## 2. INFRASTRUCTURE AS CODE

### 2.1 IaC Implementation

- [ ] Snowflake 对象以 IaC/脚本化定义（禁止手工漂移）

### 2.2 IaC Quality & Management

- [ ] 评审/状态管理/非生产验证/文档更新

## 3. RESILIENCE & AVAILABILITY

- [ ] 多区域/DR 方案，关键任务具备故障切换/重试

## 4. BACKUP & DISASTER RECOVERY

- [ ] 备份策略/保留期/演练记录完备

## 5. MONITORING & OBSERVABILITY

- [ ] 指标/日志/追踪/用户体验监控覆盖；SLO 与告警

## 6. PERFORMANCE & OPTIMIZATION

- [ ] 基准/容量/延迟吞吐目标；仓库尺寸与 auto-suspend 调优

## 7. OPERATIONS & GOVERNANCE

- [ ] 运行手册、变更记录、配置基线、责任矩阵

## 8. CI/CD & DEPLOYMENT

- [ ] 流水线、配置校验、零停机/回滚演练与记录

## 9. NETWORKING & CONNECTIVITY

- [ ] 专线/私有端点/路由/防火墙策略与监控

## 10. COMPLIANCE & DOCUMENTATION

- [ ] 证据留存、NFR 验证、许可证/三方依赖记录

## 11. BMAD WORKFLOW INTEGRATION

- [ ] 与开发/产品/架构的需求与时序完全对齐

## 12. ARCHITECTURE DOCUMENTATION VALIDATION

- [ ] 文档完整/一致/可用；图/ADR/演进/强规则高亮

## 13. CONTAINER PLATFORM VALIDATION

- [ ] （若使用）K8s 集成/RBAC/网络/镜像安全/弹性

## 14. GITOPS WORKFLOWS VALIDATION

- [ ] （若使用）控制器/仓库结构/参数化/策略/回滚

## 15. SERVICE MESH VALIDATION

- [ ] （若使用）流量治理/mTLS/可观测/拓扑

## 16. DEVELOPER EXPERIENCE PLATFORM VALIDATION

- [ ] 自助/金路径模板/API/文档/度量与反馈

---

### Prerequisites Verified

- [ ] 16 章已审阅；无未解决的高危；非生产验证通过；回滚演练通过；审批完备；与 ADR/PRD/研发里程碑对齐
