#!/usr/bin/env python3
# template: https://gitlab.com/jlecomte/projects/python/reference-files

from setuptools import setup

from torxtools import __about__ as about

with open("requirements.txt", "r", encoding="UTF-8") as fd:
    requirements = fd.read().splitlines()


setup(
    name=about.__title__,
    version=about.__version__,
    author=about.__author__,
    author_email=about.__email__,
    url=about.__uri__,
    description=about.__summary__,
    license=about.__license__,
    install_requires=requirements,
)
