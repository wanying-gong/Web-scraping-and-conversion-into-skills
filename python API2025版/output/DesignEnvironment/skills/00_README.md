# ADS Python API 知识库 — 使用指南

> 本知识库来自 **Keysight ADS 2025 Update 2** Python API 官方文档，
> 经 MarkItDown 转换并按主题分类整理，专为 AI Agent 按需加载设计。

---

## Agent 使用顺序

1. 先确认任务属于本模块。
2. 先读本 README 的主题表。
3. 只加载和任务相关的 skills/*.md 文件。
4. 如果需要更细的函数签名、类说明或完整示例，再读原始单页 Markdown。
5. combined_knowledge_base.md 只用于模块级全局搜索，不要默认整篇加载。

## 读取优先级

- 快速定位：读本文件。
- 编写代码：读相关主题文件和示例主题。
- 查 API 细节：读 Reference/API 主题或对应单页 Markdown。
- 跨主题理解：读 combined_knowledge_base.md。

---

## 这个仓库包含什么

| 文件 | 内容 | 大小 |
|------|------|------|
| `01_introduction_and_concepts.md` | Introduction, Concepts & How-To | ~36 KB |
| `02_api_core_objects.md` | Core API: keysight.ads.de | ~63 KB |
| `03_api_app_ui.md` | App/UI API: keysight.ads.de.app | ~27 KB |
| `04a_api_db_core.md` | Database Core API: keysight.ads.de.db / db_dbu | ~133 KB |
| `04b_api_db_uu_elements.md` | Database UU API: keysight.ads.de.db_uu (Design Elements) | ~155 KB |
| `05_api_tech.md` | Tech API: keysight.ads.de.tech | ~100 KB |
| `06_api_experimental.md` | Experimental API: keysight.ads.de.experimental | ~98 KB |
| `07_examples_design.md` | Design Examples (pypde) | ~153 KB |
| `08_api_substrate.md` | Substrate API: keysight.ads.subst (pysubst) | ~65 KB |

---

## 如何使用（按需加载策略）

根据你的任务选择对应文件读取，**不要一次性加载所有文件**。

| 我想做什么 | 应该读取哪个文件 |
|-----------|----------------|
| 当你需要了解 ADS Python 基础、概念术语、或配置开发环境时 | `01_introduction_and_concepts.md` |
| 当你需要操作工作区、库、单元格、视图等核心设计对象时 | `02_api_core_objects.md` |
| 当你需要创建自定义菜单、窗口、插件、或响应 UI 事件时 | `03_api_app_ui.md` |
| 当你需要读写设计数据库元素、处理参数/属性/枚举/几何图形时 | `04a_api_db_core.md` |
| 当你需要在 UU 坐标系下直接操作布局元素（矩形、多边形、走线、Pin 等）时 | `04b_api_db_uu_elements.md` |
| 当你需要读取或修改工艺/技术文件、焊盘/过孔定义时 | `05_api_tech.md` |
| 当你需要使用高级/实验性功能，如符号生成、多边形操作、CDF 访问时 | `06_api_experimental.md` |
| 当你需要参考完整的可运行示例代码时 | `07_examples_design.md` |
| 当你需要创建或操作基板（Substrate）设计时 | `08_api_substrate.md` |

---

## 示例位置说明

DesignEnvironment 的示例不在顶层 `examples/` 目录，而是保留官方文档结构：

- `pypde/docs/examples/`：Design Environment 主 API 示例。
- `pysubst/docs/examples/`：Substrate API 示例。

查示例时优先读 [EXAMPLES_INDEX.md](../EXAMPLES_INDEX.md)，再按任务打开对应单页 Markdown。需要完整示例合集时读 `07_examples_design.md`；需要 Substrate 示例时读 `08_api_substrate.md`。

---

## 模块概览

```
keysight.ads
├── de                    → 02_api_core_objects.md
│   ├── .app              → 03_api_app_ui.md
│   ├── .db / .db_dbu     → 04a_api_db_core.md
│   ├── .db_uu            → 04b_api_db_uu_elements.md
│   ├── .tech             → 05_api_tech.md
│   └── .experimental     → 06_api_experimental.md
└── subst                 → 08_api_substrate.md

概念/入门/How-To           → 01_introduction_and_concepts.md
示例代码（23个）           → 07_examples_design.md
```

---

## 原始文件索引

原始转换文件保存在 `D:\MarkitdownFull\output\DesignEnvironment` 目录下（按原 HTML 目录结构镜像），可用于查阅具体细节。本 `skills/` 目录下的文件是按主题合并的精简版本。
