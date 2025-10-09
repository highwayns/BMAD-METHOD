# schema-contract - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/schema-contract/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this schema contract</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="模型（表/视图/动态表）与主键">
<action>Work on 模型（表/视图/动态表）与主键</action>
<template-output section="model"/>
</step>

<step n="3" goal="字段（类型/必填/唯一/字典/掩码）">
<action>Work on 字段（类型/必填/唯一/字典/掩码）</action>
<template-output section="fields"/>
</step>

<step n="4" goal="业务规则与约束（含示例）">
<action>Work on 业务规则与约束（含示例）</action>
<template-output section="rules"/>
</step>

<step n="5" goal="质量规则（完整性/唯一性/范围/关联）">
<action>Work on 质量规则（完整性/唯一性/范围/关联）</action>
<template-output section="quality"/>
</step>

<step n="6" goal="变更策略（向后兼容/弃用计划）">
<action>Work on 变更策略（向后兼容/弃用计划）</action>
<template-output section="changes"/>
</step>

<step n="7" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
