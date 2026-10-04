# 安路 PH1P35 实时图像处理竞赛项目

面向 2026 FPGA 创新设计竞赛安路赛道题目二，计划在 HX1P35A / PH1P35MDG324 上实现 SC520CS 摄像头采集、实时图像处理与 HDMI 显示，并完成工业零件尺寸测量与缺陷判定演示。

## 当前状态

本仓库目前保存赛题研究、来源与缺口记录，以及到板前准备包和软件参考模型。TD 6.2.1 已在本机项目目录下打开并构建 SC520CS Lab1 原图工程，生成 Bitstream。独立的时钟修复副本已完成软件构建，原有 3 条关键时钟告警在该副本中消失；仍有普通告警待分类，且没有上板验收结果。旧型号样例曾用于 TD 环境冒烟验证，不是本项目摄像头目标。原始压缩包、工程、TD 程序与生成物保存在本机，未纳入 Git。

## 入口

- [项目执行准则](AGENTS.md)
- [研究资料索引](docs/research/INDEX.md)
- [赛题要求摘录](docs/research/competition/topic2-requirements.md)
- [资料缺口](docs/research/known-gaps.md)
- [到板前准备包](preboard/README.md)
- [官方资料包文件清单](preboard/06-package-manifest.md)
- [TD 本机环境与构建记录](docs/setup/tangdynasty.md)
- [从现在到提交的详细操作手册（新手版）](docs/setup/beginner-project-guide.md)
- [SC520CS 资料与验证边界](docs/research/camera/sc520cs.md)

打开本机 SC520CS Lab1 工程：

```powershell
pwsh -File .\scripts\open-td.ps1
```

打开时钟告警修复副本：

```powershell
pwsh -File .\scripts\open-td.ps1 -ClockFix
```

运行独立于板卡的算法参考模型：

```powershell
python .\preboard\reference_model.py --self-test
```

## 官方样例与复现边界

官方资料分享入口及文件名见 `preboard/06-package-manifest.md`。本机取得的官方压缩包和解压工程尚未整理成可移植、可公开分发的工程；原始 TD 工程含生成物和本机绝对路径。因此，本仓库当前不能单独重建 Bitstream。取得来源许可和完成工程审计后，再将必要的 RTL、约束和 IP 配置作为可复现工程纳入版本控制。

项目目标、阶段门和验收证据以 `AGENTS.md` 为准；未确认的硬件参数记录在 `docs/research/known-gaps.md`。
