# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starception']

package_data = \
{'': ['*'], 'starception': ['templates/*']}

install_requires = \
['Jinja2>=3,<4',
 'MarkupSafe>=2,<3',
 'starlette>=0,<1',
 'typing_extensions>=4.4,<5.0']

setup_kwargs = {
    'name': 'starception',
    'version': '0.5.4',
    'description': 'Beautiful debugging page for Starlette apps.',
    'long_description': "# Starception\n\nBeautiful exception page for Starlette and FastAPI apps.\n\n![PyPI](https://img.shields.io/pypi/v/starception)\n![GitHub Workflow Status](https://img.shields.io/github/workflow/status/alex-oleshkevich/starception/Lint%20and%20test)\n![GitHub](https://img.shields.io/github/license/alex-oleshkevich/starception)\n![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/starception)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/starception)\n![GitHub Release Date](https://img.shields.io/github/release-date/alex-oleshkevich/starception)\n\n## Installation\n\nInstall `starception` using PIP or poetry:\n\n```bash\npip install starception\n# or\npoetry add starception\n```\n\n### With syntax highlight support\n\nIf you want to colorize code snippets, install `pygments` library.\n\n```bash\npip install starception[pygments]\n# or\npoetry add starception -E pygments\n```\n\n## Screenshot\n\n![image](screenshot.png)\n\n## Features\n\n* secrets masking\n* solution hints\n* code snippets\n* display request info: query, body, headers, cookies\n* session contents\n* request and app state\n* platform information\n* environment variables\n* syntax highlight\n* open paths in editor (vscode only)\n* exception chains\n* dark theme\n\nThe middleware will automatically mask any value which key contains `key`, `secret`, `token`, `password`.\n\n## Quick start\n\nSee example application in [examples/](examples/) directory of this repository.\n\n## Usage\n\nStarception will work only in debug mode so don't forget to set `debug=True` for local development.\n\n### Monkey patching Starlette\n\nTo replace built-in debug exception handler call `install_error_handler` before you create Starlette instance.\n> Currently, this is a recommended approach.\n\n```python\nfrom starception import install_error_handler\nfrom starlette.applications import Starlette\n\ninstall_error_handler()\napp = Starlette()\n```\n\n### Using middleware\n\nTo render a beautiful exception page you need to install a `StarceptionMiddleware` middleware to your application.\n\n\n> Note, to catch as many exceptions as possible the middleware has to be the first one in the stack.\n\n```python\nimport typing\n\nfrom starlette.applications import Starlette\nfrom starlette.middleware import Middleware\nfrom starlette.requests import Request\nfrom starlette.routing import Route\n\nfrom starception import StarceptionMiddleware\n\n\nasync def index_view(request: Request) -> typing.NoReturn:\n    raise TypeError('Oops, something really went wrong...')\n\n\napp = Starlette(\n    debug=True,\n    routes=[Route('/', index_view)],\n    middleware=[\n        Middleware(StarceptionMiddleware),\n        # other middleware go here\n    ],\n)\n```\n\n### Integration with FastAPI\n\nAttach `StarceptionMiddleware` middleware to your FastAPI application:\n\n```python\nimport typing\n\nfrom fastapi import FastAPI, Request\n\nfrom starception import StarceptionMiddleware\n\napp = FastAPI(debug=True)\napp.add_middleware(StarceptionMiddleware)  # must be the first one!\n\n\n@app.route('/')\nasync def index_view(request: Request) -> typing.NoReturn:\n    raise TypeError('Oops, something really went wrong...')\n```\n\n### Integration with other frameworks\n\n`starception` exports `starception.exception_handler(request, exc)` function, which you can use in your\nframework.\nBut keep in mind, Starlette will [not call](https://github.com/encode/starlette/issues/1802) any custom exception\nhandler\nin debug mode (it always uses built-in one).\n\nThe snipped below will not work as you expect (unfortunately).\n\n```python\nfrom starlette.applications import Starlette\n\nfrom starception import exception_handler\n\napp = Starlette(\n    debug=True,\n    exception_handlers={Exception: exception_handler}\n)\n```\n\n## Solution hints\n\nIf exception class has `solution` attribute then its content will be used as a solution hint.\n\n```python\nclass WithHintError(Exception):\n    solution = (\n        'The connection to the database cannot be established. '\n        'Either the database server is down or connection credentials are invalid.'\n    )\n```\n\n![image](hints.png)\n\n## Opening files in editor\n\nSet your current editor to open paths in your editor/IDE.\n\n```python\nfrom starception import set_editor\n\nset_editor('vscode')\n```\n\n![image](link.png)\n\n\n> Note, currently only VSCode supported. If you know how to integrate other editors - please PR\n\n### Registering link templates\n\nIf your editor is not supported, you can add it by calling `add_link_template` and then selecting it with `set_editor`.\n\n```python\nfrom starception import set_editor, add_link_template\n\nadd_link_template('vscode', 'vscode://file/{path}:{lineno}')\nset_editor('vscode')\n```\n\n## Dark theme\n\nSwitch between light/dark themes using `set_theme` utility.\n> Currently, we use `pygments` for syntax highlighting, therefore theme must be set in the code.\n> In future releases we may highlight code on client side, and then we can make Starception to follow your browser's\n> theme.\n\n```python\nfrom starception import set_theme\n\nset_theme('dark')\n```\n\n![image](dark.png)\n\n## Credentials\n\n* Look and feel inspired by [Phoenix Framework](https://www.phoenixframework.org/).\n",
    'author': 'Alex Oleshkevich',
    'author_email': 'alex.oleshkevich@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alex-oleshkevich/starception',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
