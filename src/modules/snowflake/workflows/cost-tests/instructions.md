# cost-tests - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/cost-tests/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this cost tests (unit cost/resource monitors)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="单位成本（Cost/Query/GB/Feature）">
<action>Work on 单位成本（cost/query/gb/feature）</action>
<template-output section="unit"/>
</step>

<step n="3" goal="资源监控/阈值/动作">
<action>Work on 资源监控/阈值/动作</action>
<template-output section="budgets"/>
</step>

<step n="4" goal="证据与合规">
<action>Work on 证据与合规</action>
<template-output section="evidence"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
