from setuptools import setup, find_packages

VERSION = "1.3"
DESCRIPTION = "General structure optimizer leveraging AI."


with open("requirements.txt") as f:
    required = f.read().splitlines()

# Setting up
setup(
    name="aidev",
    version=VERSION,
    author="Massimo Brivio",
    author_email="brivio@radiate.ch",
    description=DESCRIPTION,
    packages=find_packages(where=".", include=["aidev*"]),
    long_description_content_type="text/markdown",
    long_description="AiDev is a Python library for dealing with structural optimization.",
    install_requires=required,
    url="https://github.com/radiate-engineering/AiDev",
)

# 1 python setup.py sdist bdist
# 2 twine upload --repository testpypi dist/*
# 3 twine upload dist/* --> only for final release
