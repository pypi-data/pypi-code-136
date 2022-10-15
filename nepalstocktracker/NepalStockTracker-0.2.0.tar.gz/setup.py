import re
import setuptools


# Get version number from __init__.py
with open('NepalStockTracker/__init__.py') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NepalStockTracker",
    version=version,
    author="ghanteyyy",
    author_email="ghanteyyy@gmail.com",
    description="Gets the market details of the provided company. Only for Nepal's stock market",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ghanteyyy/NepalStockTracker.git",
    packages=setuptools.find_packages(),
    install_requires=['beautifulsoup4', 'requests'],
    license='MIT',
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
