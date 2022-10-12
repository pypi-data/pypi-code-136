import setuptools
import yputils

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yputils",
    version=yputils.__version__,
    author="Ryan Lu",
    author_email="156704560@qq.com",
    description="Python code segment for self using.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/RyanLuDev/yputils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
