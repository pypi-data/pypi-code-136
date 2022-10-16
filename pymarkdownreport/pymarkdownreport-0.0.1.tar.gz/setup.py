import distutils.text_file
from pathlib import Path
from typing import List

from setuptools import setup


def get_version(filename):
    import ast

    version = None
    with open(filename) as f:
        for line in f:
            if line.startswith("__version__"):
                version = ast.parse(line).body[0].value.s
                break
        else:
            raise ValueError("No version found in %r." % filename)
    if version is None:
        raise ValueError(filename)
    return version


def _parse_requirements(filename: str) -> List[str]:
    """Return requirements from requirements file."""
    return distutils.text_file.TextFile(filename=str(Path(__file__).with_name(filename))).readlines()


install_requires = _parse_requirements("requirements.txt")

module = "pymarkdownreport"
package = "pymarkdownreport"
src = "pymarkdownreport"

version = get_version(filename=f"{module}/__init__.py")

setup(
    name=package,
    packages=[module],
    version=version,
    license= 'MIT',
    author= 'Pietro Zullo',
    url = 'https://github.com/pietrozullo/pymarkdownreport',
    download_url = 'https://github.com/pietrozullo/pymarkdownreport/archive/refs/tags/v0.0.1.tar.gz',
    zip_safe=False,
    entry_points={
        "console_scripts": [
        ]
    },
    python_requires=">=3.8",  
    install_requires=install_requires,
)