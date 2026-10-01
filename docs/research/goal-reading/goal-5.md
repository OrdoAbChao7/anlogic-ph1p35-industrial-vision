# Goal 5：目标统计

## 目标

从二值图像中得到目标位置、面积、宽度和高度。

## 必读资料

- [目标统计和尺寸判断](../algorithms/object-statistics.md)
- [灰度和二值化](../algorithms/grayscale-threshold.md)
- [比赛要求](../competition/topic2-requirements.md)
- [FPGA Video Processing 参考工程](../github/selected-projects/georgeyhere-video.md)

## 输出

目标统计模块、帧结束更新逻辑、BBox 和测量结果。

## 前置知识

完成 Goal 3 的二值图像输出，理解像素坐标、帧边界和帧内累加器。

## 通过标准

使用固定测试物体时，宽度、高度、面积和位置稳定输出。
