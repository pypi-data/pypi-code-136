from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-test-hg",
    version="0.0.1",
    author="Hugo",
    description="Passo a passo passado por Karina Kato.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/htonioni/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
