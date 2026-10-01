# FHDO-ICLAB/MIPI-CSI-2-HDMI-Bridge

- URL：https://github.com/FHDO-ICLAB/MIPI-CSI-2-HDMI-Bridge
- 平台：Cologne Chip GateMate
- 语言：Verilog
- 许可证：仓库 README 未明确记录，默认只读学习
- 关联 Goal：1、2
- 适配等级：C

## 项目内容

该项目包含 MIPI CSI-2 接收、简单 Framebuffer 和 DVI 输出，可驱动 HDMI 显示器。

## 可借鉴

- 摄像头接入到显示输出的模块层次。
- CSI-2 接收后进入帧缓存的思路。
- 视频输出前的数据组织方式。

## 不可直接移植

GateMate 的 PHY、IO、时钟和约束不能直接用于 PH1P35。你们应优先使用安路官方 MIPI、DDR 和 HDMI 例程。
