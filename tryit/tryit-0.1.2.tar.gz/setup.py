# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tryit']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tryit',
    'version': '0.1.2',
    'description': '',
    'long_description': '# Tryit\n\n## Description\n\nJust a decorator to handle exceptions. It maps Python Exceptions to specific callbacks.\n\n\n## Usage\n```python\nfrom tryit import tryit, ExceptionTarget\n\n@tryit(exceptions=[\n  ExceptionTarget(ZeroDivisionError, callback=lambda err: float("nan"))\n])\ndef divide(a: int, b: int) -> float:\n  return a/b\n\n\n\n```',
    'author': 'Mario A. Visca',
    'author_email': 'mvisca89@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
