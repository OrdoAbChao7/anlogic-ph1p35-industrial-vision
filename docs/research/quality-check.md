# 资料库质量检查

## 每条资料入库检查

- 来源 URL 或本地路径存在。
- 标题和来源类型准确。
- 平台已标注，无法确认时写 `unknown`。
- 关联 Goal 已标注。
- 关键结论能定位到原文、README、PDF 页面或当前工程文件。
- 已区分可直接使用、结构参考和只读学习。
- GitHub 项目已记录许可证或明确标记为只读学习。
- 资料卡记录访问日期。

## 每次发布检查

- `INDEX.md` 能找到所有资料类别。
- `sources.yaml` 中的 ID 不重复。
- 每个 Goal 至少有一份核心资料和一份参考资料。
- 所有非 PH1P35 工程都标明平台差异。
- `known-gaps.md` 已记录关键未知项。
- 不存在把教程推断写成硬件事实的表述。
- 资料库不包含密钥、账号、私有链接或无关大文件。

## 验证命令

```powershell
rg --files docs/research
rg -n "https?://|E:/|type:|platform:|related_goals:" docs/research
```
