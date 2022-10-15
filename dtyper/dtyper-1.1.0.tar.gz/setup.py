# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['dtyper']
install_requires = \
['typer']

setup_kwargs = {
    'name': 'dtyper',
    'version': '1.1.0',
    'description': '⌨️dtyper: Call typer commands or make dataclasses from them ⌨',
    'long_description': '⌨️dtyper: Call typer commands or make dataclasses from them ⌨️\n\nInstall using ``pip install dtyper``.\n\n``dtyper.function`` takes a ``typer`` command and returns a callable function\nwith the correct defaults.\n\n``dtyper.dataclass`` is a decorator that takes a ``typer`` command and makes a\ndataclass from it, wrapping either a function or a callable class.\n\nSee ``test_dtyper.py`` for examples of use.\n',
    'author': 'Tom Ritchford',
    'author_email': 'tom@swirly.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
