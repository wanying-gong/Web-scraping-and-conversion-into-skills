# Agent Guide for ADS 2025 Python API Knowledge Base

本目录是给 AI Agent 使用的 Keysight ADS 2025 Update 2 Python API Markdown 知识库。

## 使用顺序

1. 先读 `00_API_INDEX.md`，判断任务属于哪个 API 模块。
2. 进入对应模块目录，先读 `skills/00_README.md`。
3. 根据模块 README 的主题表，只加载相关 `skills/*.md`。
4. 如果主题文件信息不够，再读对应的单页 Markdown。
5. 只有需要跨模块全局搜索或大范围学习时，才读取 `combined_knowledge_base.md`。

不要默认一次性加载所有模块，也不要默认整篇加载 `combined_knowledge_base.md`。

## 模块选择

| 任务关键词 | 优先模块 |
|---|---|
| AEL、AEL/Python 互操作、AEL 类型转换、调用 AEL 函数 | `AEL` |
| workspace、library、cell、view、schematic、layout、db、technology、substrate | `DesignEnvironment` |
| ANN、神经网络建模、ANN setup、training、modeler optimizer | `ANN` |
| dataset、ADS dataset、数据集依赖、dataset API | `Dataset` |
| DDS、数据显示、plot、marker、page、window、custom menu、add-on | `DDS` |
| Design Cloud、远程仿真、job、queue、submit simulation | `DesignCloud` |
| EDA toolbox、circuit、ADS automation、multi-python、xxpro | `EDAToolbox` |
| EM、RFPro、EM setup、substrate info、EM tools | `EM` |
| PathWave Data Tools、pwdatatools、block、group、var、file IO、load-pull data | `PWDataTools` |

如果任务同时涉及多个模块，先读最具体模块，再补读依赖模块。例如“用 Python 创建设计并提交 Design Cloud 仿真”，先读 `DesignEnvironment`，再读 `DesignCloud`。

## 文件层级

每个模块目录通常包含：

- `combined_knowledge_base.md`：模块内所有可达页面的合并知识库。
- 单页 Markdown：按 HTML 原始目录结构镜像保存。
- `skills/00_README.md`：模块内主题导航。
- `skills/*.md`：按主题合并后的 agent 友好文件。

Agent 默认应优先使用 `skills/` 目录。

## DesignEnvironment 示例位置

`DesignEnvironment` 的示例不在顶层 `examples/` 目录。

查 DesignEnvironment 示例时，应先读 `DesignEnvironment/EXAMPLES_INDEX.md`。

- 主 API 示例在 `DesignEnvironment/pypde/docs/examples/`。
- Substrate 示例在 `DesignEnvironment/pysubst/docs/examples/`。

需要完整示例合集时，再读 `DesignEnvironment/skills/07_examples_design.md` 或 `DesignEnvironment/skills/08_api_substrate.md`。

## 历史文件说明

`DesignEnvironment` 目录里存在历史生成文件：

- `document.md`

除非用户明确要求检查历史副本，否则不要优先读取这个文件。当前标准入口是 `DesignEnvironment/combined_knowledge_base.md` 和 `DesignEnvironment/skills/00_README.md`。

## 编写代码时的使用方式

1. 先确定目标 API 模块。
2. 读模块 `skills/00_README.md` 找主题文件。
3. 读相关主题文件中的概念、类、函数、示例。
4. 如果需要完整函数签名或长示例，再跳到单页 Markdown。
5. 编写代码时优先复用官方示例中的 import、对象生命周期和错误处理方式。

不要凭函数名猜测 API。没有在知识库中确认的 API，要标明不确定或继续查证。
