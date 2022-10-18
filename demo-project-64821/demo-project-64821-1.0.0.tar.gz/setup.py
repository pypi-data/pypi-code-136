import os

from setuptools import find_packages, setup

VERSION = "1.0.0"  # will be replaced by the version number during the build process


def get_readme() -> str:
    """Load the contents of the README file"""
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    with open(readme_path, "r") as f:
        return f.read()


def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="demo-project-64821",
    description="demo-project-64821",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    version=VERSION,
    packages=find_packages(include=["demo-project-64821"]),
    author="Maxim",
)
