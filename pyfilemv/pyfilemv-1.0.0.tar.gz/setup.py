from setuptools import setup, find_packages
from pathlib import Path

VERSION = '1.0.0'
DESCRIPTION = 'Alternative for unix mv, which searches through your files and updates any references to the file that you just moved.'
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
    packages=find_packages(),
    install_requires=['colorama'],
    keywords=['python', 'filesystem', 'move', 'renaming', 'organization'],
    classifiers=["Operating System :: Unix", "Operating System :: MacOS"],
    scripts=['bin/pymv']
)
