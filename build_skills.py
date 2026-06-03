r"""
build_skills.py
把已转换的 .md 文件按主题合并成 Agent 友好的 Skills 文件集。

默认输出到: D:\MarkitdownFull\output\skills\
  00_README.md                  ← 入口导航（怎么用、去哪找什么）
  01_introduction_and_concepts.md
  02_api_core_objects.md
  03_api_app_ui.md
  04_api_database.md
  05_api_tech.md
  06_api_experimental.md
  07_examples_design.md
  08_api_substrate.md
"""

from pathlib import Path
import re
import argparse
import json

# ─────────────────────────────────────────────
# 配置
# ─────────────────────────────────────────────
SOURCE_DIR = Path(r"D:\测试")
SKILLS_DIR = SOURCE_DIR / "skills"

# 页脚噪音的开始标志（命中任意一个则截断）
FOOTER_PATTERNS = [
    re.compile(r"^On this page\s*$"),
    re.compile(r"^\[Previous"),
    re.compile(r"^\* © Keysight"),
    re.compile(r"^Built with \[Sphinx\]"),
    re.compile(r"^\*arrow_drop_up\*"),
    re.compile(r"^\* \[Privacy\]"),
]

# ─────────────────────────────────────────────
# 分类映射
# ─────────────────────────────────────────────
SKILL_FILES = {
    "01_introduction_and_concepts.md": {
        "title": "Introduction, Concepts & How-To",
        "desc": (
            "ADS Python 入门介绍、许可证说明、嵌入式 Python 用法、"
            "核心概念（术语/工作区元素/连接对象/OpenAccess/脚本执行）、"
            "以及 How-To 指南（虚拟环境设置、Pytest 使用）。"
        ),
        "when_to_use": "当你需要了解 ADS Python 基础、概念术语、或配置开发环境时",
        "files": [
            "pydocs/intro/index.md",
            "pydocs/intro/licensing.md",
            "pydocs/intro/embedded.md",
            "pydocs/intro/extension.md",
            "pydocs/concepts/index.md",
            "pydocs/concepts/terminology.md",
            "pydocs/concepts/workspace_elements.md",
            "pydocs/concepts/connectivity.md",
            "pydocs/concepts/openaccess_integration.md",
            "pydocs/concepts/execution.md",
            "pydocs/howto/index.md",
            "pydocs/howto/venv.md",
            "pydocs/howto/newvenv.md",
            "pydocs/howto/existingvenv.md",
            "pydocs/howto/pytest.md",
        ],
    },
    "02_api_core_objects.md": {
        "title": "Core API: keysight.ads.de",
        "desc": (
            "核心 API 参考：Workspace（工作区）、Library（库）、Cell（单元）、"
            "View（视图）、CellviewRef（引用）、DesignHierarchy（层级）、"
            "DMData、ItemInfo、Points、Collections、AEL 接口。"
        ),
        "when_to_use": "当你需要操作工作区、库、单元格、视图等核心设计对象时",
        "files": [
            "pypde/docs/reference/de/index.md",
            "pypde/docs/reference/de/workspace.md",
            "pypde/docs/reference/de/library.md",
            "pypde/docs/reference/de/cell.md",
            "pypde/docs/reference/de/view.md",
            "pypde/docs/reference/de/cellviewref.md",
            "pypde/docs/reference/de/design_hierarchy.md",
            "pypde/docs/reference/de/dmdata.md",
            "pypde/docs/reference/de/item_info.md",
            "pypde/docs/reference/de/points.md",
            "pypde/docs/reference/de/collections.md",
            "pypde/docs/reference/de/ael.md",
        ],
    },
    "03_api_app_ui.md": {
        "title": "App/UI API: keysight.ads.de.app",
        "desc": (
            "应用层/UI API：Actions（动作）、Menus（菜单）、Addons（插件）、"
            "Callbacks（回调）、Windows/Widgets（窗口控件）、DDS 接口。"
        ),
        "when_to_use": "当你需要创建自定义菜单、窗口、插件、或响应 UI 事件时",
        "files": [
            "pypde/docs/reference/de/app/index.md",
            "pypde/docs/reference/de/app/action.md",
            "pypde/docs/reference/de/app/addon.md",
            "pypde/docs/reference/de/app/callbacks.md",
            "pypde/docs/reference/de/app/window.md",
            "pypde/docs/reference/de/app/dds.md",
        ],
    },
    "04a_api_db_core.md": {
        "title": "Database Core API: keysight.ads.de.db / db_dbu",
        "desc": (
            "数据库核心 API：Parameter Forms（参数表单）、Parameters（参数）、"
            "Properties（属性）、Enums（枚举类型）、Transaction（事务）、"
            "GenPolyline（折线）、Model Definition（模型定义）、"
            "Callbacks（数据库回调）、DBU 单位系统概览。"
        ),
        "when_to_use": "当你需要读写设计数据库元素、处理参数/属性/枚举/几何图形时",
        "files": [
            "pypde/docs/reference/de/db/index.md",
            "pypde/docs/reference/de/db/callbacks.md",
            "pypde/docs/reference/de/db/enums.md",
            "pypde/docs/reference/de/db/forms.md",
            "pypde/docs/reference/de/db/genpolyline.md",
            "pypde/docs/reference/de/db/model_def.md",
            "pypde/docs/reference/de/db/parameters.md",
            "pypde/docs/reference/de/db/properties.md",
            "pypde/docs/reference/de/db/transaction.md",
            "pypde/docs/reference/de/db_dbu/index.md",
        ],
    },
    "04b_api_db_uu_elements.md": {
        "title": "Database UU API: keysight.ads.de.db_uu (Design Elements)",
        "desc": (
            "UU 单位坐标系下的设计元素 API（最底层布局操作）：db_uu 设计元素完整参考、"
            "LayerId（图层标识符）、LineTypeInfo（线型信息）。"
            "注：此文件内容较多，包含所有布局元素的详细 API 定义。"
        ),
        "when_to_use": "当你需要在 UU 坐标系下直接操作布局元素（矩形、多边形、走线、Pin 等）时",
        "files": [
            "pypde/docs/reference/de/db_uu/index.md",
            "pypde/docs/reference/de/db_uu/db_uu.md",
            "pypde/docs/reference/de/db_uu/layer_id.md",
            "pypde/docs/reference/de/db_uu/line_type_info.md",
        ],
    },
    "05_api_tech.md": {
        "title": "Tech API: keysight.ads.de.tech",
        "desc": (
            "技术层 API：Tech 对象（工艺参数）、Padstacks（焊盘叠层）、"
            "Via Rules（过孔规则）、Nested Technology（嵌套工艺）。"
        ),
        "when_to_use": "当你需要读取或修改工艺/技术文件、焊盘/过孔定义时",
        "files": [
            "pypde/docs/reference/de/tech/index.md",
            "pypde/docs/reference/de/tech/tech.md",
            "pypde/docs/reference/de/tech/pads/pads.md",
            "pypde/docs/reference/de/tech/rule/rule.md",
            "pypde/docs/reference/de/tech/nested/nested.md",
        ],
    },
    "06_api_experimental.md": {
        "title": "Experimental API: keysight.ads.de.experimental",
        "desc": (
            "实验性 API（不保证向后兼容）：CDF（组件数据格式）、Commands（命令）、"
            "Handles（句柄）、Symbol Generator（符号生成器）、ProView、"
            "Polygon Utilities（多边形工具）、TextMaker、Preferences（偏好设置）、"
            "Netlist Helper（网表工具）。"
        ),
        "when_to_use": "当你需要使用高级/实验性功能，如符号生成、多边形操作、CDF 访问时",
        "files": [
            "pypde/docs/reference/de/experimental/index.md",
            "pypde/docs/reference/de/experimental/cdf/index.md",
            "pypde/docs/reference/de/experimental/commands.md",
            "pypde/docs/reference/de/experimental/handles.md",
            "pypde/docs/reference/de/experimental/symbol.md",
            "pypde/docs/reference/de/experimental/pro_view.md",
            "pypde/docs/reference/de/experimental/polygon_utils.md",
            "pypde/docs/reference/de/experimental/text_maker.md",
            "pypde/docs/reference/de/experimental/preferences.md",
            "pypde/docs/reference/de/experimental/netlist_helper.md",
        ],
    },
    "07_examples_design.md": {
        "title": "Design Examples (pypde)",
        "desc": (
            "完整示例代码（23 个）：创建原理图、布局、工作区、仿真+绘图、"
            "调用 AEL、CDF 组件参数、模型定义、LPF、属性、自定义菜单/插件、"
            "焊盘/过孔、嵌套工艺、规则、放置文字、多边形、PySide2 UI、"
            "层级遍历、VAR 变量、XML-RPC、GDS 导入导出。"
        ),
        "when_to_use": "当你需要参考完整的可运行示例代码时",
        "files": [
            "pypde/docs/examples/index.md",
            "pypde/docs/examples/ex_calling_ael_and_python.md",
            "pypde/docs/examples/ex_create_layout.md",
            "pypde/docs/examples/ex_create_schematic.md",
            "pypde/docs/examples/ex_workspace.md",
            "pypde/docs/examples/ex_create_sim_and_plot.md",
            "pypde/docs/examples/ex_cdf.md",
            "pypde/docs/examples/ex_parameters.md",
            "pypde/docs/examples/ex_itemdef.md",
            "pypde/docs/examples/ex_model.md",
            "pypde/docs/examples/ex_lpf.md",
            "pypde/docs/examples/ex_properties.md",
            "pypde/docs/examples/ex_menu_addon.md",
            "pypde/docs/examples/ex_padstack.md",
            "pypde/docs/examples/ex_nested.md",
            "pypde/docs/examples/ex_rules.md",
            "pypde/docs/examples/ex_place_text.md",
            "pypde/docs/examples/ex_polygon.md",
            "pypde/docs/examples/ex_pyside.md",
            "pypde/docs/examples/ex_traversing_hierarchy.md",
            "pypde/docs/examples/ex_working_with_var.md",
            "pypde/docs/examples/ex_xml_rpc.md",
            "pypde/docs/examples/ex_translate_gds.md",
        ],
    },
    "08_api_substrate.md": {
        "title": "Substrate API: keysight.ads.subst (pysubst)",
        "desc": (
            "基板 API：keysight.ads.subst 模块参考 + 示例。"
            "包括创建基板（Create Substrate）、带布局的基板（Substrate with Layout）。"
        ),
        "when_to_use": "当你需要创建或操作基板（Substrate）设计时",
        "files": [
            "pysubst/docs/index.md",
            "pysubst/docs/reference/index.md",
            "pysubst/docs/reference/subst/index.md",
            "pysubst/docs/examples/index.md",
            "pysubst/docs/examples/ex_make_substrate.md",
            "pysubst/docs/examples/ex_substrate_with_layout.md",
        ],
    },
}


# ─────────────────────────────────────────────
# 工具函数
# ─────────────────────────────────────────────

def extract_clean_content(md_path: Path) -> str:
    """
    从 .md 文件中提取干净的主体内容：
      - 跳过开头的导航噪音（header、sidebar TOC）
      - 在第一个 H1 标题处开始
      - 在页脚噪音处截断
    """
    try:
        lines = md_path.read_text(encoding="utf-8").splitlines()
    except Exception as e:
        return f"<!-- 读取失败: {e} -->\n"

    # 找第一个 H1 (以 "# " 开头，不是 "##")
    start = None
    for i, line in enumerate(lines):
        if line.startswith("# ") and not line.startswith("## "):
            start = i
            break

    # 如果找不到 H1，尝试找第一个 ## （有些页面只有 H2）
    if start is None:
        for i, line in enumerate(lines):
            if line.startswith("## "):
                start = i
                break

    # 还是找不到，就从 <!-- 来源 --> 后第2行开始，取全部内容
    if start is None:
        start = 2

    # 从 start 往后，找到页脚标志截断
    end = len(lines)
    for i in range(start, len(lines)):
        stripped = lines[i].strip()
        for pattern in FOOTER_PATTERNS:
            if pattern.match(stripped):
                end = i
                break
        if end != len(lines):
            break

    content = "\n".join(lines[start:end]).strip()
    return content + "\n"


def build_skill_file(out_path: Path, meta: dict, source_dir: Path = SOURCE_DIR) -> int:
    """生成一个 skill 文件，返回文件大小（字节）。"""
    parts = []

    # 文件标题和说明
    parts.append(f"# {meta['title']}\n")
    parts.append(f"> **说明：** {meta['desc']}\n\n")
    parts.append(f"> **何时使用：** {meta['when_to_use']}\n\n")
    parts.append("---\n\n")

    # 目录
    parts.append("## 本文件目录\n\n")
    for fpath in meta["files"]:
        md_path = source_dir / fpath.replace("/", "\\")
        # 从文件里提取 H1 标题用于目录
        try:
            first_h1 = ""
            for line in md_path.read_text(encoding="utf-8").splitlines():
                if line.startswith("# "):
                    first_h1 = line.lstrip("# ").split("[")[0].strip()
                    break
            label = first_h1 if first_h1 else Path(fpath).stem
        except Exception:
            label = Path(fpath).stem
        parts.append(f"- **{label}** (`{fpath}`)\n")
    parts.append("\n---\n\n")

    # 逐文件追加内容
    for fpath in meta["files"]:
        md_path = source_dir / fpath.replace("/", "\\")
        if not md_path.exists():
            print(f"  [警告] 文件不存在: {fpath}")
            continue
        content = extract_clean_content(md_path)
        parts.append(f"<!-- === 来源: {fpath} === -->\n\n")
        parts.append(content)
        parts.append("\n\n---\n\n")

    full_text = "".join(parts)
    out_path.write_text(full_text, encoding="utf-8")
    return len(full_text.encode("utf-8"))


def build_readme(
    skills_meta: dict,
    sizes: dict,
    *,
    skills_dir: Path = SKILLS_DIR,
    source_dir: Path = SOURCE_DIR,
    title: str = "ADS Python API 知识库 — 使用指南",
    description: str = (
        "本知识库来自 **Keysight ADS 2025 Update 2** Python API 官方文档，\n"
        "经 MarkItDown 转换并按主题分类整理，专为 AI Agent 按需加载设计。"
    ),
) -> Path:
    """生成 00_README.md 入口导航文件。"""
    lines = [
        f"# {title}\n\n",
        f"> {description.replace(chr(10), chr(10) + '> ')}\n\n",
        "---\n\n",
        "## 这个仓库包含什么\n\n",
        "| 文件 | 内容 | 大小 |\n",
        "|------|------|------|\n",
    ]

    for filename, meta in skills_meta.items():
        kb = sizes.get(filename, 0) // 1024
        lines.append(f"| `{filename}` | {meta['title']} | ~{kb} KB |\n")

    lines.append("\n---\n\n")
    lines.append("## 如何使用（按需加载策略）\n\n")
    lines.append("根据你的任务选择对应文件读取，**不要一次性加载所有文件**。\n\n")
    lines.append("| 我想做什么 | 应该读取哪个文件 |\n")
    lines.append("|-----------|----------------|\n")

    for filename, meta in skills_meta.items():
        lines.append(f"| {meta['when_to_use']} | `{filename}` |\n")

    lines.append("\n---\n\n")
    lines.append("## 模块概览\n\n")
    lines.append("```\n")
    for filename, meta in skills_meta.items():
        lines.append(f"{filename} -> {meta['title']}\n")
    lines.append("```\n\n")
    lines.append("---\n\n")
    lines.append("## 原始文件索引\n\n")
    lines.append(f"原始转换文件保存在 `{source_dir}` 目录下（按原 HTML 目录结构镜像），")
    lines.append("可用于查阅具体细节。本 `skills/` 目录下的文件是按主题合并的精简版本。\n")

    readme_path = skills_dir / "00_README.md"
    readme_path.write_text("".join(lines), encoding="utf-8")
    readme_size = readme_path.stat().st_size
    print(f"  [完成] 00_README.md  ({readme_size // 1024} KB)")
    return readme_path


def _skill_groups_to_mapping(groups: list[dict]) -> dict:
    return {group["filename"]: {k: v for k, v in group.items() if k != "filename"} for group in groups}


def discover_skill_groups(source_dir: Path) -> dict:
    """按输出目录结构自动生成主题分组。"""
    grouped: dict[str, list[str]] = {}
    for md_path in sorted(source_dir.rglob("*.md")):
        rel = md_path.relative_to(source_dir).as_posix()
        if rel == "combined_knowledge_base.md" or rel.startswith("skills/"):
            continue
        parts = rel.split("/")
        group_name = "root" if len(parts) == 1 else parts[0]
        grouped.setdefault(group_name, []).append(rel)

    skills_meta = {}
    ordered_names = sorted(grouped)
    if "root" in ordered_names:
        ordered_names.remove("root")
        ordered_names.insert(0, "root")

    for index, group_name in enumerate(ordered_names, 1):
        filename = f"{index:02d}_{group_name.lower().replace(' ', '_')}.md"
        title = group_name.replace("_", " ").replace("-", " ").title()
        skills_meta[filename] = {
            "title": title,
            "desc": f"{title} 相关页面。",
            "when_to_use": f"当你需要查阅 {title} 相关内容时",
            "files": grouped[group_name],
        }

    return skills_meta


def build_skills(
    skills_meta: dict,
    *,
    source_dir: Path = SOURCE_DIR,
    skills_dir: Path = SKILLS_DIR,
    readme_title: str = "ADS Python API 知识库 — 使用指南",
    readme_description: str = (
        "本知识库来自 **Keysight ADS 2025 Update 2** Python API 官方文档，\n"
        "经 MarkItDown 转换并按主题分类整理，专为 AI Agent 按需加载设计。"
    ),
) -> list[Path]:
    """按主题配置生成 skill 文件和入口导航文件。"""
    skills_dir.mkdir(parents=True, exist_ok=True)
    sizes = {}
    built_paths: list[Path] = []

    for filename, meta in skills_meta.items():
        out_path = skills_dir / filename
        size = build_skill_file(out_path, meta, source_dir)
        sizes[filename] = size
        built_paths.append(out_path)
        print(f"  [完成] {filename}  ({size // 1024} KB)")

    readme_path = build_readme(
        skills_meta,
        sizes,
        skills_dir=skills_dir,
        source_dir=source_dir,
        title=readme_title,
        description=readme_description,
    )
    built_paths.append(readme_path)
    return built_paths


def build_skills_from_config(config_path: Path) -> list[Path]:
    """从转换 JSON 配置生成主题知识库文件。"""
    config_path = config_path.resolve()
    data = json.loads(config_path.read_text(encoding="utf-8"))
    config_dir = config_path.parent

    output_dir = Path(data.get("output_dir", "output"))
    if not output_dir.is_absolute():
        output_dir = (config_dir / output_dir).resolve()
    skills_dir = Path(data.get("skills_dir", output_dir / "skills"))
    if not skills_dir.is_absolute():
        skills_dir = (config_dir / skills_dir).resolve()

    groups = data.get("skill_groups", [])
    skills_meta = _skill_groups_to_mapping(groups) if groups else discover_skill_groups(output_dir)
    readme = data.get("readme", {})

    return build_skills(
        skills_meta,
        source_dir=output_dir,
        skills_dir=skills_dir,
        readme_title=readme.get("title", "ADS Python API 知识库 — 使用指南"),
        readme_description=readme.get(
            "description",
            "本知识库来自 **Keysight ADS 2025 Update 2** Python API 官方文档，\n"
            "经 MarkItDown 转换并按主题分类整理，专为 AI Agent 按需加载设计。",
        ),
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build topic Markdown files for agent use.")
    parser.add_argument("--config", type=Path, help="JSON config path.")
    return parser.parse_args(argv)


# ─────────────────────────────────────────────
# 主入口
# ─────────────────────────────────────────────

def main(argv: list[str] | None = None):
    args = parse_args(argv)
    if args.config:
        built_paths = build_skills_from_config(args.config)
        print("\n" + "=" * 60)
        print(f"  完成！共生成 {len(built_paths)} 个文件")
        print("=" * 60)
        return 0

    print("=" * 60)
    print("  构建 ADS Python API Skills 知识库")
    print("=" * 60)

    built_paths = build_skills(SKILL_FILES)

    print("\n" + "=" * 60)
    print(f"  完成！输出目录: {SKILLS_DIR}")
    print(f"  共 {len(built_paths)} 个文件")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
