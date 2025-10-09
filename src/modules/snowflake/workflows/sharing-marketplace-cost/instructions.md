# sharing-marketplace-cost - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/sharing-marketplace-cost/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data sharing/marketplace cost controls</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="Listing/Share 配额与限制">
<action>Work on listing/share 配额与限制</action>
<template-output section="listings"/>
</step>

<step n="3" goal="条款/用途/撤销与计量">
<action>Work on 条款/用途/撤销与计量</action>
<template-output section="contracts"/>
</step>

<step n="4" goal="监控与异常">
<action>Work on 监控与异常</action>
<template-output section="monitoring"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
