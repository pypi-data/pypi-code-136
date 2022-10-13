#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
from version import __VERSION__, __NAME__, __DESCRIPTION__


with open('requirements.txt', encoding='utf-8') as f:
    install_requires = [
        line for line in f.read().strip().splitlines()
        if not line.startswith('#')]


setup(
    name=__NAME__,
    version=__VERSION__,
    description=(
        __DESCRIPTION__
    ),
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author='readerror',
    author_email='readerror@sina.com',
    maintainer='readerror',
    maintainer_email='readerror@sina.com',
    license='GPL License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/DJMIN/ddn',
    # python_requires='',
    install_requires=install_requires,
)