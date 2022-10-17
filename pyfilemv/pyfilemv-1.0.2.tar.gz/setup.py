from setuptools import setup, find_packages
from pathlib import Path

VERSION = '1.0.2'
DESCRIPTION = 'Extension of the unix mv command, which will also searches through your files and updates any references to the file that you just moved.'
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="pyfilemv",
    version=VERSION,
    author="nickhir",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/nickhir/pyfilemv/",
    packages=find_packages(),
    install_requires=['colorama', 'tqdm'],
    keywords=['python', 'filesystem', 'move', 'renaming', 'organization'],
    classifiers=["Operating System :: Unix", "Operating System :: MacOS"],
    scripts=['bin/pymv']
)
