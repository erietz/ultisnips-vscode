import json
from pathlib import Path
from src import vim2vscode
from copy import deepcopy
import json
# from typing import Union

"""
self._snippets_data = {
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
    def __init__(
        self,
        ultisnip_dir: Path,
        vscode_dir: Path,
        language_map: dict = None
        ):
        self.ultisnip_dir = ultisnip_dir
        self.vscode_dir = vscode_dir
        self._snippets_data = {}
        if language_map is None:
            self.language_map = deepcopy(vim2vscode)
        else:
            self.language_map = deepcopy(language_map)

    def _detect_scopes(self, ultisnip_file: Path) -> list:
        base = ultisnip_file.parent
        with open(ultisnip_file) as f:
            scopes = []
            for line in f:
                if line.startswith('extends'):
                    scopes = line.split()[1].strip().split(',')
                    scopes = [base / f'{s}.snippets' for s in scopes if s]
        return scopes


    def _replace_variables(self, string):
        """Replaces all of the ultisnips variables with the corresponding vscode
        variables. TODO: Needs updated
        """

        conversions = {'VISUAL': 'TM_SELECTED_TEXT'}
        for old, new in conversions.items():
            string = string.replace(old, new)
        return string

    def _parse_snippet(self, ultisnip_file: Path) -> dict:
        """
        Parses out the snippets into JSON form with the following schema

        {
            "prefix" : {
                "prefix": "",
                "description": "",
                "body": "",
            },
            ...
        }
        """
        snippets_dictionary = {}
        with open(ultisnip_file, 'r') as f:
            for line in f:
                if line.startswith('snippet'):
                    snippet = {}
                    prefix = line.split()[1].strip()
                    snippet['prefix'] = prefix
                    if '\"' in line:
                        snippet_name = line.split("\"")[1].strip()
                        snippet['description'] = snippet_name
                    body = []
                    line = next(f)
                    while not line.startswith('endsnippet'):
                        body.append(self._replace_variables(line.strip('\n')))
                        line = next(f)
                    snippet['body'] = body
                    snippets_dictionary[prefix] = snippet
        return snippets_dictionary

    def parse_snippets(self) -> None:

        for file in self.ultisnip_dir.glob("*.snippets"):
            snippet_data = {
                "snippets": [],
            }
            vscode_file_type = self.language_map.get(file.stem)
            if vscode_file_type is None:
                continue
            else:
                snippet_data["vscode_file"] = self.vscode_dir.joinpath(vscode_file_type + ".json")

            scopes = self._detect_scopes(file)
            snippet_data["scopes"] = scopes
            scopes.append(file)
            for scope in scopes:
                snippets = self._parse_snippet(scope)
                snippet_data["snippets"].append(snippets)

            self._snippets_data[file.name] = snippet_data


    def write_snippets(self) -> None:
        for ultisnip_file, snippet_data in self._snippets_data.items():
            with open(snippet_data.get("vscode_file"), "w") as f:
                json.dump(snippet_data.get("snippets"), f, indent=2)

    def get_snippet_data(self, ultisnip_file: Path = None) -> dict:
        if ultisnip_file == None:
            return self._snippet_data
        else:
            return self._snippet_data.get(ultisnip_file)
