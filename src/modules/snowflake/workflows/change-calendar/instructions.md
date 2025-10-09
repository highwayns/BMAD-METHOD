# change-calendar - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/change-calendar/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this change calendar (windows/freeze/conflicts)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="发布窗口与黑名单">
<action>Work on 发布窗口与黑名单</action>
<template-output section="windows"/>
</step>

<step n="3" goal="冲突检测与解决">
<action>Work on 冲突检测与解决</action>
<template-output section="conflicts"/>
</step>

<step n="4" goal="沟通与公告模板">
<action>Work on 沟通与公告模板</action>
<template-output section="comms"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
