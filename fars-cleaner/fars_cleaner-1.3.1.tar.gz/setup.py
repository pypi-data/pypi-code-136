# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fars_cleaner']

package_data = \
{'': ['*'], 'fars_cleaner': ['lookup_tables/*']}

install_requires = \
['dask',
 'distributed>=2022,<2023',
 'pathlib',
 'pooch>=1.6.0',
 'pyjanitor>=0.23.1,<0.24.0',
 'requests',
 'scipy>=1.7.0,<2.0.0',
 'thefuzz',
 'tqdm']

extras_require = \
{':python_version >= "3.8"': ['pandas>=1.4,<2.0', 'numpy>=1.22.0,<2.0.0'],
 'dev': ['pytest>=7.1.0,<8.0.0', 'hypothesis']}

setup_kwargs = {
    'name': 'fars-cleaner',
    'version': '1.3.1',
    'description': 'A package for loading and preprocessing the NHTSA FARS crash database',
    'long_description': '![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/mzabrams/fars-cleaner)\n![PyPI](https://img.shields.io/pypi/v/fars-cleaner)\n[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)\n[![DOI](https://zenodo.org/badge/252038452.svg)](https://zenodo.org/badge/latestdoi/252038452)\n\n[![status](https://joss.theoj.org/papers/2ca54c6935611fe3cb0303c49a354c51/status.svg)](https://joss.theoj.org/papers/2ca54c6935611fe3cb0303c49a354c51)\n\n# FARS Cleaner `fars-cleaner`\n\n`fars-cleaner` is a Python library for downloading and pre-processing data \nfrom the Fatality Analysis Reporting System, collected annually by NHTSA since\n 1975. \n\n## Installation\n\nThe preferred installation method is through `conda`.\n```bash\nconda install -c conda-forge fars-cleaner\n```\nYou can also install with [pip](https://pip.pypa.io/en/stable/).\n\n```bash\npip install fars-cleaner\n```\n\n## Usage\n\n### Downloading FARS data\nThe `FARSFetcher` class provides an interface to download and unzip selected years from the NHTSA FARS FTP server. \nThe class uses `pooch` to download and unzip the selected files. By default, files are unzipped to your OS\'s cache directory.\n\n```python\nfrom fars_cleaner import FARSFetcher\n\n# Prepare for FARS file download, using the OS cache directory. \nfetcher = FARSFetcher()\n```\nSuggested usage is to download files to a data directory in your current project directory. \nPassing `project_dir` will download files to `project_dir/data/fars` by default. This behavior can be \noverridden by setting `cache_path` as well. Setting `cache_path` alone provides a direct path to the directory\nyou want to download files into.\n```python\nfrom pathlib import Path\nfrom fars_cleaner import FARSFetcher\n\nSOME_PATH = Path("/YOUR/PROJECT/PATH") \n# Prepare to download to /YOUR/PROJECT/PATH/data/fars\n# This is the recommended usage.\nfetcher = FARSFetcher(project_dir=SOME_PATH)\n\n# Prepare to download to /YOUR/PROJECT/PATH/fars\ncache_path = "fars"\nfetcher = FARSFetcher(project_dir=SOME_PATH, cache_path=cache_path)\n\ncache_path = Path("/SOME/TARGET/DIRECTORY")\n# Prepare to download directly to a specific directory.\nfetcher = FARSFetcher(cache_path=cache_path)\n```\n\nFiles can be downloaded in their entirety (data from 1975-2018), as a single year, or across a specified year range.\nDownloading all of the data can be quite time consuming. The download will simultaneously unzip the folders, and delete \nthe zip files. Each zipped file will be unzipped and saved in a folder `{YEAR}.unzip`\n```python\n# Fetch all data\nfetcher.fetch_all()\n\n# Fetch a single year\nfetcher.fetch_single(1984)\n\n# Fetch data in a year range (inclusive).\nfetcher.fetch_subset(1999, 2007)\n```\n\n### Processing FARS data\nCalling `load_pipeline` will allow for full loading and pre-processing of the FARS data requested by the user.\n```python\nfrom fars_cleaner import FARSFetcher, load_pipeline\n\nfetcher = FARSFetcher(project_dir=SOME_PATH)\nvehicles, accidents, people = load_pipeline(fetcher=fetcher,\n                                            first_run=True,\n                                            target_folder=SOME_PATH)\n```\n\nCalling `load_basic` allows for simple loading of the FARS data for a single year, with no preprocessing. Files must\nbe prefetched using a `FARSFetcher` or similar method. A `mapper` dictionary must be provided to identify what, if \nany, columns require renaming. \n\n```python\nfrom fars_cleaner.data_loader import load_basic\n\nvehicles, accidents, people = load_basic(year=1975, data_dir=SOME_PATH, mapping=mappings)\n```\n\n## Requirements\nDownloading and processing the full FARS dataset currently runs out of memory on Windows machines with only 16GB RAM. It is recommended to have at least 32GB RAM on Windows systems. macOS and Linux run with no issues on 16GB systems.\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.\n\n## License\n[BSD-3 Clause](https://choosealicense.com/licenses/bsd-3-clause/)\n',
    'author': 'Mitchell Abrams',
    'author_email': 'mitchell.abrams@duke.edu',
    'maintainer': 'Mitchell Abrams',
    'maintainer_email': 'mitchell.abrams@duke.edu',
    'url': 'https://github.com/mzabrams/fars-cleaner',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
