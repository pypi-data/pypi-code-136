# This file is required to create a python library

from setuptools import find_packages, setup

setup(
    name='rechtspraak-extractor',
    packages=find_packages(include=['rechtspraak-extractor']),
    version='1.0.1',
    description='Library for extracting rechtspraak data',
    author='LawTech Lab',
    license='MIT',
    install_requires=['bs4', 'numpy', 'pandas', 'lxml==4.6.3', 'requests==2.26.0', 'xmltodict==0.13.0']
)