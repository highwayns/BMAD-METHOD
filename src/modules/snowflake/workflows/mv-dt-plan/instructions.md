# mv-dt-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/mv-dt-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this materialized views & dynamic tables plan</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="物化视图：聚合/过滤/维护成本">
<action>Work on 物化视图：聚合/过滤/维护成本</action>
<template-output section="mv"/>
</step>

<step n="3" goal="动态表：TARGET_LAG/优先级/依赖">
<action>Work on 动态表：target_lag/优先级/依赖</action>
<template-output section="dt"/>
</step>

<step n="4" goal="失败检测/回退与回算">
<action>Work on 失败检测/回退与回算</action>
<template-output section="fallback"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
