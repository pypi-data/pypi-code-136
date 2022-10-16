from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.5'
DESCRIPTION = 'Document based light weight NoSQL database.'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory /"touchdb" /"README.md").read_text()

#Setting up
setup(
    name = 'touchdb',
    version=VERSION,
    author = 'Kabilan Mahathevan',
    author_email = '<kabilanen@gmail.com>',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description = LONG_DESCRIPTION,
    packages = find_packages(),
    install_requires = [],
    keywords = ['touchdb', 'python', 'embedded database', 'nosql','document'],
    classifiers = [
        'Development Status :: 1 - Planning', 
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        ]
)
