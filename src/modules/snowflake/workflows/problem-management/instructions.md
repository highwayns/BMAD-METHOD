# problem-management - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/problem-management/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this problem management (rca/ke/backlog)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="根因分析（Fishbone/5Whys/Mapping）">
<action>Work on 根因分析（fishbone/5whys/mapping）</action>
<template-output section="rca"/>
</step>

<step n="3" goal="知识库与Runbook更新">
<action>Work on 知识库与runbook更新</action>
<template-output section="knowledge"/>
</step>

<step n="4" goal="积压与优先级/跟踪">
<action>Work on 积压与优先级/跟踪</action>
<template-output section="backlog"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
