# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['finance_tracker',
 'finance_tracker.aggregators',
 'finance_tracker.categories',
 'finance_tracker.entries',
 'finance_tracker.money',
 'finance_tracker.readers']

package_data = \
{'': ['*']}

install_requires = \
['Deprecated>=1.2.13,<2.0.0', 'inquirer>=2.10.0,<3.0.0', 'pandas>=1.5.0,<2.0.0']

setup_kwargs = {
    'name': 'finance-tracker',
    'version': '1.0.0',
    'description': 'Python tool to track finances over a year',
    'long_description': '# finance-tracker\n\nPython tool to track finances over a year\n\n[![PyPI](https://img.shields.io/pypi/v/finance-tracker)](https://pypi.org/project/finance-tracker/)\n[![GitHub release (latest by date)](https://img.shields.io/github/v/release/w0rmr1d3r/finance-tracker)](https://github.com/w0rmr1d3r/finance-tracker/releases)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/finance-tracker)\n[![CI](https://github.com/w0rmr1d3r/finance-tracker/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/w0rmr1d3r/finance-tracker/actions/workflows/ci.yml)\n![GitHub last commit](https://img.shields.io/github/last-commit/w0rmr1d3r/finance-tracker)\n[![PyPi downloads](https://img.shields.io/pypi/dm/finance-tracker?label=PyPi%20downloads)](https://pypistats.org/packages/finance-tracker)\n\n## Installation\n\n### PyPi package\n\n```bash\npip install finance-tracker\n```\n\n## Usage\n\n### From repository\n\n1. Clone the repo\n2. Install poetry\n3. Run `make install`\n4. Load the categories and categories to filter as incomes wanted in a file called `categories.json`\n   in `./load/categories/`. Such as:\n\n    ```json\n    {\n      "CATEGORIES": {\n        "CATEGORY_ONE": [\n          "TITLE TO CATEGORIZE"\n        ],\n        "CATEGORY_TWO": [\n          "TITLE 2 TO CATEGORIZE"\n        ]\n      },\n      "POSITIVE_CATEGORIES": [\n        "CATEGORY_TWO"\n      ]\n    }\n    ```\n\n5. Load the CSV files in the folder `./load/entries_files/`. Those files have 3 _headers_ (2 with text and 1 with column\n   titles) and the following columns:\n\n    ```csv\n    HEADER1;;;;;\n    HEADER2;;;;;\n    DATE;DATE TWO;TITLE;OTHER DATA;QUANTITY;OTHER\n    01/01/1999;01/01/1999;PAYCHECK;PAYCHECK FROM COMPANY 1;1.000;1.000\n    ```\n\n6. Run `make run`\n\n### From package installation\n\n1. Follow the steps in [Installation](#installation)\n2. Load the categories and categories to filter as incomes wanted in a file called `categories.json`\n   in `./load/categories/`. Such as:\n\n    ```json\n    {\n      "CATEGORIES": {\n        "CATEGORY_ONE": [\n          "TITLE TO CATEGORIZE"\n        ],\n        "CATEGORY_TWO": [\n          "TITLE 2 TO CATEGORIZE"\n        ]\n      },\n      "POSITIVE_CATEGORIES": [\n        "CATEGORY_TWO"\n      ]\n    }\n    ```\n\n3. Load the CSV files in the folder `./load/entries_files/`. Those files have 3 _headers_ (2 with text and 1 with column\n   titles) and the following columns:\n\n    ```csv\n    HEADER1;;;;;\n    HEADER2;;;;;\n    DATE;DATE TWO;TITLE;OTHER DATA;QUANTITY;OTHER\n    01/01/1999;01/01/1999;PAYCHECK;PAYCHECK FROM COMPANY 1;1.000;1.000\n    ```\n\n4. Import it and use it in your project like this:\n    ```python\n    from finance_tracker.__main__ import run\n\n    if __name__ == "__main__":\n        run()\n    ```\n\n## Contributing\n\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'w0rmr1d3r',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/w0rmr1d3r/finance-tracker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
