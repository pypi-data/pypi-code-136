# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['runtime_config',
 'runtime_config.entities',
 'runtime_config.enums',
 'runtime_config.libs',
 'runtime_config.sources']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp[speedups]>=3.8.1,<4.0.0', 'pydantic>=1.10.1,<2.0.0']

setup_kwargs = {
    'name': 'runtime-config-py',
    'version': '0.0.4',
    'description': 'Library for runtime updating project settings.',
    'long_description': "![license](https://img.shields.io/pypi/l/runtime-config-py?style=for-the-badge) ![python version](https://img.shields.io/pypi/pyversions/runtime-config-py?style=for-the-badge) [![version](https://img.shields.io/pypi/v/runtime-config-py?style=for-the-badge)](https://pypi.org/project/runtime-config-py/) [![coverage](https://img.shields.io/codecov/c/github/runtime-config/runtime-config-py/master?style=for-the-badge)](https://app.codecov.io/gh/runtime-config/runtime-config-py) [![tests status](https://img.shields.io/github/workflow/status/runtime-config/runtime-config-py/Tests/master?style=for-the-badge)](https://github.com/runtime-config/runtime-config-py/actions?query=branch%3Amaster) [![](https://img.shields.io/pypi/dm/runtime-config-py?style=for-the-badge)](https://pypi.org/project/runtime-config-py/)\n\nruntime-config-py\n=================\n\nThis library allows you to update project settings at runtime. In its basic use case, it is just a client for the\n[server](https://github.com/runtime-config/runtime-config), but if necessary, you can implement your adapter for the\ndesired source and get settings from them.\n\nruntime-config-py supports Python 3.8+.\n\nExamples of using:\n\n- Create feature flags to control which features are enabled for users. Feature flags are especially useful when the\nservice is based on a microservice architecture and the addition of a new feature affects multiple services.\n\n- Quick response to problems in project infrastructure. For example, if one of consumers sends too many requests to\nanother service, and you need to reduce its performance.\n\n\nTable of contents:\n\n- [Installation](#installation)\n- [Usage](#usage)\n- [Backend](#backend)\n- [Development](#development)\n  - [Tests](#tests)\n  - [Style code](#style-code)\n\n\n# Installation\n\nThis project can be installed using pip:\n\n```\npip install runtime-config-py\n```\n\nOr it can be installed directly from git:\n\n```\npip install git+https://github.com/runtime-config/runtime-config-py.git\n```\n\n# Usage\n\nLet's see a simple example of using this library together with aiohttp.\n\n```python\nfrom aiohttp import web\n\nfrom runtime_config import RuntimeConfig\nfrom runtime_config.sources import ConfigServerSrc\n\n\nasync def hello(request):\n    name = request.app['config'].name\n    return web.Response(text=f'Hello world {name}!')\n\n\nasync def init(application):\n    source = ConfigServerSrc(host='http://127.0.0.1:8080', service_name='hello_world')\n    config = await RuntimeConfig.create(init_settings={'name': 'Alex'}, source=source)\n    application['config'] = config\n\n\nasync def shutdown(application):\n    await application['config'].close()\n\n\napp = web.Application()\napp.on_startup.append(init)\napp.on_shutdown.append(shutdown)\napp.add_routes([web.get('/', hello)])\nweb.run_app(app, port=5000)\n```\n\nBefore running this code, you need to run [server](https://github.com/runtime-config/runtime-config) from which this\nlibrary can take new values for your variables.\nIf you don't do this, nothing bad will not happen. You simply cannot change the value of the name variable at runtime :)\n\n**Automatic source initialization**\n\nYou can simplify library initialization by automatically creating a source instance. Simply define the following\nenvironment variables and the source instance will be created automatically:\n\n- RUNTIME_CONFIG_HOST\n- RUNTIME_CONFIG_SERVICE_NAME\n\n**Ways to access settings**\n\nThis library supports several ways to access variables. All of them are shown below:\n\n```python\nprint(config.name)\nprint(config['name'])\nprint(config.get('name', default='Dima'))\n```\n\n# Backend\n\nCurrently, only 1 [backend](https://github.com/runtime-config/runtime-config) is supported. Later, support for other\nbackends, such as redis, will probably be added to the library, but this is not in the nearest plans.\n\nIf you need support for another settings storage source right now, you can write your own source. Implementing this is\nvery simple. You need to create a class that will be able to retrieve data from the desired source and will inherit\nfrom `runtime_config.sources.base.BaseSource`. After that, an instance of the class you created must be passed to\nthe `RuntimeConfig.create` method.\n\n```python\nyour_source = YourSource(...)\nconfig = await RuntimeConfig.create(..., source=your_source)\n```\n\n\n# Development\n\n## Tests\n\nCheck the work of the library on several versions of Python at once using the command below:\n\n```\nmake test\n```\n\n## Style code\n\nFor automatic code formatting and code verification, you need to use the command below:\n\n```\nmake lint\n```\n",
    'author': 'Aleksey Petrunnik',
    'author_email': 'petrunnik.a@gmail.com',
    'maintainer': 'Aleksey Petrunnik',
    'maintainer_email': 'petrunnik.a@gmail.com',
    'url': 'https://github.com/runtime-config/runtime-config-py',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
