# 目标统计和尺寸判断

- 关联 Goal：5、6
- 类型：应用算法

## 第一版硬件方案

从二值图像中逐像素统计：

```text
foreground_count += foreground
xmin = min(xmin, x)
xmax = max(xmax, x)
ymin = min(ymin, y)
ymax = max(ymax, y)
```

帧结束时计算：

```text
width  = xmax - xmin
height = ymax - ymin
area   = foreground_count
```

## 判定

```text
width、height、area 在允许范围内 → PASS
否则                         → DEFECT
```

## 后续扩展

- 多目标分离。
- 连通域标记。
- 质心计算。
- 缺陷区域数量和面积统计。

第一版不引入复杂目标检测网络，优先保证规则检测可解释、可验证和可实时运行。
