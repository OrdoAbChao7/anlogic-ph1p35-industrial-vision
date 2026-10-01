# hdl-util/hdmi

- URL：https://github.com/hdl-util/hdmi
- 语言：SystemVerilog
- 关联 Goal：1、2、6
- 适配等级：C

## 项目内容

提供 HDMI 1.4b 视频/音频输出、视频模式参数和 VGA 兼容文字模式。README 列出了 1280×720@60Hz 使用 74.25 MHz 像素时钟。

## 可借鉴

- 视频输出时序参数。
- RGB 到 TMDS 的概念。
- 字符 ROM 和文字叠加方式。

## 不可直接移植

该项目的平台支持不包含 PH1P35。比赛工程应使用安路官方 HDMI 输出方案。
