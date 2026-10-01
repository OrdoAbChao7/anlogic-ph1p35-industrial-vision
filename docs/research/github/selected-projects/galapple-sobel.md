# Galapple/Image-processing---Verilog

- URL：https://github.com/Galapple/Image-processing---Verilog
- 平台：PYNQ-Z2 / Xilinx
- 语言：Verilog
- 许可证：需以仓库当前 LICENSE 为准
- 关联 Goal：4
- 适配等级：B

## 项目内容

项目实现 Sobel 边缘检测，包含 4 行缓存、9 像素窗口、卷积模块、图像控制模块和输出 FIFO。

## 可借鉴

- Line Buffer 的缓存组织。
- 3×3 卷积的输入输出关系。
- 一帧图像仿真结果的检查方式。

## 实现注意

迁移到 PH1P35 时必须重新确定 RAM 推断方式、时钟、输入像素接口和有效信号延迟。
