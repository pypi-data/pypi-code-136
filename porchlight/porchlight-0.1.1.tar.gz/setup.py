# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['porchlight', 'porchlight.tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'porchlight',
    'version': '0.1.1',
    'description': 'A function-managing package for models and systems with shared variables.',
    'long_description': "[porchlight](https://porchlight.readthedocs.io/en/latest/)\n==========\n\n`porchlight` is a function management suite that manages common inputs and\noutputs of methods and/or functions.\n\nThis package's original intent was to be a part of a modular scientific package\nyet to be released. Rather than isolating this method to a single model, the\nalready-developed work has been modified to stand alone as a package.\n\n`porchlight` does not have any dependencies outside of the standard CPython\nlibrary. Please note that `porchlight` requires Python 3.9\\+.\n\nInstallation\n------------\n\nYou can install `porchlight` by cloning this repository to a local directory,\nopening a command line, and running:\n```pip install porchlight```\n\nUsage\n-----\n\nThe main object used in `porchlight` is the `porchlight.Neighborhood` object.\nThis groups all functions together and keeps track of call order and\nparameters.\n\n```python\nimport porchlight\n\n\n# We call a porchlight.Neighborhood object to instantiate it with no functions\n# yet.\nneighborhood = porchlight.Neighborhood()\n\n# To add a function, we simply define it and pass it to porchlight.\ndef increment_x(x: int, y: int) -> int:\n    x = x * y\n    return x\n\nneighborhood.add_function(increment_x)\n\n# The neighborhood object inspects the function, finding input and output\n# variables if present. These are added to the collections of functions and\n# parameters.\nprint(neighborhood)  # porchlight.Neighborhood has a pretty-print string.\n```\n\nAlthough this is the current extent of documentation, there should be some more\ncomplete documentation within the next couple weeks/months.\n\nDocumentation\n-----------\n\nDocumentation for `porchlight` can be found on Read the Docs here: https://porchlight.readthedocs.io/en/latest/\n",
    'author': 'Teal, D',
    'author_email': 'teal.dillon@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
