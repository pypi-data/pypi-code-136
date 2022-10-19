# coding: utf-8
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setupargs = {
    'name': 'nopea',
    'description': 'Provides an ORM for MySQL, PostgreSQL and SQLite.',

    'license': 'GPLv3',
    'version': '0.0.18',

    'packages': ['nopea', 'nopea.adaptors'],
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',

    'author': 'Christian Kokoska',
    'author_email': 'info@softcreate.de',
    'install_requires': [
        'colorama==0.3.9',
        'ipython'
    ],
}

if __name__ == '__main__':
    setup(**setupargs)
