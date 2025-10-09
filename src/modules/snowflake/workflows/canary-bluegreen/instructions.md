# canary-bluegreen - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/canary-bluegreen/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this canary/blue-green strategy</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="分流/门槛/回退">
<action>Work on 分流/门槛/回退</action>
<template-output section="strategy"/>
</step>

<step n="3" goal="SLI/统计检验与门槛">
<action>Work on sli/统计检验与门槛</action>
<template-output section="metrics"/>
</step>

<step n="4" goal="状态页与利益相关者沟通">
<action>Work on 状态页与利益相关者沟通</action>
<template-output section="comms"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
