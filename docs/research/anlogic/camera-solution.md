# 安路摄像头方案资料卡

- URL：https://www.anlogic.com/news/company-news/35.html
- 平台：PH1A90
- 类型：安路官方架构参考
- 关联 Goal：1、3
- 状态：reference

## 可借鉴内容

该方案给出了 `MIPIIO → MIPI D-PHY → CSI-2 解包 → RAW → 颜色插值/白平衡 → DDR → 视频叠加 → HDMI` 的完整数据流。

## 适配边界

这不是 PH1P35 的题目二工程。PH1A 的 PHY、DDR、SerDes、PLL、管脚约束和具体资源不能直接复制到 PH1P35。它只用于帮助理解 Goal 1 的模块关系。
