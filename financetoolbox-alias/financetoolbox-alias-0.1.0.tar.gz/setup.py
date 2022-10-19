import os
from setuptools import setup, find_namespace_packages

with open(os.path.join("src", "financetoolbox", "FTBX_ALIAS_VERSION"), "r") as file:
    version = file.read().strip()


setup(
    name="financetoolbox-alias",
    version=version,
    description="Financial Toolbox - Alias Extension",
    author="Rodrigo H. Mota",
    author_email="contact@rhdzmota.com",
    packages=find_namespace_packages(where="src"),
    package_dir={
        "": "src"
    },
)
