from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="checksudoku",
    version="0.0.1",
    author="APSN4",
    author_email="arty.ar@mail.ru",
    description="Check if any NxN Sudoku is solved correctly in Python",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/APSN4/checksudoku",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
    ],
)