# 视频链路一致性检查

## 当前可确认的架构

```text
SC500CS
  ↓ MIPI CSI-2 / RAW 数据（具体位宽、Bayer 和 Lane 待确认）
PH1P35 MIPI 官方 IP
  ↓ 并行像素流（端口和位宽待以 IP 手册确认）
基础 ISP / Demosaic
  ↓ RGB 或灰度像素流
算法流水线
  ↓ 处理后的像素和同步信号
DDR / Framebuffer
  ↓ HDMI 视频输出时钟域
HDMI 官方 IP
```

## 已确认

- 题目要求 MIPI 摄像头输入和 HDMI 输出。
- 官方示例包含 MIPI、DDR、HDMI 和图像算法路径。
- 1280×720@60Hz 是题目建议的视频模式。

## 待确认

- SC500CS 的 RAW 位宽、Bayer 顺序、Lane 数量和初始化寄存器。
- 安路 MIPI IP 输出的像素位宽、valid、frame/line boundary 和时钟。
- DDR 帧缓存像素格式、缓冲深度和读写仲裁方式。
- HDMI IP 的输入格式、PLL 配置和开发板电气连接。

## 结论

在上述待确认项关闭前，Goal 3 的算法接口应设计成可适配像素位宽和输入格式的模块，不能假定摄像头已经直接输出 RGB。
