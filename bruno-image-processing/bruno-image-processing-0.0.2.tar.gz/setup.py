from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="bruno-image-processing",
    version="0.0.2",
    author="Bruno Carvalho",
    author_email="brunoandradecarvalho2@gmail.com",
    description="Pacote cirado com intruções da DIO",
    long_description=page_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
