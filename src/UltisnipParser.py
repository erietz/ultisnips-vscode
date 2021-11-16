import json
from pathlib import Path
from src import vim2vscode
from copy import deepcopy

"""
self.snippet_data = {
        "ultisnip_file": {
            "scopes" = ["sh.snippets", "bash.snippets", "zsh.snippets"],
            "vscode_file" = Path("/path/to/file.json"),
            "snippets" = [
                {
                    "prefix": "",
                    "description": "",
                    "body": "",
                },
                ...
            ]
        }
    }
"""

class UltisnipParser:
    def __init__(self, ultisnip_dir_path: Path, vscode_dir_path: Path):
        self.ultisnip_dir = ultisnip_dir_path
        self.vscode_dir = vscode_dir_path
        self.language_map = deepcopy(vim2vscode)
        self.snippet_data = {}

    def _detect_scopes(self, ultisnip_file: Path):
        pass

    def parse_snippets(self, ultisnip_file: Path):
        pass

    def write_snippets(self):
        pass
