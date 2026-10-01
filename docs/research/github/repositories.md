# GitHub 参考工程总表

这些仓库用于学习协议、视频链路、图像算法和验证方法。它们面向不同 FPGA 平台，默认不能直接移植到 PH1P35。

| 仓库 | 平台/语言 | 主要关联 | 适配等级 | 使用边界 |
|---|---|---|---|---|
| [FHDO-ICLAB/MIPI-CSI-2-HDMI-Bridge](https://github.com/FHDO-ICLAB/MIPI-CSI-2-HDMI-Bridge) | GateMate / Verilog | MIPI CSI-2、Framebuffer、DVI | C | 只看链路结构 |
| [circuitvalley/mipi_csi_receiver_FPGA](https://github.com/circuitvalley/mipi_csi_receiver_FPGA) | Lattice / Verilog | 通用 MIPI 接收 | C | README 标注 Legacy，只看协议和模块划分 |
| [georgeyhere/fpga-video-processing](https://github.com/georgeyhere/fpga-video-processing) | Artix-7 / Verilog | 灰度、Gaussian、Sobel、FIFO、HDMI | B | 重点借鉴图像流水线 |
| [Galapple/Image-processing---Verilog](https://github.com/Galapple/Image-processing---Verilog) | PYNQ-Z2 / Verilog | Line Buffer、3×3、Sobel、FIFO | B | 重点借鉴 Sobel 和仿真 |
| [olivier-le-sage/camera-filters](https://github.com/olivier-le-sage/camera-filters) | Spartan-7 / VHDL | MIPI 到 HDMI 中间的颜色处理 | B | 借鉴定点颜色处理，不能直接用底层接口 |
| [hdl-util/hdmi](https://github.com/hdl-util/hdmi) | 多平台 / SystemVerilog | HDMI/DVI 输出、视频模式、文字模式 | C | 只作 HDMI 时序和 OSD 参考 |
| [cliffordwolf/SimpleVOut](https://github.com/cliffordwolf/SimpleVOut) | 多平台 / Verilog | VGA/DVI/HDMI 输出、视频 DMA、Overlay | C | 只作视频输出结构参考 |
| [hdl-util/mipi-demo](https://github.com/hdl-util/mipi-demo) | 多平台 | MIPI CSI-2 和 MIPI CCS | C | 只看协议示例 |
| [gatecat/CSI2Rx](https://github.com/gatecat/CSI2Rx) | Xilinx / VHDL | CSI-2 Receiver | C | 不移植 PHY 和器件原语 |

## 适配等级

- A：算法或验证代码可以直接参考。
- B：模块结构可以参考，需要改接口和时序。
- C：只适合协议和架构学习。
- D：与当前项目关联较弱。

## 选择原则

优先阅读带有完整 README、模块图、仿真说明和许可证的仓库。任何直接进入比赛工程的代码，都需要重新检查平台原语、时钟、复位、数据位宽、视频时序和许可证。
