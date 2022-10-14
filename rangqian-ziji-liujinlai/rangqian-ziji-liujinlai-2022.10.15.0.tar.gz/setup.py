#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import RangqianZijiLiujinlai
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('RangqianZijiLiujinlai'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="rangqian-ziji-liujinlai",
    version=RangqianZijiLiujinlai.__version__,
    url="https://github.com/apachecn/rangqian-ziji-liujinlai",
    author=RangqianZijiLiujinlai.__author__,
    author_email=RangqianZijiLiujinlai.__email__,
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
    description="让钱自己流进来",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "rangqian-ziji-liujinlai=RangqianZijiLiujinlai.__main__:main",
            "RangqianZijiLiujinlai=RangqianZijiLiujinlai.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
