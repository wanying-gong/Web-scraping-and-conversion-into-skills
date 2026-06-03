# ADS2026 Python API Agent Guide

本指南用于让 Agent 快速定位 ADS2026 Python API Markdown 知识库。不要默认加载所有 Markdown；按任务路由到具体模块和主题文件。

## 推荐读取顺序

1. 先读 [00_API_INDEX.md](00_API_INDEX.md) 判断模块。
2. 再读目标模块的 `skills/00_README.md`。
3. 只加载相关主题文件，例如 `skills/03_examples.md` 或 `skills/06_reference.md`。
4. 需要细节时读取模块内对应单页 Markdown。
5. 只有需要模块级全文搜索时才使用 `combined_knowledge_base.md`。

## 模块路由

| 任务关键词 | 优先模块 | 说明 |
|----------|----------|------|
| AEL, expression, legacy automation | [AEL](AEL/skills/00_README.md) | AEL Python API 与脚本自动化。 |
| ANN, neural network, model training | [ANN](ANN/skills/00_README.md) | 神经网络建模和 ANN 相关 API。 |
| dataset, ds, data access, measurement data | [Dataset](Dataset/skills/00_README.md) | 数据集读写、数据访问和测量结果处理。 |
| data display, plot, graph, marker | [DDS](DDS/skills/00_README.md) | Data Display 图表、页面、trace、marker 和后处理。 |
| workspace, design, schematic, layout, technology, substrate | [DesignEnvironment](DesignEnvironment/skills/00_README.md) | ADS DE 主 API，包含 pypde 与 pysubst 文档。 |
| cloud simulation, RFPro Design Cloud | [DesignCloud](DesignCloud/skills/00_README.md) | Design Cloud 与云端工作流。 |
| EDA toolbox | [EDAToolbox](EDAToolbox/skills/00_README.md) | EDA Toolbox 辅助接口。 |
| EM, RFPro, PEPro, EM setup | [EMTools](EMTools/skills/00_README.md) | EM Tools / RFPro / PEPro 相关 API。 |
| HSD, pyhsd, high speed digital | [HSD](HSD/skills/00_README.md) | High Speed Digital Python API。 |
| PathWave Data Tools, pwdatatools | [PWDataTools](PWDataTools/skills/00_README.md) | PathWave 数据工具接口。 |
| quantum | [Quantum](Quantum/skills/00_README.md) | Quantum Python API。 |

## SI/PI/RF/PE/QPro 说明

在 `D:\Program Files\Keysight\ADS2026_Update2.1\doc\python` 下没有发现独立的 `SI/PI/RF/PE/QPro` Python 文档目录。遇到这类任务时按下面顺序查：

1. [DesignEnvironment](DesignEnvironment/skills/00_README.md)：workspace、design、layout、technology、substrate、UI 和通用 DE API。
2. [EMTools](EMTools/skills/00_README.md)：EM、RFPro、PEPro、EM setup 相关接口。
3. [DesignCloud](DesignCloud/skills/00_README.md)：RFPro on Design Cloud 或云端仿真流程。

## DesignEnvironment 示例位置

DesignEnvironment 的示例不在顶层 `examples/`。应先读 [DesignEnvironment/EXAMPLES_INDEX.md](DesignEnvironment/EXAMPLES_INDEX.md)。主 API 示例在 `pypde/docs/examples/`，Substrate 示例在 `pysubst/docs/examples/`。
