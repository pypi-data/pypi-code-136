# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypgsync', 'pypgsync.mode', 'pypgsync.util']

package_data = \
{'': ['*']}

install_requires = \
['coverage-badge>=1.1.0,<2.0.0',
 'psycopg[binary]>=3.1.2,<4.0.0',
 'pytest-cov>=3.0.0,<4.0.0']

setup_kwargs = {
    'name': 'pypgsync',
    'version': '1.2.0',
    'description': '',
    'long_description': '![test-badge](https://github.com/danielschweigert/pypgsync/actions/workflows/lint-and-test.yml/badge.svg)\n\n[//]: # (![coverage-badge]&#40;https://raw.githubusercontent.com/danielschweigert/pypgsync/main/coverage-manual.svg&#41;)\n\n# pypgsync\nPython utility to sync two postgresql databases\n\n\n## Installation\n\n```bash\npip install pypgsync\n```\n\n## Usage\nGiven two databases, pypgsync can determine which records differ. In the `primarykey` use case, \nrecords are identified by their primary key.\n```python\nimport psycopg\nfrom pypgsync.mode.primarykey import delta_by_primary_key, apply_delta_by_primary_key\n\ncon_source = psycopg.connect(host="host_source", dbname="db_source", user="user_source", \n                             password="secret_source")\ncon_destination = psycopg.connect(host="host_destination", dbname="db_destination", \n                                  user="user_destination", password="secret_destination")\n\ncur_source = con_source.cursor()\ncur_destination = con_destination.cursor()\n\ndelta = delta_by_primary_key(cur_source=cur_source, cur_destination=cur_destination,\n                                 table_name="products", primary_key="id",\n                                 columns=["name", "count", "price"], pk_values=[1, 2, 3, 4, 5],)\n```\n`delta` provides an overview of the differences between the two database tables, in terms of which \ndatabase operations (`delete`, `insert`, `update`) have to be applied to the destination database \nin order to match the source database. The primary key identifies the rows that have to be modified.\n```console\n{\n    "table_name": "products",\n    "primary_key": "id",\n    "intersection": set([1, 2]),\n    "delete": set([3, ]),\n    "insert": [{"id": 5, "name": "bread", "count": 5, "price": 3.2}],\n    "update": [{"id": 2, "count": 20}, ]\n}\n```\n`delta` can then be used to apply the necessary changes to the destination database.\n```python\nfrom pypgsync.mode.primarykey import apply_delta_by_primary_key\n\napply_delta_by_primary_key(con_destination, delta)\n```\nAfter which the two database tables are identical within the column and primary key range specified.\n\nTo accomplish the sync in one step, use the `sync_by_primary_key` function.\n```python\nfrom pypgsync.mode.primarykey import sync_by_primary_key\nsync_by_primary_key(cur_source, con_destination, table_name="products", primary_key="id")\n```\n',
    'author': 'Daniel Schweigert',
    'author_email': 'dan.schweigert@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/danielschweigert/pypgsync',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
