# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['logfmt']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'logfmt-julian-sobott',
    'version': '0.3.0',
    'description': 'Logging Formatter to format log messages in logfmt format',
    'long_description': '# Logfmt for python\n\nLogging Formatter to format log messages in [logfmt format](https://www.brandur.org/logfmt).\n\n[![PyPI version](https://badge.fury.io/py/logfmt-julian-sobott.svg)](https://badge.fury.io/py/logfmt-julian-sobott)\n![publish workflow](https://github.com/JulianSobott/python-logfmt/actions/workflows/python-publish.yml/badge.svg)\n![test workflow](https://github.com/JulianSobott/python-logfmt/actions/workflows/python-test.yml/badge.svg)\n\n> Logfmt is a simple text-based format for structured logging. It is designed to be easy to read by both humans and machines. \n> It is also designed to be easy to parse and generate.\n\n## Example output\n```\nts=2022-10-14T17:41:15+0200 lvl=INFO msg="Hello World"\n```\n\n## Log context\n\nAdditionally, this library supports to add additional information to the log message via LogContexts. \nThis is also known as MDC (Mapped Diagnostic Context).\nThis adds values, to the log message across multiple log statements.\n\n```python\nwith LogContext(foo="bar"):\n    logger.info("Hello World")\n    logger.info("This is a second test")\nlogger.info("Outside of context")\n# ts=2022-10-14T17:41:15+0200 lvl=INFO msg="Hello World" foo=bar\n# ts=2022-10-14T17:41:15+0200 lvl=INFO msg="This is a second test" foo=bar\n# ts=2022-10-14T17:41:15+0200 lvl=INFO msg="Outside of context"\n```\n\n## Installation\n\n```bash\npip install logfmt-julian-sobott\n```\n\n## Example usage\n\n```python\nimport logging\nfrom logfmt import LogFmtFormatter, LogContext, CallableLogContext\n\nlogger = logging.getLogger(__name__)\nlogger.setLevel(logging.INFO)\nformatter = LogFmtFormatter()\nch = logging.StreamHandler()\nch.setFormatter(formatter)\nlogger.addHandler(ch)\n\nlogger.info("Hello World")\n# ts=2022-10-14T17:41:15+0200 lvl=INFO msg="Hello World"\n\nlogger.info("Hello World", extra={"foo": "bar"})\n# ts=2022-10-14T17:41:15+0200 lvl=INFO msg="Hello World" foo=bar\n\nwith LogContext(foo="bar"):\n    logger.info("Hello World")\n    logger.info("This is a second test")\nlogger.info("Outside of context")\n# ts=2022-10-14T17:41:15+0200 lvl=INFO msg="Hello World" foo=bar\n# ts=2022-10-14T17:41:15+0200 lvl=INFO msg="This is a second test" foo=bar\n# ts=2022-10-14T17:41:15+0200 lvl=INFO msg="Outside of context"\n\n@CallableLogContext()\ndef foo(name: str):\n    logger.info("Hello World")\nfoo("bar")\n# ts=2022-10-14T17:41:15+0200 lvl=INFO msg="Hello World" name=bar\n\n\n@CallableLogContext("name", "args")\ndef foo(name: str, surname: str, *args):\n    logger.info("Hello World")\nfoo("bar with spaces", "baz", "qux")\n# ts=2022-10-14T17:45:58+0200 lvl=INFO msg="Hello World" args=(\'qux\',) name="bar with spaces"\n\ntry:\n    raise Exception("Something went wrong")\nexcept Exception as e:\n    logger.exception("trying to fix it")\n# ts=2022-10-14T22:49:31+0200 lvl=ERROR msg="trying to fix it" \n# exception="\n# Traceback (most recent call last):\n#   File \\"/src/tests/x.py\\", line 17, in <module>\n#     raise Exception(\\"Something went wrong\\")\n# Exception: Something went wrong"\n```\n',
    'author': 'JulianSobott',
    'author_email': 'julian.sobott@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JulianSobott/python-logfmt',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
