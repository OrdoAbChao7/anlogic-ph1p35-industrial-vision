# RAW10 和 Bayer 资料卡

- 关联 Goal：1、2、3
- 类型：通用视频原理
- 状态：reference

## 要理解的内容

- RAW10 一个像素的有效位数。
- CSI-2 payload 的打包方式。
- Bayer 四种排列：RGGB、GRBG、GBRG、BGGR。
- 偶数行、奇数行和偶数列、奇数列对应的颜色。
- Demosaic 输入输出像素格式。

## 参考资料

- [MIPI CSI-2 for Multi-Camera](https://www.mipi.org/hubfs/Bangalore-Xilinx-MIPI-CSI-2-for-Multi-Camera-1.pdf)
- [Linux IPU3 RAW Bayer 文档](https://docs.kernel.org/admin-guide/media/ipu3.html)
- [Linux Qualcomm Camera 文档](https://docs.kernel.org/admin-guide/media/qcom_camss.html)

## 与本项目的关系

这些资料用于检查像素位宽、打包和 Bayer 方向是否理解正确。实际解包和 PHY 接收优先使用安路官方 IP。
