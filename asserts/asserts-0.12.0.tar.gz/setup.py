# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asserts']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'asserts',
    'version': '0.12.0',
    'description': 'Stand-alone Assertions',
    'long_description': 'Python Asserts\n==============\n\n[![License](https://img.shields.io/pypi/l/asserts.svg)](https://pypi.python.org/pypi/asserts/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/asserts)](https://pypi.python.org/pypi/asserts/)\n[![GitHub](https://img.shields.io/github/release/srittau/python-asserts/all.svg)](https://github.com/srittau/python-asserts/releases/)\n[![pypi](https://img.shields.io/pypi/v/asserts.svg)](https://pypi.python.org/pypi/asserts/)\n[![Travis CI](https://travis-ci.org/srittau/python-asserts.svg?branch=master)](https://travis-ci.org/srittau/python-asserts)\n\nStand-alone Assertions for Python\n\nThis package provides a few advantages over the assertions provided by\nunittest.TestCase:\n\n* Can be used stand-alone, for example:\n    * In test cases, not derived from TestCase.\n    * In fake and mock classes.\n    * In implementations as rich alternative to the assert statement.\n* PEP 8 compliance.\n* Custom stand-alone assertions can be written easily.\n* Arguably a better separation of concerns, since TestCase is responsible\n  for test running only, if assertion functions are used exclusively.\n\nThere are a few regressions compared to assertions from TestCase:\n\n* The default assertion class (`AssertionError`) can not be overwritten. This\n  is rarely a problem in practice.\n* asserts does not support the `addTypeEqualityFunc()` functionality.\n\nUsage:\n\n```python\n>>> from asserts import assert_true, assert_equal, assert_raises\n>>> my_var = 13\n>>> assert_equal(13, my_var)\n>>> assert_true(True, msg="custom failure message")\n>>> with assert_raises(KeyError):\n...     raise KeyError()\n```\n\nFailure messages can be customized:\n\n```python\n>>> assert_equal(13, 14, msg_fmt="{got} is wrong, expected {expected}")\nTraceback (most recent call last):\n  ...\nAssertionError: 14 is wrong, expected 13\n```\n',
    'author': 'Sebastian Rittau',
    'author_email': 'srittau@rittau.biz',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/srittau/python-asserts',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
