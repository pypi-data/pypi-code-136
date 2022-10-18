from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="imgpro",
    version="0.0.1",
    author="naniavalone",
    author_email="marianne.avalone@gmail.com",
    description="Image processing tool package",
    long_description=page_description,
    url="https://github.com/nanipumpkin/imgpro-pkg",
    packages=find_packages(),
    install_requires=[
        'matplotlib==3.6.1',
        'numpy==1.23.4', 
        'scikit-image==0.19.3'],
    python_requires=">=3.9"
)