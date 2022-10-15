# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pnq',
 'pnq.__base',
 'pnq._itertools',
 'pnq._itertools._async',
 'pnq._itertools._sync',
 'pnq._itertools._sync_generate',
 'pnq.aio',
 'pnq.concurrent',
 'pnq.ds',
 'pnq.operators',
 'pnq.selectors',
 'pnq.types']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pnq',
    'version': '0.0.17',
    'description': '',
    'long_description': '# PNQ\n\n[![CI](https://github.com/sasano8/pnq/actions/workflows/test.yml/badge.svg)](https://github.com/sasano8/pnq/actions)\n[![pypi](https://img.shields.io/pypi/v/pnq.svg)](https://pypi.python.org/pypi/pnq)\n[![Downloads](https://pepy.tech/badge/pnq/month)](https://pepy.tech/project/pnq)\n\nPNQ is a Python implementation like Language Integrated Query (LINQ).\n\n!!! danger\n    PNQはベータ版です。\n\n    - 現在、ドキュメントとAPIが一致していません。\n    - ライブラリが十分な品質に到達するまで、頻繁に内部実装やAPIが更新される恐れがあります。\n    - 本番環境では利用しないでください。\n\n---\n\n\n## Features\n\n- コレクション操作に関する多彩な操作\n- アクセシブルなインタフェース\n- 型ヒントの活用\n- 非同期ストリームに対応\n\n## Similar tools\n\n- [PyFunctional](https://github.com/EntilZha/PyFunctional)\n- [linqit](https://github.com/avilum/linqit)\n- [python-linq](https://github.com/jakkes/python-linq)\n- [aioitertools](https://github.com/omnilib/aioitertools)\n- [asyncstdlib](https://github.com/maxfischer2781/asyncstdlib)\n- [asq](https://github.com/sixty-north/asq)\n\n## Documentation\n\n- See [documentation](https://sasano8.github.io/pnq/) for more details.\n\n## Dependencies\n\n- Python 3.8+\n\n## Installation\n\nInstall with pip:\n\n```shell\n$ pip install pnq\n```\n\n## Getting Started\n\n``` python\nimport pnq\n\nfor x in pnq.query([1, 2, 3]).map(lambda x: x * 2):\n    print(x)\n# => 2, 4, 6\n\npnq.query([1, 2, 3]).map(lambda x: x * 2).result()\n# => [2, 4, 6]\n\npnq.query([1, 2, 3]).filter(lambda x: x == 3).one()\n# => 2\n```\n\n``` python\nimport asyncio\nimport pnq\n\nasync def aiter():\n    yield 1\n    yield 2\n    yield 3\n\nasync def main():\n    async for x in pnq.query(aiter()).map(lambda x: x * 2):\n        print(x)\n    # => 2, 4, 6\n\n    await pnq.query(aiter()).map(lambda x: x * 2)\n    # => [2, 4, 6]\n\n    await pnq.query(aiter()).filter(lambda x: x == 3)._.one()\n    # => 3\n\nasyncio.run(main())\n```\n\n## release note\n\n### v0.0.1 (2021-xx-xx)\n\n* Initial release.\n',
    'author': 'sasano8',
    'author_email': 'y-sasahara@ys-method.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sasano8/pnq',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
