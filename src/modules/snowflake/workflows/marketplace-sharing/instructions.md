# marketplace-sharing - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/marketplace-sharing/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this marketplace sharing (provider/consumer)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="列表与元数据（描述/标签/SLA）">
<action>Work on 列表与元数据（描述/标签/sla）</action>
<template-output section="listing"/>
</step>

<step n="3" goal="访问/用量与限制">
<action>Work on 访问/用量与限制</action>
<template-output section="access"/>
</step>

<step n="4" goal="支持与联系渠道">
<action>Work on 支持与联系渠道</action>
<template-output section="support"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
