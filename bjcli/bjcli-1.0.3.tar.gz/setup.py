import os
import codecs
from setuptools import setup, find_packages

from bjcli import __version__, __author__

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = __version__

AUTHOR = __author__

DESCRIPTION = 'Simple command line utility to run Bjoern WSGI'

# Setting up
setup(
    name="bjcli",
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    url="https://notabug.org/kapustlo/bjcli",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['python', 'bjoern', 'cli', 'bjoern-cli', 'wsgi'],
    entry_points={
        'console_scripts': [
            'bjcli=bjcli.__main__:main'
        ]
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Server",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Unix"
    ],
    python_requires=">=3.9",
    install_requires=[ 
        'bjoern'
    ]
)
