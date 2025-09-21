# API Contract Testing & Mock Strategy

## Purpose

以契约测试保护接口兼容性，并通过Mock加速开发与CI。

## Inputs

- API定义/依赖/变更计划
- templates/api-contract-spec-tmpl.yaml
- templates/mock-service-spec-tmpl.yaml
- checklists/api-contract-compatibility.md

## Outputs

- 契约规范与Mock服务说明。

## Steps

1. 选择IDL/规范（OpenAPI/GraphQL等）
2. 场景与破坏性变更检测
3. 提供Mock/录制回放/金丝雀比对
4. 在PR与合并门强制契约测试
5. 版本与弃用策略/发布节奏
