# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_nomadstalker']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-nomadstalker',
    'version': '0.3.0',
    'description': 'This is our test project',
    'long_description': '# Instructions\n\n#### This is our test project.\n\n#### Please install this package\n```\npip install functions-by-nomadstalker\n```\n\n\n#### You can also install older packages\n```\npip install functions_by_nomadstalker==VERSION_NUMBER\n```',
    'author': 'Omurbek Orozaliev',
    'author_email': 'boexpresskg@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
