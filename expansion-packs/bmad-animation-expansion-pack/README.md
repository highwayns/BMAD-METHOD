# BMAD-Method｜动画制作小组（Creative Pipeline）扩展包

## Overview

本扩展包为动画制作（前期→中期→后期）提供 **标准化的管理团队角色、代理、任务、输出模板、检查清单与编排**，帮助你以 BMAD 方法落地从 **创意立项→资产与镜头生产→合成与交付** 的完整闭环。

## Purpose

在 BMAD 核心流程之外，补齐动画项目中的：

- 管线（Pipeline-as-Code）、资产与镜头管理、命名与版本规范
- DCC 工具栈（Maya/Blender/Houdini/Nuke/DaVinci 等）与自动化发布
- 渲染与队列/农场、缓存与性能、成本与排期（FinOps for Rendering）
- 评审与 Dailies、可观测与 KPI，安全与 IP 合规（水印/权限/加密）

## When to Use This Pack

- 新建或升级动画项目的制作流程/管线
- 需要标准化的角色分工、文档模板、质量门与交接契约
- 需要任务驱动的自动化代理与统一检查清单

## What's Included

### Agents

- `agents/animation-production.md` — 动画制作代理（人格化、命令化、依赖映射）

### Templates (Output)

- `templates/output/animation-architecture-tmpl.yaml`
- `templates/output/animation-implementation-tmpl.yaml`

### Tasks

- `tasks/create-doc-animation-architecture.md` — 交互式产出《动画制作架构》
- `tasks/review-production.md` — 渐进式/YOLO 复核
- `tasks/validate-production.md` — 16 节检查清单驱动的验证与评分

### Checklists

- `checklists/animation-production-checklist.md` — 16 大章节、生产前质量门

### Roles & Manifests

- `roles/*.md`（18 角色）与 `manifests/*`

### Workflows

- `workflows/*` — 编排手册、泳道图与交接契约

### Data & Policies

- `templates/data/*.csv`（资产/镜头/渲染预算/KPI）与 `templates/policies/*`（内容安全）

## Integration with Core BMad

1. **After Creative Brief**：锁定制作契约（镜头/资产口径）→ 进入《制作架构》
2. **Parallel to Production**：资产/镜头流水线运转，自动化发布与评审
3. **Before Delivery**：走 `validate-production` 与检查清单质量门

## Installation

**Manual**

```bash
# 将本扩展包克隆/下载至项目仓库，如 ./bmad-packs/animation
```

## Usage Examples

### 1) 生成制作架构文档

```
*agent animation-production → *create-doc animation-architecture
```

### 2) 复核制作流程

```
*agent animation-production → *review-production
```

### 3) 验证与准入

```
*agent animation-production → *validate-production
```

## Team Integration

- 将本扩展包的检查清单作为**出片/交付前质量门**；在架构模板中引用**文档验证章节**与强规则。

## Dependencies

- 需要选择 DCC 工具栈与评审平台（如 ShotGrid/Ftrack/Kitsu）；渲染与存储方案需可用；变量渲染前需赋值。

## Customization

- 可自定义命名规范、资产/镜头数据契约、评审节奏、渲染预算与告警阈值。

## Notes

- 模板变量使用 `{var}`；`<critical_rule>` 标记的规则为强制性。
- 交付前务必先在样片/测试镜头上验证，并保留评审与签字记录。

---

_Version: 1.0.0_ · _Compatible with BMad Core >= 1.10_
