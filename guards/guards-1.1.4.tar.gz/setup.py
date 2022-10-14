# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['guards']

package_data = \
{'': ['*']}

install_requires = \
['typing-inspect>=0.8.0,<0.9.0']

setup_kwargs = {
    'name': 'guards',
    'version': '1.1.4',
    'description': 'Tools for guarding Defaults, Null and creating Singletons.',
    'long_description': "![PythonSupport](https://img.shields.io/static/v1?label=python&message=%203.8|%203.9|%203.10&color=blue?style=flat-square&logo=python)\n![PyPI version](https://badge.fury.io/py/guards.svg)\n\n\n\n# Overview\n\nVarious objects that allow for sentinel-like singleton guards for various purposes, including:\n\n- Ones pre-defined in this library:\n  - Default\n  - Null\n- Also, Easily create your own custom singletons/sentinels types.\n\n**[📄 Detailed Documentation](https://xyngular.github.io/py-guards/latest/)** | **[🐍 PyPi](https://pypi.org/project/guards/)**\n\n# Install\n\n```bash\n# via pip\npip install guards\n\n# via poetry\npoetry add guards\n```\n\n# Quick Start\n\n```python\nfrom guards import Default\nimport os\n\ndef my_func(my_param = Default):\n    if my_param is Default:\n        # Resolve default value for parameter, otherwise None.\n        my_param = os.environ.get('MY_PARAM', None)\n    ...\n```\n\n# Licensing\n\nThis library is licensed under the MIT-0 License. See the LICENSE file.\n",
    'author': 'Josh Orr',
    'author_email': 'josh@orr.blue',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xyngular/py-guards',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
