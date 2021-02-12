from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="ultisnips-vscode",
    version="1.0.0",
    description="Converts a directory of ultisnips snippets to json for vscode",
    long_description=readme,
    author="Ethan Rietz",
    author_email='ewrietz@gmail.com',
    url='https://github.com/erietz/ultisnips-vscode',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    #scripts=['scripts/ultisnips2vscode'],
    keywords="vim ultisnips snippets vscode json",
)
