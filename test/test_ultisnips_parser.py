import unittest
from pathlib import Path
from shutil import rmtree
from ultisnips2vscode import UltisnipParser
import json

class TestParseSnippet(unittest.TestCase):
    def test_parsing_a_single_file(self):
        parser = UltisnipParser(
            Path("./test/ultisnips_snippets"),
            Path("./test/vscode_snippets/")
        )

        snippets = parser._parse_snippet(Path("./test/ultisnips_snippets/python.snippets"))

        self.assertDictEqual(
            snippets.get("main"),
            {
                "prefix": "main",
                "description": "main block",
                "body": [
                    "if __name__ == '__main__':",
                    "    pass"
                ]
            }
        )

        self.assertDictEqual(
            snippets.get("modules-math"),
            {
                "prefix": "modules-math",
                "description": "import math modules",
                "body": [
                    "import numpy as np",
                    "import matplotlib.pyplot as plt",
                    "import pandas as pd"
                ]
            }
        )

        self.assertDictEqual(
            snippets.get("shebang"),
            {
                "prefix": "shebang",
                "description": "shebang",
                "body": [
                    "#!/usr/bin/env python3",
                    "$0"
                ]
            }
        )

        # NOTE: this snippet does not contain the optional description
        self.assertDictEqual(
            snippets.get("delim"),
            {
                "prefix": "delim",
                "body": [
                    "# In[$1]:",
                    "",
                    "$0"
                ]
            }
        )

class TestParseSnippetsDirectory(unittest.TestCase):
    def test_parse_snippets(self):
        parser = UltisnipParser(
            Path("./test/ultisnips_snippets"),
            Path("./test/vscode_snippets/")
        )
        parser.parse_snippets()

        self.assertIsInstance(parser._snippets_data, dict)
        python_snippet_data = parser._snippets_data.get("python.snippets")
        self.assertIsInstance(python_snippet_data, dict)
        self.assertIsInstance(python_snippet_data.get("snippets"), dict)

        self.assertEqual(
            python_snippet_data.get("vscode_file"),
            Path("./test/vscode_snippets/python.json")
            )

class TestWriteSnippets(unittest.TestCase):
    def setUp(self):
        generated_snippets_dir = Path("./test/vscode_snippets/")
        rmtree(generated_snippets_dir)

    def test_write_all_snippets(self):
        ultisnip_dir = Path("./test/ultisnips_snippets")
        vscode_dir = Path("./test/vscode_snippets")
        parser = UltisnipParser(ultisnip_dir, vscode_dir)
        parser.parse_snippets()
        parser.write_snippets()

        self.assertTrue(Path.exists(vscode_dir / "python.json"))
        self.assertTrue(Path.exists(vscode_dir / "global.code-snippets"))
