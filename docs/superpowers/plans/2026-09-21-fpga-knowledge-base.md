# FPGA 题目二资料库建设实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** 为安路 PH1P35 题目二建立一个可检索、可追溯、按 Goal 1～8 使用的项目资料库。

**Architecture:** 资料库分为官方资料、比赛资料、通用教程、GitHub 参考工程和项目内部实验记录五层。所有资料通过统一索引进入库，每份资料都有来源、版本、用途、关联 Goal、可信度和复核状态；Codex 只把经过索引的资料作为项目参考。

**Tech Stack:** Markdown、YAML、PDF、GitHub 仓库、PowerShell、Codex workspace 文件检索。

**Spec:** [赛题二原始 PDF](../../research/snapshots/competition/topic2.pdf) 和本对话已经确认的 Goal 1～8 项目路线。

## Global Constraints

- 当前项目平台固定为安路 PH1P35，摄像头固定为 SC500CS，主视频链路为 MIPI 输入和 HDMI 输出。
- 安路官方资料优先于第三方教程和 GitHub 工程。
- 其他 FPGA 平台的 MIPI PHY、PLL、DDR、HDMI 和管脚约束默认只能参考，未经验证不得直接移植。
- 每条资料必须记录原始 URL 或本地文件路径、访问或下载日期、资料类型和关联 Goal。
- 资料库建设阶段不修改 RTL、不改变 FPGA 工程配置、不批量克隆未经筛选的仓库。
- 原始资料和整理后的摘要分开保存，摘要不得替代原始来源。

## Review Focus

- 安路资料与其他 FPGA 资料混用：验证索引是否标明平台和可复用边界。
- SC500CS 资料缺失或版本不确定：验证资料卡是否标记未知项和待补来源。
- 网页内容变化：验证每条网页资料是否有访问日期和来源 URL。
- GitHub 工程许可证和适配限制：验证每个参考仓库是否记录许可证、目标 FPGA 和是否建议移植。
- Codex 阅读范围过大：验证入口索引能否把当前 Goal 限定到必要资料。

### Task 1: 建立资料库目录和入口规范

**Files:**
- Create: `docs/research/INDEX.md`
- Create: `docs/research/sources.yaml`
- Create: `docs/research/README.md`
- Create: `docs/research/templates/source-card.md`
- Create: `docs/research/templates/github-card.md`
- Create: `docs/research/templates/goal-reading-list.md`

**Interfaces:**
- `INDEX.md` 是 Codex 进入资料库的唯一入口。
- `sources.yaml` 是来源清单的机器可读版本。
- `source-card.md` 定义网页、PDF 和教程资料卡字段。
- `github-card.md` 定义 GitHub 项目资料卡字段。
- `goal-reading-list.md` 定义每个 Goal 的推荐阅读清单格式。

- [x] **Step 1: 创建资料库目录**

  建立以下目录：

  ```text
  docs/research/
  docs/research/anlogic/
  docs/research/competition/
  docs/research/camera/
  docs/research/mipi-video/
  docs/research/algorithms/
  docs/research/github/
  docs/research/experiments/
  docs/research/templates/
  docs/research/snapshots/
  ```

- [x] **Step 2: 写入口文件**

  `INDEX.md` 必须包含：项目目标、资料分层、Goal 1～8 入口、资料可信度定义、Codex 使用规则。

- [x] **Step 3: 写来源登记格式**

  `sources.yaml` 每条记录至少包含：

  ```yaml
  id: unique_id
  title: source title
  url_or_path: source location
  type: official|competition|tutorial|github|experiment
  platform: PH1P35|generic|xilinx|lattice|gatemate|unknown
  related_goals: [1, 2]
  priority: high|medium|low
  status: discovered|captured|reviewed|verified|rejected
  accessed_at: YYYY-MM-DD
  notes: short note
  ```

- [x] **Step 4: 写资料卡模板**

  资料卡必须要求填写：资料解决的问题、关键章节、对当前项目的关联、能否直接复用、适配风险和下一步动作。

- [x] **Step 5: 做结构检查**

  检查所有入口链接都指向存在的目录或文件；检查 YAML 可以被正常解析；检查模板没有空的关键字段。

### Task 2: 收录比赛和安路官方资料

**Files:**
- Create: `docs/research/competition/topic2-requirements.md`
- Create: `docs/research/anlogic/official-index.md`
- Create: `docs/research/anlogic/ph1p35.md`
- Create: `docs/research/anlogic/td-tool.md`
- Create: `docs/research/anlogic/ip-reference.md`
- Create: `docs/research/snapshots/README.md`
- Copy or reference: `docs/research/snapshots/competition/topic2.pdf`

**Interfaces:**
- `topic2-requirements.md` 提供赛题约束、评分点和硬件清单。
- `official-index.md` 提供安路官方网页、IP 手册和参考设计入口。
- `ph1p35.md` 只记录 PH1P35 相关事实，不从 PH1A 资料推断 PH1P35 的具体资源。

- [x] **Step 1: 登记比赛 PDF**

  将附件登记为 `competition_topic2_pdf`，记录本地路径和页面范围；保留原始 PDF，不把 PDF 内容改写后替代原文件。

- [x] **Step 2: 整理题目二需求**

  明确记录：SC500CS、MIPI 输入、HDMI 输出、图像算法、OSD、推荐分辨率、稳定运行和扩展方向。

- [x] **Step 3: 收录安路官方入口**

  收录安路 IP/参考设计页、开发板教程页、摄像头采集方案页、工具下载页，并为每个入口建立资料卡。

- [x] **Step 4: 标记官方资料的适用范围**

  对 PH1A 摄像头方案只标记为“架构参考”；对明确支持 PH1P 的 IP 手册标记为“平台优先资料”；对无法确认适用器件的资料标记为 `unknown`。

- [x] **Step 5: 做官方资料覆盖检查**

  输出一张表，检查以下主题是否都有来源：TD、PH1P、MIPI D-PHY/CSI-2、DDR、HDMI/视频输出、MCU、SC500CS 配置。

### Task 3: 收录摄像头和视频链路资料

**Files:**
- Create: `docs/research/camera/sc500cs.md`
- Create: `docs/research/camera/raw10-bayer.md`
- Create: `docs/research/mipi-video/mipi-csi2.md`
- Create: `docs/research/mipi-video/hdmi-timing.md`
- Create: `docs/research/mipi-video/ddr-framebuffer.md`

**Interfaces:**
- 这些资料只解释数据格式、时序和模块职责，不替代安路底层 IP。
- `sc500cs.md` 必须把“已确认参数”和“尚未确认参数”分开。

- [x] **Step 1: 整理 SC500CS 资料**

  收录传感器数据手册、模组说明、初始化代码和官方例程中的寄存器表；如果缺少公开资料，记录缺口，不用其他型号传感器资料代替。

- [x] **Step 2: 整理 RAW10/Bayer**

  记录 RAW10 打包方式、Bayer 四种排列、颜色插值的输入输出和像素位宽。

- [x] **Step 3: 整理 MIPI CSI-2**

  只保留理解题目二所需的内容：Lane、D-PHY、CSI-2 packet、RAW10 payload、frame/line boundary 和有效像素。

- [x] **Step 4: 整理 HDMI 和 DDR**

  记录 1280×720@60Hz 视频时序、pixel clock、DE/HS/VS、帧缓存用途、写入和读取的时钟域关系。

- [x] **Step 5: 做链路一致性检查**

  用一张数据流图核对：摄像头输出格式、MIPI 接收输出、ISP 输入、DDR 像素格式和 HDMI 输入格式是否前后一致。

### Task 4: 收录算法教程和参考工程

**Files:**
- Create: `docs/research/algorithms/grayscale-threshold.md`
- Create: `docs/research/algorithms/sobel.md`
- Create: `docs/research/algorithms/line-buffer.md`
- Create: `docs/research/algorithms/object-statistics.md`
- Create: `docs/research/github/repositories.md`
- Create: `docs/research/github/selected-projects/*.md`

**Interfaces:**
- 算法资料必须同时说明软件参考模型和 FPGA 实现方式。
- GitHub 资料卡必须记录仓库目标平台、语言、许可证、活跃状态、可借鉴模块和不可直接移植部分。

- [x] **Step 1: 收录基础算法**

  覆盖灰度、二值化、Gaussian/Median 可选滤波、Sobel、形态学、ROI、Bounding Box、面积和质心。

- [x] **Step 2: 收录 Line Buffer 资料**

  解释 3×3 窗口、行缓存、移位寄存器、边界像素、流水线延迟和 valid 信号同步。

- [x] **Step 3: 收录 GitHub MIPI/HDMI 工程**

  首批登记：`FHDO-ICLAB/MIPI-CSI-2-HDMI-Bridge`、`circuitvalley/mipi_csi_receiver_FPGA`、`hdl-util/mipi-demo`、`gatecat/CSI2Rx`。

- [x] **Step 4: 收录 GitHub 图像工程**

  首批登记：`georgeyhere/fpga-video-processing`、`Galapple/Image-processing---Verilog`、`ykqiu/image-processing`、`olivier-le-sage/camera-filters`。

- [x] **Step 5: 给每个仓库做适配评估**

  使用以下等级：

  ```text
  A：算法或验证代码可直接参考
  B：模块结构可参考，需要改接口
  C：只适合协议和架构学习
  D：与本项目关系较弱
  ```

- [x] **Step 6: 做许可证记录**

  记录仓库许可证和源码使用边界；没有明确许可证的仓库标记为“只读学习参考”。

### Task 5: 建立 Goal 1～8 阅读路线

**Files:**
- Create: `docs/research/goal-reading/goal-1.md`
- Create: `docs/research/goal-reading/goal-2.md`
- Create: `docs/research/goal-reading/goal-3.md`
- Create: `docs/research/goal-reading/goal-4.md`
- Create: `docs/research/goal-reading/goal-5.md`
- Create: `docs/research/goal-reading/goal-6.md`
- Create: `docs/research/goal-reading/goal-7.md`
- Create: `docs/research/goal-reading/goal-8.md`

**Interfaces:**
- 每个 Goal 文件只列当前阶段需要阅读的资料，不把整个资料库一次性注入 Codex。
- 每个 Goal 文件包含：目标、必读资料、选读资料、前置知识、输出物和通过标准。

- [x] **Step 1: 建立 Goal 1～2 清单**

  Goal 1 聚焦官方工程、Camera、MIPI、HDMI、下载和硬件验证；Goal 2 聚焦 Verilog、时钟、复位、FIFO、像素流和工程结构。

- [x] **Step 2: 建立 Goal 3～4 清单**

  Goal 3 聚焦 RGB/Gray/Binary；Goal 4 聚焦 Line Buffer、3×3 Window、Sobel、滤波和流水线。

- [x] **Step 3: 建立 Goal 5～6 清单**

  Goal 5 聚焦目标统计；Goal 6 聚焦工业检测应用、OSD 和 PASS/DEFECT。

- [x] **Step 4: 建立 Goal 7～8 清单**

  Goal 7 聚焦资源、时序、MCU 协同和自适应算法；Goal 8 聚焦稳定性、性能数据、发布工程和答辩。

- [x] **Step 5: 设定阅读门槛**

  每个 Goal 至少要有：一份官方或比赛资料、一份原理教程、一份可运行或可检查的参考工程，才允许进入下一阶段开发。

### Task 6: 建立资料库质量验证流程

**Files:**
- Create: `docs/research/quality-check.md`
- Create: `docs/research/CHANGELOG.md`
- Create: `docs/research/known-gaps.md`

**Interfaces:**
- `quality-check.md` 定义每次资料入库的检查项。
- `known-gaps.md` 记录目前无法确认的事实，避免 Codex 把猜测当结论。
- `CHANGELOG.md` 记录资料新增、替换、失效和复核。

- [x] **Step 1: 定义入库检查**

  每份资料检查：来源可访问、标题准确、来源类型准确、平台已标注、关联 Goal 已标注、关键结论有定位、适配风险已写明。

- [x] **Step 2: 定义冲突处理**

  冲突时按以下顺序判断：当前 PH1P35 工程和官方资料、比赛 PDF、安路其他系列资料、通用教程、GitHub 参考工程。

- [x] **Step 3: 建立缺口清单**

  初始重点缺口：SC500CS 完整初始化表、PH1P35 对应官方 Camera Demo、PH1P35 HDMI/DDR 具体例程、比赛提供工程的位置和版本。

- [x] **Step 4: 做一次资料库审计**

  审计输出必须回答：哪些内容已确认、哪些内容只有架构参考、哪些内容还不能开始实现、当前 Goal 最应该读哪几份资料。

### Task 7: 设置 Codex 使用规则

**Files:**
- Create or modify: `AGENTS.md` only if the project has no existing project-level instruction file
- Create: `docs/research/codex-usage.md`

**Interfaces:**
- Codex 开始题目二相关任务时先读 `docs/research/INDEX.md`。
- Codex 根据当前 Goal 读取对应 `goal-reading/goal-N.md`，再读取被引用的资料卡。

- [x] **Step 1: 写 Codex 资料读取规则**

  规定资料优先级、平台适配边界、事实与推断的区分、缺口处理方式。

- [x] **Step 2: 写任务提示词模板**

  模板必须包含：当前 Goal、要读取的资料、允许使用的参考工程、禁止直接移植的模块、输出验证要求。

- [x] **Step 3: 写资料库审计提示词**

  提供一个固定提示词，用于检查索引、缺口、冲突和过期资料。

- [x] **Step 4: 进行最小读取测试**

  让 Codex 只读取 `INDEX.md` 和 `goal-reading/goal-1.md`，检查它是否能正确回答 Goal 1 的资料范围、资料优先级和未解决问题。

### Task 8: 资料库验收并冻结第一版

**Files:**
- Modify: `docs/research/INDEX.md`
- Modify: `docs/research/sources.yaml`
- Modify: `docs/research/known-gaps.md`
- Create: `docs/research/releases/v0.1.md`

**Interfaces:**
- `releases/v0.1.md` 是第一版资料库的快照，记录可用资料、缺口和后续维护方式。

- [x] **Step 1: 检查目录完整性**

  确认所有索引中的文件和链接都存在，确认没有资料卡脱离入口索引。

- [x] **Step 2: 检查 Goal 覆盖率**

  确认 Goal 1～8 每个阶段至少都有一份核心资料和一份参考资料。

- [x] **Step 3: 检查平台边界**

  确认所有非 PH1P35 工程都标注为参考用途，并写明不能直接移植的原因。

- [x] **Step 4: 检查关键缺口**

  确认 SC500CS、PH1P35、TD、MIPI、DDR 和 HDMI 的缺口已明确记录。

- [x] **Step 5: 生成 v0.1 验收报告**

  报告包含资料数量、官方资料数量、GitHub 工程数量、已验证条目、待补条目和推荐的下一步。

- [x] **Step 6: 交给用户审核**

  用户审核重点是：目录是否符合使用习惯、资料层级是否合理、是否允许下载/克隆、哪些资料需要加入第一版。

## 验收标准

第一版资料库必须满足：

1. Codex 从 `docs/research/INDEX.md` 能找到所有资料类别。
2. 每个 Goal 都有明确的必读资料和输出目标。
3. 每条来源都能追溯到 URL 或本地文件。
4. 官方资料、通用教程和其他 FPGA 项目有清楚的边界。
5. SC500CS 和 PH1P35 的未知信息单独列在缺口清单中。
6. Codex 能根据当前 Goal 只读取相关资料，而不是扫描整个资料库。
7. 资料库审计能发现断链、缺字段、平台混用和未经确认的推断。

## 暂不纳入第一版的内容

- 大规模下载所有搜索结果。
- 直接克隆几十个 GitHub 仓库。
- 将第三方 FPGA 工程改造成 PH1P35 工程。
- 收集与题目二没有直接关系的深度学习、Linux、PCIe 和复杂 NPU 资料。
- 在资料库验收前编写图像处理 RTL。

## 计划完成后的下一步

资料库 v0.1 通过审核后，再执行资料采集：先收录比赛 PDF 和安路官方资料，再收录 SC500CS/MIPI/HDMI 资料，最后收录精选 GitHub 工程。资料采集完成后，才开始 Goal 1 的硬件工程审计。
