# posture-review - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/posture-review/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this platform posture review (quarterly)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="可靠性与SLO达成">
<action>Work on 可靠性与slo达成</action>
<template-output section="reliability"/>
</step>

<step n="3" goal="安全/审计/权限">
<action>Work on 安全/审计/权限</action>
<template-output section="security"/>
</step>

<step n="4" goal="成本/预算/优化">
<action>Work on 成本/预算/优化</action>
<template-output section="cost"/>
</step>

<step n="5" goal="风险/改进与路线图">
<action>Work on 风险/改进与路线图</action>
<template-output section="roadmap"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
