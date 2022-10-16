# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bareasgi',
 'bareasgi.basic_router',
 'bareasgi.http',
 'bareasgi.lifespan',
 'bareasgi.middlewares',
 'bareasgi.websockets']

package_data = \
{'': ['*']}

install_requires = \
['bareutils>=4.0.0,<5.0.0', 'jetblack-asgi-typing>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'bareasgi',
    'version': '4.3.0',
    'description': 'A lightweight ASGI framework',
    'long_description': "# bareASGI\n\nA lightweight Python [ASGI](user-guide/asgi) web server framework\n(read the [docs](https://rob-blackbourn.github.io/bareASGI/)).\n\n## Overview\n\nThis is a _bare_ ASGI web server framework. The goal is to provide\na minimal implementation, with other facilities (serving static files, CORS,\nsessions, etc.) being implemented by optional packages.\n\nThe framework is targeted at micro-services which require a light footprint\n(in a container for example), or as a base for larger frameworks.\n\nPython 3.8+ is required.\n\n## Optional Packages\n\n- [bareASGI-cors](https://github.com/rob-blackbourn/bareASGI-cors) for cross origin resource sharing,\n- [bareASGI-static](https://github.com/rob-blackbourn/bareASGI-static) for serving static files,\n- [bareASGI-jinja2](https://github.com/rob-blackbourn/bareASGI-jinja2) for [Jinja2](https://github.com/pallets/jinja) template rendering,\n- [bareASGI-graphql-next](https://github.com/rob-blackbourn/bareASGI-graphql-next) for [GraphQL](https://github.com/graphql-python/graphql-core) and [graphene](https://github.com/graphql-python/graphene),\n- [bareASGI-rest](https://github.com/rob-blackbourn/bareASGI-rest) for REST support,\n- [bareASGI-prometheus](https://github.com/rob-blackbourn/bareASGI-prometheus) for [prometheus](https://prometheus.io/) metrics,\n- [bareASGI-session](https://github.com/rob-blackbourn/bareASGI-session) for sessions.\n\n## Functionality\n\nThe framework provides the basic functionality required for developing a web\napplication, including:\n\n- Http,\n- WebSockets,\n- Routing,\n- Lifecycle,\n- Middleware\n\n## Simple Server\n\nHere is a simple server with a request handler that returns some text.\n\n```python\nimport uvicorn\nfrom bareasgi import Application, HttpRequest, HttpResponse, text_writer\n\nasync def example_handler(request: HttpRequest) -> HttpResponse:\n    return HttpResponse(\n        200,\n        [(b'content-type', b'text/plain')],\n        text_writer('This is not a test')\n    )\n\napp = Application()\napp.http_router.add({'GET'}, '/', example_handler)\n\nuvicorn.run(app, port=9009)\n```\n",
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/bareasgi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
