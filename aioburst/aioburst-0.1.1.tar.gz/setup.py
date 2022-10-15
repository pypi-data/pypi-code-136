# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioburst']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aioburst',
    'version': '0.1.1',
    'description': 'A library to limit async calls using a waterwheel approach to ensure calls maximize the rate limit.',
    'long_description': '# aioburst\nA library to limit async calls using a waterwheel approach to ensure calls maximize the rate limit. The library is extremely light, using only core python packages.\n\n## Usage\n\nInstall the package using pip:\n\n`pip install aioburst`\n\nImport the limiter:\n\n`from aioburst import limiter`\n\nThe package is purely functional, so there is no class to instantiate. `limiter` is used as a context manager:\n\n```\nasync with limiter(semaphore, period):\n    ...\n```\n\n`semaphore` is an instance of `asyncio.Semaphore` instantiated with a value equal to the number of simultanous calls that are allowed. Pass the `semaphore` instance to `limiter`. `period` is the period over which the number of calls are evaluated in seconds. For example, if you want to make 4 calls/second, you would pass in `semaphore=Semaphore(4)` and `period=1`.\n\n\n',
    'author': 'ericfeunekes',
    'author_email': 'ericwill.f@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
