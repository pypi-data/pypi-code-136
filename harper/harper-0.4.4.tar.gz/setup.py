# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['harper', 'harper.audio', 'harper.io', 'harper.music']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.2,<2.0.0']

extras_require = \
{'graph': ['matplotlib>=3.5.1,<4.0.0'], 'sound': ['pyalsaaudio>=0.9.0,<0.10.0']}

setup_kwargs = {
    'name': 'harper',
    'version': '0.4.4',
    'description': 'Audio and music tools for python',
    'long_description': 'None',
    'author': 'Jim U',
    'author_email': 'jim.ulbright@tutanota.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
