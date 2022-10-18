# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['testscribe', 'testscribe.api']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.2', 'typer']

entry_points = \
{'console_scripts': ['testscribe = testscribe.__main__:app']}

setup_kwargs = {
    'name': 'testscribe',
    'version': '0.0.1a2',
    'description': 'Unit test automation tool',
    'long_description': '# TestScribe for Python - unit test made easier\n\nA tool to make python unit testing easier by automating the boring and repetitive parts.\n\n# A simple example\n\nHere is a very basic simple example to illustrate the basic usage.\nSuppose you have a function called is_prime in a file prime.py. It checks if the input\nnumber is a prime number. You can unit test the function using TestScribe without writing any boilerplate \nunit test code as follows:\n\n    $ testscribe create prime.py is_prime\n    ...\n    Please provide the value for the parameter (n) of type: (int) []: 8\n    Calling is_prime(n=8)\n    ***** Result:\n    type: <class \'bool\'>\n    value:\n    False\n    ***** Result end\n\nYou can run it multiple times with different inputs and inspect the displayed output.\nIf the output is not correct, fix the production code and test again.\n\nTestScribe automatically creates fully functional unit test files. You can use them to debug a test run or save\nthem as regression tests or simply discard them. \n\nThe example above generates the following test file test_prime_g.py\n    \n    from prime import is_prime\n    def test_is_prime():\n        result = is_prime(n=8)\n        assert result is False\n\nThis is the code you would likely have to write to unit test the same without TestScribe\'s help.\n\n# Easy to get started and setup\nAdding testscribe to your development dependencies is all you need to start using the basic features.\nMost of the features should be self-explanatory to developers.\nAdditional features such as launching the tool more easily only require simple setups. \n\n# Low risk to try\n* The tool doesn\'t modify the code you test in any way.\n* It doesn\'t introduce any dependency to your production code.\n* At any time, removing the tool won\'t break your existing production code or tests.\n* It\'s free and open source with the Apache 2.0 license.\n* You can always fall back to the traditional ways of testing for use cases the tool doesn\'t support yet. \nThe tool won\'t get in your way.\n\n# Demo\nYou can find demos [here](https://happyray.github.io/testscribe/demo.html).\nFeel free to download the demo project and try for yourself.\n\n# Documentation\nIt\'s capable of handling class instances, exceptions, class methods, mocking inputs, patching dependencies...\nPlease see the full documentation [here](https://happyray.github.io/testscribe/).\n\n# Copyright and license\n\nCopyright 2022 Ruiguo (Ray) Yang\n\n     Licensed under the Apache License, Version 2.0 (the "License");\n     you may not use this file except in compliance with the License.\n     You may obtain a copy of the License at\n\n         http://www.apache.org/licenses/LICENSE-2.0\n\n     Unless required by applicable law or agreed to in writing, software\n     distributed under the License is distributed on an "AS IS" BASIS,\n     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n     See the License for the specific language governing permissions and\n     limitations under the License.\n',
    'author': 'Ray Yang',
    'author_email': 'ruiguo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/HappyRay/testscribe',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
