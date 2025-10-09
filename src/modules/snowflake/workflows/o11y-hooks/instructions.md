# o11y-hooks - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/o11y-hooks/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this observability hooks (dashboards/alerts/runbooks)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="仪表盘/链接/阈值">
<action>Work on 仪表盘/链接/阈值</action>
<template-output section="dashboards"/>
</step>

<step n="3" goal="告警路由/静默/升级">
<action>Work on 告警路由/静默/升级</action>
<template-output section="alerts"/>
</step>

<step n="4" goal="运行手册与自动修复">
<action>Work on 运行手册与自动修复</action>
<template-output section="runbooks"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
