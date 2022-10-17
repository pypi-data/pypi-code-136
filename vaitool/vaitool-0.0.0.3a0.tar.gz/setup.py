from setuptools import find_packages, setup

package_name = "vaitool"
version = "0.0.0.3a"

setup(
    name=package_name,
    version=version,
    python_requires=">=3.9, <4",
    packages=find_packages(),
    author="LinkerNetworks",
)
