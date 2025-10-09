# pipeline-tests - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/pipeline-tests/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this pipeline tests (streams/tasks/dynamic tables)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="拓扑/依赖/优先级">
<action>Work on 拓扑/依赖/优先级</action>
<template-output section="topology"/>
</step>

<step n="3" goal="失败/重试/死信/回算">
<action>Work on 失败/重试/死信/回算</action>
<template-output section="failure"/>
</step>

<step n="4" goal="SLI（延迟/错误率/新鲜度）">
<action>Work on sli（延迟/错误率/新鲜度）</action>
<template-output section="slis"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
