# training-awareness - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/training-awareness/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this training & awareness program</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="角色与课程大纲">
<action>Work on 角色与课程大纲</action>
<template-output section="audience"/>
</step>

<step n="3" goal="周期/考核/记录">
<action>Work on 周期/考核/记录</action>
<template-output section="cadence"/>
</step>

<step n="4" goal="演练与钓鱼测试">
<action>Work on 演练与钓鱼测试</action>
<template-output section="simulations"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
