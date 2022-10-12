from os import chdir, pardir
from os.path import join, exists, dirname, normpath, abspath
from setuptools import find_packages, setup

reqs_default = join(dirname(__file__), "requirements.txt")
required = []

if exists(reqs_default):
    with open(reqs_default) as f:
        required += f.read().splitlines()

with open(join(dirname(__file__), "README.md")) as f:
    long_desc = f.read()

# Allow setup.py to be run from any path
chdir(normpath(join(abspath(__file__), pardir)))

setup(
    name="gnss_models",
    version="0.1.4",
    description="Tool to generate and evaluate mathematical models from GNSS satellites u-center csv files",
    long_description=long_desc,
    author="Melvin Martins from NIST IT Lab",
    author_email="melvin.martins@nist.gov",
    url="https://github.com/MelvinMartins/gnss-models",
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
)
