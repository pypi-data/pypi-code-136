# -*- coding: utf-8 -*-

from setuptools import setup
from codecs import open
from os import path
import re

package_name = "sapt"

setup(
    name=package_name,

    version="2.0.1",

    license="MIT License",

    entry_points={
        "console_scripts": [
            "sapt = SakuraPackage:sapt"
        ]
    }
)