# elt-pipelines - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/elt-pipelines/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this elt pipelines (tasks/dt/sos/mv)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="拓扑/依赖/优先级">
<action>Work on 拓扑/依赖/优先级</action>
<template-output section="topology"/>
</step>

<step n="3" goal="新鲜度与目标延迟（TARGET_LAG）">
<action>Work on 新鲜度与目标延迟（target_lag）</action>
<template-output section="freshness"/>
</step>

<step n="4" goal="失败/重试/回退/回算">
<action>Work on 失败/重试/回退/回算</action>
<template-output section="reliability"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
