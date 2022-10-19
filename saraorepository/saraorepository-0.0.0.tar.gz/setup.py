#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="saraorepository",
    version="0.0.0",
    description="Package to generate DOIs,create a webpage and upload data",
    long_description=readme + "\n\n",
    author="Sydil Kupa",
    author_email="skupa@ska.ac.za",
    url="https://github.com/ska-sa/katsdparchive/",
    packages=setuptools.find_packages(where="src", include=["saraorepository"]),
    package_dir={"": "src"},
    scripts=["scripts/doi.py"],
    include_package_data=True,
    license="None",
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)
