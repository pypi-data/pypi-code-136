# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['radial']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'radial',
    'version': '0.1.0',
    'description': 'An intiutive interface for your requests in seconds',
    'long_description': '<br>\n<h1 align="center">\n💫 Radial\n</h1>\n<p align="center">\nAn intiutive interface for your requests in seconds\n</p>\n\n***\n\n**Radial abstracts painful low-levels request handling and presents a simple and intiutive interface to handle requests for your application.**\n\n## Example\n```py\n@radial("https://dog.ceo/api")\nclass Dog:\n    @get("/breeds/image/random")\n    def random(self, response):\n        return response.json()\n\ndog = Dog()\nrandom = dog.random()\nprint(random)\n```\n\nCurrently work in progress',
    'author': 'Shiv',
    'author_email': 'hello@shivs.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
