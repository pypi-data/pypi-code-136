# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dop_library']

package_data = \
{'': ['*']}

install_requires = \
['apache-airflow-providers-google>=6,<7']

setup_kwargs = {
    'name': 'dop-library-dinigo',
    'version': '0.1.2',
    'description': 'This package contains all the utils and functions that are used in the DOP framework.',
    'long_description': "# DOP Library\n\nThis package contains all the utils and functions that are used in the DOP\nframework.\n\n\n## run_results_to_bq\nTakes a `run_results.json` file from either local storage or GCS and uploads it\nto a BigQuery table using the included\n[run_results table schema](/dop_library/run_results_table_schema.json).\n\nIt is important that the `run_results` table is created according to this\nschema. If the schema doesn't match, the insertion might fail silently.\n\n```python\nfrom dop_library import run_results_to_bq\n\nrun_results_to_bq(\n    run_results_path='gs://dbt-data/artifacts/run_results.csv',\n    dest_dataset_id='dop_test',\n    dest_table_id='run_results',\n)\n```\n\n",
    'author': 'Daniel Iñigo',
    'author_email': 'daniel.inigo@datatonic.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
