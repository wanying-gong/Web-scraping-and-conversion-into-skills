# ADS2026 Python API Markdown 知识库索引

本目录来自 `D:\Program Files\Keysight\ADS2026_Update2.1\doc\python`，输出到 `D:\MarkitdownFull\output_ADS2026`。

## 模块入口

| 模块 | 适用场景 | 入口 |
|------|----------|------|
| AEL | AEL Python API / 自动化表达式与脚本接口 | [AEL/skills/00_README.md](AEL/skills/00_README.md) |
| ANN | Artificial Neural Network / 神经网络建模 API | [ANN/skills/00_README.md](ANN/skills/00_README.md) |
| Dataset | Dataset 读写、数据结构和测量数据处理 | [Dataset/skills/00_README.md](Dataset/skills/00_README.md) |
| DDS | Data Display / 图表、数据展示与后处理脚本接口 | [DDS/skills/00_README.md](DDS/skills/00_README.md) |
| DesignEnvironment | ADS Design Environment / workspace、design、layout、schematic、technology、substrate 等 API | [DesignEnvironment/skills/00_README.md](DesignEnvironment/skills/00_README.md) |
| DesignCloud | Design Cloud / 云端仿真、RFPro Design Cloud 工作流 | [DesignCloud/skills/00_README.md](DesignCloud/skills/00_README.md) |
| EDAToolbox | EDA Toolbox / EDA 工具链辅助 API | [EDAToolbox/skills/00_README.md](EDAToolbox/skills/00_README.md) |
| EMTools | EM Tools / EM、RFPro、PEPro 相关 Python 接口 | [EMTools/skills/00_README.md](EMTools/skills/00_README.md) |
| HSD | High Speed Digital / pyhsd 高速数字相关 API | [HSD/skills/00_README.md](HSD/skills/00_README.md) |
| PWDataTools | PathWave Data Tools / 数据工具、文件和数据处理 API | [PWDataTools/skills/00_README.md](PWDataTools/skills/00_README.md) |
| Quantum | Quantum Python API / 量子相关 Python 接口 | [Quantum/skills/00_README.md](Quantum/skills/00_README.md) |

## 路由规则

- 先用本索引判断任务属于哪个模块。
- 进入模块后先读 `skills/00_README.md`，再按主题读取 `skills/*.md`。
- 需要完整 API 签名、类说明或示例时，再读模块内镜像生成的单页 Markdown。
- `combined_knowledge_base.md` 只用于模块内全局搜索，不要默认整篇加载。
- 截图里的 `SI/PI/RF/PE/QPro` 在 `doc/python` 下未发现独立目录；相关任务优先查 `DesignEnvironment`、`EMTools`、`DesignCloud`。
