# coverage-report - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/coverage-report/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this coverage report (tables/columns/rules/scenarios)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="覆盖对象与列/规则/场景">
<action>Work on 覆盖对象与列/规则/场景</action>
<template-output section="inventory"/>
</step>

<step n="3" goal="缺口与优先级">
<action>Work on 缺口与优先级</action>
<template-output section="gaps"/>
</step>

<step n="4" goal="改进路线图与KPI">
<action>Work on 改进路线图与kpi</action>
<template-output section="roadmap"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
