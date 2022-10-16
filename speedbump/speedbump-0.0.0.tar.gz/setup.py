#!/usr/bin/env python
from setuptools import setup

NAME = "speedbump"
setup(
    name=NAME,
    use_scm_version={
        "local_scheme": "dirty-tag",
        "write_to": f"{NAME}/_version.py",
        "fallback_version": "0.0.0",
    },
    author="Ross Fenning",
    author_email="github@rossfenning.co.uk",
    packages=[NAME],
    package_data={NAME: ["py.typed"]},
    description="Fastest path to bump nirvana.",
    setup_requires=[
        "setuptools_scm>=3.3.1",
        "pre-commit",
    ],
    entry_points={"console_scripts": [f"speedbump = {NAME}.cli:main"]},
    install_requires=["PyGithub", "typer", "PyYAML"],
)
