# snowpark-components - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/snowpark-components/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this snowpark components (udf/udaf/sp)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="UDF/UDAF 设计与限制">
<action>Work on udf/udaf 设计与限制</action>
<template-output section="functions"/>
</step>

<step n="3" goal="依赖包管理与版本">
<action>Work on 依赖包管理与版本</action>
<template-output section="packages"/>
</step>

<step n="4" goal="安全/沙箱/最小权限">
<action>Work on 安全/沙箱/最小权限</action>
<template-output section="security"/>
</step>

<step n="5" goal="部署与回滚">
<action>Work on 部署与回滚</action>
<template-output section="deployment"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
