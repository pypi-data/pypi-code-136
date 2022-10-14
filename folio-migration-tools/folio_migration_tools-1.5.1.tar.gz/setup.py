# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['folio_migration_tools',
 'folio_migration_tools.mapping_file_transformation',
 'folio_migration_tools.marc_rules_transformation',
 'folio_migration_tools.migration_tasks',
 'folio_migration_tools.test_infrastructure',
 'folio_migration_tools.transaction_migration']

package_data = \
{'': ['*']}

install_requires = \
['argparse-prompt>=0.0.5,<0.0.6',
 'defusedxml>=0.7.1,<0.8.0',
 'folio-uuid>=0.2.5,<0.3.0',
 'folioclient>=0.42.0,<0.43.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyhumps>=3.7.3,<4.0.0',
 'pymarc>=4.2.0,<5.0.0',
 'python-dateutil>=2.8.2,<3.0.0']

setup_kwargs = {
    'name': 'folio-migration-tools',
    'version': '1.5.1',
    'description': 'A tool allowing you to migrate data from legacy ILS:s (Library systems) into FOLIO LSP',
    'long_description': '# FOLIO Migration Tools\n![example workflow](https://github.com/FOLIO-FSE/MARC21-To-FOLIO/actions/workflows/python-app.yml/badge.svg)[![codecov](https://codecov.io/gh/FOLIO-FSE/folio_migration_tools/branch/main/graph/badge.svg?token=ZQL5ILWWGT)](https://codecov.io/gh/FOLIO-FSE/folio_migration_tools)\nA toolkit that enables you to migrate data over from a legacy ILS system into [FOLIO LSP](https://www.folio.org/)\n\n# What is it good for?\nFOLIO Migration tools enables you to migrate libraries with the most common ILS:s over to FOLIO without data losses or any major data transformation tasks. \nThe tools transforms and loads the data providing you and the library with good actionable logs and data cleaning task lists together with the migrated data.\n\n## What data does it cover?\nFOLIO Migration Tools currently covers the following data sets:\n* Catalog (Inventory and SRS in FOLIO terminology)\n* Circulation transactions (Open loans and requests)\n* Users/Patrons (In FOLIO, these share the same app/database)\n* Courses and Reserves (Course reserves)\n\n### What additional functionality is on the roadmap?\nThis is the loose roadmap, in order of most likely implementations first\n* Organizations (Vendor records)\n* Orders\n* ERM-related objects\n* Financial records\n\n### Can I use the tools for ongoing imports and integrations?\nThe tools are primarliy maintained for performing initial data migrations. We recommend that you use native FOLIO functionality for ongoing loads where possible. \nIn theory, these tools can be used for ongoing patron loads from systems like Banner, Workday, or PeopleSoft. But we recommend you to weigh your options carefully before going down this path. \n\n# Contributing\nWant to contribute? Read the [CONTRIBUTING.MD](https://github.com/FOLIO-FSE/folio_migration_tools/blob/main/CONTRIBUTING.md)\n\n# Found an issue?\nReport it on the [Github Issue tracker](https://github.com/FOLIO-FSE/folio_migration_tools/issues)\n\nThe scripts requires a FOLIO tenant with reference data properly set up. The script will throw messages telling what reference data is missing.\n# Installing\nMake sure you are running Python 3.9 or above. \n## 1. Using pip and venv\n1. Create and activate a [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)\n2. Install using pip: `python3 -m pip install folio_migration_tools`\n3. Test the installation by running `python3 -m folio_migration_tools -h`\n## 2. Using pipenv\n1. Run `pipenv install folio-migration-tools`\n2. Test the installation by calling `pipenv run python3 -m folio_migration_tools -h`\n\n\n# FOLIO migration process\nThis repo plays the main part in a process using a collection of tools. The process itself is documented in more detail, including example configuration files, at [this template repository](https://github.com/FOLIO-FSE/migration_repo_template)\nIn order to perform migrations according to this process, you need the following:\n* An Installation of [FOLIO Migration Tools](https://pypi.org/project/folio-migration-tools/). Installation instructions above.\n* A clone, or a separate repo created from [migration_repo_template](https://github.com/FOLIO-FSE/migration_repo_template)\n* Access to the [Data mapping file creator](https://data-mapping-file-creator.folio.ebsco.com/data_mapping_creation) web tool\n* A FOLIO tenant running the latest or the second latest version of FOLIO\n\n\n\n# Running the scripts\nFor information on syntax, what files are needed and produced by the toolkit, refer to the documentation and example files in the [template repository](https://github.com/FOLIO-FSE/migration_repo_template). We are building out the docs section in this repository as well: [Documentation](https://github.com/FOLIO-FSE/folio_migration_tools/tree/main/docs)\n¨\n\n\n# Tests\nThere is a test suite for Bibs-to-Instance mapping. You need to add arguments in order to run it against a FOLIO environment. The tests are run against the latest [FOLIO Bugfest environment](https://wiki.folio.org/dosearchsite.action?cql=siteSearch%20~%20%22bugfest%22%20AND%20type%20in%20(%22space%22%2C%22user%22%2C%22com.atlassian.confluence.extra.team-calendars%3Acalendar-content-type%22%2C%22attachment%22%2C%22page%22%2C%22com.atlassian.confluence.extra.team-calendars%3Aspace-calendars-view-content-type%22%2C%22blogpost%22)&includeArchivedSpaces=false) as part of the commit process in this repo.\n\nIMPORTANT!\nthe tests and the tools relies on many calls to GitHub, and you need to create a [GitHub personal Access token](https://github.com/settings/tokens) and add a .env file in the root of the folder with the following contents:   \n```GITHUB_TOKEN=ghp_.....```   \nThen, either restart your shell or run   \n```source .env```    \nfrom the command line\n\n## Running the tests for the Rules mapper\n### Pipenv\n* Install the packages in the Pipfile\n* Run ```clear; pipenv run pytest -v --log-level=DEBUG --password PASSWORD --tenant_id TENANT_ID --okapi_url OKAPI URL --username USERNAME```\n### Poetry\n* Install the packages from the pyproject.toml\n* Run ```clear; poetry run pytest -v --log-level=DEBUG --password folio --tenant_id fs09000000 --okapi_url https://okapi-bugfest-lotus.int.aws.folio.org --username folio --cov```\n',
    'author': 'Theodor Tolstoy',
    'author_email': 'github.teddes@tolstoy.se',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/FOLIO-FSE/folio_migration_tools',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
