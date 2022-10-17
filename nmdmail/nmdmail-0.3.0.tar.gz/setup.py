# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nmdmail']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.4.1,<4.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'emails>=0.6,<0.7',
 'lxml>=4.9.1,<5.0.0',
 'premailer>=3.10.0,<4.0.0']

entry_points = \
{'console_scripts': ['nmdmail = nmdmail.cli:main']}

setup_kwargs = {
    'name': 'nmdmail',
    'version': '0.3.0',
    'description': 'Send emails written in Markdown',
    'long_description': '# nMdmail: Send emails written in Markdown\n\nFork of https://github.com/yejianye/mdmail, which looks dead.\n\n[![PyPI version](https://badge.fury.io/py/nmdmail.svg)](https://pypi.org/project/nmdmail)\n[![Tests](https://github.com/nim65s/nmdmail/actions/workflows/test.yml/badge.svg)](https://github.com/nim65s/nmdmail/actions/workflows/test.yml)\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/nim65s/nmdmail/main.svg)](https://results.pre-commit.ci/latest/github/nim65s/nmdmail/main)\n[![codecov](https://codecov.io/gh/nim65s/nmdmail/branch/main/graph/badge.svg?token=BLGISGCYKG)](https://codecov.io/gh/nim65s/nmdmail)\n[![Maintainability](https://api.codeclimate.com/v1/badges/6737a84239590ddc0d1e/maintainability)](https://codeclimate.com/github/nim65s/nmdmail/maintainability)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n\nnMdmail sends emails written in Markdown. It could be used as a standalone command-line script or as a python module. The features includes\n\n- Have a sane default CSS style and support CSS customization\n- Support local images as inline images\n\nScreenshot of an email sent via nmdmail viewed in Google Inbox\n\n<img src="screenshot.png" height="640"></img>\n\nTo install nmdmail\n\n```bash\n$ python -m pip install nmdmail\n```\n\n## Send Email in Command-line\n\nWhen sending emails from command-line, the body of the email could be read from a file or stdin.\n\nEmail headers such as subject, from/to, cc etc could be specified at the beginning of the markdown file, Or be specified in command-line arguments.\n\nHere is an example of Markdown file with email headers\n\n```\nSubject: Sample Email\nFrom: foo@xyz.com\nTo: bar@xyz.com\nCc: baz@xyz.com\n\n# Sample Email\n\n-\n\n![Embed local image](../assets/image.jpg)\n```\n\nTo send this email with nmdmail\n\n```bash\n$ nmdmail sample_email.md\n```\n\nHere is an example of specifying subject, from/to in command-line\n\n```bash\n$ nmdmail --from=foo@xyz.com --to=bar@xyz.com --subject=\'Sample\' sample_email.md\n```\n\nTo read email content from stdin,\n\n```bash\n$ echo \'# Sample Email\' | nmdmail --from=foo@xyz.com --to=bar@xyz.com --subject=\'Sample\'\n```\n\nSMTP server configurations are read from the following environment variables\n\n```bash\nexport MDMAIL_HOST="" # default: localhost\nexport MDMAIL_PORT="" # default: 25\nexport MDMAIL_USE_TLS="" # default: false\nexport MDMAIL_USE_SSL="" # default: false\nexport MDMAIL_USERNAME="" # default: None\nexport MDMAIL_PASSWORD="" # default: None\nexport MDMAIL_DEFAULT_SENDER="" # default: None\n```\n\nFull help of `nmdmail` command-line script\n\n```bash\nusage: nmdmail [-h] [--subject SUBJECT] [--from FROM_] [--to TO] [--cc CC]\n               [--bcc BCC] [--reply-to REPLY_TO] [--css CSS] [--print-only]\n               [file]\n\nSend email written in Markdown.\n\npositional arguments:\n  file                  Markdown file for email content. Default to STDIN.\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --subject SUBJECT, -s SUBJECT\n                        Subject line\n  --from FROM, -f FROM\n                        From address\n  --to TO, -t TO        To addresses, separated by comma\n  --cc CC, -c CC        CC address, separated by comma\n  --bcc BCC, -b BCC     Bcc address, separated by comma\n  --reply-to REPLY_TO, -r REPLY_TO\n                        Reply-to address\n  --css CSS             Use a custom CSS file\n  --print-only, -p      Only print out rendered html\n```\n\n## Send Email in Python Code\n\nSending emails in python is straight-forward.\n\n```python\nimport nmdmail\n\nemail="""\n# Sample Email\n\n- Python is awesome\n- Markdown is cool\n\n![Embed local image](../assets/image.jpg)\n"""\n\nnmdmail.send(email, subject=\'Sample Email\',\n            from_email=\'foo@example.com\', to_email=\'bar@example.com\')\n```\n\nBy default, it will use SMTP server on localhost. You could specify a SMTP server as well.\n\n```python\n# Specify SMTP server\nsmtp = {\n  \'host: \'my-mailserver.com\',\n  \'port\': 25,\n  \'tls\': False,\n  \'ssl\': False,\n  \'user: \'\',\n  \'password\': \'\',\n}\n\nnmdmail.send(content,\n             subject=\'Sample Email\',\n             from_email=\'foo@example.com\',\n             to_email=\'bar@example.com\',\n             smtp=smtp)\n```\n\n\n### API documentation `nmdmail.send`\n\n- **email** (str/obj): A markdown string or EmailContent object\n- **subject** (str): subject line\n- **from_email** (str): sender email address\n- **to_email** (str/list): recipient email addresses\n- **cc** (str/list): CC email addresses (string or a list)\n- **bcc** (str/list): BCC email addresses (string or a list)\n- **reply_to** (str): Reply-to email address\n- **smtp** (dict): SMTP configuration with following keys\n    - *host* (str): SMTP server host. Default: localhost\n    - *port* (int): SMTP server port. Default: 25\n    - *tls* (bool): Use TLS. Default: False\n    - *ssl* (bool): Use SSL. Default: False\n    - *user* (bool): SMTP login user. Default empty\n    - *password* (bool): SMTP login password. Default empty\n\n## Use nmdmail with Vim and Emacs\n\nSince `nmdmail` can read from stdin and support email headers such as subject/from/to in the markdown file itself,\nintegrating nmdmail with Vim, Emacs or other text editors is easy.\n\nTo use nmdmail in Vim, just write a markdown email with headers, and then execute `w !nmdmail` command, which will send\ncurrent buffer as stdin to nmdmail.\n\nIn Emacs, you could write a small function to do the same thing\n\n```lisp\n(defun nmdmail-send-buffer ()\n  (interactive)\n  (shell-command-on-region (point-min) (point-max) "nmdmail"))\n```\n\nThen `M-x nmdmail-send-buffer` will send current buffer to nmdmail.\n',
    'author': 'Guilhem Saurel',
    'author_email': 'guilhem.saurel@laas.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nim65s/nmdmail',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
