import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lkcom",
    version="0.1.4",
    author="Lukas Kontenis",
    author_email="dse.ssd@gmail.com",
    description="A Python library of useful routines.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/lukaskontenis/lkcom/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'numpy', 'matplotlib>=2.1.0'
    ],
    python_requires='>=3.6'
)
