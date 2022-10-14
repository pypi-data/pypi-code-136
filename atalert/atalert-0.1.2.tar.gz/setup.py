# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['atalert']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'atalert',
    'version': '0.1.2',
    'description': 'Atalert slack alerting service helper module',
    'long_description': "# Atalert Python Package\n\nhttps://atalert.dev\n\nToo many different data notification or alert packages got you down?\n\nStart by using the Atalert Slack App to generate alert webhooks.\n\nCustomize the template, delivery channel, and notify your team. \n\nThen, take note of the webhook url slug for the code examples below!\n\nIt's a best practice to make as many different webhooks as you need for different functional areas, such as code deployments, new user registrations, results of a long-running data pipeline. If there's information somewhere that's difficult to get to, use Atalert to send it to your Slack workspace.\n\n## Installation\n\n`pip install atalert` or `poetry add atalert`\n\n\n## Basic Usage\n\n```\nimport atalert\n\n\n# add these to wherever you need to send a slack atalert, customize with your own data payload\n\n# send an 'ok' atalert\natalert.ok('alert_slug_here', data)\n\n# send a 'warning' atalert\natalert.warn('alert_slug_here', data)\n\n# send an 'error' atalert\natalert.err('alert_slug_here', data)\n\n```\n\nYou'll immediately get a custom alert notification in slack according to your webhook configuration. \n\nThen all your data or platform alerts are in the one place you are every day, Slack!\n\n\n## Sending Files to Slack\n\nFirst, configure your alert within the Atalert Slack App to use the 'attachment' template type.\n\nThen, use any of the following methods:\n\n```\nfrom atalert import ok_file, warn_file, err_file\n\n# send 'data.json' in the current working directory as a file attachment with OK status\nok_file('alert_slug_here', './data.json')\n\n# send 'error.log' in as a file with ERROR status\nerr_file('alert_slug_here', './error.log')\n\n# send 'datacat.jpg' as a picture with WARNING status\nwarn_file('alert_slug_here', './datacat.jpg')\n\n```\n\nEnjoy fine file-based data in your Slack workspace!\n\n\n## Decorator Usage\n\nWant to simplify error notifications? Need to automatically send a method's return object somewhere? Use the decorators!\n\n```\nfrom atalert import atalert_on_error\nfrom atalert import atalert_ok_result\n\n# decorator configured with a webhook url slug, will forward any exceptions\n@atalert_on_error('alert_slug_here')\ndef main_processing_method(*args, **kwargs):\n\n\t# do some things here that may go wrong and throw exceptions\n\tnumbers = business / 0\n\n\treturn numbers\n\n@atalert_ok_result('alert_slug_here')\ndef alternate_processing_method(*args, **kwargs):\n\t# do some math here that you want to send to slack\n\tnumbers = statistics.stdev(args)\n\t# whatever you return will automagically go to your predefined slack channel\n\treturn numbers \n\n```\n\nYou'll get your code exception or method results sent directly to slack!\n\n",
    'author': 'Kevin Haggerty',
    'author_email': 'kevin@splatcollision.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://atalert.dev',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
