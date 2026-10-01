# 来源与可用性记录

核对日期：2026-09-26。`official` 指来源发布主体的正式资料；网页列出的产品能力不等于本板卡的实际接线或工程配置。`project` 指当前工作区直接可核对的文件。

| ID | 来源及定位 | 已能确认 | 尚不能确认 |
| --- | --- | --- | --- |
| C1 | [`docs/research/snapshots/competition/topic2.pdf`](../docs/research/snapshots/competition/topic2.pdf)，35 页，SHA-256 见 `01-baseline-audit.md` | 第 1 页 2026 封面；第 6–8 页 HX1P35A 平台、SC500CS、样例及资料包入口；第 16–18 页 2026 题目二要求与显示器建议 | 原始线上下载地址与该快照的发布链。第 6–8 页的“2025”页眉为何未更新 |
| A1 | [安路 PH1P 产品页](https://www.anlogic.com/product/fpga/phoenix/ph1p)，PH1P35MDG324 选型表 | 器件型号、38,189 LUT4、42,432 DFF、40 DSP、6 PLL、2 个 MIPI D-PHY；这些是器件级标称能力 | 板卡引脚、MIPI Lane 接线、DDR/HDMI IP 配置和可用资源余量 |
| A2 | [安路 IP 和参考设计页](https://www.anlogic.com/support/ip) | 页面列有 `IPUG214 MIPI D-PHY IP`（2026-09-02，v1.0，标记“全系列器件”）及 PH1P 专项手册条目 | 手册正文、当前工程采用的 IP 版本与端口；网页提示部分资料需会员权限 |
| A3 | [安路 TangDynasty 产品页](https://www.anlogic.com/product/software/1.html) | TD 是安路 FPGA 开发工具，提供 RTL 综合、布局布线、位流生成等流程 | 本机安装路径、版本、授权与 PH1P35 工程运行结果 |
| A4 | [安路开发板教程页](https://www.anlogic.com/support/university/development-board) | 通用 TD 入门资料入口 | HX1P35A 专用原理图、手册和接线说明 |
| S1 | [SmartSens SC500CS Product Flyer V4.0](https://smartsens.oss-cn-beijing.aliyuncs.com/web/products/SC500CS_V4.0.pdf)，第 2 页 | 传感器产品支持 10/8-bit 2-Lane MIPI、RAW RGB，列有 2592×1944@30fps 10bit 的产品能力 | 本模组在 720p 模式下的 RAW 位宽、Bayer 顺序、Lane 速率、初始化寄存器与 60fps 设置。该文件是两页宣传规格，不是完整 datasheet |
| B1 | C1 第 8 页所列 [HX1P35A_Contest_202606 网盘分享](https://pan.baidu.com/s/12hjB7BiAxT3CIVqzh4Amnw?pwd=Q614)，提取码 `Q614` | 交互读取能看到 10 个根目录条目，以及 `7_lab_ex_2026_nosoft` 中三个 SC500 720P 样例 ZIP；细目见 [`06-package-manifest.md`](06-package-manifest.md) | 尚未取得任何包体、SHA-256 或工程文件内容；不能声称构建入口和 IP 配置已经核对 |
| C2 | [FPGA 创新设计赛道官网](http://www.fpgachina.cn/) | 2026 竞赛公告入口 | 未从公开页面定位到与 C1 完全同一文件的下载地址 |

## 使用边界与冲突

- C1 的 PDF 文件是真实存在的本地快照，但其最初来自本机下载目录，缺少可复查的线上来源链接。涉及赛题正文时引用页码，不把快照路径当作公开下载 URL。
- C1 第 6 页写 `38184` LUT，而 C1 第 16 页与 A1 均写 `38189`。保留冲突，待官方板卡资料或 TD 器件库核对；不据第 6 页的数值做资源承诺。
- S1 证明传感器**支持**两种位宽和 2-Lane MIPI，不证明当前模组已设为 RAW10，也不提供 Bayer 顺序或寄存器表。
