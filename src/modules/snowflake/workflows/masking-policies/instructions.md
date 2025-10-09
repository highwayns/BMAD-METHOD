# masking-policies - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/masking-policies/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this masking policies (column/conditional/context-aware)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="模式（正则/哈希/置换/部分显示）">
<action>Work on 模式（正则/哈希/置换/部分显示）</action>
<template-output section="patterns"/>
</step>

<step n="3" goal="基于角色/会话/标签的条件">
<action>Work on 基于角色/会话/标签的条件</action>
<template-output section="context"/>
</step>

<step n="4" goal="例外与审计">
<action>Work on 例外与审计</action>
<template-output section="exceptions"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
