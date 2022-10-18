#!/usr/bin/env python

from distutils.core import setup
from os.path import dirname
import sys
sys.path.append(dirname(__file__))
from confluence_tool import __version__

setup(
    name='confluence-tool',
    version=__version__,
    description='Confluence API and CLI',
    author='Kay-Uwe (Kiwi) Lorenz',
    author_email='tabkiwi@gmail.com',
    install_requires=[
            'requests',
            'keyring',
            'keyrings.alt',
            'html5print',
            'pyquery',
            'pyaml',
            'pystache',
            'six',
            'argdeco',
            'lxml'
        ],
    extras_require={
        'docs':[
            'sphinx >= 1.4',
            'sphinx_rtd_theme',
            'sphinxcontrib-autoprogram'
            ]
        },
    url='https://github.com/klorenz/python-confluence-tool',
    packages=['confluence_tool', 'confluence_tool.cli', ],
    package_data = {
        'confluence_tool': ['templates/*.mustache', 'templates/*.html']
    },
    include_package_data = True,

    entry_points = dict(
        console_scripts = [
            'ct = confluence_tool.cli:main',
            'confluence-tool = confluence_tool.cli:main',
        ]
    ),
    license="MIT",
    )
