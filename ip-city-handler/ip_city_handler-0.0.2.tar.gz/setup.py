#!/usr/bin/env python
# coding: utf-8
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ip_city_handler",
    version="0.0.2",
    author="Oren Zhang",
    url="https://www.oren.ink/",
    author_email="oren_zhang@outlook.com",
    description="A Tool deals with IpCity Data",
    packages=["ip_city_handler"],
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
