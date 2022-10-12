# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['data_detective_airflow',
 'data_detective_airflow.dag_generator',
 'data_detective_airflow.dag_generator.dags',
 'data_detective_airflow.dag_generator.results',
 'data_detective_airflow.dag_generator.works',
 'data_detective_airflow.operators',
 'data_detective_airflow.operators.extractors',
 'data_detective_airflow.operators.sinks',
 'data_detective_airflow.operators.transformers',
 'data_detective_airflow.test_utilities',
 'data_detective_airflow.utils']

package_data = \
{'': ['*']}

install_requires = \
['apache-airflow-providers-amazon',
 'apache-airflow-providers-celery',
 'apache-airflow-providers-postgres',
 'apache-airflow-providers-redis',
 'apache-airflow-providers-ssh',
 'apache-airflow>=2.4,<2.5',
 'pandas>=1.1,<1.6',
 'petl>=1.7,<2.0']

setup_kwargs = {
    'name': 'data-detective-airflow',
    'version': '2.1.0',
    'description': 'Framework with task testing over Apache Airflow',
    'long_description': '## Data Detective Airflow\n\n[Data Detective Airflow](https://github.com/tinkoff/data-detective/tree/master/data-detective-airflow) is a framework\nwhose main idea is to add the concepts of work and result to [Apache Airflow](https://airflow.apache.org/).\nIt supports tasks testing over [Apache Airflow](https://airflow.apache.org/).\nData Detective Airflow allows developers to create workflows in the form of directed acyclic graphs (DAGs) of tasks.\nThe easy-to-use Data Detective Airflow scheduler makes it possible to run tasks and save results into works. \nWork storage support for s3, ftp, local disk and database is also included.\n\n[More information about Data Detective Airflow](https://data-detective.dev/docs/data-detective-airflow/intro)\n\n## Installation\n\n#### Install from [PyPi](https://pypi.org/project/data-detective-airflow/)\n\n```bash\npip install data-detective-airflow\n```\n\nSee example DAG-s in [dags/dags](https://github.com/tinkoff/data-detective/tree/master/data-detective-airflow/dags/dags) folder.\n',
    'author': 'Tinkoff Data Detective Team',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
