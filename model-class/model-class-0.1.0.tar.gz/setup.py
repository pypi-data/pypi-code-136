# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['model_class']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'model-class',
    'version': '0.1.0',
    'description': 'Decorators for property-based model classes',
    'long_description': '# Model Class Decorator Toolkit\n\nThese are some decorators that make life easier for property-based model classes.\nThe documentation will be improved soon. For now, look at the tests for how to use.\n',
    'author': 'Julian Heise',
    'author_email': 'jam.heise@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/juheise/model-class/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
