# service-catalog - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/service-catalog/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this service catalog (runbooks/slas/owners)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="清单（数据产品/作业/端点）">
<action>Work on 清单（数据产品/作业/端点）</action>
<template-output section="inventory"/>
</step>

<step n="3" goal="SLA/SLO/预算">
<action>Work on sla/slo/预算</action>
<template-output section="sla"/>
</step>

<step n="4" goal="运行手册与值班信息">
<action>Work on 运行手册与值班信息</action>
<template-output section="runbooks"/>
</step>

<step n="5" goal="生命周期与弃用">
<action>Work on 生命周期与弃用</action>
<template-output section="lifecycle"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
