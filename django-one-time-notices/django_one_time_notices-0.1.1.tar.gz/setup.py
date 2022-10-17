# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['notices',
 'notices.example_project',
 'notices.example_project.example_app',
 'notices.example_project.example_app.migrations',
 'notices.example_project.example_project',
 'notices.migrations',
 'notices.templatetags']

package_data = \
{'': ['*'],
 'notices': ['static/notices/css/*',
             'static/notices/js/*',
             'templates/notices/*'],
 'notices.example_project.example_app': ['templates/example_app/*']}

install_requires = \
['Django>=4.1,<5.0', 'django-classy-tags>=3.0.1,<4.0.0']

setup_kwargs = {
    'name': 'django-one-time-notices',
    'version': '0.1.1',
    'description': '',
    'long_description': '# django-one-time-notices\n\nDisplays a modal with notice content if a user hasn\'t seen it yet.\n\n## Install\n```\npip install django-one-time-notices\n```\n\n## Settings\n\nAdd to `INSTALLED_APPS`:\n\n```\ndjango.contrib.auth\ndjango.contrib.admin\n...\nnotices\n```\n\n\nAdd to `TEMPLATES[\'OPTIONS\']`:\n```\nTEMPLATES = [\n    {\n        \'BACKEND\': \'django.template.backends.django.DjangoTemplates\',\n        \'DIRS\': [],\n        \'APP_DIRS\': True,\n        \'OPTIONS\': {\n            \'context_processors\': [\n                ...\n                \'django.core.context_processors.request\'\n                ...\n                \'notices.context_processors.notices\',\n            ]\n        }\n    }\n]\n```             \n\nTo customise the notice colour (button and title border), add\n```\nNOTICES_COLOR=<color>  # any css-acceptable colour\n```\n\n## Static assets\nAdd `notices/css/notices.css` and `notices/js/notices.js` to your markup.\n\n## Usage\nIn templates, load the tags:\n```\n{% load notices_tags %}\n```\n\nand add the modal:\n```\n{% NoticesModal %} \n```\n\nThe modal will be shown.  Once it has been dismissed it won\'t be shown again unless the notice version changes (see below) or the `notice_seen` cookie is deleted.\n\n## Setting/updating the notice\n\n### via models and django admin\nAdd a `Notice` instance in the django admin. \n\nNotices have `title`, `content`, `version` and optional `expires_at` fields.\n\nVersion can be any positive number; it defaults to incrementing the last version number.  Set the `expires_at` datetime to avoid showing this notice after the specified date, even if the user has never seen/dismissed it.\n\nTo show a new notice, add another Notice instance with an incremented version number.\n\n### via django settings\n\nOverride the Notice model by adding to your `settings.py`:\n`NOTICES_VERSION` # an integer\n`NOTICES_TITLE`  # optional, default = "New!"\n`NOTICES_CONTENT`  # optional, default = ""\n\nSet `NOTICES_VERSION = 0` to clear the cookie and disable showing notices at all.\n',
    'author': 'Becky Smith',
    'author_email': 'rebkwok@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
