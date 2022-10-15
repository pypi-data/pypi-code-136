# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ctnx']

package_data = \
{'': ['*']}

extras_require = \
{'docs': ['Sphinx>=5.2.3,<6.0.0']}

setup_kwargs = {
    'name': 'chiecthuyenngoaixa',
    'version': '0.1.1',
    'description': 'An utility library for processing Vietnamese texts',
    'long_description': '# chiecthuyenngoaixa\n\n[![GitHub issues](https://img.shields.io/github/issues/IoeCmcomc/chiecthuyenngoaixa)](https://github.com/IoeCmcomc/chiecthuyenngoaixa/issues)\n[![GitHub license](https://img.shields.io/github/license/IoeCmcomc/chiecthuyenngoaixa)](https://github.com/IoeCmcomc/chiecthuyenngoaixa/blob/master/LICENSE)\n[![Documentation Status](https://readthedocs.org/projects/chiecthuyenngoaixa/badge/?version=latest)](https://chiecthuyenngoaixa.readthedocs.io/en/latest/?badge=latest)\n![PyPI](https://img.shields.io/pypi/v/chiecthuyenngoaixa)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/chiecthuyenngoaixa)\n\n**chiecthuyenngoaixa** is a Python library which provides functions and\nclasses for various tasks in _processing Vietnamese texts_, such as\nremoving diacritics, converting numbers to words, sorting strings,\nvalidations and more.\n\nThis library is written on pure Python with no dependencies. Python 3.8\nand above is supported.\n\n## Installation\n\nChiecthuyenngoaixa is available on\n[PyPI](https://pypi.org/project/chiecthuyenngoaixa/). Open a terminal or\n_Command Prompt_ (on Windows) and run the following command:\n\n``` console\npip install chiecthuyenngoaixa\n```\n\nIf you are using [Poetry](https://python-poetry.org/), use this instead:\n\n``` console\npoetry add chiecthuyenngoaixa\n```\n\n## Basic usage\n\nThe library will now be available as `ctnx` module (abbreviation of\n_chiecthuyenngoaixa_).\n\nSome commonly used functions and classes can be imported directly. For\nexample:\n\n- To convert Vietnamese text to ASCII-only text:\n\n```python\n>>> from ctnx import remove_diacritics\n>>> remove_diacritics("Đàn ong thấy cái lon thì bu vào.")\n\'Dan ong thay cai lon thi bu vao.\'\n```\n\n- To convert a number to Vietnamese text:\n\n```python\n>>> from ctnx import num_to_words\n>>> num_to_words(123456789021003.45)\n\'một trăm hai mươi ba nghìn tỉ bốn trăm năm mươi sáu tỉ bảy trăm tám mươi chín triệu không trăm hai mươi mốt nghìn không trăm linh ba phẩy bốn năm\'\n```\n\n- To sort Vietnamese texts:\n\n```python\n>>> from ctnx import ViSortKey\n>>> lines = [\'Hà Nam\', \'Hải Dương\', \'Hà Nội\', \'Hà Tĩnh\', \'Hải Phòng\', \'Hậu Giang\', \'Hoà Bình\', \'Hưng Yên\', \'Hạ Long\', \'Hà Giang\', \'Điện Biên\'\\]\n>>> sorted(lines, key=ViSortKey)\n[\'Điện Biên\', \'Hà Giang\', \'Hà Nam\', \'Hà Nội\', \'Hà Tĩnh\', \'Hải Dương\', \'Hải Phòng\', \'Hạ Long\', \'Hậu Giang\', \'Hoà Bình\', \'Hưng Yên\']\n```\n\nFor further usages, see the documentation, which is hosted on [chiecthuyenngoaixa.readthedocs.io](https://chiecthuyenngoaixa.readthedocs.io/en/latest/).\n',
    'author': 'IoeCmcomc',
    'author_email': '53734763+IoeCmcomc@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/IoeCmcomc/chiecthuyenngoaixa',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
