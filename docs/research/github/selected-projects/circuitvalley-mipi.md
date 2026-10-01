# circuitvalley/mipi_csi_receiver_FPGA

- URL：https://github.com/circuitvalley/mipi_csi_receiver_FPGA
- 平台：Lattice MachXO3LF
- 语言：Verilog
- 许可证：CC BY 4.0
- 关联 Goal：1、2
- 适配等级：C

## 项目内容

通用 MIPI CSI-2 接收器，README 提到测试过 IMX219，并覆盖多个分辨率和帧率。

## 可借鉴

- CSI-2 接收模块的拆分方式。
- 摄像头数据、帧率和分辨率控制思路。
- 传感器控制和视频流调试方法。

## 风险

仓库 README 标记该版本为 Legacy，且目标是 Lattice。不得直接复制其 PHY、时钟和管脚约束。
