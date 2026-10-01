# 灰度和二值化

- 关联 Goal：3
- 类型：算法基础

## 灰度

常用近似：

```text
gray = (77*R + 150*G + 29*B) >> 8
```

硬件实现可以使用常数乘法、移位和加法，并通过流水线保证每周期处理一个像素。

## 二值化

```text
gray > threshold  →  255
gray <= threshold →  0
```

## FPGA 接口要求

算法模块必须同步传递像素和视频控制信号，并明确算法产生的 pipeline latency。
