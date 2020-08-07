# About

I don't always use VSCode. But when I do, I use Ultisnips.

![](./mim.jpeg)

This script allows you to write all of your snippets in vims 
Ultisnips format, and convert the whole batch to json format 
for use in vscode.

# Installation

- Clone this repository
- `cd ultisnips-vscode`
- `pip install .`

# Usage

- Create a config file at `~/.vscode/ultisnips-vscode.json`
- Add the paths to your snippets folders. For example:

``` json
{
    "ultisnips-snippets":  "~/.vim/UltiSnips/",
    "vscode-snippets": "~/Library/Application Support/Code/User/snippets/"
}
```

- Source your shell, or log out and log back in so the script is in your `$PATH`
- Run the command `ultisnips_to_vscode` to synchronize your snippets. This will
output something like:

``` 
------------------------------------------------------------------------------------------------------------------------
/Users/ethan/.vim/UltiSnips/zsh.snippets           ----->     /Users/ethan/Library/Application Support/Code/User/snippets/shellscript.json
/Users/ethan/.vim/UltiSnips/texmath.snippets       ----->     /Users/ethan/Library/Application Support/Code/User/snippets/tex.json
/Users/ethan/.vim/UltiSnips/tex.snippets           ----->     /Users/ethan/Library/Application Support/Code/User/snippets/tex.json
/Users/ethan/.vim/UltiSnips/python.snippets        ----->     /Users/ethan/Library/Application Support/Code/User/snippets/python.json
/Users/ethan/.vim/UltiSnips/texmath.snippets       ----->     /Users/ethan/Library/Application Support/Code/User/snippets/markdown.json
/Users/ethan/.vim/UltiSnips/markdown.snippets      ----->     /Users/ethan/Library/Application Support/Code/User/snippets/markdown.json
/Users/ethan/.vim/UltiSnips/all.snippets           ----->     /Users/ethan/Library/Application Support/Code/User/snippets/global.code-snippets
------------------------------------------------------------------------------------------------------------------------
```
