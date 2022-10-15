# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['conf',
 'core',
 'core.auth',
 'core.lib',
 'core.management',
 'core.management.commands',
 'core.middleware',
 'core.migrations',
 'core.models',
 'core.ocr',
 'core.openapi',
 'core.serializers',
 'core.views',
 'notifications',
 'notifications.consumers',
 'search',
 'search.migrations']

package_data = \
{'': ['*'],
 'core': ['locale/de/LC_MESSAGES/*', 'locale/fr/LC_MESSAGES/*'],
 'search': ['templates/search/indexes/core/*']}

install_requires = \
['Whoosh>=2.7.4,<3.0.0',
 'celery[gevent,redis]>=5.2,<6.0',
 'channels-redis>=3.2,<4.0',
 'channels>=3.0,<4.0',
 'configula>=0.5,<0.6',
 'daphne>=3.0.2,<4.0.0',
 'django-celery-results>=2.2,<3.0',
 'django-cors-headers>=3.9.0,<4.0.0',
 'django-dynamic-preferences>=1.13,<2.0',
 'django-haystack>=3.2.1,<4.0.0',
 'django-modelcluster>=6.0,<7.0',
 'django-mptt>=0.13.4,<0.14.0',
 'django-polymorphic-tree>=2.0,<3.0',
 'django-polymorphic>=3.0,<4.0',
 'django-rest-knox>=4.2.0,<5.0.0',
 'django-taggit>=3.0.0,<4.0.0',
 'django>=4.0,<5.0',
 'django_filter>=21.1,<22.0',
 'djangorestframework-jsonapi>=5.0.0,<6.0.0',
 'djangorestframework>=3.13.1,<4.0.0',
 'drf-spectacular-sidecar>=2022.3.21,<2023.0.0',
 'drf-spectacular>=0.22.0,<0.23.0',
 'elasticsearch>=7,<8',
 'lxml>=4.9.0,<5.0.0',
 'ocrmypdf-papermerge>=0.4.5,<0.5.0',
 'ocrmypdf>=13.5.0,<14.0.0',
 'pdf2image>=1.16.0,<2.0.0',
 'persisting-theory>=1.0,<2.0',
 'psycopg2-binary>=2.9.2,<3.0.0',
 'psycopg2>=2.9.2,<3.0.0',
 'python-magic>=0.4,<0.5',
 'pyyaml>=6.0,<7.0',
 'redis>=4.3.3,<5.0.0',
 'uWSGI>=2.0.20,<3.0.0',
 'uritemplate>=4.1.1,<5.0.0',
 'yapian-haystack>=3.1.0,<4.0.0']

setup_kwargs = {
    'name': 'papermerge-core',
    'version': '2.1.0b11',
    'description': 'Open source document management system for digital archives',
    'long_description': '[![Tests](https://github.com/papermerge/papermerge-core/actions/workflows/tests.yml/badge.svg)](https://github.com/papermerge/papermerge-core/actions/workflows/tests.yml)\n\n# Papermerge RESTful Backend Server\n\n\nThis python package is the heart of Papermerge project. It consists of a set\nof reusable Django apps which are consumed across different bundles of\nPapermerge Document Management System (DMS).\n\nTechnically speaking, it contains following Django apps:\n\n* ``papermerge.core`` - the epicenter of Papermerge DMS project\n* ``papermerge.notifications`` - Django Channels app for sending notifications via websockets\n* ``papermerge.search`` - RESTful search. Supports four backends: [Xapian](https://getting-started-with-xapian.readthedocs.io/en/latest/),\n  [Whoosh](https://whoosh.readthedocs.io/en/latest/intro.html), [Elasticsearch](https://github.com/elastic/elasticsearch),\n  [Solr](https://solr.apache.org/).\n\n\n## What is Papermerge?\n\nPapermerge is an open source document management system (DMS) primarily\ndesigned for archiving and retrieving your digital documents. Instead of\nhaving piles of paper documents all over your desk, office or drawers - you\ncan quickly scan them and configure your scanner to directly upload to\nPapermerge DMS. Papermerge DMS on its turn will extract text data from the\nscanned documents using Optical Character Recognition (OCR) technology the\nindex it and make it searchable. You will be able to quickly find any\n(scanned!) document using full text search capabilities.\n\nPapermerge is perfect tool to manage documents in PDF, JPEG, TIFF and PNG formats.\n\n## Features Highlights\n\n* RESTul API\n* Works well with PDF documents\n* OCR (Optical Character Recognition) of the documents (uses [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF))\n* Full Text Search of the scanned documents (supports four search engine backends, uses [Xapian](https://getting-started-with-xapian.readthedocs.io/en/latest/) by default)\n* Document Versions\n* Tags - assign colored tags to documents or folders\n* Documents and Folders - users can organize documents in folders\n* Multi-User (supports user groups)\n* User permissions management\n* Page Management - delete, reorder, cut & paste pages (uses [PikePDF](https://github.com/pikepdf/pikepdf))\n\n\n## Documentation\n\nOnline documentation is available at [https://docs.papermerge.io](https://docs.papermerge.io/)\n\n\n## Tests\n\nTest suite is divided into two big groups:\n\n1. tests.core\n2. tests.search\n\n\nFirst group is concerned with tests which do not depend on elasticsearch while\nsecond one **tests.search** is concerned with tests for which **depend on elasticsearch**\nand as result run very slow (hence the grouping). In\norder to run `tests.core` tests you need to have redis up and running; in\norder to run `test.search` you need to both **redis and elasticsearch** up and\nrunning.\n\nBefore running core tests suite, make sure redis service is up and running. Run tests:\n\n     poetry run task test-core\n\nBefore running search tests suite, make sure both **redis and elasticsearch**\nservices are up and running:\n\n     poetry run task test-search\n\nIn order to run all tests suite (core + search):\n\n    poetry run task test\n\n\n## Linting\n\nUse following command to make sure that your code is formatted per PEP8 spec:\n\n    poetry run task lint\n',
    'author': 'Eugen Ciur',
    'author_email': 'eugen@papermerge.com',
    'maintainer': 'Eugen Ciur',
    'maintainer_email': 'eugen@papermerge.com',
    'url': 'https://www.papermerge.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<=3.10.6',
}


setup(**setup_kwargs)
