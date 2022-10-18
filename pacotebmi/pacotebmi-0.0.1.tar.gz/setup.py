from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pacotebmi",
    version="0.0.1",
    author="Glauco Issamu Pereira Mori",
    author_email="glauco.mori@outlook.com",
    description="Package for individual Body Mass Index.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glaucomori/projetobmi",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)