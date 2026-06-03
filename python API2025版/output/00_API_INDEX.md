# ADS 2025 Update 2 Python API Markdown Knowledge Bases

本目录按 API 模块整理 Keysight ADS 2025 Update 2 的 Python HTML 文档转换结果。页面数量按入口 index.html 通过内部超链接 BFS 可达的 HTML 页面统计。

Agent 使用入口：

1. 先读 [AGENT_GUIDE.md](AGENT_GUIDE.md)。
2. 再根据下方关键词选择模块。
3. 进入模块后优先读该模块的 `skills/00_README.md`。
4. 不要默认加载所有 `combined_knowledge_base.md`。

## 模块关键词路由

| 任务关键词 | 优先读取 |
|---|---|
| AEL、AEL/Python 互操作、AEL 类型转换、调用 AEL 函数 | [AEL/skills/00_README.md](AEL/skills/00_README.md) |
| workspace、library、cell、view、schematic、layout、db、technology、substrate | [DesignEnvironment/skills/00_README.md](DesignEnvironment/skills/00_README.md) |
| ANN、神经网络建模、ANN setup、training、modeler optimizer | [ANN/skills/00_README.md](ANN/skills/00_README.md) |
| dataset、ADS dataset、数据集依赖、dataset API | [Dataset/skills/00_README.md](Dataset/skills/00_README.md) |
| DDS、数据显示、plot、marker、page、window、custom menu、add-on | [DDS/skills/00_README.md](DDS/skills/00_README.md) |
| Design Cloud、远程仿真、job、queue、submit simulation | [DesignCloud/skills/00_README.md](DesignCloud/skills/00_README.md) |
| EDA toolbox、circuit、ADS automation、multi-python、xxpro | [EDAToolbox/skills/00_README.md](EDAToolbox/skills/00_README.md) |
| EM、RFPro、EM setup、substrate info、EM tools | [EM/skills/00_README.md](EM/skills/00_README.md) |
| PathWave Data Tools、pwdatatools、block、group、var、file IO、load-pull data | [PWDataTools/skills/00_README.md](PWDataTools/skills/00_README.md) |

## 模块清单

| 模块 | 入口可达 HTML | 单页 Markdown | 合并知识库 | 入口导航 |
|---|---:|---:|---|---|
| AEL | 13 | 13 | [AEL/combined_knowledge_base.md](AEL/combined_knowledge_base.md) | [AEL/skills/00_README.md](AEL/skills/00_README.md) |
| DesignEnvironment | 94 | 94 | [DesignEnvironment/combined_knowledge_base.md](DesignEnvironment/combined_knowledge_base.md) | [DesignEnvironment/skills/00_README.md](DesignEnvironment/skills/00_README.md) |
| ANN | 23 | 23 | [ANN/combined_knowledge_base.md](ANN/combined_knowledge_base.md) | [ANN/skills/00_README.md](ANN/skills/00_README.md) |
| Dataset | 5 | 5 | [Dataset/combined_knowledge_base.md](Dataset/combined_knowledge_base.md) | [Dataset/skills/00_README.md](Dataset/skills/00_README.md) |
| DDS | 68 | 68 | [DDS/combined_knowledge_base.md](DDS/combined_knowledge_base.md) | [DDS/skills/00_README.md](DDS/skills/00_README.md) |
| DesignCloud | 28 | 28 | [DesignCloud/combined_knowledge_base.md](DesignCloud/combined_knowledge_base.md) | [DesignCloud/skills/00_README.md](DesignCloud/skills/00_README.md) |
| EDAToolbox | 34 | 34 | [EDAToolbox/combined_knowledge_base.md](EDAToolbox/combined_knowledge_base.md) | [EDAToolbox/skills/00_README.md](EDAToolbox/skills/00_README.md) |
| EM | 8 | 8 | [EM/combined_knowledge_base.md](EM/combined_knowledge_base.md) | [EM/skills/00_README.md](EM/skills/00_README.md) |
| PWDataTools | 424 | 424 | [PWDataTools/combined_knowledge_base.md](PWDataTools/combined_knowledge_base.md) | [PWDataTools/skills/00_README.md](PWDataTools/skills/00_README.md) |
