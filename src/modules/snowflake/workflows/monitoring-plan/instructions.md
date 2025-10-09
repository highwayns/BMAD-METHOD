# monitoring-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/monitoring-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this monitoring & sli plan</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="监控SLI与仪表盘">
<action>Work on 监控sli与仪表盘</action>
<template-output section="slis"/>
</step>

<step n="3" goal="告警阈值/路由/当班表">
<action>Work on 告警阈值/路由/当班表</action>
<template-output section="alerts"/>
</step>

<step n="4" goal="成本预算/资源监控（可选）">
<action>Work on 成本预算/资源监控（可选）</action>
<template-output section="budgets"/>
</step>

<step n="5" goal="故障排查SOP与回退">
<action>Work on 故障排查sop与回退</action>
<template-output section="runbooks"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
