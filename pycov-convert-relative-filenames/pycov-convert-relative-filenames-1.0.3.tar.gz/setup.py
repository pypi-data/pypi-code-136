#!/usr/bin/env python3
# template: https://gitlab.com/jlecomte/projects/python/reference-files

from setuptools import setup

from pycov_convert_relative_filenames import __about__ as about

with open("requirements.txt", "r", encoding="UTF-8") as fd:
    requirements = fd.read().splitlines()
    requirements = [x for x in requirements if x and not x.startswith("--")]

setup(
    name=about.__title__,
    version=about.__version__,
    author=about.__author__,
    author_email=about.__email__,
    url=about.__uri__,
    description=about.__summary__,
    license=about.__license__,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "pycov-convert-relative-filenames = pycov_convert_relative_filenames.__main__:main",
        ],
    },
)
