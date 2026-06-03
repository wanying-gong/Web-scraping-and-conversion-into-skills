r"""
fix_links.py
把 D:\测试\ 下所有 .md 文件中的相对 .html 链接替换为 .md 链接。
例如: [介绍](pydocs/intro/index.html) → [介绍](pydocs/intro/index.md)
     [概念](../concepts/index.html#anchor) → [概念](../concepts/index.md#anchor)
只替换相对路径（不动 http/https 链接）。
"""

import re
from pathlib import Path

OUTPUT_DIR = Path(r"D:\测试")

# 匹配 Markdown 链接中的相对 .html（不以 http/https 开头）
# 格式: (path/to/file.html) 或 (path/to/file.html#anchor)
LINK_RE = re.compile(
    r'\((?!https?://)([^)]*?)\.html((?:#[^)]*)?)\)'
)

def fix_file(md_path: Path) -> int:
    """替换文件中所有相对 .html 链接，返回替换次数。"""
    original = md_path.read_text(encoding="utf-8")
    fixed, count = LINK_RE.subn(r'(\1.md\2)', original)
    if count > 0:
        md_path.write_text(fixed, encoding="utf-8")
    return count


def fix_links_in_dir(output_dir: Path = OUTPUT_DIR) -> tuple[int, int]:
    """修复目录中所有 Markdown 文件链接，返回(修改文件数, 替换总数)。"""
    md_files = list(output_dir.rglob("*.md"))
    total_files = 0
    total_replacements = 0

    for md_path in md_files:
        count = fix_file(md_path)
        if count > 0:
            rel = md_path.relative_to(output_dir)
            print(f"  [{count:3d} 处] {rel}")
            total_files += 1
            total_replacements += count

    return total_files, total_replacements


def main():
    total_files, total_replacements = fix_links_in_dir(OUTPUT_DIR)
    print(f"\n[完成] 共修改 {total_files} 个文件，替换 {total_replacements} 处 .html -> .md 链接。")


if __name__ == "__main__":
    print("=" * 55)
    print("  修复 Markdown 链接: .html → .md")
    print("=" * 55)
    main()
