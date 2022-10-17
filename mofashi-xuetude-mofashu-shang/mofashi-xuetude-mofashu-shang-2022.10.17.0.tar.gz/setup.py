#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import MofashiXuetudeMofashuShang
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('MofashiXuetudeMofashuShang'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="mofashi-xuetude-mofashu-shang",
    version=MofashiXuetudeMofashuShang.__version__,
    url="https://github.com/apachecn/mofashi-xuetude-mofashu-shang",
    author=MofashiXuetudeMofashuShang.__author__,
    author_email=MofashiXuetudeMofashuShang.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Documentation",
        "Topic :: Documentation",
    ],
    description="魔法师学徒的魔法书上",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "mofashi-xuetude-mofashu-shang=MofashiXuetudeMofashuShang.__main__:main",
            "MofashiXuetudeMofashuShang=MofashiXuetudeMofashuShang.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
