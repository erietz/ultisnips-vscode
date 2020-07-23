from setuptools import setup, find_packages

setup(
    name="ultisnips-to-vscode",
    version="0.0.1",
    description="Converts a directory of ultisnips snippets to json for vscode",
    author="Ethan Rietz",
    keywords="vim ultisnips snippets vscode json",
    #packages=['scripts'],
    scripts=['scripts/ultisnips-to-vscode']
)

