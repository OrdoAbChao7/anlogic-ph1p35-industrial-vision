# SC520CS 当前目标资料卡

- `project`：用户确认已购 SC520 摄像头；本机 `SC520CS摄像头资料/` 有 Lab1 原图、Lab2 边缘、Lab3 OSD 工程及 SC520CS-03 数据手册、应用指南。
- `official`：比赛 PDF `docs/research/snapshots/competition/topic2.pdf` 第 16 页要求 MIPI 摄像头；平台章节第 7 页列 SC500CS。SC520CS 是本项目根据实物选择的目标型号，不是将 PDF 的 SC500CS 改写成 SC520CS。
- `project`：Lab1 的 `user_source/hdl_source/design_top_wrapper.v` 实例化 `uicfgcs520`；`uics520_cfg/uicfgcs520.v` 实例化 `uics520reg_720p60`。`.al` 中仍包含 SC500 文件引用，但顶层传感器配置走 SC520 模块，不能仅凭文件列表判定型号。
- `project`：`代码改动说明.txt` 称 Lab1/2/3 使用 1280×720@60fps HD 配置，并保留 Lab1 的 2560×1920@30fps 寄存器表。这是资料包和代码中的配置声明，尚无板级实测。

当前工作副本是 `.tools/td/work/lab_ex1_mipi_hdmi_sc520/`，原件保存在 Git 忽略的 `SC520CS摄像头资料/`。工程软件构建记录见 [`../../setup/tangdynasty.md`](../../setup/tangdynasty.md)。

仍待核对实物型号与模组修订、FPC 引脚和供电、传感器 ID/I2C 回应、MIPI 锁定、真实 RAW/Bayer 格式、输出分辨率和帧率。软件构建不能证明这些硬件条件。
