# Codex 资料库使用规范

## 开始任务时

```text
请先读取 docs/research/INDEX.md、docs/research/sources.yaml 和当前 Goal 的阅读清单。
只读取当前 Goal 需要的资料卡。
```

## 开发任务提示词模板

```text
当前 Goal：Goal N

请先读取：
- docs/research/INDEX.md
- docs/research/goal-reading/goal-N.md
- 该清单引用的资料卡
- 当前工程中与任务相关的源码和约束

请区分：
1. 安路官方或比赛资料明确说明的事实；
2. 当前工程已经验证的事实；
3. 来自其他 FPGA 工程的参考做法；
4. 仍需硬件验证的推断。

禁止直接复制其他平台的 MIPI PHY、PLL、DDR、HDMI 和管脚约束。
输出中必须写明修改文件、验证方式、已知风险和未关闭的资料缺口。
```

## 资料库审计提示词

```text
请审计 docs/research 资料库：
1. 检查 INDEX.md 中的入口是否存在；
2. 检查 sources.yaml 的来源是否有重复或缺少平台标记；
3. 检查 Goal 1～8 是否都有核心资料；
4. 检查非 PH1P35 工程是否标记为参考用途；
5. 检查 SC500CS、PH1P35、TD、MIPI、DDR、HDMI 的缺口；
6. 输出下一步最应该补齐的资料。
```
