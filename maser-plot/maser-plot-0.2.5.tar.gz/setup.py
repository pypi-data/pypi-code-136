# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['maser', 'maser.plot', 'maser.plot.rpw']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.2,<4.0.0']

setup_kwargs = {
    'name': 'maser-plot',
    'version': '0.2.5',
    'description': 'Maser4py submodule to plot radio data',
    'long_description': '# About maser-plot\n\nmaser-plot is a submodule of [maser4py](https://pypi.org/project/maser4py/).\n\nIt can be used with [maser.data](https://pypi.org/project/maser.data/) to plot radio data from the following missions:\n\n- RPW/Solar Orbiter\n\n# Installation\n\nTo install the package, run the following command:\n\n```\npip install maser-plot\n```\n\nor use one of the extra options:\n\n- `jupyter` for Jupyter notebook support\n- `spacepy` for CDF data format support (note that this requires the [CDF library](https://cdf.gsfc.nasa.gov/html/sw_and_docs.html))\n- `nenupy` for NenuFAR data products support\n- `all` to install all the above\n\nFor example use `maser-plot[jupyter,spacepy]` if you want to use `maser-plot` with spacepy and jupyter notebooks:\n\n```bash\npip install maser-plot[jupyter,spacepy]\n```\n\n# Usage\n\nSee in `examples` folder about illustrations on how to use `maser-plot`.\n\nExamples can also be run on Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/git/https%3A%2F%2Fgitlab.obspm.fr%2Fmaser%2Fmaser4py.git/master) You can also launch a Binder environment and browse through the notebook [examples](https://gitlab.obspm.fr/maser/maser4py/-/tree/namespace/examples).\n\n# Development\n\nTo contribute to the development of the package, you will need to install a local copy of maser-plot\n\n```\ngit clone https://gitlab.obspm.fr/maser/maser4py.git\n```\n\nThen, you can install the package locally\n\n## Requirements\n\n`maser-plot` requirements are detailed in the `src/maser_plot/pyproject.toml` file\n\n### poetry\n\nTo install the package, it is recommended to use [poetry](https://python-poetry.org/docs/#installing-with-pip):\n\n```\npip install poetry\n```\n\n### CDF file format\n\nTo use `maser-plot` to read CDF files you have to install the [CDF library](https://cdf.gsfc.nasa.gov/html/sw_and_docs.html) and the [spacepy.pycdf](https://spacepy.github.io/install.html) package.\n\n## Installing a local copy of maser-plot\n\nUse the following command from `src/maser_plot` folder to install the package:\n\n```bash\npoetry install\n```\n\nor this one if you want to use `maser-plot` with spacepy to handle CDF files:\n\n```bash\npoetry install --extras "spacepy"\n```\n\n## Tests\n\nUse `pytest -m "not test_data_required"` to skip tests that require test data (and to skip auto download).\n\n## Manually publish `maser-plot` on pypi\n\nTo publish `maser-plot` with `poetry` you will have to build a `dist` package:\n\n```\npoetry build\n```\n\nAnd then publish the package on pypi (and/or on Gitlab, see https://python-poetry.org/docs/cli/#publish):\n\n```\npoetry publish\n```\n\nCommands above must be run from `src/maser_plot` directory.\n',
    'author': 'Baptiste Cecconi',
    'author_email': 'baptiste.cecconi@obspm.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
