#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import MianfeiMoshiVer2ZhizhongjiPingtaiMoshi
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('MianfeiMoshiVer2ZhizhongjiPingtaiMoshi'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="mianfei-moshi-ver2-zhizhongji-pingtai-moshi",
    version=MianfeiMoshiVer2ZhizhongjiPingtaiMoshi.__version__,
    url="https://github.com/apachecn/mianfei-moshi-ver2-zhizhongji-pingtai-moshi",
    author=MianfeiMoshiVer2ZhizhongjiPingtaiMoshi.__author__,
    author_email=MianfeiMoshiVer2ZhizhongjiPingtaiMoshi.__email__,
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
    description="免费模式2.0之终极平台模式",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "mianfei-moshi-ver2-zhizhongji-pingtai-moshi=MianfeiMoshiVer2ZhizhongjiPingtaiMoshi.__main__:main",
            "MianfeiMoshiVer2ZhizhongjiPingtaiMoshi=MianfeiMoshiVer2ZhizhongjiPingtaiMoshi.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
