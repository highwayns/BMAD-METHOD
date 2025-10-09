# dynamic-tables-promo - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/dynamic-tables-promo/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this dynamic tables promotion (target lag/refresh)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="TARGET_LAG/优先级/依赖">
<action>Work on target_lag/优先级/依赖</action>
<template-output section="target_lag"/>
</step>

<step n="3" goal="刷新策略与失败回退">
<action>Work on 刷新策略与失败回退</action>
<template-output section="refresh"/>
</step>

<step n="4" goal="验证与回算">
<action>Work on 验证与回算</action>
<template-output section="verification"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
