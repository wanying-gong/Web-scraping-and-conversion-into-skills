import tempfile
import unittest
from pathlib import Path

from build_skills import build_skills_from_config
from crawl_and_convert import CrawlConfig, crawl_and_convert, load_config, main, merge_md_files
from fix_links import fix_links_in_dir


class Web2MdPipelineTests(unittest.TestCase):
    def test_load_config_defaults_output_inside_workspace(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            html_dir = root / "html"
            html_dir.mkdir()
            (html_dir / "index.html").write_text("<html><body>Hello</body></html>", encoding="utf-8")
            config_path = root / "config.json"
            config_path.write_text(
                '{"base_html_dir": "html", "entry_html": "index.html"}',
                encoding="utf-8",
            )

            config = load_config(config_path, project_root=root)

            self.assertEqual(config.base_html_dir, html_dir.resolve())
            self.assertEqual(config.entry_html, (html_dir / "index.html").resolve())
            self.assertEqual(config.output_dir, (root / "output").resolve())
            self.assertEqual(config.combined_output, (root / "output" / "combined_knowledge_base.md").resolve())

    def test_crawl_converts_reachable_html_once_despite_link_cycle(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            html_dir = root / "html"
            output_dir = root / "output"
            html_dir.mkdir()
            (html_dir / "index.html").write_text(
                '<html><body><h1>Index</h1><a href="child.html">Child</a></body></html>',
                encoding="utf-8",
            )
            (html_dir / "child.html").write_text(
                '<html><body><h1>Child</h1><a href="index.html">Index</a></body></html>',
                encoding="utf-8",
            )
            config = CrawlConfig(
                base_html_dir=html_dir.resolve(),
                entry_html=(html_dir / "index.html").resolve(),
                output_dir=output_dir.resolve(),
                combined_output=(output_dir / "combined_knowledge_base.md").resolve(),
                skip_files=set(),
            )

            md_paths = crawl_and_convert(config)
            merge_md_files(md_paths, config)

            self.assertEqual([p.relative_to(output_dir.resolve()).as_posix() for p in md_paths], ["index.md", "child.md"])
            self.assertTrue((output_dir / "index.md").exists())
            self.assertTrue((output_dir / "child.md").exists())
            combined = (output_dir / "combined_knowledge_base.md").read_text(encoding="utf-8")
            self.assertIn("index.md", combined)
            self.assertIn("child.md", combined)
            self.assertNotIn("<!-- 来源:", combined)

    def test_fix_links_in_dir_rewrites_relative_html_links_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp)
            md_path = output_dir / "page.md"
            md_path.write_text(
                "[local](child.html#part) [nested](../guide/index.html) "
                "[external](https://example.com/index.html)",
                encoding="utf-8",
            )

            changed_files, replacements = fix_links_in_dir(output_dir)

            self.assertEqual(changed_files, 1)
            self.assertEqual(replacements, 2)
            self.assertEqual(
                md_path.read_text(encoding="utf-8"),
                "[local](child.md#part) [nested](../guide/index.md) "
                "[external](https://example.com/index.html)",
            )

    def test_build_skills_from_config_creates_topic_files_and_readme(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_dir = root / "output"
            docs_dir = output_dir / "docs"
            docs_dir.mkdir(parents=True)
            (docs_dir / "intro.md").write_text(
                "<!-- 来源: docs/intro.html -->\n\n# Intro\n\nUseful intro.\n\nOn this page\nnoise",
                encoding="utf-8",
            )
            config_path = root / "config.json"
            config_path.write_text(
                """
{
  "base_html_dir": "html",
  "entry_html": "index.html",
  "output_dir": "output",
  "skill_groups": [
    {
      "filename": "01_intro.md",
      "title": "Intro Topic",
      "desc": "Intro docs.",
      "when_to_use": "Need intro",
      "files": ["docs/intro.md"]
    }
  ]
}
""".strip(),
                encoding="utf-8",
            )

            built = build_skills_from_config(config_path)

            self.assertEqual([p.name for p in built], ["01_intro.md", "00_README.md"])
            topic = output_dir / "skills" / "01_intro.md"
            readme = output_dir / "skills" / "00_README.md"
            self.assertIn("# Intro Topic", topic.read_text(encoding="utf-8"))
            self.assertIn("Useful intro.", topic.read_text(encoding="utf-8"))
            self.assertIn("01_intro.md", readme.read_text(encoding="utf-8"))

    def test_build_skills_from_config_auto_groups_when_no_skill_groups(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_dir = root / "output"
            (output_dir / "reference").mkdir(parents=True)
            (output_dir / "examples").mkdir(parents=True)
            (output_dir / "index.md").write_text("# Root\n\nRoot page.", encoding="utf-8")
            (output_dir / "reference" / "api.md").write_text("# API\n\nReference page.", encoding="utf-8")
            (output_dir / "examples" / "basic.md").write_text("# Basic\n\nExample page.", encoding="utf-8")
            (output_dir / "combined_knowledge_base.md").write_text("# Combined\n", encoding="utf-8")
            config_path = root / "config.json"
            config_path.write_text(
                """
{
  "base_html_dir": "html",
  "entry_html": "index.html",
  "output_dir": "output",
  "readme": {
    "title": "Generic Docs",
    "description": "Generic docs."
  }
}
""".strip(),
                encoding="utf-8",
            )

            built = build_skills_from_config(config_path)
            names = [p.name for p in built]

            self.assertIn("01_root.md", names)
            self.assertIn("02_examples.md", names)
            self.assertIn("03_reference.md", names)
            self.assertIn("00_README.md", names)
            self.assertIn("Root page.", (output_dir / "skills" / "01_root.md").read_text(encoding="utf-8"))
            self.assertIn("Example page.", (output_dir / "skills" / "02_examples.md").read_text(encoding="utf-8"))

    def test_main_can_run_full_pipeline_from_config(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            html_dir = root / "html"
            html_dir.mkdir()
            (html_dir / "index.html").write_text(
                '<html><body><h1>Index</h1><a href="child.html#x">Child</a></body></html>',
                encoding="utf-8",
            )
            (html_dir / "child.html").write_text(
                '<html><body><h1>Child</h1><a href="index.html">Back</a></body></html>',
                encoding="utf-8",
            )
            config_path = root / "config.json"
            config_path.write_text(
                """
{
  "base_html_dir": "html",
  "entry_html": "index.html",
  "output_dir": "output",
  "combined_output": "output/combined.md",
  "skill_groups": [
    {
      "filename": "01_pages.md",
      "title": "Pages",
      "desc": "Converted pages.",
      "when_to_use": "Need converted pages",
      "files": ["index.md", "child.md"]
    }
  ]
}
""".strip(),
                encoding="utf-8",
            )

            exit_code = main(["--config", str(config_path), "--fix-links", "--build-skills"])

            self.assertEqual(exit_code, 0)
            self.assertTrue((root / "output" / "index.md").exists())
            self.assertTrue((root / "output" / "child.md").exists())
            self.assertTrue((root / "output" / "combined.md").exists())
            self.assertTrue((root / "output" / "skills" / "01_pages.md").exists())
            self.assertTrue((root / "output" / "skills" / "00_README.md").exists())


if __name__ == "__main__":
    unittest.main()
