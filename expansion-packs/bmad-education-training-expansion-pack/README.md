# BMAD-Method｜教育培训（Education & Training）管理团队扩展包

## Overview

本扩展包面向 K12/高教/职教/企业内训/在线教育等场景，提供 **标准化的管理团队角色、代理、任务、输出模板、检查清单与编排**，
以 BMAD 方法落地 **从办学治理→项目/课程→教学设计→授课与运营→评估与认证→数据与隐私→市场与招生→就业与成果** 的闭环。

## Purpose

补齐教育培训管理的关键能力：

- **治理与合规**（办学资质、认证/评估、师资资质、未成年保护/FERPA/GDPR）
- **课程体系与教学设计**（O\*Net/职教能力标准、布鲁姆、ADDIE、Backward Design、微课/项目制）
- **学习平台与交付**（LMS/LXP、课堂/在线/混合、考勤与互动、SCORM/xAPI 追踪）
- **测评与学术诚信**（题库、Rubric、监考、防作弊、证书/学分）
- **学习数据与干预**（学习分析、预警、保留率、就业/转化）
- **招生与市场**（品牌/活动、漏斗、CRM、B2B/B2G 合作）
- **师训与教研**（教案/磨课/观摩、同行评审、持续改进）

## What's Included

- Agents：`agents/education-training.md`
- Templates (Output)：`templates/output/edu-architecture-tmpl.yaml`、`templates/output/edu-implementation-tmpl.yaml`
- Tasks：`tasks/create-doc-edu-architecture.md`、`tasks/review-operations.md`、`tasks/validate-operations.md`
- Checklists：`checklists/edu-operations-checklist.md`（16 大质量门）
- Roles & Manifests：`roles/*.md`（18 角色）与 `manifests/*`
- Workflows：`workflows/*`（编排手册、Mermaid 泳道图与交接契约）
- Data & Policies：`templates/data/*.csv` 与 `templates/policies/*`，`templates/monitoring/*`

## Integration with Core BMAD

1. **After Program Blueprint**：锁定项目/课程/认证与合规边界 → 进入《运营架构》
2. **Parallel to Delivery**：教研/授课/考评/学服/招生流水线联动
3. **Before Accreditation/Release/Reporting**：走 `validate-operations` 与检查清单质量门

## Usage

```
*agent education-training → *create-doc edu-architecture
*agent education-training → *review-operations
*agent education-training → *validate-operations
```

## Notes

- 模板变量使用 `{var}`；`<critical_rule>` 为强规则。
- 本扩展包用于流程与文档标准化，不替代当地监管/认证机构要求。

---

_Version: 1.0.0_ · _Compatible with BMAD Core >= 1.10_ · _Last Updated: 2025-09-10_
