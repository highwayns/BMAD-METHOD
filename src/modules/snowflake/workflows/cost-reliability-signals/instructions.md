# cost-reliability-signals - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/cost-reliability-signals/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this cost & reliability composite signals</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="单位成本（Cost/Query/GB/Metric）">
<action>Work on 单位成本（cost/query/gb/metric）</action>
<template-output section="unit_cost"/>
</step>

<step n="3" goal="可靠性与成本耦合（队列/溢写→Credit）">
<action>Work on 可靠性与成本耦合（队列/溢写→credit）</action>
<template-output section="coupling"/>
</step>

<step n="4" goal="建议与ROI">
<action>Work on 建议与roi</action>
<template-output section="actions"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
