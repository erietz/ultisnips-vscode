from setuptools import setup

setup(
    name="ultisnips-to-vscode",
    version="0.0.3",
    description="Converts a directory of ultisnips snippets to json for vscode",
    author="Ethan Rietz",
    keywords="vim ultisnips snippets vscode json",
    packages=['src'],
    scripts=['scripts/ultisnips2vscode']
)

