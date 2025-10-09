# consent-purpose - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/consent-purpose/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this consent & purpose limitation</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="同意获取/撤回/记录/有效期">
<action>Work on 同意获取/撤回/记录/有效期</action>
<template-output section="consent"/>
</step>

<step n="3" goal="用途白名单/黑名单与运行时校验">
<action>Work on 用途白名单/黑名单与运行时校验</action>
<template-output section="purpose"/>
</step>

<step n="4" goal="同意与用途在下游传播（视图/策略）">
<action>Work on 同意与用途在下游传播（视图/策略）</action>
<template-output section="propagation"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
