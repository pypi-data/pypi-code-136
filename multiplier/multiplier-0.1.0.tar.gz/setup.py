from setuptools import setup, find_packages

from codecs import open 
from os import path 

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file 
with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    readme_description = f.read()
    
    
setup(
    name="multiplier",
    version="0.1.0",
    description="Multiplier library",
    long_description=readme_description,
    long_description_content_type="text/markdown",
    url="https://multiplier.readthedocs.io/",
    author="John Robert",
    author_email="condo@gmail.com",
    packages=["multiplier"],
    include_package_data=True,
    install_requires=["numpy"]
)