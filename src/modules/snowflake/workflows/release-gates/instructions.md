# release-gates - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/release-gates/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this release gates (blocking conditions)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="阻断条件与豁免流程">
<action>Work on 阻断条件与豁免流程</action>
<template-output section="blockers"/>
</step>

<step n="3" goal="门禁→合规条款/风险">
<action>Work on 门禁→合规条款/风险</action>
<template-output section="mapping"/>
</step>

<step n="4" goal="证据与审计">
<action>Work on 证据与审计</action>
<template-output section="audit"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
