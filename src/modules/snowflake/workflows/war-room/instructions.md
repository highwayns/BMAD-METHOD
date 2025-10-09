# war-room - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/war-room/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this war room (bridge/zoom/slack/notes)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="工具（Bridge/Zoom/录制/笔记）">
<action>Work on 工具（bridge/zoom/录制/笔记）</action>
<template-output section="tools"/>
</step>

<step n="3" goal="规则（单线程沟通/指令复述）">
<action>Work on 规则（单线程沟通/指令复述）</action>
<template-output section="rules"/>
</step>

<step n="4" goal="时间线与决策记录">
<action>Work on 时间线与决策记录</action>
<template-output section="timeline"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
