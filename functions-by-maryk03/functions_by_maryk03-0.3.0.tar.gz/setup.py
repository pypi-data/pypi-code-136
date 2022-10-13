# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_maryK03']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-maryk03',
    'version': '0.3.0',
    'description': 'This is our test project',
    'long_description': '# Instractions\n\n#### This is our test project\n#### Please install this package\n```\npip install function-by-maryK03\n```\n\n\n\n#### You can also install older packages\n```\npip install function-by-maryK03=VERSION_NUMBER\n```',
    'author': 'Maryna Kozak',
    'author_email': 'marykozak750@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
