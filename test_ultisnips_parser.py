import unittest
from pathlib import Path
from src import UltisnipParser

class Foo(unittest.TestCase):
    def test_test(self):
        parser = UltisnipParser(
            Path("./test/ultisnips_snippets"),
            Path("./test/vscode_snippets/")
        )

        snippets = parser._parse_snippet(Path("./test/ultisnips_snippets/python.snippets"))
        print(snippets)

