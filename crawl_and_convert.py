"""
crawl_and_convert.py
BFS 爬取本地 HTML 文档，用 MarkItDown 转换为 Markdown，
最后合并成一个知识库文件。
"""

import sys
import json
import argparse
from dataclasses import dataclass, field
from pathlib import Path
from collections import deque

# ─────────────────────────────────────────────
# 0. 依赖检查
# ─────────────────────────────────────────────
def ensure_deps():
    required = ["bs4", "markitdown"]
    missing = []
    for pkg in required:
        try:
            __import__(pkg if pkg != "bs4" else "bs4")
        except ImportError:
            missing.append("beautifulsoup4" if pkg == "bs4" else "markitdown[all]")

    if missing:
        raise RuntimeError(
            "缺少依赖: "
            + ", ".join(missing)
            + "。请先在项目虚拟环境中安装依赖，不要在脚本 import 阶段自动安装。"
        )

ensure_deps()
from bs4 import BeautifulSoup
from markitdown import MarkItDown

# ─────────────────────────────────────────────
# 1. 配置
# ─────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_BASE_HTML_DIR = Path(r"D:\Program Files\Keysight\ADS2025_Update2.3\de\python\docs\html")
DEFAULT_ENTRY_HTML = DEFAULT_BASE_HTML_DIR / "index.html"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "output"
DEFAULT_COMBINED_OUT = DEFAULT_OUTPUT_DIR / "combined_knowledge_base.md"

# 跳过纯工具性页面
DEFAULT_SKIP_FILES = {"genindex.html", "search.html", "py-modindex.html"}


@dataclass(frozen=True)
class CrawlConfig:
    base_html_dir: Path
    entry_html: Path
    output_dir: Path = DEFAULT_OUTPUT_DIR
    combined_output: Path = DEFAULT_COMBINED_OUT
    skip_files: set[str] = field(default_factory=lambda: set(DEFAULT_SKIP_FILES))
    combined_title: str = "ADS Python API 知识库"
    combined_description: str = "本文件由 MarkItDown 自动转换，BFS 遍历自 Keysight ADS2025 Python 文档。"


DEFAULT_CONFIG = CrawlConfig(
    base_html_dir=DEFAULT_BASE_HTML_DIR,
    entry_html=DEFAULT_ENTRY_HTML,
    output_dir=DEFAULT_OUTPUT_DIR,
    combined_output=DEFAULT_COMBINED_OUT,
    skip_files=set(DEFAULT_SKIP_FILES),
    combined_title="ADS Python API 知识库",
    combined_description="本文件由 MarkItDown 自动转换，BFS 遍历自 Keysight ADS2025 Python 文档。",
)

md_converter = MarkItDown(enable_plugins=False)


def _resolve_config_path(value: str | Path, *, base_dir: Path) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = base_dir / path
    return path.resolve()


def load_config(config_path: Path, *, project_root: Path = PROJECT_ROOT) -> CrawlConfig:
    """从 JSON 配置加载转换参数。相对路径按配置文件所在目录解析。"""
    config_path = config_path.resolve()
    data = json.loads(config_path.read_text(encoding="utf-8"))
    config_dir = config_path.parent

    base_html_dir = _resolve_config_path(data["base_html_dir"], base_dir=config_dir)
    entry_raw = data.get("entry_html", "index.html")
    entry_path = Path(entry_raw)
    if entry_path.is_absolute():
        entry_html = entry_path.resolve()
    else:
        entry_html = (base_html_dir / entry_path).resolve()

    output_dir = _resolve_config_path(
        data.get("output_dir", project_root / "output"),
        base_dir=config_dir,
    )
    combined_output = _resolve_config_path(
        data.get("combined_output", output_dir / "combined_knowledge_base.md"),
        base_dir=config_dir,
    )
    skip_files = set(data.get("skip_files", DEFAULT_SKIP_FILES))
    combined = data.get("combined", {})

    return CrawlConfig(
        base_html_dir=base_html_dir,
        entry_html=entry_html,
        output_dir=output_dir,
        combined_output=combined_output,
        skip_files=skip_files,
        combined_title=combined.get("title", "ADS Python API 知识库"),
        combined_description=combined.get(
            "description",
            "本文件由 MarkItDown 自动转换，BFS 遍历自 Keysight ADS2025 Python 文档。",
        ),
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Crawl local HTML docs and convert reachable pages to Markdown."
    )
    parser.add_argument(
        "--config",
        type=Path,
        help="JSON config path. Defaults to built-in ADS2025 paths when omitted.",
    )
    parser.add_argument(
        "--fix-links",
        action="store_true",
        help="Rewrite relative .html links in generated Markdown files to .md links.",
    )
    parser.add_argument(
        "--build-skills",
        action="store_true",
        help="Build topic split files and 00_README.md from the JSON config.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    config = load_config(args.config) if args.config else DEFAULT_CONFIG

    print("=" * 60)
    print("  HTML Docs -> Markdown 知识库 转换器")
    print("=" * 60)
    print(f"  基准目录 : {config.base_html_dir}")
    print(f"  入口文件 : {config.entry_html}")
    print(f"  输出目录 : {config.output_dir}")
    print(f"  合并文件 : {config.combined_output}")
    print("=" * 60 + "\n")

    if not config.entry_html.exists():
        print(f"入口文件不存在: {config.entry_html}")
        return 1

    config.output_dir.mkdir(parents=True, exist_ok=True)

    bfs_order = crawl_and_convert(config)
    merge_md_files(bfs_order, config)

    if args.fix_links:
        from fix_links import fix_links_in_dir

        total_files, total_replacements = fix_links_in_dir(config.output_dir)
        print(
            f"[完成] 链接修复完成，共修改 {total_files} 个文件，"
            f"替换 {total_replacements} 处 .html -> .md 链接。"
        )

    if args.build_skills:
        if args.config is None:
            print("构建主题文件需要通过 --config 指定 JSON 配置。")
            return 1
        from build_skills import build_skills_from_config

        built_paths = build_skills_from_config(args.config)
        print(f"[完成] 主题知识库生成完成，共 {len(built_paths)} 个文件。")

    print("[完成] 全部完成！")
    return 0

# ─────────────────────────────────────────────
# 2. 辅助函数
# ─────────────────────────────────────────────

def resolve_local_path(
    current_file: Path,
    href: str,
    *,
    base_html_dir: Path = DEFAULT_BASE_HTML_DIR,
) -> Path | None:
    """
    把相对/绝对 href 解析为绝对本地路径（Path 对象）。
    不在 BASE_HTML_DIR 内 或 非 .html 文件 → 返回 None。
    """
    href = href.strip()
    # 跳过外部链接、锚点、javascript 等
    if not href or href.startswith(("http://", "https://", "javascript:", "mailto:", "#")):
        return None
    # 去掉 fragment
    if "#" in href:
        href = href.split("#")[0]
    if not href:
        return None
    # 只处理 .html 文件
    if not href.lower().endswith(".html"):
        return None
    # 解析相对路径
    resolved = (current_file.parent / href).resolve()
    # 必须在基准目录内
    try:
        resolved.relative_to(base_html_dir.resolve())
    except ValueError:
        return None
    return resolved


def html_to_md_path(html_path: Path, config: CrawlConfig = DEFAULT_CONFIG) -> Path:
    """把 html_path 映射到 OUTPUT_DIR 下的 .md 路径（保留目录结构）。"""
    rel = html_path.resolve().relative_to(config.base_html_dir.resolve())
    md_rel = rel.with_suffix(".md")
    return config.output_dir / md_rel


def convert_html_to_md(html_path: Path) -> str:
    """用 MarkItDown 把 HTML 文件转成 Markdown 字符串。"""
    try:
        result = md_converter.convert(str(html_path))
        return result.text_content or ""
    except Exception as e:
        print(f"  [警告] 转换失败 {html_path.name}: {e}")
        return f"<!-- 转换失败: {e} -->\n"


def extract_links(html_path: Path, config: CrawlConfig = DEFAULT_CONFIG) -> list[Path]:
    """解析 HTML，提取所有合法本地链接，返回 Path 列表（去重）。"""
    try:
        with open(html_path, "r", encoding="utf-8", errors="replace") as f:
            soup = BeautifulSoup(f.read(), "lxml")
    except Exception as e:
        print(f"  [警告] 解析失败 {html_path.name}: {e}")
        return []

    seen = set()
    links = []
    for tag in soup.find_all("a", href=True):
        resolved = resolve_local_path(
            html_path,
            tag["href"],
            base_html_dir=config.base_html_dir,
        )
        if resolved and resolved not in seen:
            # 跳过黑名单文件
            if resolved.name in config.skip_files:
                continue
            if resolved.exists():
                seen.add(resolved)
                links.append(resolved)
    return links


# ─────────────────────────────────────────────
# 3. BFS 爬取 + 转换
# ─────────────────────────────────────────────

def crawl_and_convert(config: CrawlConfig = DEFAULT_CONFIG):
    """BFS 遍历所有本地 HTML，转换并保存 MD 文件。返回 BFS 顺序的 md 路径列表。"""
    visited: set[Path] = set()
    queue: deque[Path] = deque()
    bfs_order: list[Path] = []  # 记录 md 输出路径（BFS 顺序）

    start = config.entry_html.resolve()
    queue.append(start)
    visited.add(start)

    total = 0
    while queue:
        html_path = queue.popleft()
        total += 1

        # 输出路径
        md_path = html_to_md_path(html_path, config)
        md_path.parent.mkdir(parents=True, exist_ok=True)

        # 转换
        rel_display = html_path.relative_to(config.base_html_dir.resolve())
        print(f"[{total:03d}] 转换: {rel_display}")
        md_text = convert_html_to_md(html_path)
        # 写入文件
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"<!-- 来源: {rel_display} -->\n\n")
            f.write(md_text)
        print(f"       → 已保存: {md_path.relative_to(config.output_dir)}")

        bfs_order.append(md_path)

        # 提取子链接加入队列
        for child in extract_links(html_path, config):
            child_res = child.resolve()
            if child_res not in visited:
                visited.add(child_res)
                queue.append(child_res)

    print(f"\n[完成] BFS 遍历完成，共处理 {total} 个页面。\n")
    return bfs_order


# ─────────────────────────────────────────────
# 4. 合并所有 MD 文件
# ─────────────────────────────────────────────

def merge_md_files(bfs_order: list[Path], config: CrawlConfig = DEFAULT_CONFIG):
    """按 BFS 顺序合并所有 Markdown 文件，生成知识库大文件。"""
    print(f"[合并] 正在合并 {len(bfs_order)} 个 Markdown 文件...")

    # 生成目录
    toc_lines = [
        f"# {config.combined_title}\n",
        f"> {config.combined_description}\n",
        f"> 共 {len(bfs_order)} 个页面。\n\n",
        "---\n\n",
        "## 目录 (Table of Contents)\n\n",
    ]
    for i, md_path in enumerate(bfs_order, 1):
        rel = md_path.relative_to(config.output_dir)
        # 把路径转成标题锚点（简化）
        anchor = str(rel).replace("\\", "/").replace("/", "--").replace(".md", "").lower()
        toc_lines.append(f"{i}. [{rel}](#{anchor})\n")

    toc_lines.append("\n---\n\n")

    config.combined_output.parent.mkdir(parents=True, exist_ok=True)
    with open(config.combined_output, "w", encoding="utf-8") as out:
        out.writelines(toc_lines)

        for i, md_path in enumerate(bfs_order, 1):
            rel = md_path.relative_to(config.output_dir)
            anchor = str(rel).replace("\\", "/").replace("/", "--").replace(".md", "").lower()

            # 写分隔符 + 文件内容
            out.write(f'\n\n---\n\n## {i}. {rel} {{#{anchor}}}\n\n')
            try:
                from build_skills import extract_clean_content

                out.write(extract_clean_content(md_path))
            except Exception as e:
                out.write(f"<!-- 读取失败: {e} -->\n")

    size_mb = config.combined_output.stat().st_size / 1024 / 1024
    print(f"[完成] 合并完成！输出: {config.combined_output}  ({size_mb:.2f} MB)\n")


# ─────────────────────────────────────────────
# 5. 主入口
# ─────────────────────────────────────────────

if __name__ == "__main__":
    sys.exit(main())
