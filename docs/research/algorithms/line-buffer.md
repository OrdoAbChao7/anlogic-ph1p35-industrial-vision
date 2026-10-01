# Line Buffer 和 3×3 Sliding Window

- 关联 Goal：4
- 类型：FPGA 图像处理结构

## 基本结构

对于 3×3 卷积，不需要保存整帧，只需保存相邻图像行，并使用移位寄存器构造窗口：

```text
p00 p01 p02
p10 p11 p12
p20 p21 p22
```

## 需要处理

- 每行缓存的深度等于图像有效宽度。
- 前两行未填满时输出无效。
- 每行开头和结尾的边界像素需要明确策略。
- 输出像素相对于输入像素存在固定延迟。
- `valid`、`x/y` 或 `DE` 必须和延迟后的结果对齐。

## 参考工程

- [georgeyhere/fpga-video-processing](https://github.com/georgeyhere/fpga-video-processing)
- [Galapple/Image-processing---Verilog](https://github.com/Galapple/Image-processing---Verilog)
- [FPGA lover Three-Line Buffer](https://www.fpgalover.com/index.php/boards/40-de2-115/100-three-line-buffers-for-image-processing-de2-115)
