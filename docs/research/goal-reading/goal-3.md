# Goal 3：灰度和二值化

## 目标

确认 SC500CS 的 RAW 位宽、Bayer 顺序和 Demosaic 输出后，在正确的像素接口上加入 RGB 转灰度和阈值二值化。

## 必读资料

- [SC500CS](../camera/sc500cs.md)
- [RAW10 和 Bayer](../camera/raw10-bayer.md)
- [灰度和二值化](../algorithms/grayscale-threshold.md)
- [camera-filters](../github/selected-projects/camera-filters.md)

## 输出

RTL 模块、仿真参考模型和 Original/Gray/Binary 三种模式。

## 前置知识

完成 Goal 1 的视频闭环，理解 RAW/Bayer/RGB 的格式转换，以及 valid、DE 和 pipeline latency。

## 通过标准

上板实时运行，控制信号和像素数据同步，没有明显错位。
