import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='py1kgp',
    version='0.1.2',
    author='Anthony Aylward',
    author_email='aaylward@salk.edu',
    description='Utilities for working with 1000 Genomes data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/aaylward/py1kgp',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=['pyhg19']
)
