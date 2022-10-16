from os.path import dirname, join

from setuptools import find_packages, setup

setup(
    name="dememefy",
    version="1.2.4",
    url="https://github.com/pinktoxin/dememefy",
    description="dememefy - make pics fun again",
    packages=["dememefy"],
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        "toml",
        "pillow",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "dememefy = dememefy.cli:main",
        ],
    }
)
