# TangDynasty 6.2.1 本机环境

## 2026-10-02 验收状态

- 官方比赛资料包的版本提醒要求统一使用 **TD 6.2.1**。本机取得的 `安路开发软件TD_6.2.1版本.zip` 内为 `TD_6.2.1_Engineer_168116.exe`；ZIP 的 SHA-256 为 `E50D9BE62268A4FA7D01839DA476E35444472E30697ED88FFEAA88EC74DAFEBC`，7-Zip 完整性检查通过，安装程序的 Authenticode 签名有效，签名者为安路科技。
- 使用安装程序的 `/extract` 功能取得完整程序文件，放在仓库内被 Git 忽略的 `.tools/td/app/`。配套 `Anlogic.lic` 已按官方安装提示放入 `.tools/td/app/license/`。此方式没有执行 MSI 系统注册；本机 TD GUI 已能启动，窗口显示 `Anlogic TD 6.2.1`。
- 当前目标为 SC520CS。Lab1 原图工程工作副本在 `.tools/td/work/lab_ex1_mipi_hdmi_sc520/`，原件在 `SC520CS摄像头资料/`；副本 `.al` 的工程根路径已指向本地目录，57 个文件引用均存在。顶层 `design_top_wrapper.v` 实例化 `uicfgcs520`，后者使用 `uics520reg_720p60`；工程仍引用一些 SC500 源文件，但顶层没有使用其摄像头配置模块。
- SC520 工作副本执行 `Read Design → Optimize RTL → Optimize Gate → Optimize Placement → Optimize Routing → Generate Bitstream`，均有完成标记。`best_result/camera_to_dsi_display.bit` 大小 1,789,539 字节，SHA-256 为 `F723C738F45A5052E0E5AE8E912010891179099BDB514B397DA1123A5904E397`。`phy_1/route.qor` 报告 Setup WNS `1242 ps`、Hold WNS `20 ps`、两类 TNS 均为 `0 ps`，使用 12,390 slices、39 RAMs、8 DSPs。构建日志未发现 `ERROR` 或 `FATAL` 行。
- SC520 构建日志有 3 条 `CRITICAL-WARNING`：两条 `PHY-5060` 提示候选时钟网混用时钟与数据/控制扇出，一条 `PHY-5079` 提示时钟网使用本地布线。综合日志另有 120 行普通 WARNING，物理实现日志有 13 行 WARNING（含上述 3 条关键告警）；尚未逐项分类。构建通过不等于这些告警已被证明无害。
- 此前 SC500CS 原图样例工作副本 `.tools/td/work/lab_ex1_mipi_hdmi/` 已完成一次软件构建，Bitstream SHA-256 为 `40ED75A47B57164F01C235D956C099C94E59D39B0294893F20FCA74F9E335F2E`。它只用于验证 TD 环境，不能用于用户的 SC520 摄像头验收。

SC520 构建证据保存在本地 `.tools/td/work/lab_ex1_mipi_hdmi_sc520/td_project/camera_to_dsi_display_Runs/` 的 `syn_1/run.log`、`phy_1/run.log`、`phy_1/route.qor` 和 `best_result/`。这些厂商生成物未纳入 Git。

## 打开环境

在仓库根目录运行：

```powershell
pwsh -File .\scripts\open-td.ps1
```

脚本启动 `.tools/td/app/bin/td.exe` 并打开 SC520CS Lab1 原图工程工作副本。TD、许可文件、安装 ZIP 和工作副本都在 `.tools/td/`，由 `.gitignore` 排除；克隆 GitHub 仓库不会自动得到它们。

## 尚待上板

`.tools/td/app/driver/` 含下载器驱动文件，但尚未按到手板卡和下载器型号安装、连接或验证。Bitstream 没有下载到 FPGA，也没有实测摄像头、MIPI、HDMI、帧率和稳定性。到板后按板卡手册及 [`preboard/04-bringup-and-demo.md`](../../preboard/04-bringup-and-demo.md) 验证，并优先分析上面的关键时钟告警。
