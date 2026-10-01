# Tang Dynasty 工具资料卡

- 官方入口：https://www.anlogic.com/support/university/development-board
- 用途：工程创建、综合、布局布线、时序分析、Bitstream 生成和下载
- 关联 Goal：1、2、7、8
- 状态：入口已收录，具体版本待结合本机安装环境确认

## 需要掌握的流程

```text
Create/Open Project
  ↓
Add RTL and IP
  ↓
Pin/Clock Constraints
  ↓
Synthesis
  ↓
Place and Route
  ↓
Timing Report
  ↓
Bitstream
  ↓
JTAG Download
```

## 重点输出

- 综合错误和警告
- 时钟约束是否生效
- Setup/Hold Slack
- LUT、FF、RAM、DSP 和 PLL 占用
- Bitstream 生成路径

## 使用边界

TD 的具体菜单和工程文件格式可能随版本变化。后续应以本机 TD 版本和官方例程为准，不用其他 FPGA 工具的操作说明替代。
