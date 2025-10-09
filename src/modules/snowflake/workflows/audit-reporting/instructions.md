# audit-reporting - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/audit-reporting/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this audit & regulatory reporting</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="控制项与证据清单">
<action>Work on 控制项与证据清单</action>
<template-output section="controls"/>
</step>

<step n="3" goal="仪表盘与周期报表">
<action>Work on 仪表盘与周期报表</action>
<template-output section="dashboards"/>
</step>

<step n="4" goal="监管接口与材料库">
<action>Work on 监管接口与材料库</action>
<template-output section="regulators"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
