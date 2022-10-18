# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['expecttest']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'expecttest',
    'version': '0.1.4',
    'description': '',
    'long_description': '# expecttest [![PyPI version](https://badge.fury.io/py/expecttest.svg)](https://badge.fury.io/py/expecttest)\n\nThis library implements expect tests (also known as "golden" tests). Expect\ntests are a method of writing tests where instead of hard-coding the expected\noutput of a test, you run the test to get the output, and the test framework\nautomatically populates the expected output.  If the output of the test changes,\nyou can rerun the test with the environment variable `EXPECTTEST_ACCEPT=1` to\nautomatically update the expected output.\n\nSomewhat unusually, this library implements *inline* expect tests: that is to\nsay, the expected output isn\'t saved to an external file, it is saved directly\nin the Python file (and we modify your Python file when updating the expect\ntest.)\n\nThe general recipe for how to use this is as follows:\n\n  1. Write your test and use `assertExpectedInline()` instead of a normal\n     `assertEqual`.  Leave the expected argument blank with an empty string:\n     ```py\n     self.assertExpectedInline(some_func(), "")\n     ```\n\n  2. Run your test.  It should fail, and you get an error message about\n     accepting the output with `EXPECTTEST_ACCEPT=1`\n\n  3. Rerun the test with `EXPECTTEST_ACCEPT=1`.  Now the previously blank string\n     literal will contain the expected value of the test.\n     ```py\n     self.assertExpectedInline(some_func(), "my_value")\n     ```\n\nSome tips and tricks:\n\n  - Often, you will want to expect test on a multiline string.  This framework\n    understands triple-quoted strings, so you can just write `"""my_value"""`\n    and it will turn into triple-quoted strings.\n\n  - Take some time thinking about how exactly you want to design the output\n    format of the expect test.  It is often profitable to design an output\n    representation specifically for expect tests.\n',
    'author': 'Edward Z. Yang',
    'author_email': 'ezyang@mit.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ezyang/expecttest',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
