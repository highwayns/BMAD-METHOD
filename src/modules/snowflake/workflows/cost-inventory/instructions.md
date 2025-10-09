# cost-inventory - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/cost-inventory/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this cost inventory & baseline</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="数据源（Account Usage/Information Schema/自定义）">
<action>Work on 数据源（account usage/information schema/自定义）</action>
<template-output section="sources"/>
</step>

<step n="3" goal="维度（仓库/角色/项目/域/标签）">
<action>Work on 维度（仓库/角色/项目/域/标签）</action>
<template-output section="breakdown"/>
</step>

<step n="4" goal="基线（d/w/m）与单位成本">
<action>Work on 基线（d/w/m）与单位成本</action>
<template-output section="baseline"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
