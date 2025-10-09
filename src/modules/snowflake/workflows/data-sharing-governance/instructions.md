# data-sharing-governance - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/data-sharing-governance/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data sharing governance (reader/provider/consumer)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="模式（直连/Reader/Listing/跨租）">
<action>Work on 模式（直连/reader/listing/跨租）</action>
<template-output section="patterns"/>
</step>

<step n="3" goal="限制/审计/撤销/SLAs">
<action>Work on 限制/审计/撤销/slas</action>
<template-output section="controls"/>
</step>

<step n="4" goal="数据契约与隐私条款">
<action>Work on 数据契约与隐私条款</action>
<template-output section="contracts"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
