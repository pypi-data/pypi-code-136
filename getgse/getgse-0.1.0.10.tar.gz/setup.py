from setuptools import setup, find_packages
from io import open
from os import path
import pathlib
from getgse.__init__ import __version__

pname = "getgse"

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

VERSION = __version__

# automatically captured required modules for install_requires in requirements.txt and as well as configure dependency links
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]

dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]

setup (
    name = pname,
    description = '',
    version = VERSION,
    packages = find_packages(), # list of all packages
    install_requires = install_requires,
    python_requires='>=3.7', 
    author="William Jeong",
    author_email='wjd5480@gmail.com',
    entry_points='''
        [console_scripts]
        getgse=getgse.getgse:cli
    ''',
    # scruots=[pname],
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/Alopaxalgo/getGSE',
    keywords=pname,
    dependency_links=dependency_links,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ]
)