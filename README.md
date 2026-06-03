# Web Scraping and Conversion into Skills

把本地 HTML / Sphinx 文档从入口页开始递归抓取，转换成 Markdown，并整理成适合 AI Agent 按需读取的知识库文件。

本项目当前主要用于转换 Keysight ADS Python API 本地文档，但工具本身按配置文件运行，也可以复用于其他本地 HTML 文档集。

## 功能

- 从 `index.html` 或任意入口 HTML 开始 BFS 遍历。
- 自动跟随文档内部 `.html` 链接。
- 只抓取 `base_html_dir` 范围内的本地页面，避免跑到外部网页。
- 用 MarkItDown 将每个 HTML 页面转换为对应的 Markdown。
- 按原 HTML 目录结构镜像输出单页 `.md` 文件。
- 生成 `combined_knowledge_base.md` 合并知识库。
- 可选修复 Markdown 内的相对 `.html` 链接为 `.md`。
- 可选生成 `skills/` 主题分割文件和 `skills/00_README.md`，方便 Agent 按需加载。

## 目录结构

```text
.
├── AGENTS.md
├── crawl_and_convert.py
├── fix_links.py
├── build_skills.py
├── configs/
├── tests/
├── markitdown/
├── output/
└── output_ADS2026/
```

核心脚本：

- `crawl_and_convert.py`：主入口，负责抓取、转换、合并，并可串联链接修复和 skills 构建。
- `fix_links.py`：把 Markdown 中的相对 `.html` 链接改成 `.md` 链接。
- `build_skills.py`：把转换后的 Markdown 按主题合并成 Agent 友好的 `skills/*.md`。
- `configs/*.json`：每个转换任务的路径和输出配置。

## 环境准备

建议使用项目本地虚拟环境，不要安装全局依赖。

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m ensurepip --upgrade
.\.venv\Scripts\python.exe -m pip install beautifulsoup4 lxml "markitdown[all]"
```

如果你已经有 `.venv`，直接使用：

```powershell
.\.venv\Scripts\python.exe
```

## 快速使用

1. 复制一个配置文件，例如：

```powershell
Copy-Item configs\ads2026_ael_python_docs.json configs\my_docs.json
```

2. 修改 `configs\my_docs.json`：

```json
{
  "base_html_dir": "D:\\path\\to\\docs\\html",
  "entry_html": "index.html",
  "output_dir": "D:\\MarkitdownFull\\output\\MyDocs",
  "combined_output": "D:\\MarkitdownFull\\output\\MyDocs\\combined_knowledge_base.md",
  "skip_files": ["genindex.html", "search.html", "py-modindex.html"],
  "combined": {
    "title": "My Docs Knowledge Base",
    "description": "Converted from local HTML docs."
  },
  "build_skills": true,
  "readme": {
    "title": "My Docs 知识库 — 使用指南",
    "description": "本知识库由 HTML 文档转换而来，供 AI Agent 按需读取。"
  }
}
```

3. 运行完整流水线：

```powershell
.\.venv\Scripts\python.exe crawl_and_convert.py --config configs\my_docs.json --fix-links --build-skills
```

## 输出结果

一次转换会生成类似结构：

```text
output/MyDocs/
├── index.md
├── reference/
│   └── api.md
├── examples/
│   └── basic.md
├── combined_knowledge_base.md
└── skills/
    ├── 00_README.md
    ├── 01_root.md
    ├── 02_examples.md
    └── 03_reference.md
```

Agent 使用时建议按这个顺序读取：

1. 先读 `skills/00_README.md`。
2. 再读任务相关的 `skills/*.md`。
3. 需要 API 细节时读对应的单页 Markdown。
4. `combined_knowledge_base.md` 只用于全文搜索，不建议默认整篇加载。

## ADS2026 示例

仓库内包含 ADS2026 Python API 的配置示例，源目录形如：

```text
D:\Program Files\Keysight\ADS2026_Update2.1\doc\python\<module>\html
```

已准备的模块配置包括：

- `ads2026_ael_python_docs.json`
- `ads2026_ann_python_docs.json`
- `ads2026_dataset_python_docs.json`
- `ads2026_dds_python_docs.json`
- `ads2026_de_python_docs.json`
- `ads2026_designcloud_python_docs.json`
- `ads2026_edatoolbox_python_docs.json`
- `ads2026_emtools_python_docs.json`
- `ads2026_hsd_python_docs.json`
- `ads2026_pwdatatools_python_docs.json`
- `ads2026_quantum_python_docs.json`

批量转换示例：

```powershell
$configs = @(
  "configs\ads2026_ael_python_docs.json",
  "configs\ads2026_ann_python_docs.json",
  "configs\ads2026_dataset_python_docs.json",
  "configs\ads2026_dds_python_docs.json",
  "configs\ads2026_de_python_docs.json",
  "configs\ads2026_designcloud_python_docs.json",
  "configs\ads2026_edatoolbox_python_docs.json",
  "configs\ads2026_emtools_python_docs.json",
  "configs\ads2026_hsd_python_docs.json",
  "configs\ads2026_pwdatatools_python_docs.json",
  "configs\ads2026_quantum_python_docs.json"
)

foreach ($cfg in $configs) {
  .\.venv\Scripts\python.exe crawl_and_convert.py --config $cfg --fix-links --build-skills
}
```

ADS2026 的全局 Agent 入口在：

```text
output_ADS2026/
├── AGENT_GUIDE.md
└── 00_API_INDEX.md
```

其中 `DesignEnvironment` 的示例不在顶层 `examples/`，请先看：

```text
output_ADS2026/DesignEnvironment/EXAMPLES_INDEX.md
```

## 配置字段说明

| 字段 | 说明 |
|------|------|
| `base_html_dir` | HTML 文档根目录，只抓取这个目录内的 HTML。 |
| `entry_html` | 入口 HTML，可以是相对 `base_html_dir` 的路径。 |
| `output_dir` | Markdown 输出目录。 |
| `combined_output` | 合并知识库文件路径。 |
| `skip_files` | 跳过的 HTML 文件名，例如 Sphinx 的搜索页和索引页。 |
| `combined.title` | 合并知识库标题。 |
| `combined.description` | 合并知识库说明。 |
| `build_skills` | 是否用于构建 skills，当前 CLI 仍以 `--build-skills` 参数为准。 |
| `readme.title` | `skills/00_README.md` 标题。 |
| `readme.description` | `skills/00_README.md` 描述。 |
| `skill_groups` | 可选。手动指定主题文件分组；不写时按目录自动分组。 |

`skill_groups` 示例：

```json
{
  "skill_groups": [
    {
      "filename": "01_examples.md",
      "title": "Examples",
      "desc": "Runnable examples.",
      "when_to_use": "Need complete example code",
      "files": ["examples/basic.md", "examples/advanced.md"]
    }
  ]
}
```

## 验证

修改代码后建议运行：

```powershell
.\.venv\Scripts\python.exe -m py_compile crawl_and_convert.py fix_links.py build_skills.py tests\test_web2md_pipeline.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test*.py"
```

检查输出中是否还残留相对 `.html` 链接：

```powershell
rg -n -P "\]\((?!https?://)[^)]*\.html" output_ADS2026
```

如果 `rg` 没有输出，通常表示没有残留相对 `.html` Markdown 链接。

## 注意事项

- 默认只处理本地 HTML 文件，不抓取外部网站。
- 纯锚点、`mailto:`、`javascript:`、外部 `http/https` 链接会被跳过。
- 页面去重按不含 fragment 的文件路径处理，避免循环链接导致死循环。
- 输出目录可能很大，不建议默认把大规模转换结果提交到仓库。
- 不要把工具写死到某个 ADS 版本；新增文档源时优先新增 JSON 配置。

