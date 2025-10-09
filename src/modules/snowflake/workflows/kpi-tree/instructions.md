# kpi-tree - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/kpi-tree/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this kpi tree</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="北极星指标">
<action>Work on 北极星指标</action>
<template-output section="north-star"/>
</step>

<step n="3" goal="分解（输入/过程/输出指标）">
<action>Work on 分解（输入/过程/输出指标）</action>
<template-output section="breakdown"/>
</step>

<step n="4" goal="Owner 与报表频率">
<action>Work on owner 与报表频率</action>
<template-output section="ownership"/>
</step>

<step n="5" goal="目标与阈值（告警门槛）">
<action>Work on 目标与阈值（告警门槛）</action>
<template-output section="targets"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
