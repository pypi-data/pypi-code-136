#
# Copyright (c) 2018, Centrica Hive Ltd.
#
#     This file is part of ccalogging.
#
#     ccalogging is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     ccalogging is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with ccalogging.  If not, see <http://www.gnu.org/licenses/>.
#
from setuptools import setup
from setuptools import find_packages
from ccalogging import __version__ as v

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ccalogging",
    version=v,
    author="Chris Allison",
    author_email="chris.charles.allison+ccalogging@gmail.com",
    url="https://github.com/ccdale/ccalogging",
    description="python module for easy logging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["docs", "tests*"]),
    python_requires=">=3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
)
