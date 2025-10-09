# streaming-pipeline - Instructions

<critical>The workflow execution engine is governed by: {project-root}/bmad/core/tasks/workflow.xml</critical>
<critical>You MUST have already loaded and processed: {project-root}/bmad/snowflake/workflows/streaming-pipeline/workflow.yaml</critical>

<workflow>

<step n="1" goal="Understand Requirements">
<action>Ask the user about their requirements for this streaming pipeline (snowpipe/pipes/tasks)</action>
<ask>What are your specific needs and constraints?</ask>
</step>

<step n="2" goal="Ingestion（外部事件/文件）">
<action>Work on ingestion（外部事件/文件）</action>
<template-output section="ingestion"/>
</step>

<step n="3" goal="顺序/去重/迟到与乱序处理">
<action>Work on 顺序/去重/迟到与乱序处理</action>
<template-output section="ordering"/>
</step>

<step n="4" goal="重试/死信/补偿">
<action>Work on 重试/死信/补偿</action>
<template-output section="retries"/>
</step>

<step n="5" goal="并发与背压/慢启动">
<action>Work on 并发与背压/慢启动</action>
<template-output section="scaling"/>
</step>

<step n="6" goal="延迟SLO与监控">
<action>Work on 延迟slo与监控</action>
<template-output section="latency"/>
</step>

<step n="7" goal="Review and Finalize">
<action>Review complete document output</action>
<ask>Any final adjustments needed? (y/n)</ask>
<check>If yes:</check>
  <action>Make requested changes and regenerate output</action>
</step>

</workflow>
