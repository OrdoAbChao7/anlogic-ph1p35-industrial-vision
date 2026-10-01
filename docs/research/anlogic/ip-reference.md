# 安路 IP 和参考设计资料卡

- 来源：https://www.anlogic.com/support/ip
- 类型：官方资料入口
- 关联 Goal：1、2、3

## 重点检索对象

- MIPI D-PHY / CSI-2
- 视频输入和视频输出
- DDR / Framebuffer
- PLL / 时钟
- MCU / 外设控制
- OSD 或 Logo 叠加

## 使用方法

先确认手册的支持系列和版本，再确认端口定义、时钟要求、复位要求、输入输出像素格式和示例工程。

## 复用原则

安路官方 IP 和官方例程优先复用。自写模块主要放在：

```text
rgb2gray
threshold
sobel
line_buffer
object_stats
osd
```

MIPI PHY、DDR Controller、HDMI PHY、复杂时钟和管脚约束暂不自行重写。
