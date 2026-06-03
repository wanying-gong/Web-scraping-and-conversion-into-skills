## 项目定位

本项目是一个可复用的“本地/网页 HTML 文档转 Markdown 知识库”工具。

当前主要场景是把 Keysight ADS Python API 的本地 Sphinx HTML 文档转换为 Markdown，并进一步整理成适合 AI Agent 按需读取的知识库文件。后续允许扩展到其他 HTML 文档源，但不能把项目写死成只服务 ADS 的一次性脚本。

核心产品行为：

- 从入口 HTML 页面开始抓取。
- 如果页面内存在其他允许范围内的 HTML 跳转入口，必须继续进入这些页面抓取。
- 每个被抓取到的 HTML 页面都要转换成对应的 Markdown 文件。
- 必须维护已访问集合，避免循环链接造成重复抓取或死循环。
- 输出必须包含单页 Markdown、合并 Markdown、若干主题分割文件，以及 1 个入口导航文件。

## 使用者约定

- 默认沟通语言为中文。
- 代码、命令、变量名、文件名使用英文。
- 结论先行；方案有问题直接指出。
- 不为了“跑通”而隐藏错误、吞掉关键异常或注释掉失败逻辑。

## 工作空间结构

当前根目录为 `D:\MarkitdownFull`。

约定结构如下：

```text
D:\MarkitdownFull
├── AGENTS.md
├── .venv\
├── crawl_and_convert.py
├── fix_links.py
├── build_skills.py
├── document.md
└── markitdown\
```

后续重构为复用工具时，优先演进为：

```text
D:\MarkitdownFull
├── AGENTS.md
├── pyproject.toml
├── configs\
├── output\
├── src\
│   └── web2md_kb\
├── tests\
└── markitdown\
```

目录约定：

- `configs/`：放转换任务配置，例如 ADS 文档路径、输出目录、跳过文件列表。
- `output/`：默认转换输出目录，放生成的 Markdown 和主题知识库文件。
- `src/web2md_kb/`：放复用工具源码。
- `tests/`：放单元测试和小型样例测试。
- `markitdown/`：上游 MarkItDown 源码，除非明确需要修改转换器行为，否则不要随意改。
- 外部输出目录，例如 `D:\测试`，只能作为运行结果目录，不作为源码目录。

## 虚拟环境

项目已包含本地虚拟环境：

```text
D:\MarkitdownFull\.venv
```

所有 Python 命令默认使用：

```powershell
.\.venv\Scripts\python.exe
```

不要使用系统 Python 作为默认解释器。不要安装全局依赖。新增或变更依赖时，优先写入项目依赖配置；如需联网安装，必须先说明原因并获得确认。

如果 `.venv` 缺少 `pip`，优先使用 Python 自带的 `ensurepip` 补齐：

```powershell
.\.venv\Scripts\python.exe -m ensurepip --upgrade
```

本项目已有 `uv` 时不重复安装 `uv`。如果未来需要安装或升级 `uv`，必须先确认。

## 当前脚本职责

### `crawl_and_convert.py`

职责：

- 从入口 HTML 开始遍历本地 HTML 文档。
- 提取合法的本地 `.html` 链接。
- 对发现的子页面继续遍历，直到允许范围内的可达 HTML 页面全部处理完。
- 使用 `visited` 或等价机制去重，防止循环链接。
- 调用 `MarkItDown` 转换为 Markdown。
- 按原 HTML 目录结构输出 `.md` 文件。
- 合并生成一个总知识库 Markdown 文件。

当前问题：

- 输入目录、输出目录写死。
- import 时会触发依赖检查和可能的安装行为。
- 链接修复不是主流程的一部分。

后续重构要求：

- 不允许脚本在 import 时产生安装依赖、写文件、联网等副作用。
- 输入、输出、入口文件、跳过文件列表必须配置化。
- 核心逻辑必须可被单元测试直接调用。

### `fix_links.py`

职责：

- 把 Markdown 文件中的相对 `.html` 链接替换为 `.md` 链接。

后续重构要求：

- 作为转换流水线中的可选步骤。
- 只处理相对链接，不改外部链接。
- 保留 fragment，例如 `index.html#anchor` 转为 `index.md#anchor`。

### `build_skills.py`

职责：

- 把已转换的 Markdown 文件按主题合并成适合 Agent 使用的知识库文件。

后续重构要求：

- 主题映射从代码迁移到配置文件。
- 缺失文件要汇总报告，不要只零散打印。
- 输出文件结构稳定，便于后续被 Codex/Agent 按需加载。

## 路径与配置规则

硬编码路径只允许出现在示例配置中，不允许散落在核心逻辑里。

配置文件使用 JSON。不要为了配置文件引入 YAML 依赖。

配置至少应表达：

- `base_html_dir`：HTML 文档根目录。
- `entry_html`：入口 HTML，默认相对 `base_html_dir`。
- `output_dir`：Markdown 输出目录。
- `combined_output`：合并后的 Markdown 文件路径。
- `skip_files`：跳过的 HTML 文件名集合。
- `build_skills`：是否构建主题知识库。
- `skill_groups`：主题知识库的分组规则。

默认不把大规模转换结果写进仓库，除非用户明确要求。

## 输出目录规则

运行结果可能很大，默认输出到：

```text
D:\MarkitdownFull\output
```

如果配置中显式指定其他输出目录，以配置为准。

如果输出目录在工作区外，例如 `D:\测试`：

- 写入前需要明确告知。
- 不要把该目录当成源码的一部分。
- 不要自动清理该目录中的旧文件。
- 删除任何已有输出文件或目录前必须先问用户。

标准输出产物：

- 页面级 Markdown：每个被抓取的 HTML 页面生成一个对应 `.md` 文件。
- 合并知识库：按遍历顺序生成一个合并 Markdown 文件。
- 主题分割文件：按配置中的主题分组生成若干 Markdown 文件。
- 入口导航文件：生成 1 个入口导航 Markdown 文件，默认命名为 `00_README.md`。

## 依赖规则

禁止在模块 import 阶段自动安装依赖。

允许的做法：

- 在 README 或错误提示中说明缺失依赖。
- 在 CLI 启动时检查依赖并给出清晰报错。
- 使用项目级依赖配置管理依赖。

不允许的做法：

- 在库代码中直接 `pip install`。
- 静默安装依赖。
- 安装全局 Python 包。

## 代码设计规则

复用工具的核心边界：

- `crawler`：负责本地 HTML 图遍历和链接解析。
- `converter`：负责单文件 HTML 到 Markdown。
- `link_rewriter`：负责 Markdown 链接后处理。
- `merger`：负责按遍历顺序合并 Markdown。
- `skill_builder`：负责按主题构建 Agent 知识库。
- `cli`：负责命令行参数、配置加载和流程编排。

核心模块不得直接读取固定路径；路径必须来自参数或配置。

优先使用 `pathlib.Path` 处理路径。处理 URL 或 HTML 链接时使用标准库 `urllib.parse`，不要手写脆弱的字符串拼接逻辑。

抓取边界：

- 默认只抓取 `base_html_dir` 内部的 HTML 文件。
- 默认跳过外部 URL、`mailto:`、`javascript:`、纯锚点链接。
- 保留链接中的 fragment 信息用于后续 Markdown 链接修复，但页面去重时按不含 fragment 的文件路径去重。
- 默认遍历策略为 BFS，使输出顺序接近从入口页展开的阅读顺序。

## 验证命令

修改 Python 代码后，至少运行：

```powershell
.\.venv\Scripts\python.exe -m py_compile crawl_and_convert.py fix_links.py build_skills.py
```

后续新增 `src/` 和 `tests/` 后，验证命令升级为：

```powershell
.\.venv\Scripts\python.exe -m py_compile src\web2md_kb\*.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test*.py"
```

只改文档时，不强制运行 Python 验证，但需要确认文档路径和内容无明显矛盾。

## Git 与文件安全红线

以下操作必须先问用户：

- 删除文件或目录。
- 修改 `.env`、密钥、token、CI/CD 配置。
- 数据库 schema 变更或数据迁移。
- `git push`、`git rebase`、`git reset --hard`、强制推送。
- 安装新的全局依赖或修改系统配置。
- 发布包、部署生产、公开发布内容。

不要回滚用户已有修改。发现工作区有无关改动时，忽略它们；如果影响当前任务，先说明冲突点。

## 后续重构顺序

把项目改成复用工具时，按以下顺序推进：

1. 先补测试样例和最小单元测试。
2. 去掉 import 阶段自动安装依赖。
3. 把硬编码路径迁移到配置。
4. 拆出 crawler、converter、link_rewriter、merger、skill_builder。
5. 增加 CLI 子命令。
6. 用真实 ADS 文档跑一次端到端验证。

不要一上来大面积重写。每一步都要能验证。
