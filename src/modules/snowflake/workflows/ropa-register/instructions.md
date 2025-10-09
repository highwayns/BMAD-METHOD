# ropa-register - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/ropa-register/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this records of processing activities (ropa)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="处理目的/合法基础/数据主体">
<action>Work on 处理目的/合法基础/数据主体</action>
<template-output section="purposes"/>
</step>

<step n="3" goal="接收者/共享/跨境">
<action>Work on 接收者/共享/跨境</action>
<template-output section="recipients"/>
</step>

<step n="4" goal="保留策略/删除流程">
<action>Work on 保留策略/删除流程</action>
<template-output section="retention"/>
</step>

<step n="5" goal="技术与组织措施（TOMs）">
<action>Work on 技术与组织措施（toms）</action>
<template-output section="safeguards"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
