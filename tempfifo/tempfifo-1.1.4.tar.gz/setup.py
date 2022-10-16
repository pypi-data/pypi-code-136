import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tempfifo',
    version='1.1.4',
    author='Anthony Aylward',
    author_email='aaylward@salk.edu',
    description='This module creates temporary named pipes',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/aaylward/tempfifo',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
