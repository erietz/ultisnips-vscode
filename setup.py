from setuptools import setup

setup(
    name="ultisnips-vscode",
    version="1.0",
    description="Converts a directory of ultisnips snippets to json for vscode",
    author="Ethan Rietz",
    author_email="ewrietz@gmail.com",
    url="https://github.com/erietz/ultisnips-vscode",
    keywords="vim ultisnips snippets vscode json",
    packages=['ultisnips2vscode'],
    scripts=['scripts/ultisnips2vscode']
)

