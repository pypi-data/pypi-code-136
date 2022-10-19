# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['teachingtoolshed', 'teachingtoolshed.api', 'teachingtoolshed.gradebook']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.0,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'teaching-toolshed',
    'version': '0.0.95',
    'description': 'Helpful libraries for running classes',
    'long_description': '# Teaching Toolshed\n\nA library of useful classes for writing scripts related to managing classes. Has helper classes for talking to various teaching APIs and for compiling gradebooks in Python. \n\nSee [Teaching Toolshed Examples](https://github.com/hschafer/teaching-toolshed-examples) to see example scripts of how these libraries are used in my classes.\n\nAny questions or comments can be handled here on GitHub or you can email me at [hschafer@cs.washington.edu](mailto:hschafer@cs.washington.edu).\n\n## Publish New Version\n\nSee [here](https://realpython.com/pypi-publish-python-package/#publish-your-package-to-pypi)\n',
    'author': 'Hunter Schafer',
    'author_email': 'hschafer@uw.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
