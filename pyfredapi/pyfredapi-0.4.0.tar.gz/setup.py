# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfredapi', 'pyfredapi.api', 'pyfredapi.api.utils']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.0,<2.0.0',
 'plotly>=5.10.0,<6.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.6.0,<13.0.0']

setup_kwargs = {
    'name': 'pyfredapi',
    'version': '0.4.0',
    'description': 'A fully featured FRED API client library for Python.',
    'long_description': '# pyfredapi - Python client for the Federal Reserve Economic Data (FRED) API\n<!-- badges: start -->\n\n[![PyPi Version](https://img.shields.io/pypi/v/pyfredapi.svg)](https://pypi.python.org/pypi/pyfredapi/)\n[![Supported Python Versions](https://img.shields.io/pypi/pyversions/pyfredapi)](https://pypi.python.org/pypi/pyfredapi)\n[![Documentation Status](https://readthedocs.org/projects/pyfredapi/badge/?version=latest)](https://pyfredapi.readthedocs.io/en/latest/?badge=latest)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n<!-- badges: end -->\n\n`pyfredapi` is a Python client for the [FRED API web service](https://fred.stlouisfed.org/docs/api/fred/). `pyfredapi` covers all the FRED api endpoints and can return data as a [pandas](https://pandas.pydata.org/) dataframe or json. Checkout the [docs](https://pyfredapi.readthedocs.io/en/latest/) to learn more.\n\n## Installation\n\n```bash\npip install pyfredapi\n```\n\n## Basic Usage\n\nBefore using `pyfredapi` and must have an API key to the FRED API web service. You can apply for [one for free](https://fred.stlouisfed.org/docs/api/api_key.html) on the FRED website.\n\nYou can either be set as the environment variable `FRED_API_KEY`, or pass it to the `api_key` parameters when initializing `pyfredapi`.\n\n```python\nfrom pyfredapi import FredSeries\n\n# api key set as environment variable\nclient = FredSeries()\n\n# api key passed to initializer\nclient = FredSeries(api_key = "my_api_key")\n\n# get GDP data\nclient.get_series("GDP")\n```\n',
    'author': 'Greg Moore',
    'author_email': 'gwmoore.career@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
