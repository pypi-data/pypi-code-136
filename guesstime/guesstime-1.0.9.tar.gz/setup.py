#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages
from version import __VERSION__

with open('README.md', encoding='utf-8') as f:
    long_text = f.read()

with open('requirements.txt', encoding='utf-8') as f:
    install_requires = f.read().strip().splitlines()

setup(
    name='guesstime',
    version=__VERSION__,
    description=(
        'guesstime'
    ),
    long_description=long_text,
    long_description_content_type="text/markdown",
    author='readerror',
    author_email='readerror@sina.com',
    maintainer='readerror',
    maintainer_email='readerror@sina.com',
    license='GPL License',
    packages=find_packages(),
    package_data={'': ['*']},
    platforms=["all"],
    zip_safe=True,
    url='https://github.com/DJMIN/dao',
    python_requires='>=3.5',
    install_requires=install_requires,
)