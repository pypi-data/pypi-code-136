from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="ntrprtr",            
    version="1.1.0",
    author="5f0",
    url="https://github.com/5f0ne/ntrprtr",
    description="Interpret bytes through different customizable actions",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    install_requires=[
        "cnvrtr==1.1.1"
    ],
     entry_points={
        "console_scripts": [
            "ntrprtr = ntrprtr.__main__:main"
        ]
    }
)
