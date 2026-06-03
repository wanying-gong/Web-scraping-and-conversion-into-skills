# AEL Python Documentation 知识库 — 使用指南

> 本知识库来自 Keysight ADS 2025 Update 2 AEL Python HTML 文档，经 MarkItDown 转换并按主题分类整理，专为 AI Agent 按需加载设计。

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
| `01_intro.md` | Introduction | ~1 KB |
| `02_concepts.md` | Concepts | ~10 KB |
| `03_reference.md` | Reference | ~1 KB |
| `04_examples.md` | Examples | ~4 KB |
| `05_howto.md` | How-To | ~1 KB |

---

## 如何使用（按需加载策略）

根据你的任务选择对应文件读取，**不要一次性加载所有文件**。

| 我想做什么 | 应该读取哪个文件 |
|-----------|----------------|
| 当你需要了解 AEL Python 文档结构或基础使用方式时 | `01_intro.md` |
| 当你需要理解 AEL/Python 互操作机制或类型转换规则时 | `02_concepts.md` |
| 当你需要查询 keysight.ads.ael 模块 API 时 | `03_reference.md` |
| 当你需要参考可运行示例或调用模式时 | `04_examples.md` |
| 当你需要配置 AEL Python 开发环境或测试流程时 | `05_howto.md` |

---

## 模块概览

```
01_intro.md -> Introduction
02_concepts.md -> Concepts
03_reference.md -> Reference
04_examples.md -> Examples
05_howto.md -> How-To
```

---

## 原始文件索引

原始转换文件保存在 `D:\MarkitdownFull\output` 目录下（按原 HTML 目录结构镜像），可用于查阅具体细节。本 `skills/` 目录下的文件是按主题合并的精简版本。
