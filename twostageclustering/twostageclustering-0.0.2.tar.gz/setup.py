from setuptools import find_packages, setup
from pathlib import Path
import os

# The directory containing this file
HERE = Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name = "twostageclustering",
    version = "0.0.2",
    author = "Ishita Roy,  Rama Chaitanya Karanam",
    author_email = "ramachaitanya0@gmail.com",
    description = 'Multi Stage Clustering',
    long_description = README,
    long_description_content_type = 'text/markdown',
    url = "https://github.com/ramachaitanya0/MultiStageClustering",

    classifiers = [ 
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ] ,
    
    package_dir={"":"multistageclustering"},
    license='MIT',
    # packages = ["MultiStageClustering"],
    install_requires = [ 'pandas>=1.2.0','numpy>=1.20.1','scikit-learn>=1.0.2']
)

