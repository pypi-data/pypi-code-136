import os
import codecs
from setuptools import setup, find_packages

import build_django

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = build_django.__version__

AUTHOR = build_django.__author__

DESCRIPTION = 'Command line utility for building Django projects'

# Setting up
setup(
    name="build-django",
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    url='https://notabug.org/kapustlo/build-django',
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['python', 'django', 'build', 'cli', 'generate', 'code'],
    entry_points={
        'console_scripts': [
            'build-django=build_django.__main__:main'
        ]
    },
    classifiers=[
        "Framework :: Django",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Code Generators",
        "Environment :: Console",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.9",
        "Operating System :: POSIX :: Linux",
        "Natural Language :: English"
    ],
    python_requires=">=3.9",
    install_requires=(
        'django',
        'aiofiles'
    )
)


