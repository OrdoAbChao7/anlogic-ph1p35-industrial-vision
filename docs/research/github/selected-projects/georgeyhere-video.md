# georgeyhere/fpga-video-processing

- URL：https://github.com/georgeyhere/fpga-video-processing
- 平台：Artix-7
- 语言：Verilog
- 许可证：需以仓库当前 LICENSE 为准
- 关联 Goal：3、4
- 适配等级：B

## 项目内容

项目从 OV7670 采集视频，经过 RGB 转灰度、Gaussian 低通和 Sobel 边缘检测，再通过 Framebuffer 和 HDMI 输出。

## 可借鉴

- 图像处理模块的串联方式。
- 3 行缓存和 3×3 像素窗口。
- FIFO、Framebuffer 和 HDMI 之间的关系。
- 通过按键和开关切换处理模式。

## 不可直接移植

OV7670、Artix-7、I2C、Framebuffer 和 HDMI 底层实现与 PH1P35 不同。只移植算法结构和验证思路。
