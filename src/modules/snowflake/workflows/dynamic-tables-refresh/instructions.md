# dynamic-tables-refresh - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/dynamic-tables-refresh/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this dynamic tables refresh strategy</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="TARGET_LAG/优先级与依赖">
<action>Work on target_lag/优先级与依赖</action>
<template-output section="target_lag"/>
</step>

<step n="3" goal="专用仓库/并发策略">
<action>Work on 专用仓库/并发策略</action>
<template-output section="warehouse"/>
</step>

<step n="4" goal="失败检测/重算/回退">
<action>Work on 失败检测/重算/回退</action>
<template-output section="failure"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
