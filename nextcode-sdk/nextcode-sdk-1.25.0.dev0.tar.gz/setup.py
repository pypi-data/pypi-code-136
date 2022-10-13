# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nextcode',
 'nextcode.services',
 'nextcode.services.phenoteke',
 'nextcode.services.phenotype',
 'nextcode.services.pipelines',
 'nextcode.services.project',
 'nextcode.services.query',
 'nextcode.services.queryserver',
 'nextcode.services.workflow']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=1.7.1,<2.0.0',
 'PyYAML>=6.0,<7.0',
 'boto3>=1.24.89,<2.0.0',
 'hjson>=3.1.0,<4.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'requests>=2.28.1,<3.0.0']

extras_require = \
{'jupyter': ['pandas>=1.5.0,<2.0.0',
             'ipython>=8.5.0,<9.0.0',
             'termcolor>=2.0.1,<3.0.0',
             'tqdm>=4.64.1,<5.0.0',
             'ipywidgets>=8.0.2,<9.0.0',
             'plotly>=5.10.0,<6.0.0']}

setup_kwargs = {
    'name': 'nextcode-sdk',
    'version': '1.25.0.dev0',
    'description': 'Python SDK for Genuity Science Services',
    'long_description': '[![Latest version on\nPyPi](https://badge.fury.io/py/nextcode-sdk.svg)](https://badge.fury.io/py/nextcode-sdk)\n[![Build Status](https://api.travis-ci.org/wuxi-nextcode/nextcode-python-sdk.svg?branch=master)](https://travis-ci.org/wuxi-nextcode/nextcode-python-sdk)\n[![codecov](https://codecov.io/gh/wuxi-nextcode/nextcode-python-sdk/branch/master/graph/badge.svg)](https://codecov.io/gh/wuxi-nextcode/nextcode-python-sdk/branch/master)\n[![Supported Python\nversions](https://img.shields.io/pypi/pyversions/nextcode-sdk.svg)](https://pypi.org/project/nextcode-sdk/)\n[![Code style:\nblack](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n# nextcode Python SDK\n\nNextcode-sdk is a python package for interfacing with Wuxi Nextcode services.\n\n### Installation\n```bash\n$ pip install nextcode-sdk -U\n```\n\n```bash\n$ pip install nextcode-sdk[jupyter] -U\n```\n\n### Getting started\n\n```python\nimport nextcode\nclient = nextcode.Client(api_key="xxx")\nqry = client.service("query")\nqry.status()\nqry.get_queries()\nqry.get_query(query_id)\nqry.list_templates()\n\n```\n\n### Jupyter notebooks\n\nTo start using the python sdk in Jupyter Notebooks you will first need to install it using the `jupyter` extras and then load the gor `%` magic extension.\n\n```bash\n! pip install nextcode-sdk[jupyter] -U\n%load_ext nextcode\n```\n\nJupyter notebooks running on the Wuxi Nextcode servers are preconfigured with a `GOR_API_KEY` and `GOR_PROJECT`. If you are running outside such an environment you will need to configure your environment accordingly:\n```bash\n%env GOR_API_KEY="***"\n%env GOR_API_PROJECT="test_project"\n# optionally set the LOG_QUERY environment variable to get more information about running queries.\n%env LOG_QUERY=1\n```\n\nNow you can run gor with the following syntax:\n```python\n# simple one-liner\n%gor gor #dbsnp# | top 100\n\n# one-liner which outputs to local variable as a pandas dataframe\nresults = %gor gor #dbsnp# | top 100\n\n# multi-line statement\n%%gor \ngor #dbsnp# \n  | top 100\n\n# multi-line statement which writes results into project folder\n%%gor user_data/results.tsv <<\nnor #dbsnp# \n  | top 100\n\n# output results to local variable as a pandas dataframe\n%%gor myvar <<\nnor #dbsnp# \n  | top 100\n\n# read from a pandas dataframe in a local variable\n%%gor\nnor [var:myvar] \n  | top 100\n\n# reference a local variable\nnum = 10\n%%gor\nnor [var:myvar] \n  | top $num\n\n```\n',
    'author': 'WUXI NextCODE',
    'author_email': 'support@wuxinextcode.com',
    'maintainer': 'Genuity Science Software Development',
    'maintainer_email': 'sdev@genuitysci.com',
    'url': 'https://www.github.com/wuxi-nextcode/nextcode-python-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
