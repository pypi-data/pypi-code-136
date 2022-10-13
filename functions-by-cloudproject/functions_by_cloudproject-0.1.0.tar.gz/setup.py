# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_cloudproject']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-cloudproject',
    'version': '0.1.0',
    'description': 'This is our test project',
    'long_description': '# python_class\n\nsource workspace/bin/activate\n',
    'author': 'Cloud',
    'author_email': 'cloudproject092022@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
