# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_easy_cache']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fastapi-easy-cache',
    'version': '0.1.0',
    'description': 'A simple tool for caching fastapi response',
    'long_description': "# Fastapi easy cache\n\n<hr>\nAn easy to use tool for caching fastapi response\n\n### When should I use fastapi-easy-cache?\n1. Returning json serializable data\n2. Using GET method\n3. Returning dynamic but repeated data (like data refresh everyday)\n4. Don't have complicated requirements and too lazy to build a tool yourself\n\n### When should I NOT use fastapi-easy-cache?\n1. Returning not json serializable data (bytes, datetime, etc)\n2. Using POST method\n3. Returning frequently changing data (like data refresh every second)\n4. Need advanced features (recommend: [fastapi-cache](https://github.com/long2ice/fastapi-cache))\n\n<hr>\n\n## Installation\nWe recommend you have fastapi installed\n```shell\npip install fastapi-easy-cache\n```\n\n## Usage\n\n### Initializing\n\nThe following code will\n1. create a sqlite database in **dbPath**\n2. using peformance mode when calculating route identifier\n```python\nimport fastapi_easy_cache\n\nfastapi_easy_cache.apiCache(dbPath='cachedb/cache.db',\n                              peformance_or_capacity='peformance')\n```\n#### args\n    dbPath: path to sqlite database, expected str\n    peformance_or_capacity (optional): more peformance or capacity when calculating route id, epected 'peformance' or 'capacity'\n\n\n### Using\nYou just need to add `@cache(expire=20)` under fastapi route decorator, add flil in expire time and it's all done.\n\n`expire` is counted in second\n\n```python\nfrom fastapi_easy_cache import cache\n\n@app.get('/testCache/{path}')\n@cache(expire=20)\ndef test(path):\n    data = path\n    return data\n```\n\nWith GET route with arguments, you must add request: Request to your function\n```python\nfrom starlette.requests import Request\nfrom fastapi_easy_cache import cache\n\n@app.get('/testCacheWithArg/{path}')\n@cache(expire=20)\ndef testArg(path, arg1, arg2, request: Request):\n    data = {'path': path,\n         'arg1': arg1,\n         'arg2': arg2}\n    return data\n```",
    'author': 'dregg',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
