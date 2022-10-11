# mypy: ignore-errors
import sys

from setuptools import setup

sys.stderr.write(
    """
===============================
Unsupported installation method
===============================
This project no longer supports installation with `python setup.py install`.
Please use `python -m pip install .` instead.
"""
)
sys.exit(1)


# The below code will never execute, however GitHub is particularly
# picky about where it finds Python packaging metadata.
# See: https://github.com/github/feedback/discussions/6456
#
# To be removed once GitHub catches up.

setup(
    name="jwt-signature-validator",
    install_requires=["pyjwt>=2.4.0"],
)
