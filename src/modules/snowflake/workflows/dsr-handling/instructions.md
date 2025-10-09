# dsr-handling - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/dsr-handling/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data subject requests (access/erase/portability)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="受理/身份验证/时限">
<action>Work on 受理/身份验证/时限</action>
<template-output section="intake"/>
</step>

<step n="3" goal="定位与提取（查询/导出/删除）">
<action>Work on 定位与提取（查询/导出/删除）</action>
<template-output section="find"/>
</step>

<step n="4" goal="响应/记录/申诉">
<action>Work on 响应/记录/申诉</action>
<template-output section="response"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
