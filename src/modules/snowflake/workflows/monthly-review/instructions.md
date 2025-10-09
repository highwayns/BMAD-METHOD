# monthly-review - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/monthly-review/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this monthly review & optimization roadmap</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="KPI（Credit/Unit Cost/Savings/Hit Ratio）">
<action>Work on kpi（credit/unit cost/savings/hit ratio）</action>
<template-output section="kpis"/>
</step>

<step n="3" goal="当月优化项与节省">
<action>Work on 当月优化项与节省</action>
<template-output section="wins"/>
</step>

<step n="4" goal="下月计划与风险">
<action>Work on 下月计划与风险</action>
<template-output section="roadmap"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
