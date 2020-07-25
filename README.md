# About

This script allows you to write all of your snippets in vims 
Ultisnips format, and convert the whole batch to json format 
for use in vscode.

# Installation

- Clone this repository
- `cd ultisnips-vscode`
- `pip install ultisnips-to-vscode`
- *Or to install in editable mode: `pip install -e .`*


# Usage

- Create a config file at `~/.vscode/ultisnips-vscode.json`
- Add the paths to your snippets folders. For example:

``` json
{
    "ultisnips-snippets":  "~/.vim/UltiSnips/",
    "vscode-snippets": "~/Library/Application Support/Code/User/snippets/"
}
```

- Run the command `ultisnips-to-vscode` to synchronize your snippets.
