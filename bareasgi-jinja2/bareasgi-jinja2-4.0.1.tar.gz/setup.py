# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bareasgi_jinja2']

package_data = \
{'': ['*']}

install_requires = \
['bareasgi>=4.0.0,<5.0.0', 'jinja2>=3.0,<4.0']

setup_kwargs = {
    'name': 'bareasgi-jinja2',
    'version': '4.0.1',
    'description': 'Jinja2 support for bareasgi',
    'long_description': '# bareASGI-jinja2\n\nJinja2 support for [bareASGI](http://github.com/rob-blackbourn/bareasgi)\n(read the [documentation](https://rob-blackbourn.github.io/bareASGI-jinja2/))\n\n## Usage\n\nTry the following.\n\n```python\nfrom typing import Mapping, Any\nimport jinja2\nimport os.path\nimport uvicorn\nfrom bareasgi import Application\nfrom bareasgi_jinja2 import Jinja2TemplateProvider, add_jinja2\n\nhere = os.path.abspath(os.path.dirname(__file__))\n\nasync def http_request_handler(request: HttpRequest) -> HttpResponse:\n    """Handle the request"""\n    template = \'example1.html\'\n    variables = {\'name\': \'rob\'}\n    return await Jinja2TemplateProvider.apply(request, template, variables)\n\napp = Application()\n\nenv = jinja2.Environment(\n    loader=jinja2.FileSystemLoader(os.path.join(here, \'templates\')),\n    autoescape=jinja2.select_autoescape([\'html\', \'xml\']),\n    enable_async=True\n)\n\nadd_jinja2(app, env)\n\napp.http_router.add({\'GET\'}, \'/example1\', http_request_handler)\n\nuvicorn.run(app, port=9010)\n\n```\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/bareasgi-jinja2',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
