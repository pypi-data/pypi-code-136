# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['param']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0', 'roster>=0.1.8,<0.2.0']

setup_kwargs = {
    'name': 'tombulled-param',
    'version': '0.1.9',
    'description': 'Enhanced function parameters',
    'long_description': '# param\nEnhanced function parameters\n\n## Installation\n```console\npip install git+https://github.com/tombulled/param.git@main\n```\n\n## Usage\n### Functions\nThe `@params` annotation works seamlessly with functions:\n```python\nfrom param import Param, params\n\n@params\ndef get(url: str, params: dict = Param(default_factory=dict)):\n    print("GET", url, params)\n```\n```python\n>>> get("https://httpbin.com/get")\nGET https://httpbin.com/get {}\n```\n\n### Classes\nThe `@params` annotation also works seamlessly with classes. Importantly, the `@params` annotation should be specified before `@staticmethod` or `@classmethod`.\n```python\nfrom param import Param, params\n\nclass MyClass:\n    @params\n    def get(self, url: str, params: dict = Param(default_factory=dict)):\n        print("GET", url, params)\n\n    @classmethod\n    @params\n    def post(cls, url: str, params: dict = Param(default_factory=dict)):\n        print("POST", url, params)\n\n    @staticmethod\n    @params\n    def put(url: str, params: dict = Param(default_factory=dict)):\n        print("PUT", url, params)\n```\n```python\n>>> obj = MyClass()\n>>>\n>>> obj.get("https://httpbin.com/get")\nGET https://httpbin.com/get {}\n>>>\n>>> obj.post("https://httpbin.com/post")\nPOST https://httpbin.com/post {}\n>>> MyClass.post("https://httpbin.com/post")\nPOST https://httpbin.com/post {}\n>>>\n>>> obj.put("https://httpbin.com/put")\nPUT https://httpbin.com/put {}\n>>> MyClass.put("https://httpbin.com/put")\nPUT https://httpbin.com/put {}\n```',
    'author': 'Tom Bulled',
    'author_email': '26026015+tombulled@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/param/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
