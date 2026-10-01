# Sobel 边缘检测

- 关联 Goal：4
- 类型：算法和 RTL 结构

## 计算

```text
Gx = -p00 + p02 - 2*p10 + 2*p12 - p20 + p22
Gy = -p00 - 2*p01 - p02 + p20 + 2*p21 + p22
edge ≈ abs(Gx) + abs(Gy)
```

通常用阈值判断边缘，避免在 FPGA 中实现平方根：

```text
abs(Gx) + abs(Gy) > threshold → edge
```

## 参考工程

- [georgeyhere/fpga-video-processing](https://github.com/georgeyhere/fpga-video-processing)
- [Galapple/Image-processing---Verilog](https://github.com/Galapple/Image-processing---Verilog)

## 实现要求

使用 Line Buffer 和 3×3 Sliding Window；必须处理图像边界，并同步输出 valid、行场信号和延迟后的像素。
