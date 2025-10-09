# cross-border-sharing - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/cross-border-sharing/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this cross-border transfer & sharing governance</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="传输机制（SCC/CPA/备案）">
<action>Work on 传输机制（scc/cpa/备案）</action>
<template-output section="transfers"/>
</step>

<step n="3" goal="区域/租户/再分发限制">
<action>Work on 区域/租户/再分发限制</action>
<template-output section="restrictions"/>
</step>

<step n="4" goal="审计/撤销/速断机制">
<action>Work on 审计/撤销/速断机制</action>
<template-output section="monitoring"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
