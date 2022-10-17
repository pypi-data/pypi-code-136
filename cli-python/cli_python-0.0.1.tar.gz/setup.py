import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setup(
    name="cli_python",
    version="0.0.1",
    author="Andre Vieira da Silva",
    author_email="andsilvadrcc@gmail.com",
    description="An easy way to use the command line interface of a Python package",
    long_description="Command Line Interface for CLI",
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)