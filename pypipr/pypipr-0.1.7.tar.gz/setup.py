# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypipr']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=7.1.3,<8.0.0', 'pytz>=2022.4,<2023.0']

setup_kwargs = {
    'name': 'pypipr',
    'version': '0.1.7',
    'description': 'The Python Package Index Project',
    'long_description': '# About\nThe Python Package Index Project (pypipr)\n\n\n# Setup\nInstall with pip\n```\npython -m pip install pypipr\n```\n\nTest with\n```python\nfrom pypipr.pypipr import Pypipr\nPypipr.test_print()\n```\n\n\n# Feature\n\n## Pypipr Class\n`test_print()` memastikan module sudah terinstal dan dapat dijalankan\n```python\nfrom pypipr.pypipr import Pypipr\nPypipr.test_print()\n```\n\n\n## iconsole\n`@Log()` / `Log decorator` akan melakukan print ke console. Mempermudah pembuatan log karena tidak perlu mengubah fungsi yg sudah ada. Berguna untuk memberikan informasi proses program yg sedang berjalan.\n\n```python\nfrom pypipr.iconsole import log\n\n@log("Calling some function")\ndef some_function():\n    ...\n    return\n```\n\n\n## idatetime\n`datetime_now()` memudahkan dalam membuat tanggal dan waktu untuk suatu timezone\n\n```python\nfrom pypipr.idatetime import datetime_now\ndatetime_now("Asia/Jakarta")\n```\n',
    'author': 'ufiapjj',
    'author_email': 'ufiapjj@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
