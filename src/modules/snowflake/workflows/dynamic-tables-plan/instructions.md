# dynamic-tables-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/dynamic-tables-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this dynamic tables plan</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="刷新策略（TARGET_LAG/优先级）">
<action>Work on 刷新策略（target_lag/优先级）</action>
<template-output section="refresh"/>
</step>

<step n="3" goal="依赖与更新顺序">
<action>Work on 依赖与更新顺序</action>
<template-output section="dependencies"/>
</step>

<step n="4" goal="专用仓库与并发策略">
<action>Work on 专用仓库与并发策略</action>
<template-output section="warehouse"/>
</step>

<step n="5" goal="失败检测/重算/回退">
<action>Work on 失败检测/重算/回退</action>
<template-output section="failure"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
