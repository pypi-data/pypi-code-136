#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import LoveMijueZengqiangLianaiXiyinli
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('LoveMijueZengqiangLianaiXiyinli'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="love-mijue-zengqiang-lianai-xiyinli",
    version=LoveMijueZengqiangLianaiXiyinli.__version__,
    url="https://github.com/apachecn/love-mijue-zengqiang-lianai-xiyinli",
    author=LoveMijueZengqiangLianaiXiyinli.__author__,
    author_email=LoveMijueZengqiangLianaiXiyinli.__email__,
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
    description="LOVE秘诀增强恋爱吸引力",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "love-mijue-zengqiang-lianai-xiyinli=LoveMijueZengqiangLianaiXiyinli.__main__:main",
            "LoveMijueZengqiangLianaiXiyinli=LoveMijueZengqiangLianaiXiyinli.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
