# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ohmyadmin', 'ohmyadmin.ext']

package_data = \
{'': ['*'],
 'ohmyadmin': ['statics/*',
               'statics/build/*',
               'templates/ohmyadmin/*',
               'templates/ohmyadmin/images/*',
               'templates/ohmyadmin/list_page/*',
               'templates/ohmyadmin/metrics/*']}

install_requires = \
['Jinja2>=3.1,<4.0',
 'SQLAlchemy[mypy]>=1.4.35,<2.0.0',
 'WTForms>=3.0,<4.0',
 'python-multipart>=0.0.5,<0.0.6',
 'python-slugify>=6.1,<7.0',
 'starlette>=0.21,<0.22',
 'tabler-icons>=0.2,<0.3']

setup_kwargs = {
    'name': 'ohmyadmin',
    'version': '0.3.1',
    'description': 'Awesome admin panel for your business.',
    'long_description': '# OhMyAdmin\n\nAwesome admin panel for your business.\n\n![PyPI](https://img.shields.io/pypi/v/ohmyadmin)\n![GitHub Workflow Status](https://img.shields.io/github/workflow/status/alex-oleshkevich/ohmyadmin/Lint%20and%20test)\n![GitHub](https://img.shields.io/github/license/alex-oleshkevich/ohmyadmin)\n![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/ohmyadmin)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/ohmyadmin)\n![GitHub Release Date](https://img.shields.io/github/release-date/alex-oleshkevich/ohmyadmin)\n\n## Installation\n\nInstall `ohmyadmin` using PIP or poetry:\n\n```bash\npip install ohmyadmin\n# or\npoetry add ohmyadmin\n```\n\n## Features\n\n-   TODO\n\n## Quick start\n\nSee example application in `examples/` directory of this repository.\n',
    'author': 'Alex Oleshkevich',
    'author_email': 'alex.oleshkevich@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alex-oleshkevich/ohmyadmin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
