# golden-paths - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/golden-paths/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this golden paths definition</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="路径目录（ELT/Streaming/BI/ML/Contract）">
<action>Work on 路径目录（elt/streaming/bi/ml/contract）</action>
<template-output section="catalog"/>
</step>

<step n="3" goal="模板与脚手架仓库链接">
<action>Work on 模板与脚手架仓库链接</action>
<template-output section="templates"/>
</step>

<step n="4" goal="护栏（权限/预算/监控/回退）">
<action>Work on 护栏（权限/预算/监控/回退）</action>
<template-output section="guardrails"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
