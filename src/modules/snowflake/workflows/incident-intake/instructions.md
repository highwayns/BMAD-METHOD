# incident-intake - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/incident-intake/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this incident intake (signals/reports/tickets)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="来源（告警/客服/自查/他云）">
<action>Work on 来源（告警/客服/自查/他云）</action>
<template-output section="sources"/>
</step>

<step n="3" goal="去重/合并/伪阳性">
<action>Work on 去重/合并/伪阳性</action>
<template-output section="validate"/>
</step>

<step n="4" goal="工单/标签/分派">
<action>Work on 工单/标签/分派</action>
<template-output section="ticket"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
