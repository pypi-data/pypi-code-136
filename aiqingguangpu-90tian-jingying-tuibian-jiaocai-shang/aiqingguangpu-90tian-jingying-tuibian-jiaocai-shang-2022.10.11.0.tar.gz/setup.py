#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import Aiqingguangpu90tianJingyingTuibianJiaocaiShang
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('Aiqingguangpu90tianJingyingTuibianJiaocaiShang'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="aiqingguangpu-90tian-jingying-tuibian-jiaocai-shang",
    version=Aiqingguangpu90tianJingyingTuibianJiaocaiShang.__version__,
    url="https://github.com/apachecn/aiqingguangpu-90tian-jingying-tuibian-jiaocai-shang",
    author=Aiqingguangpu90tianJingyingTuibianJiaocaiShang.__author__,
    author_email=Aiqingguangpu90tianJingyingTuibianJiaocaiShang.__email__,
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
    description="爱情光谱90天精英蜕变教材上",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "aiqingguangpu-90tian-jingying-tuibian-jiaocai-shang=Aiqingguangpu90tianJingyingTuibianJiaocaiShang.__main__:main",
            "Aiqingguangpu90tianJingyingTuibianJiaocaiShang=Aiqingguangpu90tianJingyingTuibianJiaocaiShang.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
