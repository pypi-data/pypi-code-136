# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['function_by_svetlanakoroleva']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'function-by-svetlanakoroleva',
    'version': '0.4.0',
    'description': 'This is our test project',
    'long_description': '# Instruction\n\n### This is our test project\n\n```\npip install function_by_svetlanakoroleva\n```\n\n### You can also install older versions\n\n```\npip install function_by_svetlanakoroleva\n```',
    'author': 'Svetlana Koroleva',
    'author_email': 'ksvetkaqt@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
