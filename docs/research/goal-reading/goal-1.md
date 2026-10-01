# Goal 1：视频硬件闭环

## 目标

实现 `SC500CS → MIPI → PH1P35 → HDMI → 显示器` 的稳定视频闭环。

## 必读资料

- [比赛要求](../competition/topic2-requirements.md)
- [安路官方资料索引](../anlogic/official-index.md)
- [PH1P35 资料](../anlogic/ph1p35.md)
- [MIPI CSI-2](../mipi-video/mipi-csi2.md)
- [HDMI 时序](../mipi-video/hdmi-timing.md)
- [视频链路一致性检查](../mipi-video/link-consistency.md)

## 选读资料

- [安路 PH1A 摄像头方案](../anlogic/camera-solution.md)
- [FHDO MIPI-HDMI](../github/selected-projects/fhdo-mipi-hdmi.md)

## 输出

完成官方工程审计、编译、下载和硬件验收记录。

## 前置知识

无。只需要准备 PH1P35 开发板、SC500CS、HDMI 显示器、下载器和官方工程资料；MIPI、HDMI、时钟和复位概念在本 Goal 中边做边学。

## 通过标准

显示器连续显示摄像头画面，工程可重复编译和下载。
