"""Module to setup library."""
from pathlib import Path
import codecs
from setuptools import setup


LIB_NAME = "arty_random_test_lib"
VERSION = "1.0.0"
DESCRIPTION = "Dummy utility library"

def strip_comments(line: str):
    """Remove comments from line."""
    return line.split("#", 1)[0].strip()

def _reqs(file_name: str):
    """Creates a list of requirements opening the file received as parameter.

    Args:
        file_name (str): Name of file at the same level as setup.py containing the list of reqs

    Returns:
        list: list of requirements
    """
    cwd_from_path = (Path.cwd()).joinpath(file_name)
    with cwd_from_path.open("r", encoding="utf") as reqs_file:
        reqs_list = [strip_comments(l) for l in reqs_file.readlines()]
        return [[r] for r in reqs_list if r]

def reqs(file_name: str):
    """Collect project requirements.

    Args:
        file_name (str): Name of file at the same level as setup.py containing the list of reqs

    Returns:
        list: List of requirements
    """
    return [req for subreq in _reqs(file_name) for req in subreq]

with codecs.open("README.md", "r", "utf-8") as fh:
    long_description = fh.read()

setup(
    name=LIB_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description_type="text/markdown",
    long_description=long_description,
    url="https://github.com/kenshinapa/GenericPythonLib.git",
    author="Arturo Padilla Ayala",
    author_email="r2padillaayala@gmail.com",
    packages=["arty_random_test_lib"],
    zip_safe=False,
    install_requires=reqs("requirements.txt"),
)
