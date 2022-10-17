#!/usr/bin/env python3

from setuptools import setup

setup(
    use_scm_version={
        "write_to": "src/thermometerb/version.py",
        "version_scheme": "post-release",
        "local_scheme": "no-local-version",
    },
    setup_requires=["setuptools_scm"],
)
