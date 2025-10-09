# semantic-model - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/semantic-model/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this semantic model (dimensions/measures/policies)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="维度（主键/层级/慢变）">
<action>Work on 维度（主键/层级/慢变）</action>
<template-output section="dimensions"/>
</step>

<step n="3" goal="度量（聚合/口径/约束）">
<action>Work on 度量（聚合/口径/约束）</action>
<template-output section="measures"/>
</step>

<step n="4" goal="关联策略与主外键">
<action>Work on 关联策略与主外键</action>
<template-output section="joins"/>
</step>

<step n="5" goal="权限/标签/屏蔽/行访问">
<action>Work on 权限/标签/屏蔽/行访问</action>
<template-output section="policies"/>
</step>

<step n="6" goal="变更与版本（兼容策略）">
<action>Work on 变更与版本（兼容策略）</action>
<template-output section="governance"/>
</step>

<step n="7" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
