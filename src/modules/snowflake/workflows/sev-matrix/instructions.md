# sev-matrix - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/sev-matrix/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this sev matrix (impact/scope/slo breach)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="等级定义（SEV1-4）与触发器">
<action>Work on 等级定义（sev1-4）与触发器</action>
<template-output section="taxonomy"/>
</step>

<step n="3" goal="指标/阈值/SLO 映射">
<action>Work on 指标/阈值/slo 映射</action>
<template-output section="mapping"/>
</step>

<step n="4" goal="升级路径与沟通频率">
<action>Work on 升级路径与沟通频率</action>
<template-output section="actions"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
