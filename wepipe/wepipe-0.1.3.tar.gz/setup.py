# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wepipe',
 'wepipe.core',
 'wepipe.core.workflow',
 'wepipe.destination',
 'wepipe.integrate',
 'wepipe.integrate.postprocessor',
 'wepipe.integrate.preprocessor',
 'wepipe.integrate.scrapper',
 'wepipe.pipeline',
 'wepipe.pipeline.altair',
 'wepipe.pipeline.huggingface',
 'wepipe.source']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.41,<2.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'dateparser>=1.1.1,<2.0.0',
 'emoji>=2.1.0,<3.0.0',
 'mmh3>=3.0.0,<4.0.0',
 'pandas>=1.5.0,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'pytz>=2022.4,<2023.0',
 'requests>=2.28.1,<3.0.0']

extras_require = \
{'destination': ['uvicorn',
                 'fastapi',
                 'streamlit',
                 'psycopg2',
                 'matplotlib',
                 'mplfinance',
                 'plotly',
                 'dash',
                 'vega_datasets',
                 'altair',
                 'weanalyze-altair-theme==0.1.4'],
 'pipeline': ['matplotlib',
              'mplfinance',
              'plotly',
              'dash',
              'palettable',
              'lux-api',
              'vega_datasets',
              'altair',
              'weanalyze-altair-theme==0.1.4',
              'nltk',
              'spacy',
              'sentencepiece',
              'sacremoses',
              'torch',
              'torchvision',
              'torchmetrics',
              'torchaudio',
              'transformers'],
 'source': ['psycopg2',
            'newspaper3k',
            'gnews',
            'slack-sdk',
            'google-api-python-client',
            'app-store-reviews-reader',
            'praw',
            'reddit-rss-reader']}

setup_kwargs = {
    'name': 'wepipe',
    'version': '0.1.3',
    'description': '',
    'long_description': '<!-- markdownlint-disable MD033 MD041 -->\n<h1 align="center">\n    Wepipe\n</h1>\n\n<p align="center">\n    <strong>A low/no-code tools for data pipeline designing, sharing, and more.</strong>\n</p>\n\n<p align="center">\n    <a href="https://pypi.org/project/wepipe/" title="PyPi Version"><img src="https://img.shields.io/pypi/v/wepipe?color=green&style=flat"></a>\n    <a href="https://pypi.org/project/orpyter/" title="Python Version"><img src="https://img.shields.io/badge/Python-3.8%2B-blue&style=flat"></a>\n    <a href="https://github.com/weanalyze/wepipe/blob/main/LICENSE" title="Project License"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg"></a>\n</p>\n\n<p align="center">\n  <a href="#getting-started">Getting Started</a> •\n  <a href="#license">License</a> •\n  <a href="https://github.com/weanalyze/wepipe/releases">Changelog</a>\n</p>\n\nTurn your Python functions into pipeline. \n\n<sup>Pre-alpha Version: Not feature-complete and only suggested for experimental usage.</sup>\n\n<img align="center" style="width: 80%" src="https://github.com/weanalyze/orpyter/blob/main/docs/images/orpyter-header.png?raw=true"/>\n\n---\n\n## Highlights\n\n- 🔌&nbsp; Wrap multiple tasks into all-in-one pipeline.\n- 📦&nbsp; Save and share configurations for reproducible analyis.\n- 🧩&nbsp; Reuse pre-defined components & combine with existing pipelines.\n- 📈&nbsp; Instantly deploy and scale for production usage.\n\n## Getting Started\n\n### Installation\n\n> _Requirements: Python 3.8+._\n\n```bash\npip install wepipe\n```\n\nfor all features\n\n```bash\npip install wepipe[source,pipeline,destination]\n```\n\n### Usage\n\n\n\n## License\n\nApache 2.0 License.\n\nThis project is inspired by [Obsei](https://github.com/obsei/obsei) and [Opyrator](https://github.com/ml-tooling/opyrator/).',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
