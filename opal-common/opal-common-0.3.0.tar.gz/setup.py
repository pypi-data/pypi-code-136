import os
from types import SimpleNamespace

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
root = os.path.abspath(os.path.join(here, "../../"))
project_root = os.path.normpath(os.path.join(here, os.pardir))

print(project_root)


def get_package_metadata():
    metadata = {}
    with open(os.path.join(here, "../__packaging__.py")) as f:
        exec(f.read(), metadata)
    return SimpleNamespace(**metadata)


def get_relative_path(path):
    return os.path.join(here, os.path.pardir, path)


def get_long_description():
    readme_path = os.path.join(root, "README.md")

    with open(readme_path, "r", encoding="utf-8") as fh:
        return fh.read()


def get_install_requires():
    """Gets the contents of install_requires from text file.

    Getting the minimum requirements from a text file allows us to pre-install
    them in docker, speeding up our docker builds and better utilizing the docker layer cache.

    The requirements in requires.txt are in fact the minimum set of packages
    you need to run OPAL (and are thus different from a "requirements.txt" file).
    """
    with open(os.path.join(here, "requires.txt")) as fp:
        return [
            line.strip() for line in fp.read().splitlines() if not line.startswith("#")
        ]


about = get_package_metadata()
common_install_requires = get_install_requires()

setup(
    name="opal-common",
    version=about.__version__,
    author="Or Weis, Asaf Cohen",
    author_email="or@permit.io",
    description="OPAL is an administration layer for Open Policy Agent (OPA), detecting changes"
    + " to both policy and data and pushing live updates to your agents. opal-common contains"
    + " common code used by both opal-client and opal-server.",
    long_description_content_type="text/markdown",
    long_description=get_long_description(),
    url="https://github.com/permitio/opal",
    license=about.__license__,
    packages=find_packages(include=("opal_common*",)),
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
    ],
    python_requires=">=3.7",
    install_requires=common_install_requires + about.get_install_requires(project_root),
)
