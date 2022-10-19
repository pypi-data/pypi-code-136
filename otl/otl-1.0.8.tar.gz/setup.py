# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from otl.__version__ import __title__, __version__, __author__, __license__

requires = []
with open('requirements.txt', 'r') as f1:
    for line in f1.readlines():
        requires.append(line.strip())

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name=__title__,
    version=__version__,
    description="运维工具集",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    author_email='xuyong@qq.com',
    url='https://github.com/xuyonggit/otl.git',
    packages=find_packages(),
    install_requires=requires,
    license=__license__,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
