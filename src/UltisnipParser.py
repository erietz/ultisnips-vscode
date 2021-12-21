import json
from pathlib import Path
from src import vim2vscode
from copy import deepcopy
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
        pass


    def _replace_variables(self, string):
        """Replaces all of the ultisnips variables with the corresponding vscode
        variables. TODO: Needs updated
        """

        conversions = {'VISUAL': 'TM_SELECTED_TEXT'}
        for old, new in conversions.items():
            string = string.replace(old, new)
        return string
    
    def _parse_snippet(self, ultisnip_file: Path) -> list:
        """
        Parses out the snippets into JSON form and return a list of dicts
        with the following schema

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
                    dictionary = {}
                    prefix = line.split()[1].strip()
                    dictionary['prefix'] = prefix
                    if '\"' in line:
                        snippet_name = line.split("\"")[1].strip()
                        dictionary['description'] = snippet_name
                    body = []
                    line = next(f)
                    while not line.startswith('endsnippet'):
                        body.append(self._replace_variables(line.strip('\n')))
                        line = next(f)
                    dictionary['body'] = body
                    snippets_dictionary[prefix] = dictionary
        return snippets_dictionary

    def parse_snippets(self) -> None:
        snippet_data = {
            "snippets": [],
        }

        for file in self.ultisnip_dir.glob("*.snippets"):
            vscode_file = self.language_map.get(file.name)
            if vscode_file is None:
                continue
            else:
                snippet_data["vscode_file"] = vscode_file

            scopes = self._detect_scopes(file)
            snippet_data["scopes"] = scopes
            scopes.append(file)
            for scope in scopes:
                snippets = self._parse_snippet(scope)
                snippet_data["snippets"].append(snippets)

        self._snippets_data[file.name] = snippet_data


    def write_snippets(self) -> None:
        pass

    def get_snippet_data(self, ultisnip_file: Path = None) -> dict:
        if ultisnip_file == None:
            return self._snippet_data
        else:
            return self._snippet_data.get(ultisnip_file)
