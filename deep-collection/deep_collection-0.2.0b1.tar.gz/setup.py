# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deep_collection']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'deep-collection',
    'version': '0.2.0b1',
    'description': 'Easy access to items in deep collections.',
    'long_description': '## DeepCollection\n\n[![PyPI version](https://badge.fury.io/py/deep-collection.svg)](https://pypi.org/project/deep-collection/)\n<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n\ndeep_collection is a Python library that provides tooling for easy access to deep collections (dicts, lists, deques, etc), while maintaining a great portion of the collection\'s original API. The class DeepCollection class will automatically subclass the original collection that is provided, and add several quality of life extensions to make using deep collections much more enjoyable.\n\nGot a bundle of JSON from an API? A large Python object from some data science problem? Some very lengthy set of instructions from some infrastructure as code like Ansible or SaltStack? Explore and modify it with ease.\n\nDeepCollection can take virtually any kind of object including all built-in iterables, everything in the collections module, and [dotty-dicts](https://github.com/pawelzny/dotty_dict), and all of these nested in any fashion.\n\n### Features\n\n- Path traversal by supplying an list of path components as a key. This works for getting, setting, and deleting.\n- Setting paths when parent parts do not exist.\n- Path traversal through dict-like collections by dot chaining for getting\n- Finding all paths to fields\n- Finding all values for fields, and deduping them.\n- Provide all of the above through a class that is:\n    - easily instantiable\n    - a native subclass of the type it was instantiated with\n    - easily subclassable\n',
    'author': 'Joseph Nix',
    'author_email': 'nixjdm@terminallabs.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/terminal-labs/deep_collection',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
