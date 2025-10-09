# registry-release - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/registry-release/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this model registry & release</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="注册信息（版本/签名/来源/Owner）">
<action>Work on 注册信息（版本/签名/来源/owner）</action>
<template-output section="registry"/>
</step>

<step n="3" goal="包装（UDF/服务接口/依赖）">
<action>Work on 包装（udf/服务接口/依赖）</action>
<template-output section="packaging"/>
</step>

<step n="4" goal="发布（金丝雀/灰度/回退）">
<action>Work on 发布（金丝雀/灰度/回退）</action>
<template-output section="rollout"/>
</step>

<step n="5" goal="兼容/弃用与迁移指南">
<action>Work on 兼容/弃用与迁移指南</action>
<template-output section="compatibility"/>
</step>

<step n="6" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
