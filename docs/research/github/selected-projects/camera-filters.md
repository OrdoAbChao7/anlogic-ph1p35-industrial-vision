# olivier-le-sage/camera-filters

- URL：https://github.com/olivier-le-sage/camera-filters
- 平台：Spartan-7，配合 MIPI-to-HDMI pipeline
- 语言：VHDL
- 许可证：MIT
- 关联 Goal：3、7
- 适配等级：B

## 项目内容

在 Demosaic 和 HDMI 之间插入颜色处理模块，包含 Gamma、对比度、亮度和 RGB/YUV 变换。

## 可借鉴

- 如何把自定义图像模块插入现有 MIPI 到 HDMI 视频链路。
- 用整数、移位和定点近似替代浮点运算。
- 通过模块化函数控制资源占用。

## 不可直接移植

该仓库主要为 VHDL 和 Xilinx 体系，底层视频接口不能直接用于 PH1P35。
