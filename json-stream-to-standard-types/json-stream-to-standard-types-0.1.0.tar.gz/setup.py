# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['json_stream_to_standard_types']
install_requires = \
['json-stream>=1,<3']

setup_kwargs = {
    'name': 'json-stream-to-standard-types',
    'version': '0.1.0',
    'description': 'Convert json-stream objects to standard Python dicts and lists',
    'long_description': '# json-stream-to-standard-types\n\nUtility function to convert `json-stream` objects to normal Python dicts/lists.\n\nParallel PR: https://github.com/daggaz/json-stream/pull/17\n\n### Installation\n\n```bash\npip install json-stream-to-standard-types\n```\n\n### Usage\n\nTo convert a json-stream `dict`-like or `list`-like object and all its\ndescendants to a standard `list` and `dict`, simply appl apply library\'s\n`to_standard_types` function:\n\n```python\nimport json_stream\nfrom json_stream_to_standard_types import to_standard_types\n\n# JSON: {"round": 1, "results": [1, 2, 3]}\ndata = json_stream.load(f)\nresults = data["results"]\nprint(results)  # prints <TransientStreamingJSONList: TRANSIENT, STREAMING>\nconverted = to_standard_types(results)\nprint(converted)  # prints [1, 2, 3]\n```\n',
    'author': 'smheidrich',
    'author_email': 'smheidrich@weltenfunktion.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
