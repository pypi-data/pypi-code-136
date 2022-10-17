# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dmdm']

package_data = \
{'': ['*']}

install_requires = \
['Django>=2.2,<5.0', 'black>=22.10.0,<23.0.0', 'nmdmail>=0.3.0,<0.4.0']

setup_kwargs = {
    'name': 'dmdm',
    'version': '2.0.1',
    'description': 'Django MarkDown Mails',
    'long_description': '#  Django MarkDown Mail\n\n[![PyPI version](https://badge.fury.io/py/dmdm.svg)](https://pypi.org/project/dmdm)\n[![Tests](https://github.com/nim65s/dmdm/actions/workflows/test.yml/badge.svg)](https://github.com/nim65s/dmdm/actions/workflows/test.yml)\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/nim65s/dmdm/master.svg)](https://results.pre-commit.ci/latest/github/nim65s/dmdm/master)\n[![codecov](https://codecov.io/gh/nim65s/dmdm/branch/master/graph/badge.svg?token=CUHNXAVJPO)](https://codecov.io/gh/nim65s/dmdm)\n[![Maintainability](https://api.codeclimate.com/v1/badges/6737a84239590ddc0d1e/maintainability)](https://codeclimate.com/github/nim65s/dmdm/maintainability)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nWrite your email in markdown, and send them in txt & html.\n\n## Requirements\n\n- Python 3.7+\n- Django 2.0+\n- [nmdmail](https://github.com/nim65s/nmdmail)\n\n## Install\n\n`python -m pip install dmdm`\n\n## Usage\n\nThis replaces django\'s `django.core.email.send_mail`, but the mail will have an html alternative rendered from the text\npart with markdown. You can also provide a custom `css` and even images (that will be inlined) located in `image_root`.\n\n\n```python\nfrom dmdm import send_mail\n\ndef send_mail(\n    subject: str,\n    message: str,\n    from_email: str,\n    recipient_list: List[str],\n    context: Optional[Dict] = None,\n    request: Optional[HttpRequest] = None,\n    fail_silently: bool = False,\n    css: Optional[str] = None,\n    image_root: str = ".",\n    auth_user: Optional[str] = None,\n    auth_password: Optional[str] = None,\n    connection: Optional[BaseEmailBackend] = None,\n    reply_to: Optional[List[str]] = None,\n) -> int\n```\n\nIf you want to write your markdown in a template, just put the name of the template in `message` and add a `context`\n(which can be `{}`) and eventually a `request`:\n\n```python\nsend_mail(\n    subject,\n    "test_email_template.md",\n    from_email,\n    recipient_list,\n    {"template_variable": "value"},\n)\n```\n',
    'author': 'Guilhem Saurel',
    'author_email': 'guilhem.saurel@laas.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nim65s/dmdm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
