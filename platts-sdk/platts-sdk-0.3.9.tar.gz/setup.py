# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['platts_sdk']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.10.0,<23.0.0',
 'cachetools==4.2.4',
 'pandas==1.3.5',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'platts-sdk',
    'version': '0.3.9',
    'description': '',
    'long_description': '# Platts Python SDK\n\nConsuming the Platts API in Python\n\n## Installation\n\n`pip install platts-sdk`\n\n## Getting Started\n\n```python\nimport platts_sdk as platts\n\ntc = platts.TokenClient("username", "password", "apikey")\nmdd = platts.MarketData(tc)\n\nsym = ["PCAAS00", "PCAAT00"]\ncur_df = mdd.get_current_assessments(sym)\nprint(cur_df)\n\nmdc = "ET"\nmdc_df = mdd.get_current_assessments_by_mdc(mdc)\nprint(mdc_df)\n```\n',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
