# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tidypandas']

package_data = \
{'': ['*']}

install_requires = \
['collections-extended>=2.0.2,<3.0.0', 'pandas>=1.0.0,<2.0.0']

extras_require = \
{'skimpy': ['skimpy>=0.0.5,<0.0.6']}

setup_kwargs = {
    'name': 'tidypandas',
    'version': '0.2.3',
    'description': 'A grammar of data manipulation for pandas inspired by tidyverse',
    'long_description': "![](docs/logo.png)\n\n[![PyPI\nversion](https://badge.fury.io/py/tidypandas.svg)](https://badge.fury.io/py/tidypandas)\n[![Test-Build](https://github.com/talegari/tidypandas/actions/workflows/test_suite.yml/badge.svg)](https://github.com/talegari/tidypandas/actions/workflows/test_suite.yml)\n\n# `tidypandas`\n\n> A **grammar of data manipulation** for\n> [pandas](https://pandas.pydata.org/docs/index.html) inspired by\n> [tidyverse](https://tidyverse.tidyverse.org/)\n\n`tidypandas` python package provides *minimal, pythonic* API for common\ndata manipulation tasks:\n\n-   `tidyframe` class (wrapper over pandas dataframe) provides a\n    dataframe with simplified index structure (no more resetting indexes\n    and multi indexes)\n-   Consistent ‘verbs’ (`select`, `arrange`, `distinct`, …) as methods\n    to `tidyframe` class which mostly return a `tidyframe`\n-   Unified interface for summarizing (aggregation) and mutate (assign)\n    operations across groups\n-   Utilites for pandas dataframes and series\n-   Uses simple python data structures, No esoteric classes, No pipes,\n    No Non-standard evaluation\n-   No copy data conversion between `tidyframe` and pandas dataframes\n-   An accessor to apply `tidyframe` verbs to simple pandas datarames\n-   …\n\n## Example\n\n-   `tidypandas` code:\n\n<!-- -->\n\n    df.filter(lambda x: x['col_1'] > x['col_1'].mean(), by = 'col_2')\n\n-   equivalent pandas code:\n\n<!-- -->\n\n    (df.groupby('col2')\n       .apply(lambda x: x.loc[x['col_1'] > x['col_1'].mean(), :])\n       .reset_index(drop = True)\n       )\n\n## Why use `tidypandas`\n\n`tidypandas` is for you if:\n\n-   you *frequently* write data manipulation code using pandas\n-   you prefer to have stay in pandas ecosystem (see accessor)\n-   you *prefer* to remember a [limited set of\n    methods](https://medium.com/dunder-data/minimally-sufficient-pandas-a8e67f2a2428)\n-   you do not want to write (or be surprised by)\n    [`reset_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html),\n    [`rename_axis`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename_axis.html)\n    often\n-   you prefer writing free flowing, expressive code in\n    [dplyr](https://dplyr.tidyverse.org/) style\n\n> `tidypandas` relies on the amazing `pandas` library and offers a\n> consistent API with a different\n> [philosophy](https://tidyverse.tidyverse.org/articles/manifesto.html).\n\n## Installation\n\n1.  Install release version from Pypi using pip:\n\n        pip install tidypandas\n\n2.  For offline installation, use whl/tar file from the [releases\n    page](https://github.com/talegari/tidypandas/releases) on github.\n\n## Contribution/bug fixes/Issues:\n\n1.  Open an issue/suggestion/bugfix on the github\n    [issues](https://github.com/talegari/tidypandas/issues) page.\n\n2.  Use the master branch from\n    [github](https://github.com/talegari/tidypandas) repo to submit your\n    PR.\n\n------------------------------------------------------------------------\n",
    'author': 'Srikanth Komala Sheshachala',
    'author_email': 'sri.teach@gmail.com',
    'maintainer': 'Srikanth Komala Sheshachala',
    'maintainer_email': 'sri.teach@gmail.com',
    'url': 'https://talegari.github.io/tidypandas/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
