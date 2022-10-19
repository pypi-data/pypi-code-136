# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tesseract_olap',
 'tesseract_olap.backend',
 'tesseract_olap.backend.clickhouse',
 'tesseract_olap.common',
 'tesseract_olap.logiclayer',
 'tesseract_olap.query',
 'tesseract_olap.schema',
 'tesseract_olap.server']

package_data = \
{'': ['*']}

install_requires = \
['PyPika>=0.48.0,<1.0',
 'httpx>=0.18.0,<1.0',
 'immutables>=0.16,<1.0',
 'lxml>=4.6.0,<5.0.0',
 'orjson>=3.8.0,<4.0.0',
 'typing-extensions>=3.7.4']

extras_require = \
{'clickhouse': ['asynch>=0.2.1,<0.3.0']}

setup_kwargs = {
    'name': 'tesseract-olap',
    'version': '0.5.1',
    'description': 'A simple OLAP library.',
    'long_description': '<p>\n<a href="https://github.com/Datawheel/tesseract-python/releases"><img src="https://flat.badgen.net/github/release/Datawheel/tesseract-python" /></a>\n<a href="https://github.com/Datawheel/tesseract-python/blob/master/LICENSE"><img src="https://flat.badgen.net/github/license/Datawheel/tesseract-python" /></a>\n<a href="https://github.com/Datawheel/tesseract-python/"><img src="https://flat.badgen.net/github/checks/Datawheel/tesseract-python" /></a>\n<a href="https://github.com/Datawheel/tesseract-python/issues"><img src="https://flat.badgen.net/github/issues/Datawheel/tesseract-python" /></a>\n</p>\n\n## Installation\n\nBesides the main contents of the package, you can install the optional dependencies for the backend driver of your choice:\n\n* `tesseract-olap[clickhouse]`  \n  Installs the dependency needed to enable the use of the `tesseract_olap.backend.clickhouse` module.\n\n## Getting started\n\nIn its most basic form, the tesseract-olap package provides you with a way to translate OLAP-type queries into request statements that a data backend can understand and execute safely. The results obtained through the execution of server methods are python objects, and as such, can be used in any way the language allows.\n\n```python\n# example.py\n\nimport asyncio\n\nfrom tesseract_olap.backend.clickhouse import ClickhouseBackend\nfrom tesseract_olap import OlapServer\n\nbackend = ClickhouseBackend("clickhouse://user:pass@localhost:9000/database")\nserver = OlapServer(backend=backend, schema="./path/to/schema.xml")\n\nasync def get_data():\n    query = DataRequest.new("cube_name", {\n      "drilldowns": ["Time", "Country"],\n      "measures": ["Units", "Duration"],\n    })\n    # `result` is an `AsyncIterable` which outputs tidy-data row dictionaries\n    result = await server.execute(query)\n    # you can handle the result with `async for`\n    return tuple([item async for item in result])\n\nif __name__ == "__main__":\n    asyncio.run(get_data())\n```\n\nThe server instance can then be used in other programs as the data provider, for simple (like data exploration) and complex (like data processing) operations.\n\n---\n&copy; 2022 [Datawheel, LLC.](https://www.datawheel.us/)  \nThis project is licensed under [MIT](./LICENSE).\n',
    'author': 'Francisco Abarzua',
    'author_email': 'francisco@datawheel.us',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Datawheel/tesseract-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
