# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypipr']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=7.1.3,<8.0.0', 'pytz>=2022.4,<2023.0']

extras_require = \
{':sys_platform == "Linux"': ['getch>=1.0,<2.0']}

setup_kwargs = {
    'name': 'pypipr',
    'version': '0.1.11',
    'description': 'The Python Package Index Project',
    'long_description': '# About\nThe Python Package Index Project (pypipr)\n\n\n# Setup\nInstall with pip\n```\npython -m pip install pypipr\n```\n\nTest with\n```python\nfrom pypipr.pypipr import Pypipr\nPypipr.test_print()\n```\n\n\n# Pypipr Class\n`test_print()` memastikan module sudah terinstal dan dapat dijalankan\n```python\nfrom pypipr.pypipr import Pypipr\nPypipr.test_print()\n```\n\n\n# iconsole\n`@Log()` / `Log decorator` akan melakukan print ke console. Mempermudah pembuatan log karena tidak perlu mengubah fungsi yg sudah ada. Berguna untuk memberikan informasi proses program yg sedang berjalan.\n\n```python\nfrom pypipr.iconsole import log\n\n@log("Calling some function")\ndef some_function():\n    ...\n    return\n```\n\n\n`print_colorize()` print ke console dengan warna\n\n```python\nfrom pypipr.iconsole import print_colorize\nprint_colorize("Print some text")\n```\n\n\n`input_char()` meminta masukan satu huruf tanpa menekan enter. Char tidak ditampilkan.\n\n```python\nfrom pypipr.iconsole import input_char\ninput_char("Input Char without print : ")\n```\n\n\n`input_char()` meminta masukan satu huruf tanpa menekan enter. Char ditampilkan.\n\n```python\nfrom pypipr.iconsole import input_char_echo\ninput_char_echo("Input Char n : ")\n```\n\n\n# idatetime\n`datetime_now()` memudahkan dalam membuat tanggal dan waktu untuk suatu timezone\n\n```python\nfrom pypipr.idatetime import datetime_now\ndatetime_now("Asia/Jakarta")\ndatetime_now("GMT")\ndatetime_now("Etc/GMT+7")\n```\n\n\n# iconstant\n`WINDOWS` True apabila berjalan di platform Windows\n\n```python\nfrom pypipr.iconstant import WINDOWS\nprint(WINDOWS)\n```\n\n`LINUX` True apabila berjalan di platform Linux\n\n```python\nfrom pypipr.iconstant import LINUX\nprint(LINUX)\n```\n',
    'author': 'ufiapjj',
    'author_email': 'ufiapjj@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
