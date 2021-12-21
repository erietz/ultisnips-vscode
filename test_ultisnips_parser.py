import unittest
from pathlib import Path
from src import UltisnipParser

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
