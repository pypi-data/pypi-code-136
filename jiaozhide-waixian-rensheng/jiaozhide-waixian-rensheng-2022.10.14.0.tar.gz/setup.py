#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import JiaozhideWaixianRensheng
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('JiaozhideWaixianRensheng'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="jiaozhide-waixian-rensheng",
    version=JiaozhideWaixianRensheng.__version__,
    url="https://github.com/apachecn/jiaozhide-waixian-rensheng",
    author=JiaozhideWaixianRensheng.__author__,
    author_email=JiaozhideWaixianRensheng.__email__,
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
    description="太阳水星金星火星交织的外显人生",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "jiaozhide-waixian-rensheng=JiaozhideWaixianRensheng.__main__:main",
            "JiaozhideWaixianRensheng=JiaozhideWaixianRensheng.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
