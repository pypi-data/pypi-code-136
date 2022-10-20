# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rbwr']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rbwr',
    'version': '0.1.0',
    'description': 'Rather be writing Rust',
    'long_description': '# `rbwr`\n\nRather be writing Rust\n\n---\n\nA small Python library providing sum types that play well with existing\ntypechecking PEPs and should work out-of-the-box with any good typechecker,\nsuch as Pyright.\n\nTo see how this scheme for encoding sum types was conceived, check out [this\nblog post][blog_post].\n\n[blog_post]: http://charles.page.computer.surgery/blog/python-has-sum-types.html\n',
    'author': 'Charles Hall',
    'author_email': 'charles@computer.surgery',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://or.computer.surgery/charles/rbwr',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
