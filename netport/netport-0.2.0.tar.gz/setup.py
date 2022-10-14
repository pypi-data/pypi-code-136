# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netport']

package_data = \
{'': ['*']}

install_requires = \
['docopt>=0.6.2,<0.7.0',
 'fastapi>=0.85.0,<0.86.0',
 'loguru>=0.6.0,<0.7.0',
 'psutil>=5.9.2,<6.0.0',
 'redis>=4.3.4,<5.0.0',
 'requests>=2.28.1,<3.0.0',
 'uvicorn[standard]>=0.18.3,<0.19.0']

entry_points = \
{'console_scripts': ['netport = scripts.cli:main']}

setup_kwargs = {
    'name': 'netport',
    'version': '0.2.0',
    'description': 'Tool for managing resources on a remove machine using openapi',
    'long_description': '# Netport\n\nNetport is a resource management solution for single Unix machine. Netport manages the access to\ndifferent types ot resources on the OS that cannot be accessed by multiple users.\n\nToday Netport is capable to manage: ports, files, processes and network interfaces.\n\n# Installation\n\nNetport is a python module that communicates with a **Redis** database in order to hold and manage\nits resources.\n\n## Netport Server\n\n### pip install\n\nTo Install Netport, run the following command in your python virtual environment\n\n```sh\npip install netport\n```\n\n> ### development installation\n>\n> Clone this repository:\n> ```sh\n> git clone https://github.com/IgalKolihman/netport.git\n> ```\n> \n> then run:\n>\n> ```sh\n> pip install -r reguirements. ext\n> ```\n\n### installing the redis database\n\nNetport integrates with redis, so in order to be able to run the Netport server, a database must be\naccessible somewhere in the network.\n\nTo install and run a basic Redis database locally on your PC, run the following commands:\n\n```sh\nsudo apt install redis\nsystemctl start redis\n```\n\nIf Redis is already installed on the machine, run the following command to check the status of the\nprocess:\n\n```sh\nsystemctl status redis\n```\n\n## Netport Client\n\n### pip install\n\nInstall the package using pip:\n\n```sh\npip install NetportClient\n```\n\nThen import the package in your code:\n\n```python\nimport netport_client\n```\n\n# Running Server\n\nPlease follow the [installation procedure](#installation) for how to install the Netport server \nand then run the following command in your terminal:\n\n```sh\nnetport\n```\n\nAfter running, a link will appear in the terminal to the server\'s url. The API documentation will\nbe available at: "http://host_ip:port/docs"\n\n# Configuration\n\nWhen initialized, Netport tries to connect to the Redis database. Netport connects with his default\nvalues, but it is possible to change them.\n\nNetport will override its default values if specific environment variables are set. The following\ntable describes those variables and their purpose:\n\n| *Variable*         | **Description**                   | **Defanlt** |\n|--------------------|-----------------------------------|-------------|\n| NETPORT_REDIS_HOST | Redis\'s host name to connect      | 0.0.0.0     |\n| NETPORT_REDIS_PORT | Redis\'s DB port to connect        | 6379        |\n| NETPORT_REDIS_DB   | The DB number inside redis to use | 0           |\n',
    'author': 'Igal Kolihman',
    'author_email': 'igalk.spam@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/IgalKolihman/netport',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
