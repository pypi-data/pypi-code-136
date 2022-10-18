# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['soloway_unofficial']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0', 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'soloway-unofficial',
    'version': '1.0.1',
    'description': 'Простейшая реализация SDK для https://dsp.soloway.ru/',
    'long_description': '# Soloway SDK (Unofficial)\n\nПростейшая реализация SDK для https://dsp.soloway.ru/\n\n### Реализованные методы\n* ``/login``\n* ``/whoami``\n* ``/clients/{clientGuid}/placements``\n* ``/placements_stat``\n* ``/placements/{placementGuid}/stat``\n\n## Установка\n```bash    \n    $ pip install soloway-unofficial\n```\n\n## Использование\n\n```python\nfrom soloway_unofficial import Client\n\nclient = Client("YOUR_LOGIN", "YOUR_PASSWORD")\n```    \n\nПолучение статистики размещений по всем кампаниям.\n* ``start_date — дата начала(включительно) периода в формате YYYY-MM-DD``\n* ``stop_date — дата конца(включительно) периода, в формате YYYY-MM-DD``\n\n```python\ndata = client.get_placements_stat_all("START_DATE", "STOP_DATE")\n```    \nПолучение статистики размещений по выбранным кампаниям.\n* ``start_date — дата начала(включительно) периода в формате YYYY-MM-DD``\n* ``stop_date — дата конца(включительно) периода, в формате YYYY-MM-DD``\n\n```python\ndata = client.get_placements_stat(list["PLACEMENT_ID"],"START_DATE", "STOP_DATE")\n```    \n\nПолучение статистики по всем кампаниям по дням.\n* ``start_date — дата начала(включительно) периода в формате YYYY-MM-DD``\n* ``stop_date — дата конца(включительно) периода, в формате YYYY-MM-DD``\n\n```python        \ndata = client.get_placements_stat_by_day("START_DATE", "STOP_DATE")\n```\n\nПолучение статистики по выбранной кампании по дням.\n* ``start_date — дата начала(включительно) периода в формате YYYY-MM-DD``\n* ``stop_date — дата конца(включительно) периода, в формате YYYY-MM-DD``\n\n```python        \ndata = client.get_placement_stat_by_day("PLACEMENT_ID", "START_DATE", "STOP_DATE")\n```',
    'author': 'viktor',
    'author_email': 'vi.dave@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ZFullio/soloway-unofficial',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
