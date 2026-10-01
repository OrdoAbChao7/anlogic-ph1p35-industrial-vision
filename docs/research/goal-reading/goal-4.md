# Goal 4：Sobel 和实时流水线

## 目标

使用 Line Buffer 和 3×3 Window 实现实时边缘检测。

## 必读资料

- [Sobel](../algorithms/sobel.md)
- [Line Buffer](../algorithms/line-buffer.md)
- [FPGA Video Processing](../github/selected-projects/georgeyhere-video.md)
- [Galapple Sobel](../github/selected-projects/galapple-sobel.md)

## 输出

Line Buffer、Sobel、模式选择和延迟说明。

## 前置知识

完成 Goal 3 的像素流处理，掌握 BRAM、移位寄存器、3×3 窗口和同步信号延迟。

## 通过标准

仿真结果可解释，TD 时序通过，上板实时显示边缘结果。
