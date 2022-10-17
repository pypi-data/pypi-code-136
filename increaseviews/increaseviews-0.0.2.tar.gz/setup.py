from setuptools import setup, find_packages
import codecs
import os
from pathlib import Path

VERSION = '0.0.2'
DESCRIPTION = 'A package to increase youtube views of any channel'
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="increaseviews",
    version=VERSION,
    author="CodeWithNazal (Nazal Ahmed)",
    author_email="<ziluzephyr@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['selenium'],
    keywords=['python', 'video', 'youtube', 'views', 'automation'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)