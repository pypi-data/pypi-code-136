
import setuptools
import re

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('pyfirth/pyfirth.py').read(),
    re.M).group(1)



with open("README.md", "r") as fh:
    long_description = fh.read()



setuptools.setup(
    name="pyfirth",
    version=version,
    author="David Blair",
    author_email="david.blair@ucsf.edu",
    description="A very simple, inefficient implemention of Firth-penalized Logistic Regression for rare event data.",
    long_description_content_type="text/markdown",
    url="https://github.com/daverblair/PyFirth",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'statsmodels',
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
