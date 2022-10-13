# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['freezable']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'freezable',
    'version': '0.1.9',
    'description': 'Dynamically immutable objects',
    'long_description': '<a href="https://badge.fury.io/py/freezable"><img src="https://badge.fury.io/py/freezable.svg" alt="PyPI version" height="18"></a>\n<a href=\'https://python-freezable.readthedocs.io/en/stable/?badge=stable\'>\n    <img src=\'https://readthedocs.org/projects/python-freezable/badge/?version=stable\' alt=\'Documentation Status\' />\n</a>\n<a href="https://github.com/ederic-oytas/python-freezable/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/ederic-oytas/python-freezable"></a>\n\n# Freezable: Dynamically Immutable Objects\n\n> NOTICE: This project is in Alpha; you may encounter bugs.\n  \nFreezable is a package that allows you to implement "freezable" types in\nPython, which can either be "frozen" or "unfrozen." When frozen, all operations\nand methods that mutate the object are disabled.\n\nHere is an example of a "freezable" stack and its usage:\n```python\nfrom freezable import Freezable, FrozenError, enabled_when_unfrozen\n\nclass FreezableStack(Freezable):\n    \n    def __init__(self):\n        self._data = []  # data of the stack\n    \n    @enabled_when_unfrozen\n    def push(self, x):  # pushes to the top of stack\n        self._data.append(x)\n\n    def top(self):  # returns top of stack, if any\n        return self._data[-1] if self._data else None\n\n# We can use the stack as normal.\nstk = FreezableStack()\nassert stk.top() is None\nstk.push(1)\nassert stk.top() == 1\nstk.push(2)\nassert stk.top() == 2\n\n# Once we freeze it, all mutating methods/operations are disabled.\nstk.freeze()\ntry:\n    stk.push(3)  # error because stk is frozen\nexcept FrozenError:\n    pass\nassert stk.top() == 2  # push did not happen\n\n# We can unfreeze it to use the stack mutably again.\nstk.unfreeze()\nstk.push(3)\nassert stk.top() == 3\n```\n\nThis package can be useful in finding logical errors in which objects are\nmutated when they are not supposed to.\n\n## Links\n\n[Documentation @ReadTheDocs][docs-stable]\n(on most recent stable release)\n\n[PyPI Page][pypi]\n\n## Installation\n\nThis package can be installed using Pip:\n```\npip install freezable\n```\n\n## Bug Reports and Feature Requests\n\nYou can [report a bug or suggest a feature][issues] on the Github repo.\n\n## Contributions\n\nContributions to this project are welcome. :)\n\nSee the [pull requests page on Github][pulls].\n\n[docs-stable]: https://python-freezable.readthedocs.io/en/stable\n[pypi]: https://pypi.org/project/freezable/\n[issues]: https://github.com/ederic-oytas/python-freezable/issues/new/choose\n[pulls]: https://github.com/ederic-oytas/python-freezable/pulls\n',
    'author': 'Ederic Oytas',
    'author_email': 'edericoytas@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ederic-oytas/python-freezable',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
