# contract-ci - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/contract-ci/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data contract ci (schema/quality/semantics)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="结构契约（列/类型/约束）">
<action>Work on 结构契约（列/类型/约束）</action>
<template-output section="schema"/>
</step>

<step n="3" goal="质量契约（规则/阈值）">
<action>Work on 质量契约（规则/阈值）</action>
<template-output section="quality"/>
</step>

<step n="4" goal="语义契约（口径/血缘）">
<action>Work on 语义契约（口径/血缘）</action>
<template-output section="semantics"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
