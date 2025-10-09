# dq-streaming-plan - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/dq-streaming-plan/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this data quality for streaming (rules/thresholds)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="规则（完整性/唯一性/范围/关联/Schema一致）">
<action>Work on 规则（完整性/唯一性/范围/关联/schema一致）</action>
<template-output section="rules"/>
</step>

<step n="3" goal="阈值/熔断与隔离">
<action>Work on 阈值/熔断与隔离</action>
<template-output section="thresholds"/>
</step>

<step n="4" goal="失败处置/回放/补偿">
<action>Work on 失败处置/回放/补偿</action>
<template-output section="remediation"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
