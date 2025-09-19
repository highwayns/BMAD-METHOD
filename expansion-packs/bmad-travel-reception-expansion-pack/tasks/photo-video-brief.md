# task: photo-video-brief

version: 1.0
role: content-branding
purpose: 拍摄Brief（地点/时段/器材/备份）。
outputs: [docs/asset/photo-video-brief.md]
steps:

- 渲染 templates/photo-video-brief-tmpl.yaml
  acceptance:
- 走位与备援到位
