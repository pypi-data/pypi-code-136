# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['leetcode_runner']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'colorama>=0.4.4,<0.5.0',
 'gql[requests]>=3.4.0,<4.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'termcolor>=1.1.0,<2.0.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['leetcode = leetcode_runner.cli:cli',
                     'leetcode_runner = leetcode_runner.cli:main']}

setup_kwargs = {
    'name': 'leetcode-runner',
    'version': '0.0.4',
    'description': 'LeetCode solutions runner',
    'long_description': '# Overview\n\nLeetCode solutions runner\n\n[![PyPI Version](https://img.shields.io/pypi/v/leetcode-runner.svg)](https://pypi.org/project/leetcode-runner)\n[![PyPI License](https://img.shields.io/pypi/l/leetcode-runner.svg)](https://pypi.org/project/leetcode-runner)\n\n# Installation\n\nInstall it directly into an activated virtual environment:\n\n```text\n$ pip install leetcode-runner\n```\n\nor add it to your [Poetry](https://poetry.eustace.io/) project:\n\n```text\n$ poetry add leetcode-runner\n```\n\n# Usage\n\n1. Install the library from PyPi\n2. Go to [LeetCode](https://leetcode.com) and pick a problem to solve\n3. Copy the title slug from the URL (e.g `is-subsequence`) and execute in your terminal:\n\n   ```shell\n   leetcode pull is-subsequence\n   ```\n\nIt will create a file called `392-is-subsequence.py` and you can start coding straight\naway!\n\n```shell\npython 392-is-subsequence.py\n# or like this, depends on how you manage your python\npoetry run python 392-is-subsequence.py\n\n------------------------------\n[ FAILED ]\ns = "abc", t = "ahbgdc"\nExpected: True\nActual  : None\n------------------------------\n[ FAILED ]\ns = "axc", t = "ahbgdc"\nExpected: False\nActual  : None\n\nPassed: 0/2\n```\n\nBy default a method `Solution` doesn\'t do anything, that\'s why the answer is None. You\nneed to actually solve the problem 😉.\n\nPlease read the next section to undestand how it works and also check the\n[limitations](#limitations) section.\n\n# Usage (manual)\n\nThis is a legacy way to work with this library\n\n1. Install the library from PyPi\n2. Go to [LeetCode](https://leetcode.com) and pick a problem to solve\n3. Open your favourite IDE and import the `leetcode_runner`\n4. Copy problem samples into some variable, like a `problem`, and copy the base\n   `Solution` class that LeetCode provides\n5. `LeetCode(problem, Solution).check()` will run these samples!\n6. Pass your own samples into `check` function\n\n```py\nfrom leetcode_runner import LeetCode, TestCase, Args\nfrom typing import *\n\n# Copied as is from the LeetCode\nproblem = """\nExample 1:\n\nInput: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nOutput: Because nums[0] + nums[1] == 9, we return [0, 1].\nExample 2:\n\nInput: nums = [3,2,4], target = 6\nOutput: [1,2]\nExample 3:\n\nInput: nums = [3,3], target = 6\nOutput: [0,1]\n"""\n\nclass Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        return [1, 2]\n\nLeetCode(problem, Solution).check()\n```\n\nWill print:\n\n```text\n------------------------------\n[ FAILED ]\nnums = [2,7,11,15], target = 9\nExpected: [0, 1]\nActual  : [1, 2]\n------------------------------\n[ OK ]\nnums = [3,2,4], target = 6\nExpected: [1, 2]\nActual  : [1, 2]\n------------------------------\n[ FAILED ]\nnums = [3,3], target = 6\nExpected: [0, 1]\nActual  : [1, 2]\n\nPassed: 1/3\n```\n\nProviding custom cases is also possible:\n\n```python\n\nlc = LeetCode(problem, Solution)\n\nlc.check(\n    extra_cases=[\n        TestCase(args=Args(nums=[0, 1, 2], target=3), answer=[1, 2]),\n        # or\n        TestCase(Args(nums=[0, 1], target=1), [0, 1])\n    ]\n)\n\n```\n\n## Code snippet\n\nJust copy & paste this in your IDE and start coding:\n\n```python\nfrom leetcode_runner import LeetCode, TestCase, Args\nfrom typing import *\n\nPROBLEM = """\n\n"""\n\n\nclass Solution:\n    pass\n\n\nLeetCode(PROBLEM, Solution).check(\n    extra_cases=[\n\n    ]\n)\n\n```\n\n# Requirements\n\n- Python 3.9+\n\n# Limitations\n\n- This tool uses Leetcode\'s GraphQL API under the hood, I\'m not sure how long will it be\n  available for public usage\n- This tool can download only public problems. Subscription-based requires\n  authentication that is currently not implemented\n\n---\n\nThis project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter)\nusing [jacebrowning/template-python](https://github.com/jacebrowning/template-python).\n',
    'author': 'fbjorn',
    'author_email': 'denis@fbjorn.cc',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/leetcode_runner',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
