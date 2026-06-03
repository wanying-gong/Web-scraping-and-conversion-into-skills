# EDA Toolbox API Documentation 知识库 — 使用指南

> 本知识库来自 Keysight ADS 2026 Update 2.1 EDA Toolbox API Documentation HTML 文档，经 MarkItDown 转换并按主题自动分类整理，专为 AI Agent 按需加载设计。

---

## 这个仓库包含什么

| 文件 | 内容 | 大小 |
|------|------|------|
| `01_root.md` | Root | ~20 KB |
| `02_api_reference.md` | Api Reference | ~47 KB |
| `03_examples.md` | Examples | ~227 KB |
| `04_how-to.md` | How To | ~21 KB |
| `05_initial_setup.md` | Initial Setup | ~9 KB |
| `06_release_notes.md` | Release Notes | ~3 KB |

---

## 如何使用（按需加载策略）

根据你的任务选择对应文件读取，**不要一次性加载所有文件**。

| 我想做什么 | 应该读取哪个文件 |
|-----------|----------------|
| 当你需要查阅 Root 相关内容时 | `01_root.md` |
| 当你需要查阅 Api Reference 相关内容时 | `02_api_reference.md` |
| 当你需要查阅 Examples 相关内容时 | `03_examples.md` |
| 当你需要查阅 How To 相关内容时 | `04_how-to.md` |
| 当你需要查阅 Initial Setup 相关内容时 | `05_initial_setup.md` |
| 当你需要查阅 Release Notes 相关内容时 | `06_release_notes.md` |

---

## 模块概览

```
01_root.md -> Root
02_api_reference.md -> Api Reference
03_examples.md -> Examples
04_how-to.md -> How To
05_initial_setup.md -> Initial Setup
06_release_notes.md -> Release Notes
```

---

## 原始文件索引

原始转换文件保存在 `D:\MarkitdownFull\output_ADS2026\EDAToolbox` 目录下（按原 HTML 目录结构镜像），可用于查阅具体细节。本 `skills/` 目录下的文件是按主题合并的精简版本。

---

## Agent 使用顺序

1. 先确认任务属于本模块。
2. 先读本 README 的主题表。
3. 只加载和任务相关的 `skills/*.md` 文件。
4. 如果需要更细的函数签名、类说明或完整示例，再读原始单页 Markdown。
5. `combined_knowledge_base.md` 只用于模块级全局搜索，不要默认整篇加载。

## 读取优先级

- 快速定位：读本文件。
- 编写代码：读相关主题文件和示例主题。
- 查 API 细节：读 Reference/API 主题或对应单页 Markdown。
- 跨主题理解：读 `combined_knowledge_base.md`。
