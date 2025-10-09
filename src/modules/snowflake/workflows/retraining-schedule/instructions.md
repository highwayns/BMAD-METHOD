# retraining-schedule - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/retraining-schedule/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this retraining schedule & triggers</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="触发（时间/漂移/性能/业务事件）">
<action>Work on 触发（时间/漂移/性能/业务事件）</action>
<template-output section="triggers"/>
</step>

<step n="3" goal="预算/资源与并发">
<action>Work on 预算/资源与并发</action>
<template-output section="budget"/>
</step>

<step n="4" goal="验证与签发/切换/回退">
<action>Work on 验证与签发/切换/回退</action>
<template-output section="validation"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
