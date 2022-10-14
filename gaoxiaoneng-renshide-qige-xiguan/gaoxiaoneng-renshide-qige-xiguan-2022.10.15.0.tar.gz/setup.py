#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import GaoxiaonengRenshideQigeXiguan
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('GaoxiaonengRenshideQigeXiguan'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="gaoxiaoneng-renshide-qige-xiguan",
    version=GaoxiaonengRenshideQigeXiguan.__version__,
    url="https://github.com/apachecn/gaoxiaoneng-renshide-qige-xiguan",
    author=GaoxiaonengRenshideQigeXiguan.__author__,
    author_email=GaoxiaonengRenshideQigeXiguan.__email__,
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
    description="高效能人士的七个习惯",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "gaoxiaoneng-renshide-qige-xiguan=GaoxiaonengRenshideQigeXiguan.__main__:main",
            "GaoxiaonengRenshideQigeXiguan=GaoxiaonengRenshideQigeXiguan.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
