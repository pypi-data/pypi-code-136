# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from setuptools import setup, find_packages


def scm_version():
    def local_scheme(version):
        if version.tag and not version.distance:
            return version.format_with("")
        else:
            return version.format_choice("+{node}", "+{node}.dirty")
    return {
        "relative_to": __file__,
        "version_scheme": "guess-next-dev",
        "local_scheme": local_scheme
    }

# Don't seem to have much success with exclude parameter of find_packages()
_packages = list(filter(lambda pkg: pkg[:4] != "test", find_packages()))

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="c4m_pdk_sky130",
    use_scm_version=scm_version(),
    author="Staf Verhaegen",
    author_email="staf@fibraservi.eu",
    description="Sky130 as PDKMaster based PDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+",
    python_requires="~=3.6",
    setup_requires=["setuptools_scm"],
    install_requires=[
        "setuptools", "PySpice>=1.5",
        "PDKMaster~=0.3.0", "c4m-flexcell~=0.2.0", "c4m-flexio~=0.2.0", "c4m-flexmem==0.0.*"
    ],
    include_package_data=True,
    packages=_packages,
    project_urls={
        #"Documentation": "???",
        "Source Code": "https://gitlab.com/Chips4Makers/c4m-pdk-sky130",
        "Bug Tracker": "https://gitlab.com/Chips4Makers/c4m-pdk-sky130/issues",
    },
)
