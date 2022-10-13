# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['castor_extractor',
 'castor_extractor.commands',
 'castor_extractor.file_checker',
 'castor_extractor.file_checker.templates',
 'castor_extractor.uploader',
 'castor_extractor.utils',
 'castor_extractor.visualization',
 'castor_extractor.visualization.looker',
 'castor_extractor.visualization.looker.api',
 'castor_extractor.visualization.metabase',
 'castor_extractor.visualization.metabase.client',
 'castor_extractor.visualization.metabase.client.api',
 'castor_extractor.visualization.metabase.client.db',
 'castor_extractor.visualization.mode',
 'castor_extractor.visualization.mode.client',
 'castor_extractor.visualization.qlik',
 'castor_extractor.visualization.qlik.client',
 'castor_extractor.visualization.qlik.client.engine',
 'castor_extractor.visualization.tableau',
 'castor_extractor.visualization.tableau.client',
 'castor_extractor.visualization.tableau.tests',
 'castor_extractor.visualization.tableau.tests.unit',
 'castor_extractor.visualization.tableau.tests.unit.graphql',
 'castor_extractor.visualization.tableau.tests.unit.rest_api',
 'castor_extractor.visualization.tableau.tests.unit.utils',
 'castor_extractor.warehouse',
 'castor_extractor.warehouse.abstract',
 'castor_extractor.warehouse.bigquery',
 'castor_extractor.warehouse.postgres',
 'castor_extractor.warehouse.redshift',
 'castor_extractor.warehouse.snowflake',
 'castor_extractor.warehouse.synapse']

package_data = \
{'': ['*'],
 'castor_extractor.visualization.metabase.client.db': ['queries/*'],
 'castor_extractor.visualization.tableau.tests.unit': ['assets/graphql/metadata/*',
                                                       'assets/rest_api/*'],
 'castor_extractor.warehouse.bigquery': ['queries/*', 'queries/cte/*'],
 'castor_extractor.warehouse.postgres': ['queries/*'],
 'castor_extractor.warehouse.redshift': ['queries/*'],
 'castor_extractor.warehouse.snowflake': ['queries/*'],
 'castor_extractor.warehouse.synapse': ['queries/*']}

install_requires = \
['cachetools>=4.2.4,<5.0.0',
 'certifi==2021.10.8',
 'charset-normalizer>=2.0.7,<3.0.0',
 'google-api-core>=2.1.1,<3.0.0',
 'google-auth>=1.6.3,<3.0.0',
 'google-cloud-bigquery-storage>=2.0.0,<3.0.0',
 'google-cloud-bigquery>=2.0.0,<=3.0.0',
 'google-cloud-core>=2.1.0,<3.0.0',
 'google-cloud-storage>=1.42.3,<2.0.0',
 'google-crc32c>=1.3.0,<2.0.0',
 'google-resumable-media>=2.0.3',
 'googleapis-common-protos>=1.53.0,<7.0.0',
 'idna>=3.0.0,<4.0.0',
 'protobuf>=2.0.0,<4.0.0',
 'pyarrow>=6.0.0,<7.0.0',
 'pyasn1-modules>=0.2.8,<1.0.0',
 'pyasn1>=0.4.8,<1.0.0',
 'pycryptodome>=3.0.0,<4.0.0',
 'python-dateutil>=2.0.0,<=3.0.0',
 'pytz==2021.3',
 'requests>=2.0.0,<3.0.0',
 'rsa>=4.0.0,<5.0.0',
 'six>=1.16.0,<2.0.0',
 'sqlalchemy>=1.3.24,<2.0.0',
 'tqdm>=4.0.0,<5.0.0',
 'typing-extensions>=3.7.4.3,<4.0.0',
 'urllib3>=1.0.0,<2.0.0']

extras_require = \
{'all': ['looker-sdk>=21.6.0,<=23.0.0',
         'psycopg2-binary>=2.0.0,<3.0.0',
         'snowflake-connector-python>=2.0.0,<3.0.0',
         'snowflake-sqlalchemy>=1.0.0,<2.0.0',
         'sqlalchemy-bigquery>=1.0.0,<=2.0.0',
         'sqlalchemy-redshift==0.8.2',
         'tableauserverclient==0.17.0',
         'websocket-client>=1.3.3'],
 'bigquery': ['sqlalchemy-bigquery>=1.0.0,<=2.0.0'],
 'looker': ['looker-sdk>=21.6.0,<=23.0.0'],
 'metabase': ['psycopg2-binary>=2.0.0,<3.0.0'],
 'qlik': ['websocket-client>=1.3.3'],
 'redshift': ['psycopg2-binary>=2.0.0,<3.0.0', 'sqlalchemy-redshift==0.8.2'],
 'snowflake': ['snowflake-connector-python>=2.0.0,<3.0.0',
               'snowflake-sqlalchemy>=1.0.0,<2.0.0'],
 'tableau': ['tableauserverclient==0.17.0']}

entry_points = \
{'console_scripts': ['castor-extract-bigquery = '
                     'castor_extractor.commands.extract_bigquery:main',
                     'castor-extract-looker = '
                     'castor_extractor.commands.extract_looker:main',
                     'castor-extract-metabase-api = '
                     'castor_extractor.commands.extract_metabase_api:main',
                     'castor-extract-metabase-db = '
                     'castor_extractor.commands.extract_metabase_db:main',
                     'castor-extract-mode = '
                     'castor_extractor.commands.extract_mode:main',
                     'castor-extract-postgres = '
                     'castor_extractor.commands.extract_postgres:main',
                     'castor-extract-qlik = '
                     'castor_extractor.commands.extract_qlik:main',
                     'castor-extract-redshift = '
                     'castor_extractor.commands.extract_redshift:main',
                     'castor-extract-snowflake = '
                     'castor_extractor.commands.extract_snowflake:main',
                     'castor-extract-tableau = '
                     'castor_extractor.commands.extract_tableau:main',
                     'castor-file-check = '
                     'castor_extractor.commands.file_check:main',
                     'castor-upload = castor_extractor.commands.upload:main']}

setup_kwargs = {
    'name': 'castor-extractor',
    'version': '0.0.35',
    'description': 'Extract your metadata assets.',
    'long_description': '# Castor Extractor <img src="https://app.castordoc.com/images/castor_icon_dark.svg" width=30 />\n\n\nThis library contains utilities to extract your metadata assets into `JSON` or `CSV` files, on your local machine.\nAfter extraction, those files can be pushed to Castor for ingestion.\n\n- Visualization assets are typically:\n  - `dashboards`\n  - `users`\n  - `folders`\n  - ...\n\n\n- Warehouse assets are typically:\n  - `databases`\n  - `schemas`\n  - `tables`\n  - `columns`\n  - `queries`\n  - ...\n\nIt also embeds utilities to help you push your metadata to Castor:\n- `File Checker` to validate your [generic](https://docs.castordoc.com/integrations/data-warehouses/generic-warehouse) CSV files before pushing to Castor\n- `Uploader` to push extracted files to our Google-Cloud-Storage (GCS)\n\n\n# Table of contents\n\n\n- [Installation](#installation)\n  * [Create castor-env](#create-castor-env)\n  * [PIP Install](#pip-install)\n  * [Create the output directory](#create-the-output-directory)\n- Documentation\n  - [Extract from BI Tools](https://docs.castordoc.com/castor-package/read-me/bi-tools)\n  - [Extract from Warehouse](https://docs.castordoc.com/castor-package/read-me/warehouse)\n  - [Uploader](https://docs.castordoc.com/castor-package/read-me/uploader)\n  - [File checker](https://docs.castordoc.com/castor-package/read-me/file-checker)\n- [Contact us](#contact-us)\n\n# Installation\n\nRequirements: **python3.7+**\n<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width=20 />\n\n\n## Create castor-env\n\nWe advise to create a dedicated [Python environment](https://docs.python.org/3/library/venv.html).\n\nHere\'s an example using `Pyenv` and Python `3.7.9`:\n\n- Install Pyenv\n```bash\nbrew install pyenv\nbrew install pyenv-virtualenv\n```\n\n- [optional] Update your `.bashrc` if you encounter this [issue](https://stackoverflow.com/questions/45577194/failed-to-activate-virtualenv-with-pyenv/45578839)\n```bash\neval "$(pyenv init -)"\neval "$(pyenv init --path)"\neval "$(pyenv virtualenv-init -)"\n```\n\n- [optional] Install python 3.7+\n\n```bash\npyenv versions # check your local python installations\n\npyenv install -v 3.7.9 # if none of the installed versions satisfy requirements 3.7+\n```\n\n- Create your virtual env\n```bash\npyenv virtualenv 3.7.9 castor-env # create a dedicated env\npyenv shell castor-env # activate the environment\n\n# optional checks\npython --version # should be `3.7.9`\npyenv version # should be `castor-env`\n```\n\n## PIP install\n\n⚠️ `castor-env` must be created AND activated first.\n```bash\npyenv shell castor-env\n(castor-env) $ # this means the environment is now active\n```\n\nℹ️ please upgrade `PIP` before installing Castor.\n```\npip install --upgrade pip\n```\n\nRun the following command to install `castor-extractor`:\n```\npip install castor-extractor\n```\n\nDepending on your use-case, you can also install one of the following `extras`:\n```\npip install castor-extractor[looker]\npip install castor-extractor[tableau]\npip install castor-extractor[metabase]\npip install castor-extractor[qlik]\npip install castor-extractor[bigquery]\npip install castor-extractor[redshift]\npip install castor-extractor[snowflake]\n```\n\n## Create the output directory\n\n```bash\nmkdir /tmp/castor\n```\n\nYou will provide this path in `extraction` scripts as following:\n```\ncastor-extract-bigquery --output=/tmp/castor\n```\n\nAlternatively, you can also set the following `ENV` in your `bashrc`:\n```bash\nexport CASTOR_OUTPUT_DIRECTORY="/tmp/castor"\n````\n\n\n# Contact\n\nFor any questions or bug report, contact us at [support@castordoc.com](mailto:support@castordoc.com)\n\n[Castor](https://castordoc.com) helps you find, understand, use your data assets\n',
    'author': 'Castor',
    'author_email': 'support@castordoc.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://www.castordoc.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
