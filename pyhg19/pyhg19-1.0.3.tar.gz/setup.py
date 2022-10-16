import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyhg19',
    version='1.0.3',
    author='Anthony Aylward',
    author_email='aaylward@salk.edu',
    description='Utilities for working with human genome build hg19',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/aaylward/pyhg19',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=['pydbsnp'],
    include_package_data=True
)
