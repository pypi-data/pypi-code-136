import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

import os
# Find the correct shared library file
library_file = None
for file in os.listdir("gcspy"):
    if file.endswith(".so"):
        library_file = file
if library_file is None:
    raise FileNotFoundError();

setuptools.setup(
    name="gcspy",
    version="0.0.2",
    author="Matthew McIlree",
    author_email="matthew.j.mcilree@gmail.com",
    description="Python bindings for the Glasgow Constraint Solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ciaranm/glasgow-constraint-solver",
    packages=['gcspy'],
    package_dir={'gcspy': 'gcspy'},
    package_data={'gcspy': [library_file]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)