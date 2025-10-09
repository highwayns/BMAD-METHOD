# contract-tests - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/contract-tests/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data contract tests (schema/quality/semantics)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="结构（列/类型/约束）">
<action>Work on 结构（列/类型/约束）</action>
<template-output section="schema"/>
</step>

<step n="3" goal="质量（空值/唯一/范围/引用）">
<action>Work on 质量（空值/唯一/范围/引用）</action>
<template-output section="quality"/>
</step>

<step n="4" goal="语义（指标口径/血缘）">
<action>Work on 语义（指标口径/血缘）</action>
<template-output section="semantics"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
