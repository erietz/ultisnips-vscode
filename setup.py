from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ultisnips-vscode",
    version="1.1",
    description="Converts a directory of ultisnips snippets to json for vscode",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ethan Rietz",
    author_email="ewrietz@gmail.com",
    url="https://github.com/erietz/ultisnips-vscode",
    keywords="vim ultisnips snippets vscode json",
    packages=['ultisnips2vscode'],
    scripts=['scripts/ultisnips2vscode']
)

