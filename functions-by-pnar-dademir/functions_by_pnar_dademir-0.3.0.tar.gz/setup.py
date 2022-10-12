# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_pnar_dademir']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-pnar-dademir',
    'version': '0.3.0',
    'description': 'This is our test project',
    'long_description': '# instructions\n\n#### This is our test project.\n#### Please install this package\n\n\npip install function-by-pnar_dademir\n\n\n\n#### You can also install older packages \n\npip install functions-by-pnar_dademir==VERSION_NUMBER\n',
    'author': 'Pinar Dasdemir',
    'author_email': 'pdasdemir49@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
