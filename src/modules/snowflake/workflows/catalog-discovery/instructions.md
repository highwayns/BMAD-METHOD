# catalog-discovery - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/catalog-discovery/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this catalog & discovery</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="术语表与口径">
<action>Work on 术语表与口径</action>
<template-output section="glossary"/>
</step>

<step n="3" goal="目录/元数据/血缘">
<action>Work on 目录/元数据/血缘</action>
<template-output section="catalog"/>
</step>

<step n="4" goal="与外部工具集成（dbt/Looker/PowerBI/Atlan/Collibra）">
<action>Work on 与外部工具集成（dbt/looker/powerbi/atlan/collibra）</action>
<template-output section="integration"/>
</step>

<step n="5" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
