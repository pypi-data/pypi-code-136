# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['linthell', 'linthell.commands']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['linthell = linthell:cli',
                     'linthell-pre-commit = '
                     'linthell.commands.lint_pre_commit:lint_pre_commit']}

setup_kwargs = {
    'name': 'linthell',
    'version': '0.4.0',
    'description': 'Universal flakehell replacement for almost any linter you like',
    'long_description': "# linthell 🔥\nUniversal flakehell alternative that works with almost any linter you like.\n\n## Usage\nAll examples are shown with `flake8`, edit them for you case.\n\nAt first generate baseline file for every linter you use:\n```bash\nflake8 . | linthell baseline -b baseline-flake8.txt -f <linter regex>\n```\n\nThen lint your project via `linthell`:\n```bash\nflake8 . | linthell lint -b baseline-flake8.txt -f <linter regex>\n```\n\n## Custom linter format\nIf you use another linter then you must provide custom regex string\nstring to parse it's output. Default format is `flake8` default format.\nSome premade formats for linters:\n- `flake8`: `(?P<path>[a-zA-Z0-9\\._-]+(?:[\\\\/][a-zA-Z0-9\\._-]+)*):(?P<line>\\d+):\\d+: (?P<message>[^\\n]+)`\n- `pydocstyle`: `(?P<path>[a-zA-Z0-9\\._-]+(?:[\\\\/][a-zA-Z0-9\\._-]+)*):(?P<line>\\d+).+\\n\\s+(?P<message>[^\\n]+)`\n- `pylint`: `(?P<path>[a-zA-Z0-9\\._-]+(?:[\\\\/][a-zA-Z0-9\\._-]+)*):(?P<line>\\d+):\\d+: (?P<message>[^\\n]+)`\n\n### Create your own format regex\nYou can use your custom format regex. Suitable regex must\ncontains 3 named [python-like](https://docs.python.org/3/howto/regex.html#:~:text=The%20syntax%20for%20a%20named%20group%20is%20one%20of%20the%20Python%2Dspecific%20extensions%3A%20(%3FP%3Cname%3E...).%20name%20is%2C%20obviously%2C%20the%20name%20of%20the%20group) capturing groups: \n- `path` - relative file path \n- `line` - line number\n- `message` - linter message\n\nYour regex should matchs all message related to an issue because \nunfiltered issues are printed by the whole match.\n\nYou can test your regex against linter output with [regexr](https://regexr.com/).\n\n## pre-commit support\nlinthell can be used as [pre-commit](https://pre-commit.com/) hook with python-based linters.\nSee `linthell lint-pre-commit --help` for more. \n\n## Config file\n`linthell` can inject params from config file (`linthell --config path/to/config.ini`). \n`common` section applies for all commands, command specific config are specified by their name\nsection, for example `lint`. Keys must have same name as\nargument name of their command function. For example, `baseline_file`.\n",
    'author': 'Alexander Bespalov',
    'author_email': 'discrimy.off@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitea.discrimy.ru/discrimy/linthell',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
