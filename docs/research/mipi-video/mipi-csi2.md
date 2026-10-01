# MIPI CSI-2 资料卡

- 关联 Goal：1、2、3
- 类型：通用协议原理
- 状态：reference

## 参考资料

- [MIPI CSI-2 for Multi-Camera](https://www.mipi.org/hubfs/Bangalore-Xilinx-MIPI-CSI-2-for-Multi-Camera-1.pdf)
- [Linux IPU3 文档](https://docs.kernel.org/admin-guide/media/ipu3.html)
- [FHDO MIPI-CSI-2-HDMI-Bridge](https://github.com/FHDO-ICLAB/MIPI-CSI-2-HDMI-Bridge)
- [circuitvalley MIPI Receiver](https://github.com/circuitvalley/mipi_csi_receiver_FPGA)

## 当前只需要掌握

```text
MIPI Lane
  ↓
D-PHY
  ↓
CSI-2 Packet
  ↓
RAW10 Payload
  ↓
有效像素和行场边界
```

## 工程边界

不因为看过开源 CSI-2 工程就替换安路 D-PHY 或 CSI-2 IP。开源工程的 PHY、时钟和器件原语通常与 PH1P35 不兼容。
