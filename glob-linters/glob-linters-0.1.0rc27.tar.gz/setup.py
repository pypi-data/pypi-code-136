#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md", encoding="utf-8") as changelog_file:
    changelog = changelog_file.read()

setup_requirements = ["setuptools_scm"]

requirements = [
    "clang-format>=14.0.6",
    "cpplint>=1.6.1",
    "pylint>=2.15.2",
    "flake8>=5.0.4",
    "black>=22.8.0",
    "isort>=5.10.1",
    "mypy>=0.971",
]

test_requirements = [
    "pytest>=3",
]


def _local_scheme(version: str) -> str:  # pylint: disable=unused-argument
    """Adjust local version

    Parameters
    ----------
    version : str
        Version string

    Returns
    -------
    str
        Adjusted version
    """
    return ""


setup(
    author="Bowen Tan",
    author_email="bowentan78@gmail.com",
    setup_requires=setup_requirements,
    use_scm_version={"local_scheme": _local_scheme},
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Integrated tool for multi-language linters for command line tool"
    "and GitHub action",
    entry_points={
        "console_scripts": [
            "glob-linters=glob_linters.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + changelog,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="glob-linters",
    name="glob-linters",
    packages=find_packages(include=["glob_linters", "glob_linters.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/bowentan/glob-linters",
    version="0.1.0-rc.27",
    zip_safe=False,
)
