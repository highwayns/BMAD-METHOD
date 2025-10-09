# release-hooks - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/release-hooks/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this release hooks (dashboards/alerts/budget/access)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="仪表盘链接与阈值">
<action>Work on 仪表盘链接与阈值</action>
<template-output section="dashboards"/>
</step>

<step n="3" goal="预算护栏（资源监控）">
<action>Work on 预算护栏（资源监控）</action>
<template-output section="budgets"/>
</step>

<step n="4" goal="临时访问与回收">
<action>Work on 临时访问与回收</action>
<template-output section="access"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
