#!/usr/bin/env python

import re
from setuptools import setup, find_packages


def GetVersion():
    with open("./aie/__init__.py") as f:
        return re.findall(r"__version__\s*=\s*\"([.\d]+)\"", f.read())[0]


__version__ = GetVersion()
requirements = open("requirements.txt").readlines()

packages = find_packages(exclude=["tests"])
# print("packages:", packages)
setup(
    name="aie-sdk",
    version=__version__,
    description="AIEarth Engine Python SDK",
    url="https://engine-aiearth.aliyun.com/",
    packages=packages,
    python_requires=">=3.5.0",
    install_requires=requirements,
)
