# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['price2bq_zfullio']

package_data = \
{'': ['*']}

install_requires = \
['bq-easy-zfullio>=1,<2',
 'loguru>=0.6.0,<0.7.0',
 'openpyxl>=3.0.10,<4.0.0',
 'pandas>=1.4.3,<2.0.0',
 'python-dotenv>=0.21,<0.22',
 'xlrd>=2.0.1,<3.0.0']

setup_kwargs = {
    'name': 'price2bq-zfullio',
    'version': '1.0.0',
    'description': "Экспорт файлов c площадок 'Яндекс Недвижимость' и 'Циан' в BigQuery",
    'long_description': "# Price to BQ\n\nЭкспорт файлов с площадок 'Яндекс Недвижимость', 'Циан', 'Avito' в BigQuery",
    'author': 'viktor',
    'author_email': 'vi.dave@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
