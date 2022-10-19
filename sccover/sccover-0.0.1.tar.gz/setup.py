#!/usr/bin/env python3

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sccover",
    version="0.0.1",
    author="Aziz Fouché, Loïc Chadoutaud, Andrei Zinovyev (Institut Curie, Paris)",
    author_email="aziz.fouche@curie.fr",
    description="A toolbox for deterministic subsampling of single-cell data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Risitop/sccover",
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "anndata>=0.8.0",
        "numpy>=1.17",
        "pynndescent",
        "scanpy",
        "scikit-learn",
        "scipy",
    ],
    python_requires=">=3.9",
)
