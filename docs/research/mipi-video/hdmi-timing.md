# HDMI 视频时序资料卡

- 关联 Goal：1、2、6、8
- 类型：通用视频接口原理
- 推荐模式：1280×720@60Hz

## 参考资料

- [Project F Video Timings](https://projectf.io/posts/video-timings-vga-720p-1080p/)
- [hdl-util/hdmi](https://github.com/hdl-util/hdmi)
- [SimpleVOut](https://github.com/cliffordwolf/SimpleVOut)

## 需要理解

- pixel clock
- horizontal active/blanking/sync
- vertical active/blanking/sync
- DE、HSYNC、VSYNC
- RGB 像素与 TMDS/HDMI 输出的关系

## 项目边界

当前项目优先使用安路官方 HDMI 输出模块。开源 HDMI 工程只作为时序和 OSD 参考。
